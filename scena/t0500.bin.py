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
        "Function_7_11EE",         # 07, 7
        "Function_8_1321",         # 08, 8
        "Function_9_1372",         # 09, 9
        "Function_10_1406",        # 0A, 10
        "Function_11_23B5",        # 0B, 11
        "Function_12_33D3",        # 0C, 12
        "Function_13_3E0C",        # 0D, 13
        "Function_14_3ED8",        # 0E, 14
        "Function_15_43C5",        # 0F, 15
        "Function_16_4632",        # 10, 16
        "Function_17_4758",        # 11, 17
        "Function_18_48C2",        # 12, 18
        "Function_19_4CFA",        # 13, 19
        "Function_20_4E87",        # 14, 20
        "Function_21_51C0",        # 15, 21
        "Function_22_5214",        # 16, 22
        "Function_23_586E",        # 17, 23
        "Function_24_587E",        # 18, 24
        "Function_25_5919",        # 19, 25
        "Function_26_591A",        # 1A, 26
        "Function_27_591B",        # 1B, 27
        "Function_28_591C",        # 1C, 28
        "Function_29_595A",        # 1D, 29
        "Function_30_59DD",        # 1E, 30
        "Function_31_5A67",        # 1F, 31
        "Function_32_5AF2",        # 20, 32
        "Function_33_5B75",        # 21, 33
        "Function_34_5C6D",        # 22, 34
        "Function_35_5D11",        # 23, 35
        "Function_36_5D4E",        # 24, 36
        "Function_37_5DB0",        # 25, 37
        "Function_38_5E91",        # 26, 38
        "Function_39_6313",        # 27, 39
        "Function_40_6373",        # 28, 40
        "Function_41_6383",        # 29, 41
        "Function_42_6396",        # 2A, 42
        "Function_43_63A9",        # 2B, 43
        "Function_44_63BC",        # 2C, 44
        "Function_45_6C21",        # 2D, 45
        "Function_46_6C3B",        # 2E, 46
        "Function_47_6CAA",        # 2F, 47
        "Function_48_6D13",        # 30, 48
        "Function_49_6D51",        # 31, 49
        "Function_50_6D92",        # 32, 50
        "Function_51_6DD3",        # 33, 51
        "Function_52_6E46",        # 34, 52
        "Function_53_6E5F",        # 35, 53
        "Function_54_7719",        # 36, 54
        "Function_55_7751",        # 37, 55
        "Function_56_77F8",        # 38, 56
        "Function_57_7887",        # 39, 57
        "Function_58_922D",        # 3A, 58
        "Function_59_925D",        # 3B, 59
        "Function_60_92B3",        # 3C, 60
        "Function_61_9306",        # 3D, 61
        "Function_62_9370",        # 3E, 62
        "Function_63_93D0",        # 3F, 63
        "Function_64_9430",        # 40, 64
        "Function_65_963E",        # 41, 65
        "Function_66_968B",        # 42, 66
        "Function_67_96D8",        # 43, 67
        "Function_68_96FD",        # 44, 68
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1125")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you inspect the bus stop signboard,\x01",
            "you will be able to ride the orbal bus.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please use it to move to various places\x01",
            "the same way you do with the orbal car.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_1125")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City North Exit\x01",          # 0
            "Bus Stop (Nearby Doll Studio)\x01",      # 1
            "Quit\x01",                               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C6")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_11E6")

    label("loc_11C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E6")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_11E6")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_1027 end

    def Function_7_11EE(): pass

    label("Function_7_11EE")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_131D")
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

    def lambda_12D4():
        OP_96(0xFE, 0xFFFFE750, 0xFFFFF830, 0x528A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12D4)
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

    label("loc_131D")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_11EE end

    def Function_8_1321(): pass

    label("Function_8_1321")

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

    # Function_8_1321 end

    def Function_9_1372(): pass

    label("Function_9_1372")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_13CD")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13C2")
    Sound(2502, 255, 100, 0)
    Jump("loc_13C8")

    label("loc_13C2")

    Sound(2503, 255, 100, 0)

    label("loc_13C8")

    Jump("loc_13F1")

    label("loc_13CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13EB")
    Sound(3347, 255, 100, 0)
    Jump("loc_13F1")

    label("loc_13EB")

    Sound(3348, 255, 100, 0)

    label("loc_13F1")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1372 end

    def Function_10_1406(): pass

    label("Function_10_1406")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1527")

    ChrTalk(
        0x8,
        (
            "W-What could that be?\x01",
            "That azure pale glittering tree...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even looking at it from Mainz which is a\x01",
            "high place, you can tell it's crazily big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even grandma who is knowledgeable\x01",
            "in history said she has never seen it...\x01",
            "Somehow I've got anxious...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15D8")

    label("loc_1527")


    ChrTalk(
        0x8,
        (
            "That azure pale glittering tree...\x01",
            "I wonder what could it be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even grandma who is knowledgeable\x01",
            "in history said she has never seen it...\x01",
            "Somehow I've got anxious...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D8")

    Jump("loc_23B1")

    label("loc_15DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_175D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C8")

    ChrTalk(
        0x8,
        (
            "Is it true that Crossbell independence\x01",
            "has become invalid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The State Guard who came to\x01",
            "search for the Resistance guys\x01",
            "went back in a super hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehen, serves them right.\x01",
            "Justice always wins!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1758")

    label("loc_16C8")


    ChrTalk(
        0x8,
        (
            "The State Guard who came to\x01",
            "search for the Resistance guys\x01",
            "went back in a super hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehen, serves them right.\x01",
            "Justice always wins!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1758")

    Jump("loc_23B1")

    label("loc_175D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_192A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187A")

    ChrTalk(
        0x8,
        (
            "The whole town of Mainz is\x01",
            "helping the resistance activities\x01",
            "of the CGF personnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No way we can have fate in\x01",
            "that President who uses the\x01",
            "jaegers who occupied Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Also, defying those in power,\x01",
            "enforcing their own justice...\x01",
            "That's cool!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1925")

    label("loc_187A")


    ChrTalk(
        0x8,
        (
            "The whole town of Mainz is\x01",
            "helping the resistance activities\x01",
            "of the CGF personnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can't trust that President...\x01",
            "Also, the Resistance who\x01",
            "defies him is cool!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1925")

    Jump("loc_23B1")

    label("loc_192A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5B")

    ChrTalk(
        0x8,
        (
            "Back then, when the jaegers\x01",
            "showed up in town, I thought\x01",
            "we were already done for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even the CGF who came to help us\x01",
            "were defeated one after the other...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, they almost didn't lay their\x01",
            "hands on the town persons and stuff.\x01",
            "I wonder what they wanted to do...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A94")

    label("loc_1A5B")


    ChrTalk(
        0x8,
        (
            "Those jaegers...\x01",
            "I wonder what they wanted to do...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A94")

    Jump("loc_23B1")

    label("loc_1A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1AA7")
    Jump("loc_23B1")

    label("loc_1AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C22")

    ChrTalk(
        0x8,
        (
            "The day after tomorrow, the\x01",
            "Arc-en-ciel renewal public performance\x01",
            "is going to take place at Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd be okay with just once, how\x01",
            "I'd want to see one of their plays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And then, I'd sit, by coincidence, next\x01",
            "to a middle age gentleman whose hobby\x01",
            "is going to the theatre, we'd lively chat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(What a mixed motive...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CC0")

    label("loc_1C22")


    ChrTalk(
        0x8,
        (
            "I'd be okay with just once, how\x01",
            "I'd want to see one of their plays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And then, I'd meet a middle-aged gentleman\x01",
            "whose hobby is going to the theater.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC0")

    Jump("loc_23B1")

    label("loc_1CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1F")

    ChrTalk(
        0x8,
        (
            "The other day, Bracers came to\x01",
            "exterminate a monster that they said\x01",
            "appeared in the north mountain region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They were able to exterminate it,\x01",
            "but they said that somehow it wasn't\x01",
            "a normal monster, but a strange one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lately I often hear talks about\x01",
            "monsters like those...\x01",
            "Maybe there's some kind of cause.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E77")

    label("loc_1E1F")


    ChrTalk(
        0x8,
        (
            "Still, defeating such\x01",
            "unknown monster...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I thought, Bracers\x01",
            "are cool, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E77")

    Jump("loc_23B1")

    label("loc_1E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_20D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2035")

    ChrTalk(
        0x8,
        (
            "There's a Sister who comes\x01",
            "periodically to the town to\x01",
            "hold Sunday School class...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But don't you think that once in a while\x01",
            "it would be nice if a young Father came?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And then, then!\x01",
            "He'd be a fashionable person with\x01",
            "his habit gaudily arranged too...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FA-Although it's a fantasy, that would\x01",
            "be quite the delinquent Father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, unexpectedly, there's\x01",
            "really such a Father...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20CF")

    label("loc_2035")


    ChrTalk(
        0x8,
        (
            "Once in a while it would be nice\x01",
            "if a young Father came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If he were a fashionable person\x01",
            "with his habit gaudily arranged,\x01",
            "I could fall for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CF")

    Jump("loc_23B1")

    label("loc_20D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_20E2")
    Jump("loc_23B1")

    label("loc_20E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_222B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21AC")

    ChrTalk(
        0x8,
        (
            "My dad works at the\x01",
            "mine as a miner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Before, he did nothing but skipping on the\x01",
            "job, but lately it seems he's doing his best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*giggle*, even grandma was happy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2226")

    label("loc_21AC")


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
        "*giggle*, even grandma was happy.\x02",
    )

    CloseMessageWindow()

    label("loc_2226")

    Jump("loc_23B1")

    label("loc_222B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_23B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2333")
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
            "#10300FHu hu, do you need something\x01",
            "from me, my cute fraeulein?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(W-W-W-W-W-Who's this man?\x01",
            "He's ultra totally my type!!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(Uuuhm, typical of Wazy...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23B1")

    label("loc_2333")

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
            "(...Wait. Is he\x01",
            "a boy? A girl?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, what a strange child.\x02",
    )

    CloseMessageWindow()

    label("loc_23B1")

    TalkEnd(0xFE)
    Return()

    # Function_10_1406 end

    def Function_11_23B5(): pass

    label("Function_11_23B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2498")

    ChrTalk(
        0x9,
        "Who would've ever thought for such a thing to appear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...No, I can't become faint-hearted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The mine was finally reopened\x01",
            "and everyone is motivated, I\x01",
            "must look forward positively.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24F6")

    label("loc_2498")


    ChrTalk(
        0x9,
        (
            "The mine was finally reopened\x01",
            "and everyone is motivated, I\x01",
            "must look forward positively.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F6")

    Jump("loc_33CF")

    label("loc_24FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2695")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FF")

    ChrTalk(
        0x9,
        (
            "A large-scale operation hasn't\x01",
            "taken place since the Resistance\x01",
            "hunt by the jaegers before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After the declaration of invalidity, I'm\x01",
            "worried about how they'll react to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'd like the Resistance\x01",
            "guys to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2690")

    label("loc_25FF")


    ChrTalk(
        0x9,
        (
            "After the declaration of invalidity, I'm worried\x01",
            "about how the jaegers will react to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'd like the Resistance\x01",
            "guys to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2690")

    Jump("loc_33CF")

    label("loc_2695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2776")

    ChrTalk(
        0x9,
        (
            "When Miss Mireille and the\x01",
            "others arrived here at first,\x01",
            "we warned them too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The people of Mainz had\x01",
            "doubts about the President\x01",
            "and State Guard's policy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "This is a battle of wills.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2803")

    label("loc_2776")


    ChrTalk(
        0x9,
        (
            "Likewise, Miss Mireille and the\x01",
            "others and the people of Mainz had\x01",
            "doubts about the President's policy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "This is a battle of wills.\x02",
    )

    CloseMessageWindow()

    label("loc_2803")

    Jump("loc_33CF")

    label("loc_2808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_29F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2949")

    ChrTalk(
        0x9,
        (
            "Rumor goes that Mainz occupation and\x01",
            "the city raid was an Empire maneuver to\x01",
            "make withdraw the independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They involved us who are innocent and\x01",
            "caused great damage to the CGF too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Sacrificing people for the sake of politics...\x01",
            "That's something we can't condone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29F2")

    label("loc_2949")


    ChrTalk(
        0x9,
        (
            "Rumor goes that Mainz occupation and\x01",
            "the city raid was an Empire maneuver...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sacrificing people for the sake of politics...\x01",
            "That's something we can't condone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F2")

    Jump("loc_33CF")

    label("loc_29F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A05")
    Jump("loc_33CF")

    label("loc_2A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF2")

    ChrTalk(
        0x9,
        (
            "Not even I who live in Mainz\x01",
            "knew that there's a studio \x01",
            "midway on the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, that studio's meister\x01",
            "never shows up in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guess that a quite eccentric\x01",
            "man lives there, hm?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B7E")

    label("loc_2AF2")


    ChrTalk(
        0x9,
        (
            "The meister of the studio midway on the\x01",
            "mountain path never shows up in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guess that a quite eccentric\x01",
            "man lives there, hm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7E")

    Jump("loc_33CF")

    label("loc_2B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7F")

    ChrTalk(
        0x9,
        (
            "The monster that recently appeared\x01",
            "on the north mountain region...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They say it had a similar form to that of the one that\x01",
            "showed up in the old abandoned mine some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm...could they be related somehow?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D41")

    label("loc_2C7F")


    ChrTalk(
        0x9,
        (
            "The monster of the north mountain region and the one\x01",
            "that showed up in the old abandoned mine some\x01",
            "time ago are said to have a similar appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm...could they be related somehow?\x02",
    )

    CloseMessageWindow()

    label("loc_2D41")

    Jump("loc_33CF")

    label("loc_2D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E06")

    ChrTalk(
        0x9,
        (
            "Seems that Gantz went straight\x01",
            "to the casino again, yesterday.\x02",
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
            "I too joined midway.\x01",
            "Man, it was quite fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E64")

    label("loc_2E06")


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
            "I too joined midway.\x01",
            "Man, it was quite fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E64")

    Jump("loc_33CF")

    label("loc_2E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_30A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FCC")

    ChrTalk(
        0x9,
        (
            "This morning I went to carry Septium\x01",
            "to the city. Since I was there, I went\x01",
            "to see the inauguration ceremony too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At the Orchis Tower inauguration,\x01",
            "it seems that everyone flaunted\x01",
            "quite the good time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From that much of a height you\x01",
            "probably have a great view of the city.\x01",
            "It's something you'd want to climb once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_309D")

    label("loc_2FCC")


    ChrTalk(
        0x9,
        (
            "At the Orchis Tower inauguration,\x01",
            "it seems that everyone flaunted\x01",
            "quite the good time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From that much of a height you\x01",
            "probably have a great view of the city.\x01",
            "It's something you'd want to climb once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_309D")

    Jump("loc_33CF")

    label("loc_30A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_324E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319F")

    ChrTalk(
        0x9,
        (
            "I transport the Septium\x01",
            "mined in this place to\x01",
            "the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On the mountain path there're\x01",
            "many curves and it's tought to\x01",
            "drive a loaded truck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because there're many cliffs too,\x01",
            "prudence is the most needed thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3249")

    label("loc_319F")


    ChrTalk(
        0x9,
        (
            "On the mountain path there're\x01",
            "many curves and a loaded truck\x01",
            "easily swings left and right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because there're many cliffs too,\x01",
            "prudence is the most needed thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3249")

    Jump("loc_33CF")

    label("loc_324E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_33CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_333E")

    ChrTalk(
        0x9,
        (
            "Gantz is working like he's\x01",
            "having a lot of fun as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears that with the Cult\x01",
            "incident as a start, he became\x01",
            "unbound from many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone was worried, but...\x01",
            "At any rate, I'm glad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33CF")

    label("loc_333E")


    ChrTalk(
        0x9,
        (
            "With the Cult incident as a start, Gantz seems\x01",
            "he became unbound from many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone was worried, but...\x01",
            "At any rate, I'm glad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33CF")

    TalkEnd(0xFE)
    Return()

    # Function_11_23B5 end

    def Function_12_33D3(): pass

    label("Function_12_33D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_34EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3461")

    ChrTalk(
        0xA,
        (
            "Father and all the miners\x01",
            "went inside the mine today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They all looked happy...\x01",
            "Ehhehe, I'm happy too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34EA")

    label("loc_3461")


    ChrTalk(
        0xA,
        (
            "I'm worried about that huge\x01",
            "tree that appeared, but I'm\x01",
            "hapy the mine reopened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I want father and the others to do their best.\x02",
    )

    CloseMessageWindow()

    label("loc_34EA")

    Jump("loc_3E08")

    label("loc_34EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3576")

    ChrTalk(
        0xA,
        (
            "They say that lately a lot\x01",
            "of wolves are helping out\x01",
            "the Resistance guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They are very smart,\x01",
            "and dependable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E08")

    label("loc_3576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_369B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3622")

    ChrTalk(
        0xA,
        (
            "Being the situation what it is,\x01",
            "even the mine is closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm happy that father is\x01",
            "at home, but...like you can\x01",
            "imagine, he looks bored.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3696")

    label("loc_3622")


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
            "I too like father\x01",
            "working as a miner...\x01",
            "I hope it reopens soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3696")

    Jump("loc_3E08")

    label("loc_369B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_385D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A9")

    ChrTalk(
        0xA,
        (
            "When those bad guys came,\x01",
            "the miners rose up against them\x01",
            "in order to protect the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, they were no match for them...\x01",
            "Father was pushed away\x01",
            "and he hurt himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It wasn't a big injury, but\x01",
            "I was incredibly worried...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3858")

    label("loc_37A9")


    ChrTalk(
        0xA,
        (
            "Father and the others fought the\x01",
            "bad guys to protect the town, but...\x01",
            "In the end, they were no match for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It wasn't a big injury, but\x01",
            "I was incredibly worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3858")

    Jump("loc_3E08")

    label("loc_385D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_386B")
    Jump("loc_3E08")

    label("loc_386B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_38CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3886")
    Call(0, 13)
    Jump("loc_38CA")

    label("loc_3886")


    ChrTalk(
        0xA,
        (
            "Ahaha, mountain\x01",
            "echo is fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "What could I scream next...?\x02",
    )

    CloseMessageWindow()

    label("loc_38CA")

    Jump("loc_3E08")

    label("loc_38CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F3")

    ChrTalk(
        0xA,
        (
            "Recently they say that Mr. Logy doesn't\x01",
            "skip on the job anymore at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He said that he was just doing it unwillingly, but...\x01",
            "His face looked like he was enjoying it a lot.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I too want to become a splendid miner\x01",
            "who can do his job while enjoying it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A44")

    label("loc_39F3")


    ChrTalk(
        0xA,
        (
            "I too want to become a splendid miner\x01",
            "who can do his job while enjoying it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A44")

    Jump("loc_3E08")

    label("loc_3A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B0F")

    ChrTalk(
        0xA,
        (
            "Today Sunday School\x01",
            "was held here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It wasn't the Sister who always\x01",
            "come here, but she taught us\x01",
            "very gently and politely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ehehe, I'd like to see her again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B98")

    label("loc_3B0F")


    ChrTalk(
        0xA,
        (
            "Today it wasn't the Sister who always\x01",
            "come here, but she taught us\x01",
            "very gently and politely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ehehe, I'd like to see her again.\x02",
    )

    CloseMessageWindow()

    label("loc_3B98")

    Jump("loc_3E08")

    label("loc_3B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3CAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C4F")

    ChrTalk(
        0xA,
        "*dejected*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The other day, I was severely scolded\x01",
            "by father and mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder if it was that bad that\x01",
            "I entered inside the mine...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CA5")

    label("loc_3C4F")


    ChrTalk(
        0xA,
        (
            "I wonder if it was that bad that\x01",
            "I entered inside the mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "*dejected*...\x02",
    )

    CloseMessageWindow()

    label("loc_3CA5")

    Jump("loc_3E08")

    label("loc_3CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3CB8")
    Jump("loc_3E08")

    label("loc_3CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3E08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DA2")

    ChrTalk(
        0xA,
        (
            "Today, early in the morning,\x01",
            "the gate of the old mine\x01",
            "outside of town was open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When I tried to sneak inside,\x01",
            "I was caught immediately by\x01",
            "Mr. Gantz who scolded me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Tsk, I wanted to explore...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E08")

    label("loc_3DA2")


    ChrTalk(
        0xA,
        (
            "I wanted to explore the old\x01",
            "mine since before, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I got scolded, so it can't be helped.\x02",
    )

    CloseMessageWindow()

    label("loc_3E08")

    TalkEnd(0xFE)
    Return()

    # Function_12_33D3 end

    def Function_13_3E0C(): pass

    label("Function_13_3E0C")

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
            "......H......HOO......\x07\x00\x02",
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
            "......a tooon......tooon......\x07\x00\x02",
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

    # Function_13_3E0C end

    def Function_14_3ED8(): pass

    label("Function_14_3ED8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EE9")
    Jump("loc_43C1")

    label("loc_3EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3F28")

    ChrTalk(
        0xB,
        "*sigh*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Won't the mine reopen...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_43C1")

    label("loc_3F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4091")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FFB")

    ChrTalk(
        0xB,
        (
            "I have a hunch that if we became\x01",
            "and independent state I'd go\x01",
            "back to a lazy life like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*siiiiigh*...and just when I finally had\x01",
            "gotten motivated for the miner's job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_408C")

    label("loc_3FFB")


    ChrTalk(
        0xB,
        (
            "And just when I finally had\x01",
            "gotten motivated for the miner's job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At this rate I guess I'll be going\x01",
            "back again to a lazy lifestyle...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_408C")

    Jump("loc_43C1")

    label("loc_4091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_409F")
    Jump("loc_43C1")

    label("loc_409F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_40AD")
    Jump("loc_43C1")

    label("loc_40AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_40BB")
    Jump("loc_43C1")

    label("loc_40BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40C9")
    Jump("loc_43C1")

    label("loc_40C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_40D7")
    Jump("loc_43C1")

    label("loc_40D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_40E5")
    Jump("loc_43C1")

    label("loc_40E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40F3")
    Jump("loc_43C1")

    label("loc_40F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_43C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4248")

    ChrTalk(
        0xB,
        (
            "Before, although sometimes I slacked\x01",
            "I was lazing around on the job, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Recently, not doing like that anymore,\x01",
            "I don't even have the time to read a book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This book...I don't mind if you have it.\x01",
            "Here, I'll give it to you.\x02",
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
    Jump("loc_43C1")

    label("loc_4248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435D")

    ChrTalk(
        0xB,
        (
            "I'd like to laze around when\x01",
            "slacking on the job now and\x01",
            "then like I did before, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Recently, because all the others are in high\x01",
            "spirits, slacking has become somehow difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Maybe it's time I\x01",
            "must get motivated.\x01",
            "*sigh*, what a bother...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_43C1")

    label("loc_435D")


    ChrTalk(
        0xB,
        (
            "...It's not that I'm slacking on the job now.\x01",
            "I'm lazing around after I properly got my break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C1")

    TalkEnd(0xFE)
    Return()

    # Function_14_3ED8 end

    def Function_15_43C5(): pass

    label("Function_15_43C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_43D6")
    Jump("loc_462E")

    label("loc_43D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_43E4")
    Jump("loc_462E")

    label("loc_43E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_448C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43FF")
    Call(0, 13)
    Jump("loc_4487")

    label("loc_43FF")


    ChrTalk(
        0xC,
        (
            "Amazing, amazing, the voice\x01",
            "has come back properly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Could there be a child like Kimmy\x01",
            "on the other side of that mountain too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4487")

    Jump("loc_462E")

    label("loc_448C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_449A")
    Jump("loc_462E")

    label("loc_449A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4579")

    ChrTalk(
        0xC,
        (
            "The Sister? She has already\x01",
            "gone back to the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, when she went\x01",
            "back it seemed she was worried\x01",
            "about the sky in that direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Uhhm, could there be something there?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4604")

    label("loc_4579")


    ChrTalk(
        0xC,
        (
            "The Sister, when she went back,\x01",
            "it seemed she was worried about\x01",
            "the sky in that direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Uhhm, could there be something there?\x02",
    )

    CloseMessageWindow()

    label("loc_4604")

    Jump("loc_462E")

    label("loc_4609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4617")
    Jump("loc_462E")

    label("loc_4617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4625")
    Jump("loc_462E")

    label("loc_4625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_462E")

    label("loc_462E")

    TalkEnd(0xFE)
    Return()

    # Function_15_43C5 end

    def Function_16_4632(): pass

    label("Function_16_4632")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4643")
    Jump("loc_4754")

    label("loc_4643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_474B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4707")

    ChrTalk(
        0xD,
        (
            "We'd like to do something too, but...\x01",
            "We can't help out the girl and the\x01",
            "others from the Resistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...As I thought, what a miner\x01",
            "can do is only dig holes...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4746")

    label("loc_4707")


    ChrTalk(
        0xD,
        (
            "...As I thought, what a miner\x01",
            "can do is only dig holes...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4746")

    Jump("loc_4754")

    label("loc_474B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4754")

    label("loc_4754")

    TalkEnd(0xFE)
    Return()

    # Function_16_4632 end

    def Function_17_4758(): pass

    label("Function_17_4758")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4769")
    Jump("loc_48BE")

    label("loc_4769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_48B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4817")

    ChrTalk(
        0xE,
        (
            "We've been driven out \x01",
            "from the inn by Lycka.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "She said is so the Resistance\x01",
            "leader can rest at leisure...\x01",
            "Well, can't be helped I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_48B0")

    label("loc_4817")


    ChrTalk(
        0xE,
        (
            "...At any rate, it's the first\x01",
            "time I have been away from\x01",
            "the miner's work for so long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'd never thought that I'd\x01",
            "have missed it this much...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B0")

    Jump("loc_48BE")

    label("loc_48B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_48BE")

    label("loc_48BE")

    TalkEnd(0xFE)
    Return()

    # Function_17_4758 end

    def Function_18_48C2(): pass

    label("Function_18_48C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD4")

    ChrTalk(
        0xFE,
        (
            "At the time of Mainz mine reopening,\x01",
            "I exterminated a highly dangerous\x01",
            "monster that got restless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wasn't anything special compared to a\x01",
            ""magic soldier" or a "Cryptid", but a monster \x01",
            "extermination is a tough job for one person alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHa ha...you're amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FI guess it can be expected from an able\x01",
            "Bracer who comes from the Empire Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmph, I still have a long way to go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...The Empire is in the middle of a civil war\x01",
            "and I wonder how my former home is doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "...No, let's stop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I first have to deal with what I have in front of me...\x01",
            "Because those who can't do that and look back at their\x01",
            "past are not qualified to desire a future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(Ha ha, a strict person as always.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 3)
    Jump("loc_4CF6")

    label("loc_4BD4")


    ChrTalk(
        0xFE,
        (
            "Although the President was restrained,\x01",
            "even Crossbell is in a sticky situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Even the guys who are resting at the inn...\x01",
            "When their stamina comes back, I'll have\x01",
            "them help me out with various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These can be hard times...\x01",
            "But that's why we have to brace our legs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CF6")

    TalkEnd(0xFE)
    Return()

    # Function_18_48C2 end

    def Function_19_4CFA(): pass

    label("Function_19_4CFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DFF")

    ChrTalk(
        0xFE,
        (
            "The Mainz mountain range.\x01",
            "I failed the challenge a little time ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll train my legs and loins, and no matter how\x01",
            "many years, I'll absolutely travel it on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...An expression of determination, for the time being.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4E83")

    label("loc_4DFF")


    ChrTalk(
        0xFE,
        (
            "I finished my expression of determination...\x01",
            "I guess it's time I return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to meet my friend after a long time.\x02",
    )

    CloseMessageWindow()

    label("loc_4E83")

    TalkEnd(0xFE)
    Return()

    # Function_19_4CFA end

    def Function_20_4E87(): pass

    label("Function_20_4E87")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EB9")
    SetScenarioFlags(0x31, 2)

    label("loc_4EB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_4EF9")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EEE")
    Sound(2499, 255, 100, 0)
    Jump("loc_4EF4")

    label("loc_4EEE")

    Sound(3537, 255, 100, 0)

    label("loc_4EF4")

    Jump("loc_4EFF")

    label("loc_4EF9")

    Sound(3344, 255, 100, 0)

    label("loc_4EFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4F72")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F52"),
        (SWITCH_DEFAULT, "loc_4F63"),
    )


    label("loc_4F52")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4F6D")

    label("loc_4F63")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F6D")

    Jump("loc_51AD")

    label("loc_4F72")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4FA4")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_4FA4")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4FD6"),
        (1, "loc_50DA"),
        (2, "loc_516B"),
        (SWITCH_DEFAULT, "loc_51A3"),
    )


    label("loc_4FD6")

    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5007")
    OP_70(0x9, 0x12C)
    OP_71(0x9, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_5017")

    label("loc_5007")

    OP_70(0x9, 0xF0)
    OP_71(0x9, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_5017")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_506D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_506D")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5090")
    Sound(461, 0, 100, 0)

    label("loc_5090")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_50B0")
    OP_70(0x9, 0x14A)
    OP_71(0x9, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_50C0")

    label("loc_50B0")

    OP_70(0x9, 0x10E)
    OP_71(0x9, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_50C0")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x9, "light", 0x1, 0x1)
    OP_70(0x9, 0x0)
    Jump("loc_4EFF")

    label("loc_50DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_514C")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_510F")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_5127")

    label("loc_510F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5122")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_5127")

    label("loc_5122")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_5127")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5166")

    label("loc_514C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_515C")
    OP_AF(0xFB)
    Jump("loc_5166")

    label("loc_515C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5166")

    Jump("loc_51AD")

    label("loc_516B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5184")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_519E")

    label("loc_5184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5194")
    OP_AF(0xFB)
    Jump("loc_519E")

    label("loc_5194")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_519E")

    Jump("loc_51AD")

    label("loc_51A3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51AD")

    Jump("loc_4EFF")

    label("loc_51B2")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_4E87 end

    def Function_21_51C0(): pass

    label("Function_21_51C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5210")
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

    label("loc_5210")

    Call(0, 6)
    Return()

    # Function_21_51C0 end

    def Function_22_5214(): pass

    label("Function_22_5214")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_542D")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Lloyd and friends, who returned to\x01",
            "Mainz, explained the circumstances in \x01",
            "general to the Town Mayor and the others.\x02\x03",
            "They said the old mine entrance gate was destroyed, but\x01",
            "they did not explain well the disorder inside the tunnel and\x01",
            "who was the culprit who set the explosive, being not clear.\x02\x03",
            "Then, they searched the environs once again, and\x01",
            "after confirming the absence of anyone suspicious...\x02\x03",
            "Lloyd and the others requested patrols to the\x01",
            "CGF and decided to go back to Crossbell City.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_542D")

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

    # Function_22_5214 end

    def Function_23_586E(): pass

    label("Function_23_586E")

    OP_79(0x9)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    Return()

    # Function_23_586E end

    def Function_24_587E(): pass

    label("Function_24_587E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5899")
    Sleep(300)
    Jump("loc_58ED")

    label("loc_5899")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_58B4")
    Sleep(600)
    Jump("loc_58ED")

    label("loc_58B4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_58CF")
    Sleep(900)
    Jump("loc_58ED")

    label("loc_58CF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_58EA")
    Sleep(1200)
    Jump("loc_58ED")

    label("loc_58EA")

    Sleep(1500)

    label("loc_58ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5918")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_58ED")

    label("loc_5918")

    Return()

    # Function_24_587E end

    def Function_25_5919(): pass

    label("Function_25_5919")

    Return()

    # Function_25_5919 end

    def Function_26_591A(): pass

    label("Function_26_591A")

    Return()

    # Function_26_591A end

    def Function_27_591B(): pass

    label("Function_27_591B")

    Return()

    # Function_27_591B end

    def Function_28_591C(): pass

    label("Function_28_591C")

    OP_9B(0x0, 0xFE, 0x1, 0x2328, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x50, 0xFA0, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Return()

    # Function_28_591C end

    def Function_29_595A(): pass

    label("Function_29_595A")

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

    def lambda_59B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_59B9)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_595A end

    def Function_30_59DD(): pass

    label("Function_30_59DD")

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

    def lambda_5A43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A43)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_59DD end

    def Function_31_5A67(): pass

    label("Function_31_5A67")

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

    def lambda_5ACE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5ACE)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_5A67 end

    def Function_32_5AF2(): pass

    label("Function_32_5AF2")

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

    def lambda_5B51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5B51)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_5AF2 end

    def Function_33_5B75(): pass

    label("Function_33_5B75")

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

    def lambda_5C49():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C49)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_5B75 end

    def Function_34_5C6D(): pass

    label("Function_34_5C6D")

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

    # Function_34_5C6D end

    def Function_35_5D11(): pass

    label("Function_35_5D11")

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

    # Function_35_5D11 end

    def Function_36_5D4E(): pass

    label("Function_36_5D4E")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -4500, -2000, 18000)
    OP_9F(0x1, -4500, -2000, 16000)
    OP_9F(0x1, -4000, -2000, 12000)
    OP_9F(0x1, -1500, -2000, 6000)
    OP_9F(0x1, 500, -2000, 0)
    OP_9F(0x1, 500, -2000, -12000)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_36_5D4E end

    def Function_37_5DB0(): pass

    label("Function_37_5DB0")

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

    # Function_37_5DB0 end

    def Function_38_5E91(): pass

    label("Function_38_5E91")

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
            "#00006F#5P*phew*...\x01",
            "In the end, we have come here on foot.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    ChrTalk(
        0x102,
        "#00100F#11PMiss Noｱl, Wazy, are you all right?\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x2D, 0x1F4)

    ChrTalk(
        0x109,
        "#10102F#6PYes, no need for concerns.\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#10306F#6PI'm all right too, however...\x01",
            "The Support Section is really an oddball.\x02\x03",
            "#10301FYou could openly use a\x01",
            "vehicle or a bus, and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PHa ha, it can be training, so we're\x01",
            "hitting two birds with a stone, no?\x02\x03",
            "#00004FAt any rate...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00012F#5PElie, you've really built up your stamina.\x02\x03",
            "#00000FAt first, just by walking a little\x01",
            "on a highway you had a hard time...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00109F#12P*giggle*, it's because I trained\x01",
            "due to certain people.\x02\x03",
            "#00100FSo, what do we do?\x01",
            "Do we try to visit the Town Mayor immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, let's do like that.\x02\x03",
            "#00000FThe Town Mayor's home is at the end of the\x01",
            "street just straight ahead after entering town.\x02",
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

    # Function_38_5E91 end

    def Function_39_6313(): pass

    label("Function_39_6313")

    Sleep(5500)

    def lambda_631B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_631B)

    def lambda_632C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_632C)

    def lambda_633D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_633D)

    def lambda_634E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_634E)
    BeginChrThread(0x101, 0, 0, 40)
    BeginChrThread(0x102, 0, 0, 41)
    BeginChrThread(0x109, 0, 0, 42)
    BeginChrThread(0x105, 0, 0, 43)
    Return()

    # Function_39_6313 end

    def Function_40_6373(): pass

    label("Function_40_6373")

    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_40_6373 end

    def Function_41_6383(): pass

    label("Function_41_6383")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x3714, 0x7D0, 0x0)
    Return()

    # Function_41_6383 end

    def Function_42_6396(): pass

    label("Function_42_6396")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x37DC, 0x7D0, 0x0)
    Return()

    # Function_42_6396 end

    def Function_43_63A9(): pass

    label("Function_43_63A9")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
    Return()

    # Function_43_63A9 end

    def Function_44_63BC(): pass

    label("Function_44_63BC")

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

    def lambda_652E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_652E)
    Sleep(50)

    def lambda_653E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_653E)
    Sleep(50)

    def lambda_654E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_654E)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68A2")

    ChrTalk(
        0x102,
        (
            "#00104F#5P*giggle*...\x01",
            "It was extremely quick.\x02\x03",
            "#00100FLike we heard, it seems the mountain\x01",
            "path region has clear weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PYeah, the scenery after\x01",
            "the rain was pretty, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#12PHmm, but still, this\x01",
            "car is something else.\x02\x03",
            "#10102FIt doesn't even sway at all on\x01",
            "places like the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PThat's ZCF for you.\x01",
            "This model 'll be a hit once it's released.\x02\x03",
            "#10300FSo, this mining town mayor\x01",
            "wants to talk to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#5PYes, he's called Town Mayor Bickson.\x02\x03",
            "After entering the town, his house is\x01",
            "at the end of the street straight ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, let's go and see.\x02\x03",
            "#00003F(...Now that I think about it, midway the mountain\x01",
            "path there's the road to the Doll Studio.)\x02\x03",
            "#00008F(Renne isn't here anymore, but...\x01",
            "I wanted to check the situation a little.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BE8")

    label("loc_68A2")


    ChrTalk(
        0x105,
        (
            "#10305F#6PEeh, this is Mainz?\x02\x03",
            "#10302FI only knew it in name, it's\x01",
            "my first time coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PWell, unless you have some business\x01",
            "you probably don't have chance to comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#5PBy the way, Miss Noｱl, you\x01",
            "come quite often to Mainz, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#12PYes, after all it's even become \x01",
            "a course on the fixed patrols.\x02\x03",
            "#10102FBy the way, the SSS has a\x01",
            "connection to Mainz region, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PHa ha, you can say that.\x02\x03",
            "#00000FWe were together on the military dogs\x01",
            "case and on the temple investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PT-That's right...\x01",
            "(I ended up remembering some unpleasant things.)\x02\x03",
            "#00100FSo, what do we do?\x01",
            "Do we try to visit the Town Mayor immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, let's do like that.\x02\x03",
            "#00000FThe Town Mayor's home is at the end of the\x01",
            "street just straight ahead after entering town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE8")

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

    # Function_44_63BC end

    def Function_45_6C21(): pass

    label("Function_45_6C21")

    Sleep(5500)
    BeginChrThread(0x18, 0, 0, 46)
    WaitChrThread(0x18, 0)
    BeginChrThread(0x18, 0, 0, 47)
    BeginChrThread(0x1E, 1, 0, 52)
    Return()

    # Function_45_6C21 end

    def Function_46_6C3B(): pass

    label("Function_46_6C3B")

    SetChrPos(0xFE, 0, -1950, -500, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x2CEC, 0xFA0, 0x0)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFEB7E0, 0xBB8, 0x1)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFFF060, 0x7D0, 0x1)
    OP_71(0x9, 0x5B, 0x78, 0x1, 0x8)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFFF830, 0x3E8, 0x1)
    Sleep(300)
    Return()

    # Function_46_6C3B end

    def Function_47_6CAA(): pass

    label("Function_47_6CAA")

    OP_74(0x9, 0xA)
    OP_71(0x9, 0xB4, 0x79, 0x0, 0x20)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF448, 0x7D0, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFEC398, 0xBB8, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF060, 0x7D0, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF830, 0x3E8, 0x4)
    OP_70(0x9, 0x78)
    Return()

    # Function_47_6CAA end

    def Function_48_6D13(): pass

    label("Function_48_6D13")


    def lambda_6D18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D18)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x145, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_48_6D13 end

    def Function_49_6D51(): pass

    label("Function_49_6D51")

    Sleep(1300)

    def lambda_6D59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D59)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x6D6, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_49_6D51 end

    def Function_50_6D92(): pass

    label("Function_50_6D92")

    Sleep(2600)

    def lambda_6D9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D9A)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_50_6D92 end

    def Function_51_6DD3(): pass

    label("Function_51_6DD3")

    Sleep(3900)

    def lambda_6DDB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6DDB)
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

    # Function_51_6DD3 end

    def Function_52_6E46(): pass

    label("Function_52_6E46")

    Sound(494, 0, 50, 0)
    Sleep(2000)
    Sound(459, 0, 100, 0)
    Sleep(2300)
    Sound(492, 0, 60, 0)
    Return()

    # Function_52_6E46 end

    def Function_53_6E5F(): pass

    label("Function_53_6E5F")

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

    def lambda_6F5D():

        label("loc_6F5D")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6F5D")

    QueueWorkItem2(0x101, 2, lambda_6F5D)

    def lambda_6F6F():

        label("loc_6F6F")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6F6F")

    QueueWorkItem2(0x102, 2, lambda_6F6F)

    def lambda_6F81():

        label("loc_6F81")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6F81")

    QueueWorkItem2(0x109, 2, lambda_6F81)

    def lambda_6F93():

        label("loc_6F93")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6F93")

    QueueWorkItem2(0x105, 2, lambda_6F93)
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

    def lambda_6FFF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6FFF)
    Sleep(50)

    def lambda_700F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_700F)
    Sleep(50)

    def lambda_701F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_701F)
    Sleep(50)

    def lambda_702F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_702F)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7392")

    ChrTalk(
        0x102,
        (
            "#00104F#12P*giggle*...\x01",
            "It was extremely quick.\x02\x03",
            "#00100FLike we heard, it seems the mountain\x01",
            "path region has clear weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PYeah, the scenery after\x01",
            "the rain was pretty, eh?\x02\x03",
            "#00006FStill, although we have a car,\x01",
            "in the end we rode the bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PUh uh.\x01",
            "I like buses.\x02\x03",
            "#10102FTheir relaxing feeling\x01",
            "is nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PI too ride them seldomly, so I\x01",
            "guess it was quite refreshing.\x02\x03",
            "#10300FSo, this mining town mayor\x01",
            "wants to talk to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PYes, he's called Town Mayor Bickson.\x02\x03",
            "After entering the town, his house is\x01",
            "at the end of the street straight ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, let's go and see.\x02\x03",
            "#00003F(...Now that I think about it, midway the mountain\x01",
            "path there's the road to the Doll Studio.)\x02\x03",
            "#00008F(Renne isn't here anymore, but...\x01",
            "I wanted to check the situation a little.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76DA")

    label("loc_7392")


    ChrTalk(
        0x105,
        (
            "#10305F#6PEeh, this is Mainz?\x02\x03",
            "#10302FI only knew it in name, it's\x01",
            "my first time coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PWell, unless you have some business\x01",
            "you probably don't have chance to comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#12PBy the way, Miss Noｱl, you\x01",
            "come quite often to Mainz, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#5PYes, after all it's even become \x01",
            "a course on the fixed patrols.\x02\x03",
            "#10102FBy the way, the SSS has a\x01",
            "connection to Mainz region, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#11PHa ha, you can say that.\x02\x03",
            "#00000FWe were together on the military dogs\x01",
            "case and on the temple investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PT-That's right...\x01",
            "(I ended up remembering some unpleasant things.)\x02\x03",
            "#00100FSo, what do we do?\x01",
            "Do we try to visit the Town Mayor immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, let's do like that.\x02\x03",
            "#00000FThe Town Mayor's home is at the end of the\x01",
            "street just straight ahead after entering town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76DA")

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

    # Function_53_6E5F end

    def Function_54_7719(): pass

    label("Function_54_7719")

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

    # Function_54_7719 end

    def Function_55_7751(): pass

    label("Function_55_7751")

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

    # Function_55_7751 end

    def Function_56_77F8(): pass

    label("Function_56_77F8")

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

    # Function_56_77F8 end

    def Function_57_7887(): pass

    label("Function_57_7887")

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

    def lambda_7D8E():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7D8E)
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
            "#07904F#5PIt seems that even the "Red Constellation"\x01",
            "has retreated for the time being.\x02\x03",
            "#07902FIt also seems that the traces of\x01",
            "their pillaging are nothing special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#12PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PThank goodness...\x01",
            "It's a blessing in disguise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PBy nature they're a lot that doesn't pillage\x01",
            "unnecessarily if they don't have the need to.\x02\x03",
            "#00308FConversely, if they had to, they'd have probably \x01",
            "done everything they're capable of......\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)

    def lambda_80A1():
        TurnDirection(0x17, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_80A1)
    Sleep(50)

    def lambda_80B1():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_80B1)
    Sleep(50)

    def lambda_80C1():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_80C1)
    Sleep(50)

    def lambda_80D1():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_80D1)
    Sleep(50)

    def lambda_80E1():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_80E1)
    Sleep(50)

    def lambda_80F1():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_80F1)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10105F#12PSenior Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07908F#5PAre you all right?\x01",
            "I heard you exaggerated\x01",
            "quite a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#11PWell, it's nothing big.\x02\x03",
            "#00306FAlthough the rifle I went to great pains to unseal\x01",
            "is goin' to be of no use for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PIt's been gnawed at by that\x01",
            "amazing chain saw, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PAnyway, speaking of Miss\x01",
            "Shirley's chainsaw rifle...\x02\x03",
            "#00201FThe "Red Constellation" jaegers\x01",
            "have some peculiar equipments, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00303F#5PYeah, they're custom ordered\x01",
            "to a specialized weapons factory...\x02\x03",
            "#00302FWell, someone like Master Guillaume\x01",
            "should be able to repair it in some way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PYeah, it's better to do like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12P*giggle*, when we'll be back in the city,\x01",
            "let's try dropping by him first things first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07904F#5P...Still, I'm glad for you.\x02\x03",
            "#07902FYou've become able to\x01",
            "use rifles once again.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00300F#11PHa ha...rather too late, though.\x02\x03",
            "#00309FWell, I've caused a lot of\x01",
            "worries to you too, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07906F#5PT-That's right...\x01",
            "If you had used rifles since the very beginning\x01",
            "you could still be enrolled in the CGF...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_8591():
        TurnDirection(0x101, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8591)
    Sleep(50)

    def lambda_85A1():
        TurnDirection(0x102, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_85A1)
    Sleep(50)

    def lambda_85B1():
        TurnDirection(0x103, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_85B1)
    Sleep(50)

    def lambda_85C1():
        TurnDirection(0x109, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_85C1)
    Sleep(50)

    def lambda_85D1():
        TurnDirection(0x105, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_85D1)
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
            "You see, I'm just wondering if this irresponsible\x01",
            "man can do properly somewhere else!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#12P(Ha ha...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12P(She's charming, somehow.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6P(I think that Mr. Randy\x01",
            "too has realised...)\x02",
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
            "#07903F#11P*cough*...\x01",
            "Mireille of the 1st Company speaking.\x02\x03",
            "#07902FI see, good job.\x01",
            "So, about their movements...\x02\x03",
            "#07905F#30W............\x02\x03",
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
            "#07906F#5P...It appears that the jaegers who\x01",
            "retreated vanished all of a sudden.\x02\x03",
            "#07901FIt seems they fled toward the ruins \x01",
            "remains after the split in the tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PThe "Temple of Moon"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PUhm...\x01",
            "Didn't they take refuge in the ruins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#07903F#5PNo, it seems there were no traces of them having\x01",
            "broken through the blockade in front of the ruins.\x02\x03",
            "#07908FWhere on earth did they...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11P...Around there, it's just\x01",
            "all steep cliffs...\x02\x03",
            "#10101FThere should be no other place\x01",
            "anywhere they could retreat to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#12PHm, it didn't seem that common\x01",
            "sense can be applied to that Shirley...\x02",
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
            "#00306F#11P──I thought that it was strange.\x02\x03",
            "#00301FThose guys who were in the Mainz region...\x01",
            "No matter how I think about it, they were too few.\x02",
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

    def lambda_8CD0():
        TurnDirection(0x17, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_8CD0)
    Sleep(50)

    def lambda_8CE0():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8CE0)
    Sleep(50)

    def lambda_8CF0():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8CF0)
    Sleep(50)

    def lambda_8D00():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8D00)
    Sleep(50)

    def lambda_8D10():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8D10)
    Sleep(50)

    def lambda_8D20():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8D20)
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
            "#00303F#5PA large quantity of them came to\x01",
            "Crossbell, about a hundred people...\x02\x03",
            "Still, those who were in the Mainz\x01",
            "area were about twenty at best.\x02\x03",
            "#00308F...And most of all,\x01",
            "Sigmund Orlando──\x02\x03",
            "#00311FThat bigger a monster than Shirley,\x01",
            "where the heck did he go...?\x02",
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
        "#07907F#5PW-Well...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x87, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#00205F#5POh...\x02\x03",
            "#00207F#4S──Everyone, look at that!\x02",
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

    def lambda_8FBB():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8FBB)
    Sleep(20)

    def lambda_8FCB():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8FCB)
    Sleep(20)

    def lambda_8FDB():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8FDB)
    Sleep(20)

    def lambda_8FEB():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8FEB)
    Sleep(20)

    def lambda_8FFB():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8FFB)
    Sleep(20)

    def lambda_900B():
        OP_93(0x17, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_900B)
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
        "#10110FN-No way...!\x02",
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
            "#00007FCrossbell City is──\x01",
            "in flames!?\x02",
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

    # Function_57_7887 end

    def Function_58_922D(): pass

    label("Function_58_922D")

    OP_96(0xFE, 0x28A, 0x0, 0xD41C, 0x3E8, 0x0)
    OP_95(0xFE, 650, 0, 55950, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_58_922D end

    def Function_59_925D(): pass

    label("Function_59_925D")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_926C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_926C)
    OP_95(0xFE, 3000, 0, 54800, 3000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_59_925D end

    def Function_60_92B3(): pass

    label("Function_60_92B3")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_92C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_92C2)
    OP_95(0xFE, 3000, 0, 53800, 3000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_60_92B3 end

    def Function_61_9306(): pass

    label("Function_61_9306")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_9315():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9315)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 650, 0, 54950, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_61_9306 end

    def Function_62_9370(): pass

    label("Function_62_9370")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_937F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_937F)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_95(0xFE, 1150, 0, 51250, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_62_9370 end

    def Function_63_93D0(): pass

    label("Function_63_93D0")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_93DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_93DF)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_95(0xFE, 2400, 0, 52100, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_63_93D0 end

    def Function_64_9430(): pass

    label("Function_64_9430")

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

    # Function_64_9430 end

    def Function_65_963E(): pass

    label("Function_65_963E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_968A")
    OP_95(0xFE, 4450, -2000, 1050, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, 6000, -2000, 3050, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    Jump("Function_65_963E")

    label("loc_968A")

    Return()

    # Function_65_963E end

    def Function_66_968B(): pass

    label("Function_66_968B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96D7")
    OP_95(0xFE, -1850, -2000, 2250, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, -2350, -2000, 9550, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    Jump("Function_66_968B")

    label("loc_96D7")

    Return()

    # Function_66_968B end

    def Function_67_96D8(): pass

    label("Function_67_96D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96FC")
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(2000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2000)
    Jump("Function_67_96D8")

    label("loc_96FC")

    Return()

    # Function_67_96D8 end

    def Function_68_96FD(): pass

    label("Function_68_96FD")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is tightly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_68_96FD end

    SaveToFile()

Try(main)
