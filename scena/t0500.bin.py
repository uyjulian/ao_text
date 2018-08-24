from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Ami",                    # 1
        "Carlos",                 # 2
        "Alec",                   # 3
        "Miner Logy",             # 4
        "Kimmy",                  # 5
        "Miner Gantz",            # 6
        "Miner Marlow",           # 7
        "Bracer Wenzel",          # 8
        "Chiruru",                # 9
        "バス",                   # 10
        "CGF Member",             # 11
        "CGF Member",             # 12
        "CGF Member",             # 13
        "CGF Member",             # 14
        "CGF Member",             # 15
        "2nd Lt. Mireille",       # 16
        "車",                     # 17
        "Zeit",                   # 18
        "Town Mayor Bickson",     # 19
        "Mrs. Anna",              # 20
        "Miner Max",              # 21
        "Mine Captain Hoffman",   # 22
        "SE制御",                 # 23
        "Mainz Mountain Road",    # 24
        "Mainz Mine",             # 25
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
        "Function_7_11DA",         # 07, 7
        "Function_8_130D",         # 08, 8
        "Function_9_135E",         # 09, 9
        "Function_10_13F2",        # 0A, 10
        "Function_11_2391",        # 0B, 11
        "Function_12_3386",        # 0C, 12
        "Function_13_3D83",        # 0D, 13
        "Function_14_3E51",        # 0E, 14
        "Function_15_4320",        # 0F, 15
        "Function_16_4576",        # 10, 16
        "Function_17_4691",        # 11, 17
        "Function_18_47DB",        # 12, 18
        "Function_19_4BED",        # 13, 19
        "Function_20_4D75",        # 14, 20
        "Function_21_50B2",        # 15, 21
        "Function_22_5106",        # 16, 22
        "Function_23_5714",        # 17, 23
        "Function_24_5724",        # 18, 24
        "Function_25_57BF",        # 19, 25
        "Function_26_57C0",        # 1A, 26
        "Function_27_57C1",        # 1B, 27
        "Function_28_57C2",        # 1C, 28
        "Function_29_5800",        # 1D, 29
        "Function_30_5883",        # 1E, 30
        "Function_31_590D",        # 1F, 31
        "Function_32_5998",        # 20, 32
        "Function_33_5A1B",        # 21, 33
        "Function_34_5B13",        # 22, 34
        "Function_35_5BB7",        # 23, 35
        "Function_36_5BF4",        # 24, 36
        "Function_37_5C56",        # 25, 37
        "Function_38_5D37",        # 26, 38
        "Function_39_6161",        # 27, 39
        "Function_40_61C1",        # 28, 40
        "Function_41_61D1",        # 29, 41
        "Function_42_61E4",        # 2A, 42
        "Function_43_61F7",        # 2B, 43
        "Function_44_620A",        # 2C, 44
        "Function_45_69FD",        # 2D, 45
        "Function_46_6A17",        # 2E, 46
        "Function_47_6A86",        # 2F, 47
        "Function_48_6AEF",        # 30, 48
        "Function_49_6B2D",        # 31, 49
        "Function_50_6B6E",        # 32, 50
        "Function_51_6BAF",        # 33, 51
        "Function_52_6C22",        # 34, 52
        "Function_53_6C3B",        # 35, 53
        "Function_54_74A7",        # 36, 54
        "Function_55_74DF",        # 37, 55
        "Function_56_7586",        # 38, 56
        "Function_57_7615",        # 39, 57
        "Function_58_8EBB",        # 3A, 58
        "Function_59_8EEB",        # 3B, 59
        "Function_60_8F41",        # 3C, 60
        "Function_61_8F94",        # 3D, 61
        "Function_62_8FFE",        # 3E, 62
        "Function_63_905E",        # 3F, 63
        "Function_64_90BE",        # 40, 64
        "Function_65_92CC",        # 41, 65
        "Function_66_9319",        # 42, 66
        "Function_67_9366",        # 43, 67
        "Function_68_938B",        # 44, 68
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1114")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you inspect the bus\x01",
            "stop sign, you can ride\x01",
            "the orbal bus.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please use it to move to\x01",
            "various places the same way\x01",
            "you do with the orbal car.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_1114")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KIt's a bus stop. Ride the bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City North Exit\x01",        # 0
            "Bus Stop (Near Doll Studio)\x01",      # 1
            "Cancel\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B2")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_11D2")

    label("loc_11B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D2")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_11D2")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_1027 end

    def Function_7_11DA(): pass

    label("Function_7_11DA")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1309")
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

    def lambda_12C0():
        OP_96(0xFE, 0xFFFFE750, 0xFFFFF830, 0x528A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12C0)
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

    label("loc_1309")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_11DA end

    def Function_8_130D(): pass

    label("Function_8_130D")

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

    # Function_8_130D end

    def Function_9_135E(): pass

    label("Function_9_135E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_13B9")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13AE")
    Sound(2502, 255, 100, 0)
    Jump("loc_13B4")

    label("loc_13AE")

    Sound(2503, 255, 100, 0)

    label("loc_13B4")

    Jump("loc_13DD")

    label("loc_13B9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13D7")
    Sound(3347, 255, 100, 0)
    Jump("loc_13DD")

    label("loc_13D7")

    Sound(3348, 255, 100, 0)

    label("loc_13DD")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_135E end

    def Function_10_13F2(): pass

    label("Function_10_13F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1511")

    ChrTalk(
        0x8,
        (
            "W-What could that be?\x01",
            "That azure pale\x01",
            "glittering tree...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even from up here in\x01",
            "Mainz, you can tell it's\x01",
            "crazily big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even grandma who is knowledgeable in history\x01",
            "said she's never seen anything like it...\x01",
            "I'm getting anxious for some reason...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15D6")

    label("loc_1511")


    ChrTalk(
        0x8,
        (
            "That azure pale glowing\x01",
            "tree... I wonder what\x01",
            "could it be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even grandma who is knowledgeable in history\x01",
            "said she's never seen anything like it...\x01",
            "I'm getting anxious for some reason...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D6")

    Jump("loc_238D")

    label("loc_15DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1756")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C3")

    ChrTalk(
        0x8,
        (
            "Is it true that\x01",
            "Crossbell's independence\x01",
            "was invalidated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The State Guard who came to\x01",
            "search for the resistance guys\x01",
            "went back in a real hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, serves them right.\x01",
            "Justice always wins!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1751")

    label("loc_16C3")


    ChrTalk(
        0x8,
        (
            "The State Guard who came to\x01",
            "search for the resistance guys\x01",
            "went back in a real hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, serves them right.\x01",
            "Justice always wins!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1751")

    Jump("loc_238D")

    label("loc_1756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_18E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185A")

    ChrTalk(
        0x8,
        (
            "The entirety of Mainz is\x01",
            "aiding the CGF\x01",
            "resistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's no way we can have faith\x01",
            "in that President who employed\x01",
            "jaegers to occupy Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Also, defying those in\x01",
            "power, enforcing their own\x01",
            "justice... That's cool!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18E3")

    label("loc_185A")


    ChrTalk(
        0x8,
        (
            "The entirety of Mainz is\x01",
            "aiding the CGF\x01",
            "resistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can't trust that\x01",
            "President... Also, the\x01",
            "resistance defying him is cool!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E3")

    Jump("loc_238D")

    label("loc_18E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A10")

    ChrTalk(
        0x8,
        (
            "Back when the jaegers showed\x01",
            "up in town, I thought we\x01",
            "were already done for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even the CGF who came to\x01",
            "help us were defeated\x01",
            "one after the next...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, they barely touched the\x01",
            "townspeople and their possessions. I\x01",
            "wonder what they were trying to do...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A4E")

    label("loc_1A10")


    ChrTalk(
        0x8,
        (
            "Those jaegers... I\x01",
            "wonder what they were\x01",
            "trying to do...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4E")

    Jump("loc_238D")

    label("loc_1A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A61")
    Jump("loc_238D")

    label("loc_1A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF0")

    ChrTalk(
        0x8,
        (
            "The day after tomorrow, the Arc-en-\x01",
            "Ciel renewal performance is going\x01",
            "to take place in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just once would be fine, but\x01",
            "I really want to see one of\x01",
            "their performance things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And then, I'd sit, by coincidence, next to a\x01",
            "middle age gentleman whose hobby is going to\x01",
            "the theatre, and we'd have a lively chat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(What a mixed motive...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C9E")

    label("loc_1BF0")


    ChrTalk(
        0x8,
        (
            "Just once would be fine, but\x01",
            "I really want to see one of\x01",
            "their performance things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And then, I'd meet a middle-\x01",
            "aged gentleman whose hobby\x01",
            "is going to the theater.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9E")

    Jump("loc_238D")

    label("loc_1CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DFE")

    ChrTalk(
        0x8,
        (
            "The other day, bracers came to\x01",
            "exterminate a monster that they said\x01",
            "appeared in the north mountain region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They were able to exterminate it, but\x01",
            "they said it wasn't a normal monster,\x01",
            "but a strange one for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lately I often hear talk about\x01",
            "monsters like that... Maybe\x01",
            "there's some kind of cause.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E58")

    label("loc_1DFE")


    ChrTalk(
        0x8,
        (
            "Still, defeating such an\x01",
            "unknown monster...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I thought, bracers\x01",
            "are cool, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E58")

    Jump("loc_238D")

    label("loc_1E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_20B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2018")

    ChrTalk(
        0x8,
        (
            "There's a sister who comes\x01",
            "to town periodically to\x01",
            "hold Sunday School class...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But don't you think that\x01",
            "once in a while it would be\x01",
            "nice if a young father came?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And then, and then! He'd be a\x01",
            "fashionable person with his\x01",
            "habit gaudily arranged too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FA-Although it's a fantasy,\x01",
            "that would be quite the\x01",
            "delinquent Father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe. Unexpectedly,\x01",
            "there really is a father\x01",
            "like that...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20AB")

    label("loc_2018")


    ChrTalk(
        0x8,
        (
            "Once in a while, it'd be\x01",
            "nice if a young father\x01",
            "came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If he were a fashionable\x01",
            "person with his habit gaudily\x01",
            "arranged, I'd fall for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AB")

    Jump("loc_238D")

    label("loc_20B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_20BE")
    Jump("loc_238D")

    label("loc_20BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2188")

    ChrTalk(
        0x8,
        (
            "My dad works at the mine\x01",
            "as a miner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Before, he did nothing but skip\x01",
            "out on the job, but lately it\x01",
            "seems he's doing his best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*giggle*, even grandma\x01",
            "was happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2202")

    label("loc_2188")


    ChrTalk(
        0x8,
        (
            "My dad did nothing but\x01",
            "skipping on the job, but\x01",
            "lately he's working properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*giggle*, even grandma\x01",
            "was happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2202")

    Jump("loc_238D")

    label("loc_2207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_238D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2310")
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        "#5SWhoa!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, do you need\x01",
            "something from me, my\x01",
            "cute frｴulein?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(W-W-W-W-W-Who IS this\x01",
            "man? He's ultra totally\x01",
            "my type!!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Hmm, how typical of\x01",
            "Wazy...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_238D")

    label("loc_2310")

    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "*sigh*, and what a\x01",
            "pretty face...㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(...Wait. Is he a boy? A\x01",
            "girl?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, what a strange\x01",
            "child.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238D")

    TalkEnd(0xFE)
    Return()

    # Function_10_13F2 end

    def Function_11_2391(): pass

    label("Function_11_2391")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2470")

    ChrTalk(
        0x9,
        (
            "Who would've ever\x01",
            "thought something like\x01",
            "that would appear...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...No, I can't lose\x01",
            "heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The mine was finally reopened\x01",
            "and everyone is motivated. I\x01",
            "must look forward positively.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24CE")

    label("loc_2470")


    ChrTalk(
        0x9,
        (
            "The mine was finally reopened\x01",
            "and everyone is motivated. I\x01",
            "must look forward positively.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24CE")

    Jump("loc_3382")

    label("loc_24D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_266D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25DE")

    ChrTalk(
        0x9,
        (
            "No large-scale operations have taken\x01",
            "place since the jaegers conducted\x01",
            "the resistance-hunt the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm worried about how\x01",
            "they'll react to the\x01",
            "declaration of invalidity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I want everyone in the\x01",
            "resistance to be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2668")

    label("loc_25DE")


    ChrTalk(
        0x9,
        (
            "I'm worried about how the\x01",
            "jaegers will react to the\x01",
            "declaration of invalidity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I want everyone in the\x01",
            "resistance to be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2668")

    Jump("loc_3382")

    label("loc_266D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_27CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2746")

    ChrTalk(
        0x9,
        (
            "When Mireille and the\x01",
            "others first arrived here,\x01",
            "we warned them too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The people of Mainz had\x01",
            "doubts about the President\x01",
            "and State Guard policies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is a battle of\x01",
            "wills.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27C8")

    label("loc_2746")


    ChrTalk(
        0x9,
        (
            "Like Mireille and the others,\x01",
            "the people of Mainz had doubts\x01",
            "about the President's policies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is a battle of\x01",
            "wills.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C8")

    Jump("loc_3382")

    label("loc_27CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_29E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2930")

    ChrTalk(
        0x9,
        (
            "Rumor has it that the Mainz occupation and the\x01",
            "attack on the city was an Imperial plot to\x01",
            "make us withdraw the independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They involved us, the innocent\x01",
            "people of Mainz, and caused great\x01",
            "damage to the CGF as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Sacrificing people for the\x01",
            "sake of politics... That's\x01",
            "something we can't condone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29E2")

    label("loc_2930")


    ChrTalk(
        0x9,
        (
            "Rumor has it that the Mainz\x01",
            "occupation and attack on the\x01",
            "city was an Imperial plot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sacrificing people for the\x01",
            "sake of politics... That's\x01",
            "something we can't condone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29E2")

    Jump("loc_3382")

    label("loc_29E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_29F5")
    Jump("loc_3382")

    label("loc_29F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADF")

    ChrTalk(
        0x9,
        (
            "Not even I, a Mainz resident,\x01",
            "knew that there's a studio\x01",
            "midway up the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, that studio's\x01",
            "meister never shows up\x01",
            "in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm guessing a rather\x01",
            "eccentric man lives\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B68")

    label("loc_2ADF")


    ChrTalk(
        0x9,
        (
            "The meister of the studio\x01",
            "midway up the mountain path\x01",
            "never shows up in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm guessing a rather\x01",
            "eccentric man lives\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B68")

    Jump("loc_3382")

    label("loc_2B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C58")

    ChrTalk(
        0x9,
        (
            "The monster that\x01",
            "recently appeared in the\x01",
            "north mountain region...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They say it had a form similar\x01",
            "to the one that showed up in\x01",
            "the Old Mine some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm... Could they be\x01",
            "related somehow?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D0D")

    label("loc_2C58")


    ChrTalk(
        0x9,
        (
            "I heard the monster in the north mountain\x01",
            "region and the one that showed up in the Old\x01",
            "Mine some time ago have a similar appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm... Could they be\x01",
            "related somehow?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0D")

    Jump("loc_3382")

    label("loc_2D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DDD")

    ChrTalk(
        0x9,
        (
            "It seems Gantz went\x01",
            "straight to the casino\x01",
            "again yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I partied big time with\x01",
            "everyone to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I joined them during it,\x01",
            "you know. Man, it was\x01",
            "quite fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E49")

    label("loc_2DDD")


    ChrTalk(
        0x9,
        (
            "Yesterday, the miners\x01",
            "partied big time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I joined them during it,\x01",
            "you know. Man, it was\x01",
            "quite fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E49")

    Jump("loc_3382")

    label("loc_2E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3064")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA2")

    ChrTalk(
        0x9,
        (
            "I went to deliver septium to the city this\x01",
            "morning, you know. While I was there, I\x01",
            "went to see the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It looked like everyone\x01",
            "had a great time at the\x01",
            "Orchis Tower unveiling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You'd probably get a great view of the\x01",
            "city from that high up. It's something\x01",
            "I want to see at least once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_305F")

    label("loc_2FA2")


    ChrTalk(
        0x9,
        (
            "It looked like everyone\x01",
            "had a great time at the\x01",
            "Orchis Tower unveiling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You'd probably get a great view of the\x01",
            "city from that high up. It's something\x01",
            "I want to see at least once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_305F")

    Jump("loc_3382")

    label("loc_3064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_320C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3159")

    ChrTalk(
        0x9,
        (
            "I transport the septium\x01",
            "we mine to the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On the mountain path there are\x01",
            "many curves and it's tough to\x01",
            "drive a loaded truck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's a lot of cliffs\x01",
            "too. Being cautious is\x01",
            "the most important thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3207")

    label("loc_3159")


    ChrTalk(
        0x9,
        (
            "There are many curves on the\x01",
            "mountain path and a loaded truck\x01",
            "easily sways left and right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's a lot of cliffs\x01",
            "too. Being cautious is\x01",
            "the most important thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3207")

    Jump("loc_3382")

    label("loc_320C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F7")

    ChrTalk(
        0x9,
        (
            "Gantz is working like\x01",
            "he's having a lot of fun\x01",
            "as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears that, through the\x01",
            "cult incident, he broke\x01",
            "through many of his worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone was worried,\x01",
            "but... At any rate, I'm\x01",
            "glad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3382")

    label("loc_32F7")


    ChrTalk(
        0x9,
        (
            "Through the cult incident,\x01",
            "it seems Gantz broke through\x01",
            "many of his worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone was worried,\x01",
            "but... At any rate, I'm\x01",
            "glad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3382")

    TalkEnd(0xFE)
    Return()

    # Function_11_2391 end

    def Function_12_3386(): pass

    label("Function_12_3386")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_34A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3417")

    ChrTalk(
        0xA,
        (
            "My dad and the rest of\x01",
            "the miners entered the\x01",
            "mine today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They all looked happy...\x01",
            "Ehehe, I'm happy too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34A0")

    label("loc_3417")


    ChrTalk(
        0xA,
        (
            "I'm worried about the huge\x01",
            "tree that appeared, but I'm\x01",
            "happy the mine reopened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I want father and the\x01",
            "others to do their best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A0")

    Jump("loc_3D7F")

    label("loc_34A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_352D")

    ChrTalk(
        0xA,
        (
            "They say that a pack of\x01",
            "wolves has been helping the\x01",
            "resistance guys lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They are very smart and\x01",
            "dependable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D7F")

    label("loc_352D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_364F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D2")

    ChrTalk(
        0xA,
        (
            "The situation being what\x01",
            "it is, even the mine is\x01",
            "closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm happy father is home,\x01",
            "but... As you might\x01",
            "imagine, he looks bored.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_364A")

    label("loc_35D2")


    ChrTalk(
        0xA,
        (
            "With the mine closed,\x01",
            "father looks bored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I like when my data\x01",
            "works as a miner too...\x01",
            "I hope it reopens soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_364A")

    Jump("loc_3D7F")

    label("loc_364F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374F")

    ChrTalk(
        0xA,
        (
            "When those bad guys came,\x01",
            "the miners rose up against\x01",
            "them to protect the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, they were no match\x01",
            "for them... Father was pushed\x01",
            "away and he hurt himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It wasn't serious, but I\x01",
            "was incredibly\x01",
            "worried...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3803")

    label("loc_374F")


    ChrTalk(
        0xA,
        (
            "Father and the others fought the bad\x01",
            "guys to protect the town, but... In\x01",
            "the end, they were no match for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He wasn't seriously\x01",
            "injured, but I was\x01",
            "incredibly worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3803")

    Jump("loc_3D7F")

    label("loc_3808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3816")
    Jump("loc_3D7F")

    label("loc_3816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_387B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3831")
    Call(0, 13)
    Jump("loc_3876")

    label("loc_3831")


    ChrTalk(
        0xA,
        (
            "Ahaha, mountain echoes\x01",
            "are fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What should I scream\x01",
            "next?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3876")

    Jump("loc_3D7F")

    label("loc_387B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_39F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A2")

    ChrTalk(
        0xA,
        (
            "Recently, they say Logy\x01",
            "hasn't been skipping out\x01",
            "on the job at all anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He said that he was just doing it\x01",
            "unwillingly, but... His face looked\x01",
            "like he was enjoying it a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I too want to become a\x01",
            "splendid miner who can do\x01",
            "his job while enjoying it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_39F3")

    label("loc_39A2")


    ChrTalk(
        0xA,
        (
            "I too want to become a\x01",
            "splendid miner who can do\x01",
            "his job while enjoying it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F3")

    Jump("loc_3D7F")

    label("loc_39F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AAA")

    ChrTalk(
        0xA,
        (
            "Sunday School was held\x01",
            "here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It wasn't the usual\x01",
            "sister, but she taught\x01",
            "us gently and politely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ehehe, I'd like to see\x01",
            "her again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B38")

    label("loc_3AAA")


    ChrTalk(
        0xA,
        (
            "Our usual sister didn't come today,\x01",
            "but the one that did come taught us\x01",
            "very gently and politely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ehehe, I'd like to see\x01",
            "her again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B38")

    Jump("loc_3D7F")

    label("loc_3B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BDE")

    ChrTalk(
        0xA,
        "Ugh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The other day, I was\x01",
            "severely scolded by\x01",
            "father and mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder if entering the\x01",
            "mine is really that\x01",
            "bad...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C23")

    label("loc_3BDE")


    ChrTalk(
        0xA,
        (
            "I wonder if entering the\x01",
            "mine is really that\x01",
            "bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ugh...\x02",
    )

    CloseMessageWindow()

    label("loc_3C23")

    Jump("loc_3D7F")

    label("loc_3C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C36")
    Jump("loc_3D7F")

    label("loc_3C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3D7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D13")

    ChrTalk(
        0xA,
        (
            "Early this morning, the\x01",
            "gate of the Old Mine\x01",
            "outside of town was open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When I tried sneaking inside,\x01",
            "I was immediately caught by\x01",
            "Gantz who scolded me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Tch, I wanted to\x01",
            "explore...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D7F")

    label("loc_3D13")


    ChrTalk(
        0xA,
        (
            "I've wanted to explore\x01",
            "the Old Mine for a long\x01",
            "time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I got scolded, so it\x01",
            "can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D7F")

    TalkEnd(0xFE)
    Return()

    # Function_12_3386 end

    def Function_13_3D83(): pass

    label("Function_13_3D83")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xA,
        "#4SYAAHHOO!!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("Echo")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "......H...... HOO......\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0xC,
        "#4SI love daddy a tooon!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("Echo")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "......a tooon......\x01",
            "tooon......\x07\x00\x02",
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

    # Function_13_3D83 end

    def Function_14_3E51(): pass

    label("Function_14_3E51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E62")
    Jump("loc_431C")

    label("loc_3E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3EA1")

    ChrTalk(
        0xB,
        "*sigh*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Won't the mine\x01",
            "reopen...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_431C")

    label("loc_3EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6A")

    ChrTalk(
        0xB,
        (
            "Ever since we became an independent\x01",
            "state, I feel like I've gone back\x01",
            "to my old boring life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*siiiiigh*... And just when\x01",
            "I finally got motivated for\x01",
            "my mining job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3FF2")

    label("loc_3F6A")


    ChrTalk(
        0xB,
        (
            "And just when I finally\x01",
            "got motivated for my\x01",
            "mining job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At this rate I guess\x01",
            "I'll be going back to a\x01",
            "lazy lifestyle again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF2")

    Jump("loc_431C")

    label("loc_3FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4005")
    Jump("loc_431C")

    label("loc_4005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4013")
    Jump("loc_431C")

    label("loc_4013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4021")
    Jump("loc_431C")

    label("loc_4021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_402F")
    Jump("loc_431C")

    label("loc_402F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_403D")
    Jump("loc_431C")

    label("loc_403D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_404B")
    Jump("loc_431C")

    label("loc_404B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4059")
    Jump("loc_431C")

    label("loc_4059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_431C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41AB")

    ChrTalk(
        0xB,
        (
            "Before, I worked slowly\x01",
            "and sometimes skipped\x01",
            "out on the job, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I haven't been doing that at\x01",
            "all recently, and I don't even\x01",
            "have the time to read a book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This book... I don't\x01",
            "mind if you have it.\x01",
            "Here, please take it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2EF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2EF, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 1)
    Jump("loc_431C")

    label("loc_41AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42BB")

    ChrTalk(
        0xB,
        (
            "I really want to work slowly\x01",
            "and skip out on work\x01",
            "sometimes like before, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Recently, because all the others\x01",
            "are in high spirits, slacking has\x01",
            "become difficult for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Maybe it's time I got\x01",
            "motivated. *sigh*, what\x01",
            "a bother...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_431C")

    label("loc_42BB")


    ChrTalk(
        0xB,
        (
            "...It's not that I'm skipping out\x01",
            "on work right now. I'm relaxing\x01",
            "properly during my break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_431C")

    TalkEnd(0xFE)
    Return()

    # Function_14_3E51 end

    def Function_15_4320(): pass

    label("Function_15_4320")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4331")
    Jump("loc_4572")

    label("loc_4331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_433F")
    Jump("loc_4572")

    label("loc_433F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_43DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435A")
    Call(0, 13)
    Jump("loc_43D5")

    label("loc_435A")


    ChrTalk(
        0xC,
        (
            "Amazing, amazing, the\x01",
            "voice came back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Could there be a child\x01",
            "like Kimmy on the other\x01",
            "side of that mountain too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D5")

    Jump("loc_4572")

    label("loc_43DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_43E8")
    Jump("loc_4572")

    label("loc_43E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_454D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C3")

    ChrTalk(
        0xC,
        (
            "The sister? She already\x01",
            "went back to the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, when she left, it\x01",
            "seemed like she was worried\x01",
            "about the sky in that direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. Could there be\x01",
            "something there?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4548")

    label("loc_44C3")


    ChrTalk(
        0xC,
        (
            "When the sister went back, it\x01",
            "seemed she was worried about\x01",
            "the sky in that direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. Could there be\x01",
            "something there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4548")

    Jump("loc_4572")

    label("loc_454D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_455B")
    Jump("loc_4572")

    label("loc_455B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4569")
    Jump("loc_4572")

    label("loc_4569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_4572")

    label("loc_4572")

    TalkEnd(0xFE)
    Return()

    # Function_15_4320 end

    def Function_16_4576(): pass

    label("Function_16_4576")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4587")
    Jump("loc_468D")

    label("loc_4587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4684")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4647")

    ChrTalk(
        0xD,
        (
            "We'd like to do something ourselves,\x01",
            "but... We can't help that girl and\x01",
            "the others from the resistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...As I thought, all\x01",
            "miners can do is dig\x01",
            "holes...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_467F")

    label("loc_4647")


    ChrTalk(
        0xD,
        (
            "...As I thought, all\x01",
            "miners can do is dig\x01",
            "holes...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_467F")

    Jump("loc_468D")

    label("loc_4684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_468D")

    label("loc_468D")

    TalkEnd(0xFE)
    Return()

    # Function_16_4576 end

    def Function_17_4691(): pass

    label("Function_17_4691")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_46A2")
    Jump("loc_47D7")

    label("loc_46A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_47CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4746")

    ChrTalk(
        0xE,
        (
            "Lycka kicked us out of\x01",
            "the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "She said it was so the resistance\x01",
            "leader can rest at leisure...\x01",
            "Well, can't be helped I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_47C9")

    label("loc_4746")


    ChrTalk(
        0xE,
        (
            "...Anyhow, this is the first\x01",
            "time I've taken a break from\x01",
            "mining for this long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I never thought I'd miss\x01",
            "it this much...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47C9")

    Jump("loc_47D7")

    label("loc_47CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_47D7")

    label("loc_47D7")

    TalkEnd(0xFE)
    Return()

    # Function_17_4691 end

    def Function_18_47DB(): pass

    label("Function_18_47DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC8")

    ChrTalk(
        0xFE,
        (
            "When the Mainz mine reopened, I\x01",
            "exterminated a highly dangerous\x01",
            "monster that got restless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wasn't anything special compared to a Magic\x01",
            "Soldier or a Cryptid, but monster extermination\x01",
            "is a tough job for one man alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHaha... You're amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FI guess that's what you can\x01",
            "expect from an able bracer\x01",
            "from the Imperial Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, I still have a\x01",
            "long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...The Empire is in the middle\x01",
            "of a civil war. I wonder how\x01",
            "my former home is doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "...No, I mustn't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to first deal with what's in front of me...\x01",
            "Because those who can't do that and look back at\x01",
            "their past aren't qualified to desire a future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Haha. Strict as\x01",
            "always.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 3)
    Jump("loc_4BE9")

    label("loc_4AC8")


    ChrTalk(
        0xFE,
        (
            "Although the President\x01",
            "was arrested, Crossbell\x01",
            "is in a sticky situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Even the guys who are resting at the\x01",
            "inn... When their stamina is back, I'll\x01",
            "have them help me out with various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These may be hard times...\x01",
            "But that's exactly why we\x01",
            "have to brace ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE9")

    TalkEnd(0xFE)
    Return()

    # Function_18_47DB end

    def Function_19_4BED(): pass

    label("Function_19_4BED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CF3")

    ChrTalk(
        0xFE,
        (
            "The Mainz mountain range.\x01",
            "I failed the challenge a\x01",
            "little time ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll train my legs and loins, and\x01",
            "no matter how many years it takes,\x01",
            "I'll absolutely walk it on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...A declaration of\x01",
            "resolve, for the time\x01",
            "being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4D71")

    label("loc_4CF3")


    ChrTalk(
        0xFE,
        (
            "I finished my declaration\x01",
            "of resolve... I guess\x01",
            "it's time I to go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a while. I\x01",
            "want to see my friend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D71")

    TalkEnd(0xFE)
    Return()

    # Function_19_4BED end

    def Function_20_4D75(): pass

    label("Function_20_4D75")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DA7")
    SetScenarioFlags(0x31, 2)

    label("loc_4DA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4DED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_4DE7")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4DDC")
    Sound(2499, 255, 100, 0)
    Jump("loc_4DE2")

    label("loc_4DDC")

    Sound(3537, 255, 100, 0)

    label("loc_4DE2")

    Jump("loc_4DED")

    label("loc_4DE7")

    Sound(3344, 255, 100, 0)

    label("loc_4DED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4E62")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4E42"),
        (SWITCH_DEFAULT, "loc_4E53"),
    )


    label("loc_4E42")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4E5D")

    label("loc_4E53")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E5D")

    Jump("loc_509F")

    label("loc_4E62")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4E94")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_4E94")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4EC8"),
        (1, "loc_4FCC"),
        (2, "loc_505D"),
        (SWITCH_DEFAULT, "loc_5095"),
    )


    label("loc_4EC8")

    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4EF9")
    OP_70(0x9, 0x12C)
    OP_71(0x9, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4F09")

    label("loc_4EF9")

    OP_70(0x9, 0xF0)
    OP_71(0x9, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4F09")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F5F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F5F")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F82")
    Sound(461, 0, 100, 0)

    label("loc_4F82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4FA2")
    OP_70(0x9, 0x14A)
    OP_71(0x9, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_4FB2")

    label("loc_4FA2")

    OP_70(0x9, 0x10E)
    OP_71(0x9, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_4FB2")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x9, "light", 0x1, 0x1)
    OP_70(0x9, 0x0)
    Jump("loc_4DED")

    label("loc_4FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_503E")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_5001")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_5019")

    label("loc_5001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5014")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_5019")

    label("loc_5014")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_5019")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5058")

    label("loc_503E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_504E")
    OP_AF(0xFB)
    Jump("loc_5058")

    label("loc_504E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5058")

    Jump("loc_509F")

    label("loc_505D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5076")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5090")

    label("loc_5076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5086")
    OP_AF(0xFB)
    Jump("loc_5090")

    label("loc_5086")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5090")

    Jump("loc_509F")

    label("loc_5095")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_509F")

    Jump("loc_4DED")

    label("loc_50A4")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_4D75 end

    def Function_21_50B2(): pass

    label("Function_21_50B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5102")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems the orbal bus service is not running.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_5102")

    Call(0, 6)
    Return()

    # Function_21_50B2 end

    def Function_22_5106(): pass

    label("Function_22_5106")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D3")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─Lloyd and the others returned to Mainz and explained\x01",
            "the general situation to the mayor and the others.\x02\x03",
            "But, the criminal who destroyed the old mine entrance\x01",
            "and set the explosive trap was unclear, and the\x01",
            "strangeness of the tunnels was unexplained as well.\x02\x03",
            "Then, after they searched the area once more for\x01",
            "anyone suspicious...\x02\x03",
            "Lloyd and the others requested a CGF patrol and\x01",
            "decided to return to Crossbell City.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_52D3")

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

    # Function_22_5106 end

    def Function_23_5714(): pass

    label("Function_23_5714")

    OP_79(0x9)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    Return()

    # Function_23_5714 end

    def Function_24_5724(): pass

    label("Function_24_5724")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_573F")
    Sleep(300)
    Jump("loc_5793")

    label("loc_573F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_575A")
    Sleep(600)
    Jump("loc_5793")

    label("loc_575A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5775")
    Sleep(900)
    Jump("loc_5793")

    label("loc_5775")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5790")
    Sleep(1200)
    Jump("loc_5793")

    label("loc_5790")

    Sleep(1500)

    label("loc_5793")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57BE")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_5793")

    label("loc_57BE")

    Return()

    # Function_24_5724 end

    def Function_25_57BF(): pass

    label("Function_25_57BF")

    Return()

    # Function_25_57BF end

    def Function_26_57C0(): pass

    label("Function_26_57C0")

    Return()

    # Function_26_57C0 end

    def Function_27_57C1(): pass

    label("Function_27_57C1")

    Return()

    # Function_27_57C1 end

    def Function_28_57C2(): pass

    label("Function_28_57C2")

    OP_9B(0x0, 0xFE, 0x1, 0x2328, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x50, 0xFA0, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Return()

    # Function_28_57C2 end

    def Function_29_5800(): pass

    label("Function_29_5800")

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

    def lambda_585F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_585F)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_5800 end

    def Function_30_5883(): pass

    label("Function_30_5883")

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

    def lambda_58E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_58E9)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_5883 end

    def Function_31_590D(): pass

    label("Function_31_590D")

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

    def lambda_5974():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5974)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_590D end

    def Function_32_5998(): pass

    label("Function_32_5998")

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

    def lambda_59F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_59F7)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_5998 end

    def Function_33_5A1B(): pass

    label("Function_33_5A1B")

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

    def lambda_5AEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5AEF)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_5A1B end

    def Function_34_5B13(): pass

    label("Function_34_5B13")

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

    # Function_34_5B13 end

    def Function_35_5BB7(): pass

    label("Function_35_5BB7")

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

    # Function_35_5BB7 end

    def Function_36_5BF4(): pass

    label("Function_36_5BF4")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -4500, -2000, 18000)
    OP_9F(0x1, -4500, -2000, 16000)
    OP_9F(0x1, -4000, -2000, 12000)
    OP_9F(0x1, -1500, -2000, 6000)
    OP_9F(0x1, 500, -2000, 0)
    OP_9F(0x1, 500, -2000, -12000)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_36_5BF4 end

    def Function_37_5C56(): pass

    label("Function_37_5C56")

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

    # Function_37_5C56 end

    def Function_38_5D37(): pass

    label("Function_38_5D37")

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
            "#00006F#5PPhew... We ended up\x01",
            "walking all the way\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    ChrTalk(
        0x102,
        "#00100F#11PNoｱl, Wazy, you ok?\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x2D, 0x1F4)

    ChrTalk(
        0x109,
        "#10102F#6PYes, no problem here.\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#10306F#6PI'm fine too, but... The\x01",
            "Support Section really\x01",
            "is strange, huh.\x02\x03",
            "#10301FHonestly, a car or bus\x01",
            "would have been better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PHaha, it's training too,\x01",
            "so this kills two birds\x01",
            "with one stone.\x02\x03",
            "#00004FIn any case...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00012F#5PYou've really built up\x01",
            "your stamina, Elie.\x02\x03",
            "#00000FWhen you started, a short\x01",
            "walk on the highway left\x01",
            "you out of breath...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00109F#12PHaha, well I was able to\x01",
            "train thanks to a\x01",
            "certain group of people.\x02\x03",
            "#00100FSo, what do we do? Do we\x01",
            "see the mayor\x01",
            "immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, let's.\x02\x03",
            "#00000FIf we enter town and go\x01",
            "straight, his house is\x01",
            "right there.\x02",
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

    # Function_38_5D37 end

    def Function_39_6161(): pass

    label("Function_39_6161")

    Sleep(5500)

    def lambda_6169():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6169)

    def lambda_617A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_617A)

    def lambda_618B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_618B)

    def lambda_619C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_619C)
    BeginChrThread(0x101, 0, 0, 40)
    BeginChrThread(0x102, 0, 0, 41)
    BeginChrThread(0x109, 0, 0, 42)
    BeginChrThread(0x105, 0, 0, 43)
    Return()

    # Function_39_6161 end

    def Function_40_61C1(): pass

    label("Function_40_61C1")

    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_40_61C1 end

    def Function_41_61D1(): pass

    label("Function_41_61D1")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x3714, 0x7D0, 0x0)
    Return()

    # Function_41_61D1 end

    def Function_42_61E4(): pass

    label("Function_42_61E4")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x37DC, 0x7D0, 0x0)
    Return()

    # Function_42_61E4 end

    def Function_43_61F7(): pass

    label("Function_43_61F7")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
    Return()

    # Function_43_61F7 end

    def Function_44_620A(): pass

    label("Function_44_620A")

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

    def lambda_637C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_637C)
    Sleep(50)

    def lambda_638C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_638C)
    Sleep(50)

    def lambda_639C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_639C)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66C8")

    ChrTalk(
        0x102,
        (
            "#00104F#5P*giggle*... That was\x01",
            "fast.\x02\x03",
            "#00100FThere was clear weather\x01",
            "on the mountain path,\x01",
            "just like we'd heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PYeah, and the scenery\x01",
            "after the rain was\x01",
            "pretty, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#12PHmm, but still, this car\x01",
            "is something else.\x02\x03",
            "#10102FEven on the mountain\x01",
            "path, it handled\x01",
            "perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PThat's ZCF for you. I bet\x01",
            "it'll sell well when it's\x01",
            "officially released.\x02\x03",
            "#10300FSo, this mining town\x01",
            "mayor wants to speak with\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#5PYes, Mayor Bickson is\x01",
            "his name.\x02\x03",
            "If we enter town and go\x01",
            "straight, his house is\x01",
            "right there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, let's go.\x02\x03",
            "#00003F(...Come to think of it, the\x01",
            "path to the Doll Studio is on\x01",
            "the mountain path, huh.)\x02\x03",
            "#00008F(Renne isn't here anymore,\x01",
            "but... I kind of wanted to\x01",
            "check on the situation there.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69C4")

    label("loc_66C8")


    ChrTalk(
        0x105,
        (
            "#10305F#6PWow, so this is Mainz.\x02\x03",
            "#10302FI knew the name, but\x01",
            "this is my first time\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PWell, unless you had business\x01",
            "here, there'd normally be no\x01",
            "reason to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#5PCome to think of it, you\x01",
            "come to Mainz quite\x01",
            "often, right Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#12PYes. It's a stop on our\x01",
            "regular patrol routes.\x02\x03",
            "#10102FThe Special Support\x01",
            "Section has a connection\x01",
            "to Mainz, don't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PHah. I guess you could\x01",
            "say that.\x02\x03",
            "#00000FWe worked together on the\x01",
            "military dogs and temple\x01",
            "investigation cases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PT-That's right... (I\x01",
            "remembered some things\x01",
            "I'd rather not.)\x02\x03",
            "#00100FSo, what do we do? Do we\x01",
            "see the mayor\x01",
            "immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, let's.\x02\x03",
            "#00000FIf we enter town and go\x01",
            "straight, his house is\x01",
            "right there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69C4")

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

    # Function_44_620A end

    def Function_45_69FD(): pass

    label("Function_45_69FD")

    Sleep(5500)
    BeginChrThread(0x18, 0, 0, 46)
    WaitChrThread(0x18, 0)
    BeginChrThread(0x18, 0, 0, 47)
    BeginChrThread(0x1E, 1, 0, 52)
    Return()

    # Function_45_69FD end

    def Function_46_6A17(): pass

    label("Function_46_6A17")

    SetChrPos(0xFE, 0, -1950, -500, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x2CEC, 0xFA0, 0x0)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFEB7E0, 0xBB8, 0x1)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFFF060, 0x7D0, 0x1)
    OP_71(0x9, 0x5B, 0x78, 0x1, 0x8)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFFF830, 0x3E8, 0x1)
    Sleep(300)
    Return()

    # Function_46_6A17 end

    def Function_47_6A86(): pass

    label("Function_47_6A86")

    OP_74(0x9, 0xA)
    OP_71(0x9, 0xB4, 0x79, 0x0, 0x20)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF448, 0x7D0, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFEC398, 0xBB8, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF060, 0x7D0, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF830, 0x3E8, 0x4)
    OP_70(0x9, 0x78)
    Return()

    # Function_47_6A86 end

    def Function_48_6AEF(): pass

    label("Function_48_6AEF")


    def lambda_6AF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6AF4)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x145, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_48_6AEF end

    def Function_49_6B2D(): pass

    label("Function_49_6B2D")

    Sleep(1300)

    def lambda_6B35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B35)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x6D6, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_49_6B2D end

    def Function_50_6B6E(): pass

    label("Function_50_6B6E")

    Sleep(2600)

    def lambda_6B76():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B76)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_50_6B6E end

    def Function_51_6BAF(): pass

    label("Function_51_6BAF")

    Sleep(3900)

    def lambda_6BB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6BB7)
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

    # Function_51_6BAF end

    def Function_52_6C22(): pass

    label("Function_52_6C22")

    Sound(494, 0, 50, 0)
    Sleep(2000)
    Sound(459, 0, 100, 0)
    Sleep(2300)
    Sound(492, 0, 60, 0)
    Return()

    # Function_52_6C22 end

    def Function_53_6C3B(): pass

    label("Function_53_6C3B")

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

    def lambda_6D39():

        label("loc_6D39")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6D39")

    QueueWorkItem2(0x101, 2, lambda_6D39)

    def lambda_6D4B():

        label("loc_6D4B")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6D4B")

    QueueWorkItem2(0x102, 2, lambda_6D4B)

    def lambda_6D5D():

        label("loc_6D5D")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6D5D")

    QueueWorkItem2(0x109, 2, lambda_6D5D)

    def lambda_6D6F():

        label("loc_6D6F")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6D6F")

    QueueWorkItem2(0x105, 2, lambda_6D6F)
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

    def lambda_6DDB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6DDB)
    Sleep(50)

    def lambda_6DEB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6DEB)
    Sleep(50)

    def lambda_6DFB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6DFB)
    Sleep(50)

    def lambda_6E0B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6E0B)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_716A")

    ChrTalk(
        0x102,
        (
            "#00104F#12P*giggle*... That was\x01",
            "fast.\x02\x03",
            "#00100FThere was clear weather\x01",
            "on the mountain path,\x01",
            "just like we'd heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PYeah, and the scenery\x01",
            "after the rain was\x01",
            "pretty, eh?\x02\x03",
            "#00006FStill, even though we\x01",
            "have a car, we ended up\x01",
            "riding the bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PHaha. I like buses too,\x01",
            "you know.\x02\x03",
            "#10102FIt was nice to take it\x01",
            "easy and relax for a\x01",
            "change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PIt was a fresh\x01",
            "experience, because I\x01",
            "hardly ever ride them.\x02\x03",
            "#10300FSo, this mining town\x01",
            "mayor wants to speak\x01",
            "with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PYes, Mayor Bickson is\x01",
            "his name.\x02\x03",
            "If we enter town and go\x01",
            "straight, his house is\x01",
            "right there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, let's go.\x02\x03",
            "#00003F(...Come to think of it, the\x01",
            "path to the Doll Studio is on\x01",
            "the mountain path, huh.)\x02\x03",
            "#00008F(Renne isn't here anymore,\x01",
            "but... I kind of wanted to\x01",
            "check on the situation there.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7468")

    label("loc_716A")


    ChrTalk(
        0x105,
        (
            "#10305F#6PWow, so this is Mainz.\x02\x03",
            "#10302FI knew the name, but\x01",
            "this is my first time\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PWell, unless you had business\x01",
            "here, there'd normally be no\x01",
            "reason to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12PCome to think of it, you\x01",
            "come to Mainz quite\x01",
            "often, right Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#5PYes. It's a stop on our\x01",
            "regular patrol routes.\x02\x03",
            "#10102FThe Special Support\x01",
            "Section has a connection\x01",
            "to Mainz, don't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PHah. I guess you could\x01",
            "say that.\x02\x03",
            "#00000FWe worked together on the\x01",
            "military dogs and temple\x01",
            "investigation cases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PT-That's right... (I\x01",
            "remembered some things\x01",
            "I'd rather not.)\x02\x03",
            "#00100FSo, what do we do? Do we\x01",
            "see the mayor\x01",
            "immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, let's.\x02\x03",
            "#00000FIf we enter town and go\x01",
            "straight, his house is\x01",
            "right there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7468")

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

    # Function_53_6C3B end

    def Function_54_74A7(): pass

    label("Function_54_74A7")

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

    # Function_54_74A7 end

    def Function_55_74DF(): pass

    label("Function_55_74DF")

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

    # Function_55_74DF end

    def Function_56_7586(): pass

    label("Function_56_7586")

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

    # Function_56_7586 end

    def Function_57_7615(): pass

    label("Function_57_7615")

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

    def lambda_7B1C():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7B1C)
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
            "#07904F#5PIt seems even Red\x01",
            "Constellation has retreated\x01",
            "for the time being.\x02\x03",
            "#07902FAnd there's no traces of\x01",
            "pillaging either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#12PIs that right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12PThank goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PThey don't pillage unless they\x01",
            "need to.\x02\x03",
            "#00308FConversely, if they did need to,\x01",
            "they'd have probably done\x01",
            "everything they're capable of...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)

    def lambda_7DC2():
        TurnDirection(0x17, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_7DC2)
    Sleep(50)

    def lambda_7DD2():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7DD2)
    Sleep(50)

    def lambda_7DE2():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7DE2)
    Sleep(50)

    def lambda_7DF2():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7DF2)
    Sleep(50)

    def lambda_7E02():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7E02)
    Sleep(50)

    def lambda_7E12():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7E12)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10105F#12PRandy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07908F#5PYou ok? I heard you did\x01",
            "something quite\x01",
            "reckless, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#11PWell, it's no big deal.\x02\x03",
            "#00306FAlthough the rifle I went to\x01",
            "great pains to unseal is gonna\x01",
            "be of no use for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PIt was chewed up pretty\x01",
            "bad by that ridiculous\x01",
            "chainsaw, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PBut speaking of Shirley's\x01",
            "chainsaw rifle...\x02\x03",
            "#00201FThe Red Constellation\x01",
            "jaegers have some peculiar\x01",
            "equipment, don't they.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00303F#5PYeah, they're custom\x01",
            "ordered from a specialized\x01",
            "weapons factory, but...\x02\x03",
            "#00302FWell, someone like Master\x01",
            "Guillaume should be able\x01",
            "to repair it somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah, that's a good\x01",
            "idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12P*giggle*, shall we stop\x01",
            "by by once we're back in\x01",
            "the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07904F#5P...Still, I'm glad.\x02\x03",
            "#07902FYou're able to use\x01",
            "rifles once again.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00300F#11PHaha... It's a little\x01",
            "late for that, though.\x02\x03",
            "#00309FMan, I've worried you a\x01",
            "lot too, haven't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07906F#5PT-That's right... If you had\x01",
            "used rifles from the start you'd\x01",
            "still be assigned to the CGF...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_8270():
        TurnDirection(0x101, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8270)
    Sleep(50)

    def lambda_8280():
        TurnDirection(0x102, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8280)
    Sleep(50)

    def lambda_8290():
        TurnDirection(0x103, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8290)
    Sleep(50)

    def lambda_82A0():
        TurnDirection(0x109, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_82A0)
    Sleep(50)

    def lambda_82B0():
        TurnDirection(0x105, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_82B0)
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
            "#07911F#5PD-Don't get me wrong, ok!?\x02\x03",
            "You see, I'm just wondering if\x01",
            "this irresponsible man can do\x01",
            "a proper job somewhere else!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#12P(Haha...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12P(She's charming,\x01",
            "somehow.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6P(I think Randy has\x01",
            "realized it too...)\x02",
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
            "#07903F#11P*cough*... Mireille of\x01",
            "1st Company speaking.\x02\x03",
            "#07902FI see, nice work. So,\x01",
            "about their movements...\x02\x03",
            "#07905F#30W...............\x02\x03",
            "#07908F...What did you say?\x02",
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
        "#00005F#12PI-Is something wrong?\x02",
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
            "#07906F#5P...It appears that the\x01",
            "jaegers who retreated\x01",
            "vanished all of a sudden.\x02\x03",
            "#07901FIt seems they fled toward\x01",
            "the ruins at the split in\x01",
            "the tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PThe Temple of Moon...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PUmm... Didn't they take\x01",
            "refuge in the ruins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07903F#5PNo, it seems there were no traces\x01",
            "of them having broken through the\x01",
            "blockade in front of the ruins.\x02\x03",
            "#07908FWhere on earth did they...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11P...Around there, it's\x01",
            "all just steep cliffs...\x02\x03",
            "#10101FThere's no other place\x01",
            "they could've retreated\x01",
            "to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#12PHmm. It seems like common\x01",
            "sense doesn't work against\x01",
            "that Shirley girl, but...\x02",
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
            "#00306F#11P─I thought that was strange.\x02\x03",
            "#00301FThose guys in the Mainz region...\x01",
            "No matter how I think about it,\x01",
            "there were too few of them.\x02",
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

    def lambda_8995():
        TurnDirection(0x17, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_8995)
    Sleep(50)

    def lambda_89A5():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_89A5)
    Sleep(50)

    def lambda_89B5():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_89B5)
    Sleep(50)

    def lambda_89C5():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_89C5)
    Sleep(50)

    def lambda_89D5():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_89D5)
    Sleep(50)

    def lambda_89E5():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_89E5)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00011F#6PWhat...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#00303F#5PA lot of them came to\x01",
            "Crossbell, about a\x01",
            "hundred people...\x02\x03",
            "But in the Mainz area,\x01",
            "there were 20 at best.\x02\x03",
            "#00308F...And above all,\x01",
            "Sigmund Orlando─\x02\x03",
            "#00311FWhere did that bigger\x01",
            "monster than Shirley run\x01",
            "off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#07907F#5PT-That's...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x87, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#00205F#5PAh...\x02\x03",
            "#00207F#4S─Everyone, look at that!\x02",
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

    def lambda_8C52():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8C52)
    Sleep(20)

    def lambda_8C62():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8C62)
    Sleep(20)

    def lambda_8C72():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8C72)
    Sleep(20)

    def lambda_8C82():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8C82)
    Sleep(20)

    def lambda_8C92():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8C92)
    Sleep(20)

    def lambda_8CA2():
        OP_93(0x17, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_8CA2)
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
        "#00107FT-That's...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(280, 280, -1, -1)

    AnonymousTalk(
        0x109,
        "#10110FN-No way!\x02",
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
            "#00007FCrossbell City is\x01",
            "burning!?\x02",
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

    # Function_57_7615 end

    def Function_58_8EBB(): pass

    label("Function_58_8EBB")

    OP_96(0xFE, 0x28A, 0x0, 0xD41C, 0x3E8, 0x0)
    OP_95(0xFE, 650, 0, 55950, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_58_8EBB end

    def Function_59_8EEB(): pass

    label("Function_59_8EEB")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_8EFA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_8EFA)
    OP_95(0xFE, 3000, 0, 54800, 3000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_59_8EEB end

    def Function_60_8F41(): pass

    label("Function_60_8F41")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_8F50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_8F50)
    OP_95(0xFE, 3000, 0, 53800, 3000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_60_8F41 end

    def Function_61_8F94(): pass

    label("Function_61_8F94")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_8FA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_8FA3)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 650, 0, 54950, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_61_8F94 end

    def Function_62_8FFE(): pass

    label("Function_62_8FFE")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_900D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_900D)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_95(0xFE, 1150, 0, 51250, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_62_8FFE end

    def Function_63_905E(): pass

    label("Function_63_905E")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_906D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_906D)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_95(0xFE, 2400, 0, 52100, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_63_905E end

    def Function_64_90BE(): pass

    label("Function_64_90BE")

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

    # Function_64_90BE end

    def Function_65_92CC(): pass

    label("Function_65_92CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9318")
    OP_95(0xFE, 4450, -2000, 1050, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, 6000, -2000, 3050, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    Jump("Function_65_92CC")

    label("loc_9318")

    Return()

    # Function_65_92CC end

    def Function_66_9319(): pass

    label("Function_66_9319")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9365")
    OP_95(0xFE, -1850, -2000, 2250, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, -2350, -2000, 9550, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    Jump("Function_66_9319")

    label("loc_9365")

    Return()

    # Function_66_9319 end

    def Function_67_9366(): pass

    label("Function_67_9366")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_938A")
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(2000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2000)
    Jump("Function_67_9366")

    label("loc_938A")

    Return()

    # Function_67_9366 end

    def Function_68_938B(): pass

    label("Function_68_938B")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is tightly\x01",
            "shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_68_938B end

    SaveToFile()

Try(main)
