from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t2000.bin",                # FileName
        "t2000",                    # MapName
        "t2000",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\x02',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 24450, 0, -890, 0, 0, 1, 89, 0, 3, 0, 4],
    )

    BuildStringList((
        "t2000",                  # 0
        "Carter members",           # 1
        "Loggers",           # 2
        "Romeo members",             # 3
        "tourist",                 # 4
        "bus",                   # 5
        "Special support vehicle",             # 6
        "Runaway vehicle",                 # 7
        "Lieutenant Mireille",           # 8
        "Traveler",                 # 9
        "Traveler",                 # 10
        "Traveler",                 # 11
        "Traveler",                 # 12
        "Traveler",                 # 13
        "Traveler",                 # 14
        "Defense Forces soldier",             # 15
        "Defense Forces soldier",             # 16
        "Defense Forces soldier",             # 17
        "Defense Forces soldier",             # 18
        "New armored car",             # 19
        "West Crossbell Highway",       # 20
    ))

    AddCharChip((
        "chr/ch32600.itc",                   # 00
        "chr/ch31200.itc",                   # 01
        "chr/ch31300.itc",                   # 02
        "chr/ch33200.itc",                   # 03
        "chr/ch41400.itc",                   # 04
        "chr/ch41500.itc",                   # 05
    ))

    DeclNpc(22430,   0,       4730,    90,   261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(22239,   0,       4294961807, 90,   261,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(13550,   0,       26559,   270,  389,  0x0, 0,   1,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(24790,   200,     4294947907, 180,  389,  0x0, 0,   3,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
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

    DeclActor(31260,   0,       27730,   1200,    31260,   1000,    27730,   0x007C, 0,  17, 0x0000)
    DeclActor(1500,    5050,    4294947296, 1200,    1500,    6050,    4294947296, 0x007C, 0,  5,  0x0000)
    DeclActor(40580,   0,       3620,    1200,    40580,   2000,    3620,    0x007C, 0,  16, 0x0000)
    DeclActor(40350,   0,       5000,    1200,    40350,   2000,    5000,    0x007C, 0,  16, 0x0000)
    DeclActor(18980,   200,     4294955576, 1200,    18980,   1700,    4294955576, 0x007C, 0,  47, 0x0000)

    PlaceName(73.0, 0.0, -4.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(5.0, 0.0, -0.800000011920929, 0x0000, 0x0052, "")
    PlaceName(30.850000381469727, 0.0, 27.90999984741211, 0x0000, 0x0055, "")

    ChipFrameInfo(1136, 0)                                       # 0

    ScpFunction((
        "Function_0_470",          # 00, 0
        "Function_1_520",          # 01, 1
        "Function_2_54B",          # 02, 2
        "Function_3_577",          # 03, 3
        "Function_4_C67",          # 04, 4
        "Function_5_E1A",          # 05, 5
        "Function_6_F6B",          # 06, 6
        "Function_7_102F",         # 07, 7
        "Function_8_115C",         # 08, 8
        "Function_9_11AD",         # 09, 9
        "Function_10_1241",        # 0A, 10
        "Function_11_1326",        # 0B, 11
        "Function_12_20F5",        # 0C, 12
        "Function_13_231B",        # 0D, 13
        "Function_14_3001",        # 0E, 14
        "Function_15_3161",        # 0F, 15
        "Function_16_3235",        # 10, 16
        "Function_17_3578",        # 11, 17
        "Function_18_35C4",        # 12, 18
        "Function_19_3928",        # 13, 19
        "Function_20_3C9C",        # 14, 20
        "Function_21_3CEF",        # 15, 21
        "Function_22_3D42",        # 16, 22
        "Function_23_3D59",        # 17, 23
        "Function_24_4971",        # 18, 24
        "Function_25_4A98",        # 19, 25
        "Function_26_4E33",        # 1A, 26
        "Function_27_5EB0",        # 1B, 27
        "Function_28_5FD0",        # 1C, 28
        "Function_29_604B",        # 1D, 29
        "Function_30_60D2",        # 1E, 30
        "Function_31_60FC",        # 1F, 31
        "Function_32_6156",        # 20, 32
        "Function_33_619B",        # 21, 33
        "Function_34_61B7",        # 22, 34
        "Function_35_61D3",        # 23, 35
        "Function_36_61EF",        # 24, 36
        "Function_37_620B",        # 25, 37
        "Function_38_6227",        # 26, 38
        "Function_39_6269",        # 27, 39
        "Function_40_6288",        # 28, 40
        "Function_41_62A7",        # 29, 41
        "Function_42_62C6",        # 2A, 42
        "Function_43_62E5",        # 2B, 43
        "Function_44_63FE",        # 2C, 44
        "Function_45_782C",        # 2D, 45
        "Function_46_7969",        # 2E, 46
        "Function_47_7AA6",        # 2F, 47
    ))


    def Function_0_470(): pass

    label("Function_0_470")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4A8"),
        (1, "loc_4B4"),
        (2, "loc_4C0"),
        (3, "loc_4CC"),
        (4, "loc_4D8"),
        (5, "loc_4E4"),
        (6, "loc_4F0"),
        (SWITCH_DEFAULT, "loc_4FC"),
    )


    label("loc_4A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_508")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_51F")

    Return()

    # Function_0_470 end

    def Function_1_520(): pass

    label("Function_1_520")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54A")
    OP_94(0xFE, 0x60D6, 0xFFFFB442, 0x7346, 0xFFFFC888, 0x3E8)
    Sleep(400)
    Jump("Function_1_520")

    label("loc_54A")

    Return()

    # Function_1_520 end

    def Function_2_54B(): pass

    label("Function_2_54B")

    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570")
    ClearMapObjFlags(0x8, 0x2000000)
    Jump("loc_576")

    label("loc_570")

    ClearMapObjFlags(0x2, 0x2000000)

    label("loc_576")

    Return()

    # Function_2_54B end

    def Function_3_577(): pass

    label("Function_3_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_58D")
    SetChrChipByIndex(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x5)
    Jump("loc_641")

    label("loc_58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5A5")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_641")

    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5B3")
    Jump("loc_641")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E8")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x40)
    SetChrPos(0xF, 13370, 0, 26130, 270)

    label("loc_5E8")

    Jump("loc_641")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5FB")
    Jump("loc_641")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_609")
    Jump("loc_641")

    label("loc_609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_625")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_END)), "loc_620")
    ClearChrFlags(0xA, 0x80)

    label("loc_620")

    Jump("loc_641")

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_633")
    Jump("loc_641")

    label("loc_633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_641")
    ClearChrFlags(0xB, 0x80)

    label("loc_641")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE")
    SetScenarioFlags(0x38, 0)

    label("loc_6CE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4")
    SetScenarioFlags(0x38, 1)

    label("loc_6E4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FA")
    SetScenarioFlags(0x38, 2)

    label("loc_6FA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_710")
    SetScenarioFlags(0x38, 3)

    label("loc_710")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_726")
    SetScenarioFlags(0x38, 4)

    label("loc_726")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C")
    SetScenarioFlags(0x38, 5)

    label("loc_73C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    SetScenarioFlags(0x38, 6)

    label("loc_752")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768")
    SetScenarioFlags(0x38, 7)

    label("loc_768")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77E")
    SetScenarioFlags(0x39, 0)

    label("loc_77E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_794")
    SetScenarioFlags(0x39, 1)

    label("loc_794")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AA")
    SetScenarioFlags(0x39, 2)

    label("loc_7AA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C0")
    SetScenarioFlags(0x39, 3)

    label("loc_7C0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6")
    SetScenarioFlags(0x39, 4)

    label("loc_7D6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EC")
    SetScenarioFlags(0x39, 5)

    label("loc_7EC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_802")
    SetScenarioFlags(0x39, 6)

    label("loc_802")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_818")
    SetScenarioFlags(0x39, 7)

    label("loc_818")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82E")
    SetScenarioFlags(0x3A, 0)

    label("loc_82E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_844")
    SetScenarioFlags(0x3A, 1)

    label("loc_844")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85A")
    SetScenarioFlags(0x3A, 2)

    label("loc_85A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_870")
    SetScenarioFlags(0x3A, 3)

    label("loc_870")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_886")
    SetScenarioFlags(0x3A, 4)

    label("loc_886")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C")
    SetScenarioFlags(0x3A, 5)

    label("loc_89C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B2")
    SetScenarioFlags(0x3A, 6)

    label("loc_8B2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C8")
    SetScenarioFlags(0x3A, 7)

    label("loc_8C8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DE")
    SetScenarioFlags(0x3B, 0)

    label("loc_8DE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F4")
    SetScenarioFlags(0x3B, 1)

    label("loc_8F4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90A")
    SetScenarioFlags(0x3B, 2)

    label("loc_90A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_920")
    SetScenarioFlags(0x3B, 3)

    label("loc_920")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_936")
    SetScenarioFlags(0x3B, 4)

    label("loc_936")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94C")
    SetScenarioFlags(0x3B, 5)

    label("loc_94C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_962")
    SetScenarioFlags(0x3B, 6)

    label("loc_962")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_978")
    SetScenarioFlags(0x3B, 7)

    label("loc_978")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98E")
    SetScenarioFlags(0x3D, 5)

    label("loc_98E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A4")
    SetScenarioFlags(0x3D, 6)

    label("loc_9A4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BA")
    SetScenarioFlags(0x3D, 7)

    label("loc_9BA")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F5")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_AE5")

    label("loc_9F5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A18")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_AE5")

    label("loc_A18")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3B")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_AE5")

    label("loc_A3B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5E")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_AE5")

    label("loc_A5E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A81")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_AE5")

    label("loc_A81")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA4")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_AE5")

    label("loc_AA4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC7")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_AE5")

    label("loc_AC7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    SetScenarioFlags(0x3C, 7)

    label("loc_AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFB")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2D")
    SetChrPos(0x0, 40630, 0, 3050, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 9)

    label("loc_B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_B60")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B60")
    SetChrPos(0x0, 40350, 0, 5000, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_B8A")
    ClearScenarioFlags(0x3E, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B87")
    Event(0, 44)
    Jump("loc_B8A")

    label("loc_B87")

    Event(0, 8)

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_BA3")
    ClearScenarioFlags(0x22, 2)
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_BC0")

    label("loc_BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_BC0")
    ClearScenarioFlags(0x22, 3)
    SetChrPos(0x0, 39720, 0, 2910, 135)

    label("loc_BC0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE9")
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_C66")

    label("loc_BE9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C08")
    Event(0, 18)
    Jump("loc_C66")

    label("loc_C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3A")
    SetMapFlags(0x10000000)
    Event(0, 44)

    label("loc_C3A")

    Jump("loc_C66")

    label("loc_C3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")
    Event(0, 45)
    Jump("loc_C66")

    label("loc_C55")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C66")
    Event(0, 46)

    label("loc_C66")

    Return()

    # Function_3_577 end

    def Function_4_C67(): pass

    label("Function_4_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C83")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C95")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_C95")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D19")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xC8, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_D30")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_D30")

    label("loc_D30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D56")
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    Jump("loc_D69")

    label("loc_D56")

    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DA6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D93")
    SetMapObjFrame(0x8, "mark00", 0x0, 0x1)
    Jump("loc_DA1")

    label("loc_D93")

    SetMapObjFrame(0x2, "mark00", 0x0, 0x1)

    label("loc_DA1")

    Jump("loc_DD5")

    label("loc_DA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC7")
    SetMapObjFrame(0x8, "mark01", 0x0, 0x1)
    Jump("loc_DD5")

    label("loc_DC7")

    SetMapObjFrame(0x2, "mark01", 0x0, 0x1)

    label("loc_DD5")

    MiniGame(0x2F, 0x2, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xC, 0x80)
    SetMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E15")
    OP_70(0x4, 0x0)
    Jump("loc_E19")

    label("loc_E15")

    OP_70(0x4, 0x1E)

    label("loc_E19")

    Return()

    # Function_4_C67 end

    def Function_5_E1A(): pass

    label("Function_5_E1A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1A")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('狙击枪管', 1)"), scpexpr(EXPR_END)), "loc_EA3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '狙击枪管'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_F15")

    label("loc_EA3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '狙击枪管'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '狙击枪管'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F15")

    Jump("loc_F5F")

    label("loc_F1A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_F5F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E1A end

    def Function_6_F6B(): pass

    label("Function_6_F6B")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Do you want to move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City West Exit\x01",            # 0
            "Stop (near the police school)\x01",      # 1
            "quit\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1007")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1027")

    label("loc_1007")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1027")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()

    label("loc_1027")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_F6B end

    def Function_7_102F(): pass

    label("Function_7_102F")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1158")
    Fade(500)
    OP_68(27670, 1000, 21230, 0)
    MoveCamera(319, 34, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, 32119, 0, 25500, 270)
    SetChrPos(0x1, 32119, 0, 24000, 270)
    SetChrPos(0x2, 32119, 0, 22500, 270)
    SetChrPos(0x3, 32119, 0, 21000, 270)
    ClearChrFlags(0xC, 0x80)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xC)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xC, 27000, 0, 10810, 0)
    OP_D5(0xC, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)

    def lambda_110F():
        OP_95(0xFE, 27000, 0, 23850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_110F)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xC, 1)
    OP_71(0x3, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x3)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_1158")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_102F end

    def Function_8_115C(): pass

    label("Function_8_115C")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, 31190, 0, 26620, 270)
    OP_31(0x1)
    OP_68(31190, 1000, 26620, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x5)
    Return()

    # Function_8_115C end

    def Function_9_11AD(): pass

    label("Function_9_11AD")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1208")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11FD")
    Sound(2502, 255, 100, 0)
    Jump("loc_1203")

    label("loc_11FD")

    Sound(2503, 255, 100, 0)

    label("loc_1203")

    Jump("loc_122C")

    label("loc_1208")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1226")
    Sound(3347, 255, 100, 0)
    Jump("loc_122C")

    label("loc_1226")

    Sound(3348, 255, 100, 0)

    label("loc_122C")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_11AD end

    def Function_10_1241(): pass

    label("Function_10_1241")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1261")
    Call(0, 23)
    Return()

    label("loc_1261")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1272")
    Jump("loc_1322")

    label("loc_1272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1280")
    Jump("loc_1322")

    label("loc_1280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_130B")

    ChrTalk(
        0xF,
        (
            "#07900FThanks to you\x01",
            "I was able to stop the runaway car.\x02\x03",
            "#07904FFor a while with this\x01",
            "You can concentrate on security at the border.\x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1322")

    label("loc_130B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1319")
    Jump("loc_1322")

    label("loc_1319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1322")

    label("loc_1322")

    TalkEnd(0xFE)
    Return()

    # Function_10_1241 end

    def Function_11_1326(): pass

    label("Function_11_1326")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1738")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156B")

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Oh, are they Randy?\x01",
            "Somehow it's been a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FWell, Carter.\x01",
            "How is the state of the Belgard gate?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "…… to this\x01",
            "You got it.\x01",
            "To be honest, it is very confusing.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Under the command of the commander,\x01",
            "In the meantime invasion of the Imperial Army\x01",
            "It is a story to watch out.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "It is also in the midst of civil war,\x01",
            "I do not think I'm worried for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FIs that so……\x01",
            "IM a litte relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, I guess it's hard to … …\x01",
            "Please hold on.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Oh, leave it to me.\x01",
            "The meaning as a defense army\x01",
            "I will show you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 1)
    Jump("loc_1733")

    label("loc_156B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1680")

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Independence has become invalidated\x01",
            "Moreover, it disappeared to Secretary of Defense ……\x01",
            "The defense armies are also confused.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Just Well … thanks to the commander\x01",
            "For the time being we will not lose sight of purpose.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "As a defense army to protect the crossbell,\x01",
            "This place is in the edge.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1733")

    label("loc_1680")


    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Independence has become invalidated\x01",
            "Moreover, it disappeared to Secretary of Defense ……\x01",
            "The defense armies are also confused.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "As a defense army to protect the crossbell,\x01",
            "This place is in the edge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1733")

    Jump("loc_20F1")

    label("loc_1738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1883")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1806")

    ChrTalk(
        0x8,
        (
            "From that raid incident,\x01",
            "The tension with the two major powers is rising considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rumor, soon\x01",
            "It is a rumor that it will be done until a massive exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As if before the conclusion of the \"treaty of non-war\"\x01",
            "I feel like I returned.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_187E")

    label("loc_1806")


    ChrTalk(
        0x8,
        (
            "From that raid incident,\x01",
            "The tension with the two major powers is rising considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As if before the conclusion of the \"treaty of non-war\"\x01",
            "I feel like I returned.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187E")

    Jump("loc_20F1")

    label("loc_1883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A55")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1959")

    ChrTalk(
        0x8,
        (
            "As for the restoration work of the track,\x01",
            "I managed to find out what I remained\x01",
            "I was cleared up during the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even then, I met yesterday.\x01",
            "That ridiculous thing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As expected after all\x01",
            "Was it the cause of the accident?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19CC")

    label("loc_1959")


    ChrTalk(
        0x8,
        (
            "To be honest, that time\x01",
            "The girl escaped\x01",
            "I'm relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As expected after all that\x01",
            "Was it the cause of the accident?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CC")

    Jump("loc_1A50")

    label("loc_19D1")


    ChrTalk(
        0x8,
        (
            "The rough car a while ago,\x01",
            "You seem to have caught it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks,\x01",
            "One security concern decreased by one.\x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A50")

    Jump("loc_20F1")

    label("loc_1A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B25")

    ChrTalk(
        0x8,
        (
            "Recently, strangely rough cars\x01",
            "I often come around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Absolutely …\x01",
            "What do you do if you woke up in an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When the border is in tension,\x01",
            "There was a guy who could not read the air.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BA7")

    label("loc_1B25")


    ChrTalk(
        0x8,
        (
            "Recently, strangely rough cars\x01",
            "I often come around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When the border is in tension,\x01",
            "There was a guy who could not read the air.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA7")

    Jump("loc_20F1")

    label("loc_1BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C8D")

    ChrTalk(
        0x8,
        (
            "Since independence advocacy at trade meeting,\x01",
            "The border is in a state of tension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's all\x01",
            "Because the mayor said,\x01",
            "Naturally it is a natural result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, to avoid distracting\x01",
            "I have to guard it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D03")

    label("loc_1C8D")


    ChrTalk(
        0x8,
        (
            "Since independence advocacy at trade meeting,\x01",
            "The border is in a state of tension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, to avoid distracting\x01",
            "I have to guard it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D03")

    Jump("loc_20F1")

    label("loc_1D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D23")
    Call(0, 12)
    Jump("loc_1DCD")

    label("loc_1D23")


    ChrTalk(
        0x8,
        (
            "Suddenly, during today's plenary session\x01",
            "Raise security level of border\x01",
            "It is said that it was decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now from the Tangram gate\x01",
            "Douglas deputy command came,\x01",
            "She seems to be meeting with the commander.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCD")

    Jump("loc_20F1")

    label("loc_1DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DED")
    Call(0, 12)
    Jump("loc_1F24")

    label("loc_1DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EAC")

    ChrTalk(
        0x8,
        (
            "During the trade meeting,\x01",
            "Border guards are becoming strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "VIPs from neighboring countries\x01",
            "Now that we are gathered in the crossbell … …\x01",
            "Failure to do so may cause international problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The guard's responsibility is serious.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F24")

    label("loc_1EAC")


    ChrTalk(
        0x8,
        (
            "VIPs from neighboring countries\x01",
            "Now that we are gathered in the crossbell … …\x01",
            "Failure to do so may cause international problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The guard's responsibility is serious.\x02",
    )

    CloseMessageWindow()

    label("loc_1F24")

    Jump("loc_20F1")

    label("loc_1F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_20F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F44")
    Call(0, 12)
    Jump("loc_20F1")

    label("loc_1F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2094")

    ChrTalk(
        0x8,
        (
            "After a strange drug was served in the case incident,\x01",
            "Their guys are truly terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because of overworking the body to the limit\x01",
            "My body screamed,\x01",
            "It was in a state not very usable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So the commander invoked Randy,\x01",
            "Rehabilitation training with actual warfare\x01",
            "That's why I did it for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to that, I could regain the can,\x01",
            "I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20F1")

    label("loc_2094")


    ChrTalk(
        0x8,
        "I was taken care of in rehabilitation training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to that, I could regain the can,\x01",
            "I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20F1")

    TalkEnd(0xFE)
    Return()

    # Function_11_1326 end

    def Function_12_20F5(): pass

    label("Function_12_20F5")


    ChrTalk(
        0x8,
        (
            "Here is the gate of the Belgian gate gate.\x01",
            "If you plan to go to the empire\x01",
            "Please take a check inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 500)

    ChrTalk(
        0x8,
        "…… Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FWell, are you guarding well today as well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, as usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so, rehabilitation training\x01",
            "Really, I was taken care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to that, I could regain the can.\x01",
            "I will reward you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHeck, I do not care.\x01",
            "What is new commander\x01",
            "It was a direct result.\x02\x03",
            "#00309FWell, when I want to be shy again\x01",
            "Please call me anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wait … … please forgive me.\x01",
            "As expected it is sorry for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 5)
    OP_93(0x8, 0x5A, 0x0)
    Return()

    # Function_12_20F5 end

    def Function_13_231B(): pass

    label("Function_13_231B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_241C")

    NpcTalk(
        0x9,
        "Soldier Logging",
        (
            "Um, it appeared in the wetland area\x01",
            "Huge trees ……\x01",
            "When it appeared I pulled my back.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Logging",
        (
            "Anyway, my one soldier\x01",
            "It seems not to be a thing to hand.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Logging",
        (
            "Role as a defense army now\x01",
            "I have to keep it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24B5")

    label("loc_241C")


    NpcTalk(
        0x9,
        "Soldier Logging",
        (
            "Um, a huge tree ……\x01",
            "One who is a soldier\x01",
            "It seems not to be a thing to hand.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Logging",
        (
            "Role as a defense army now\x01",
            "I have to keep it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B5")

    Jump("loc_2FFD")

    label("loc_24BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2602")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2598")

    ChrTalk(
        0x9,
        (
            "In the battle in the direction of Mainz,\x01",
            "The third company is destroyed …\x01",
            "The rescue troops were also hit hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A number of armored cars are crushed … …\x01",
            "To be honest, the guard's damage is\x01",
            "unfathomable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hunters ……\x01",
            "Absolutely can not forgive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25FD")

    label("loc_2598")


    ChrTalk(
        0x9,
        (
            "In a series of attacks\x01",
            "The damage of the guard is\x01",
            "unfathomable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hunters ……\x01",
            "Absolutely can not forgive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25FD")

    Jump("loc_2FFD")

    label("loc_2602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_279D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2732")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CA")

    ChrTalk(
        0x9,
        (
            "To yesterday's monster like a gigantic demon\x01",
            "I felt tremendous strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently the \"phantom beast\" that was in the report\x01",
            "It seems they were different … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm, I can not stop my career still.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_272D")

    label("loc_26CA")


    ChrTalk(
        0x9,
        (
            "To yesterday's monster like a gigantic demon\x01",
            "I felt tremendous strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm, I can not stop my career still.\x02",
    )

    CloseMessageWindow()

    label("loc_272D")

    Jump("loc_2798")

    label("loc_2732")


    ChrTalk(
        0x9,
        (
            "Absolutely …\x01",
            "It was annoying young people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… … Reassess me,\x01",
            "Let's concentrate on security.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2798")

    Jump("loc_2FFD")

    label("loc_279D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_286B")

    ChrTalk(
        0x9,
        (
            "If national independence is realized,\x01",
            "Our guard as regular army\x01",
            "You will have decent military force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Still the empire and the Republic are a threat … …\x01",
            "To show pride of Crossbell,\x01",
            "It is a place I want you to realize.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FFD")

    label("loc_286B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2956")

    ChrTalk(
        0x9,
        (
            "As we discussed at the trade meeting,\x01",
            "Compared to other countries' troops\x01",
            "It is certainly an odd existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, it is because\x01",
            "Other empire and republic ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To be made an attack material with it,\x01",
            "It feels kind of tough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29FE")

    label("loc_2956")


    ChrTalk(
        0x9,
        (
            "We guard\x01",
            "For consideration to the Empire and the Republic,\x01",
            "Only a minimum of arming is allowed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, it is because\x01",
            "Other empire and republic ……\x01",
            "It feels kind of tough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29FE")

    Jump("loc_2FFD")

    label("loc_2A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB2")

    ChrTalk(
        0x9,
        (
            "Douglas deputy commander ……\x01",
            "If it is a hand-to-hand combat, in the guard\x01",
            "It is the strongest person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I would like to respond if I have the chance\x01",
            "Though it is ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FSo like this,\x01",
            "With Douglas's older brother\x01",
            "I only made arrangements.\x02\x03",
            "#00306FNo, it was truly a strong enemy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 500)

    ChrTalk(
        0x9,
        "what……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Randy,\x01",
            "Would you like to hand in with me?\x01",
            "I hope you will try your arms by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHahaha, if there is a chance\x01",
            "I'm guarding with a spirit and guarding it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C45")

    label("loc_2BB2")

    TurnDirection(0x9, 0x104, 0)

    ChrTalk(
        0x9,
        (
            "Mu … … certainly, to the current mission\x01",
            "It is important to concentrate more than anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… Then this time please hand it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304FI wish I could remember it.\x02",
    )

    CloseMessageWindow()

    label("loc_2C45")

    OP_93(0x9, 0x5A, 0x0)
    Jump("loc_2FFD")

    label("loc_2C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D07")

    ChrTalk(
        0x9,
        (
            "Leaders in Michelam direction\x01",
            "It is guarding even in the corps\x01",
            "They are superior in fighting power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "High grade in actual practice exercises\x01",
            "If they continue to leave,\x01",
            "The security of the leaders will not be shaken.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FFD")

    label("loc_2D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F67")

    ChrTalk(
        0x9,
        (
            "Since Sonya Command was assigned,\x01",
            "The morale of the Belgard gate is also\x01",
            "I think that it has increased considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To that evidence, in that cult\x01",
            "The bounce back after having medicine\x01",
            "It was speedy up to a strange one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, if you compare with the previous command\x01",
            "Because it is a moon and a turtle.\x02\x03",
            "#00300FIf you can endure that Spartan,\x01",
            "He would not be a superior superior alone.\x01",
            "I am motivated to go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh … … From now on,\x01",
            "I should go ahead with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I, in that cult's case\x01",
            "To Joachim Gunter\x01",
            "It is that my body has been hijacked ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh, I see.\x01",
            "I wish there were such things.\x02\x03",
            "#00300FWell, let's try each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FFD")

    label("loc_2F67")


    ChrTalk(
        0x9,
        (
            "I, in that cult's case\x01",
            "To Joachim Gunter\x01",
            "It is that my body has been hijacked ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even in that sense,\x01",
            "From now on\x01",
            "I should go ahead with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FFD")

    TalkEnd(0xFE)
    Return()

    # Function_13_231B end

    def Function_14_3001(): pass

    label("Function_14_3001")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3012")
    Jump("loc_315D")

    label("loc_3012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_315D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F2")

    ChrTalk(
        0xA,
        (
            "Since the inspection of the freight train is over,\x01",
            "This time I am inspecting a new armored car … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, I still do not match numbers.\x01",
            "It seems that one of them is missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although there is a key,\x01",
            "Where the hell have you gone …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_315D")

    label("loc_30F2")


    ChrTalk(
        0xA,
        (
            "Well, guarding the security guards alarming\x01",
            "It is hard to think that there was a theft ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Where the hell have you gone …?\x02",
    )

    CloseMessageWindow()

    label("loc_315D")

    TalkEnd(0xFE)
    Return()

    # Function_14_3001 end

    def Function_15_3161(): pass

    label("Function_15_3161")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3172")
    Jump("loc_3231")

    label("loc_3172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3180")
    Jump("loc_3231")

    label("loc_3180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_318E")
    Jump("loc_3231")

    label("loc_318E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_319C")
    Jump("loc_3231")

    label("loc_319C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31AA")
    Jump("loc_3231")

    label("loc_31AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31B8")
    Jump("loc_3231")

    label("loc_31B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3231")

    ChrTalk(
        0xB,
        (
            "Compared to Galleria Fortress\x01",
            "It is a frugal border guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ho ho ho, the empire and the crossbell\x01",
            "It is a different case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3231")

    TalkEnd(0xFE)
    Return()

    # Function_15_3161 end

    def Function_16_3235(): pass

    label("Function_16_3235")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3267")
    SetScenarioFlags(0x31, 2)

    label("loc_3267")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_32A7")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_329C")
    Sound(2499, 255, 100, 0)
    Jump("loc_32A2")

    label("loc_329C")

    Sound(3537, 255, 100, 0)

    label("loc_32A2")

    Jump("loc_32AD")

    label("loc_32A7")

    Sound(3344, 255, 100, 0)

    label("loc_32AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_356A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_3326")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3306"),
        (SWITCH_DEFAULT, "loc_3317"),
    )


    label("loc_3306")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3321")

    label("loc_3317")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3321")

    Jump("loc_3565")

    label("loc_3326")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_335A")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_335A")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_338E"),
        (1, "loc_3492"),
        (2, "loc_3523"),
        (SWITCH_DEFAULT, "loc_355B"),
    )


    label("loc_338E")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_33BF")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_33CF")

    label("loc_33BF")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_33CF")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3425")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3425")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3448")
    Sound(461, 0, 100, 0)

    label("loc_3448")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3468")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_3478")

    label("loc_3468")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_3478")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_32AD")

    label("loc_3492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3504")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_34C7")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_34DF")

    label("loc_34C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_34DA")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_34DF")

    label("loc_34DA")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_34DF")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_351E")

    label("loc_3504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3514")
    OP_AF(0xFB)
    Jump("loc_351E")

    label("loc_3514")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_351E")

    Jump("loc_3565")

    label("loc_3523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3556")

    label("loc_353C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_354C")
    OP_AF(0xFB)
    Jump("loc_3556")

    label("loc_354C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3556")

    Jump("loc_3565")

    label("loc_355B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3565")

    Jump("loc_32AD")

    label("loc_356A")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_16_3235 end

    def Function_17_3578(): pass

    label("Function_17_3578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_35C0")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The guiding bus seems to be out of service.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_35C0")

    Call(0, 6)
    Return()

    # Function_17_3578 end

    def Function_18_35C4(): pass

    label("Function_18_35C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("apl/ch51617.itc", 0x1F)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 56500, -10000, -17750, 270)
    SetChrPos(0x106, 54930, -10000, -18100, 270)
    SetChrPos(0x103, 57350, -10000, -16910, 270)
    SetChrPos(0x104, 58650, -10000, -17610, 270)
    SetChrPos(0x107, 60460, -10000, -18210, 270)
    SetChrPos(0x105, 57950, -10000, -18590, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x16, 22000, 0, -4500, 90)
    SetChrPos(0x17, 22000, 0, 4500, 90)
    SetChrPos(0x18, 40000, 0, -1000, 270)
    SetChrPos(0x19, 13500, 0, 1500, 90)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x105, 0x8)
    OP_68(30000, 2600, 0, 0)
    MoveCamera(300, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(42000, 5000)

    def lambda_3745():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3745)

    def lambda_375A():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_375A)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(20000, 0, 0, 0)
    MoveCamera(295, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(35000, 0)
    OP_6F(0x79)
    OP_0D()
    PlaceName2(340, 40, "c_plac18", 0x0, 2000)
    OP_68(30000, -6000, -16300, 8000)
    MoveCamera(295, 23, 0, 8000)
    OP_6F(0x79)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x105, 0x8)
    Fade(1000)
    OP_68(34000, -9000, -18000, 0)
    MoveCamera(294, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(32000, 0)
    SetCameraDistance(26000, 3000)
    OP_9B(0x0, 0x106, 0x0, 0x36B0, 0x1388, 0x0)
    Sleep(500)
    OP_93(0x106, 0xB4, 0x1F4)
    Sleep(400)

    def lambda_384D():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_384D)
    Sleep(50)

    def lambda_3865():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3865)
    Sleep(50)

    def lambda_387D():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_387D)
    Sleep(50)

    def lambda_3895():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3895)
    Sleep(50)

    def lambda_38AD():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_38AD)
    OP_93(0x106, 0x5A, 0x1F4)
    Sleep(1500)
    OP_68(34000, -7000, -18000, 6000)
    OP_93(0x106, 0x10E, 0x1F4)

    def lambda_38E4():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_38E4)
    OP_0D()
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x106, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x107, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("t2030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_35C4 end

    def Function_19_3928(): pass

    label("Function_19_3928")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("apl/ch51617.itc", 0x1F)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 51930, 0, -950, 265)
    SetChrPos(0x104, 52610, 0, -1880, 265)
    SetChrPos(0x105, 52860, 0, -490, 265)
    SetChrPos(0x106, 53190, 0, -3040, 265)
    SetChrPos(0x107, 54210, 0, -1760, 265)
    SetChrPos(0x103, 53950, 0, 0, 265)
    SetChrSubChip(0x107, 0x5)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x16, 22090, 0, 4230, 90)
    SetChrPos(0x17, 22670, 0, -4790, 90)
    SetChrPos(0x18, 27780, 0, 18140, 0)
    SetChrPos(0x19, 30910, 0, 2200, 90)
    BeginChrThread(0x16, 1, 0, 0)
    BeginChrThread(0x17, 1, 0, 0)
    BeginChrThread(0x18, 1, 0, 20)
    BeginChrThread(0x19, 1, 0, 21)
    ClearChrFlags(0x1A, 0x80)
    OP_78(0x8, 0x1A)
    SetChrPos(0x1A, 23760, 100, 7200, 90)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_D5(0x1A, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(22660, 1000, 1180, 0)
    MoveCamera(313, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(19830, 0)
    FadeToBright(1000, 0)
    OP_68(26920, 1000, 190, 6000)
    MoveCamera(308, 27, 0, 6000)
    OP_6E(570, 6000)
    SetCameraDistance(34630, 6000)
    Sleep(6000)
    Fade(500)
    OP_68(52520, 1000, -1710, 0)
    MoveCamera(302, 25, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(14930, 0)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#10401F#12P(The security system at the Belgard gate is\x01",
            "It sounds like everything. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12P(Oh, I can not honestly hesitate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#6P(Those who retired from here\x01",
            "Looks nice … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11P(Oh, let 's do that.\x02",
    )

    CloseMessageWindow()
    OP_68(56150, 1000, -1420, 3000)
    MoveCamera(317, 29, 0, 3000)
    OP_6E(590, 3000)
    SetCameraDistance(19830, 3000)
    BeginChrThread(0x103, 1, 0, 22)
    Sleep(50)
    BeginChrThread(0x107, 1, 0, 22)
    Sleep(60)
    BeginChrThread(0x106, 1, 0, 22)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 22)
    Sleep(70)
    BeginChrThread(0x104, 1, 0, 22)
    Sleep(50)
    BeginChrThread(0x101, 1, 0, 22)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x107, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x106, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r1040", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_19_3928 end

    def Function_20_3C9C(): pass

    label("Function_20_3C9C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CEE")
    OP_95(0xFE, 27780, 0, 4550, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 27780, 0, 18140, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_20_3C9C")

    label("loc_3CEE")

    Return()

    # Function_20_3C9C end

    def Function_21_3CEF(): pass

    label("Function_21_3CEF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D41")
    OP_95(0xFE, 30910, 0, -3330, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 30910, 0, 2200, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_21_3CEF")

    label("loc_3D41")

    Return()

    # Function_21_3CEF end

    def Function_22_3D42(): pass

    label("Function_22_3D42")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    Return()

    # Function_22_3D42 end

    def Function_23_3D59(): pass

    label("Function_23_3D59")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(14790, 900, 26150, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27410, 0)
    SetChrPos(0x101, 15240, 0, 25330, 270)
    SetChrPos(0x104, 15190, 0, 26760, 270)
    SetChrPos(0x102, 15590, 0, 23920, 315)
    SetChrPos(0x103, 16000, 0, 27520, 225)
    SetChrPos(0x105, 16620, 0, 26210, 270)
    SetChrPos(0x109, 16610, 0, 24810, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07900.itp")
    OP_4B(0xF, 0xFF)
    OP_93(0xF, 0x5A, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47DD")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xF,
        (
            "Randy … and besides\x01",
            "Everyone in the Special Affairs Division.\x02\x03",
            "Is cheers for good work,\x01",
            "You came a lot.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000FLt. Mirelle, good work\x02\x03",
            "#00004FYesterday was the railroad restoration work,\x01",
            "I really appreciate your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07902FYeah, that's what it got\x01",
            "Although it was good …\x02\x03",
            "#07903FAfter all the footsteps of that giant monster\x01",
            "You can not grasp it.\x02\x03",
            "#07908FToday as well to the troops in the autonomous state patrol\x01",
            "I am instructing the search,\x01",
            "Whether honest results will improve …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F…… Well, what should be given priority\x01",
            "It was probably the restoration of the railroad.\x02\x03",
            "#00300FI forgot the things of chemistry for the time being,\x01",
            "Those who devoted to the current job\x01",
            "Is not it nice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#07903FYes, that's true\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, today I looked at the request\x01",
            "I came here.\x02\x03",
            "The contents of the request are promptly\x01",
            "Even if I tell you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07900FRight, got it\x02\x03",
            "#07903FRecently, on the West Crossbell Highway\x01",
            "Hazardous driving … … so-called\x01",
            "Runaway cars are in and out.\x02\x03",
            "#07900FEmpire tourists and regular buses\x01",
            "I am treating a lot of trouble.\x02\x03",
            "To you,\x01",
            "To crack down on that\x01",
            "I want you to cooperate.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4358")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆ \"Crackdown on Runaway Vehicles\"? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",        # 0
            "【Are doing】\x01",        # 1
            "【not doing】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_433F"),
        (1, "loc_4344"),
        (2, "loc_434E"),
        (SWITCH_DEFAULT, "loc_4358"),
    )


    label("loc_433F")

    Jump("loc_4358")

    label("loc_4344")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_4358")

    label("loc_434E")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_4358")

    label("loc_4358")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4432")

    ChrTalk(
        0x109,
        (
            "#10103FRunaway car …\x01",
            "It seems like you heard it somewhere.\x02\x03",
            "#10101FDid you mean ……\x01",
            "I caught in the city before,\x01",
            "Is it an example youth team?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FI wonder if it was \"Hybrads\".\x01",
            "The possibilities may be high …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_446A")

    label("loc_4432")


    ChrTalk(
        0x109,
        (
            "#10103FWell … indeed it is\x01",
            "It looks not good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_446A")


    ChrTalk(
        0xF,
        (
            "#07901FYes, from the Empire / Republic\x01",
            "Now that deterioration of security is regarded as a problem … …\x02\x03",
            "#07903FAccidents involving foreigners\x01",
            "It will be hard if you wake up.\x02\x03",
            "#07901FEven just yesterday, there was no derailment accident\x01",
            "I just got up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FWell, Crosbell's position is\x01",
            "It seems to be more dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07900FAlso, regarding this matter\x01",
            "With the police's wide area security office\x01",
            "Please work together in cooperation.\x02\x03",
            "Traveling route of runaway vehicle is\x01",
            "As I was on a highway,\x01",
            "I accepted it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FSpecifically, how\x01",
            "Is it OK to take control?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07903FThey go through the West Crossbell Highway\x01",
            "Fold back at the Belgard gate …\x01",
            "I use a route called.\x02\x03",
            "#07900FYou stick to the gate,\x01",
            "After confirming that a runaway car appeared\x01",
            "Please track with a power car.\x02\x03",
            "In the meantime, please contact the wide area security office\x01",
            "I'll have you wait in the west entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FI see… an ambush\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07900FYeah, that's right.\x01",
            "…… How can I ask?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8B, 0x1, 0x0)
    Jump("loc_4928")

    label("loc_47DD")


    ChrTalk(
        0xF,
        (
            "#07900FRunaway cars go through the West Crossbell Highway\x01",
            "Fold back at the Belgard gate …\x01",
            "I use a traveling route called.\x02\x03",
            "#07903FYou stick to the gate,\x01",
            "After confirming that a runaway car appeared\x01",
            "Please track with a power car.\x02\x03",
            "#07900FAs it is to the west exit of Crossbell City\x01",
            "With the standby wide area crime prevention division\x01",
            "It is a strategy that shoots runaway car and shoot it.\x02\x03",
            "…… How can I ask?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4928")

    Call(0, 24)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xF, 0x10E, 0x0)
    OP_4C(0xF, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 15370, 0, 25960, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_3D59 end

    def Function_24_4971(): pass

    label("Function_24_4971")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【undertake】\x01",      # 0
            "【quit】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49DC")
    Call(0, 25)
    Jump("loc_4A97")

    label("loc_49DC")


    ChrTalk(
        0x101,
        (
            "#00006F… …. Sorry, three lieutenant Mireille.\x01",
            "Now I can not take my hand … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07903Fso……\x01",
            "That's a pity.\x02\x03",
            "#07900FWell then, if the hands are empty\x01",
            "Please give me a voice.\x02\x03",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x178, 1)

    label("loc_4A97")

    Return()

    # Function_24_4971 end

    def Function_25_4A98(): pass

    label("Function_25_4A98")


    ChrTalk(
        0x101,
        (
            "#00000FOK.\x01",
            "I will underwrite it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07902FThanks, that's great\x02\x03",
            "#07903FThen, immediately\x01",
            "To the wide area crime prevention division\x01",
            "I will inform you of the start of the strategy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, please lead the way\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00300FWe are also driving\x01",
            "Let's get ready.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C27")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KAssistance section car to Belgard gate\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Stopped】\x01",        # 0
            "【It is not stopped】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4C27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CC4")
    TurnDirection(0x101, 0x104, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00000FRight\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FNoel, driving is\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FRoger that!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jump("loc_4DC6")

    label("loc_4CC4")

    TurnDirection(0x101, 0x104, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FRight\x01",
            "I will bring it in later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FNoel, driving is\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FRoger that!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Car that had been parked elsewhere\x01",
            "I moved to the Belgard gate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DC6")

    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Tracking Runaway Car】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8B, 0x4, 0x2)
    OP_29(0x8B, 0x1, 0x1)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0xF, 0x80)
    SetScenarioFlags(0x22, 2)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_4A98 end

    def Function_26_4E33(): pass

    label("Function_26_4E33")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch33002.itc", 0x1E)
    LoadChrToIndex("chr/ch20000.itc", 0x1F)
    LoadChrToIndex("chr/ch44000.itc", 0x20)
    LoadChrToIndex("chr/ch24400.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch21600.itc", 0x23)
    LoadEffect(0x6, "event\\eva04_00.eff")
    ClearChrFlags(0xC, 0x80)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xC)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xC, 27000, 0, 23850, 0)
    OP_D5(0xC, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    ClearChrFlags(0xD, 0x80)
    OP_78(0x5, 0xD)
    OP_49()
    SetChrPos(0xD, 8180, 0, 21490, 90)
    OP_D5(0xD, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x7, 0xE)
    OP_49()
    SetChrPos(0xE, 53480, 0, -180, 270)
    OP_D5(0xE, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 32119, 0, 25500, 270)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 32119, 0, 24000, 270)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 32119, 0, 22500, 270)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 32119, 0, 21000, 180)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 32119, 0, 19500, 0)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 32119, 0, 18000, 270)
    OP_68(28080, 1000, 21730, 0)
    MoveCamera(316, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25710, 0)
    SetChrPos(0xF, 13370, 0, 26130, 135)
    SetChrPos(0x101, 13930, 0, 21960, 135)
    SetChrPos(0x102, 13600, 0, 23380, 135)
    SetChrPos(0x103, 13010, 0, 24560, 135)
    SetChrPos(0x104, 13970, 0, 24800, 135)
    SetChrPos(0x109, 12600, 0, 21430, 135)
    SetChrPos(0x105, 12600, 0, 22840, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xF, 0xFF)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    BeginChrThread(0x10, 1, 0, 43)
    Sleep(20)
    BeginChrThread(0x13, 1, 0, 43)
    Sleep(50)
    BeginChrThread(0x11, 1, 0, 43)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x15, 1, 0, 43)
    Sleep(50)
    BeginChrThread(0x14, 1, 0, 43)
    Sleep(20)
    BeginChrThread(0x12, 1, 0, 43)
    Sleep(3000)
    OP_68(12730, 1000, 22990, 5000)
    MoveCamera(301, 22, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(24610, 5000)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x12, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x15, 0xFF)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00301F…… As of now runaway vehicles\x01",
            "There is no sign of appearance.\x02\x03",
            "#00306FI wonder if they're really coming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI wonder…\x02\x03",
            "#00003FOnce West Crossbell Highway\x01",
            "I thought it was a driving route\x01",
            "It seems to be a story … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat's why Kate's\x01",
            "The wide area crime prevention division can not handle it either.\x02\x03",
            "The jurisdiction of the police is usually,\x01",
            "Crossbell is in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FEven in that sense,\x01",
            "To the servants of irregular existence\x01",
            "The request has come around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FThat must be\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FAnyway, stay inside the city or town\x01",
            "You can not leave runaway acts.\x02\x03",
            "Let's go te them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#07902FI'm counting on you\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(26210, 1000, 21250, 0)
    MoveCamera(301, 34, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_70(0x3, 0x1E)
    OP_0D()
    Sound(463, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x1, 0x0)
    OP_79(0x1)
    Sleep(1500)
    OP_68(15610, 1000, 20790, 3000)
    MoveCamera(301, 34, 0, 3000)
    OP_6E(590, 3000)
    SetCameraDistance(23500, 3000)
    OP_6F(0x79)
    Sleep(500)
    Sound(488, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_560A")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆ \"Crackdown on Runaway Vehicles\"? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",        # 0
            "【Are doing】\x01",        # 1
            "【not doing】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_55F1"),
        (1, "loc_55F6"),
        (2, "loc_5600"),
        (SWITCH_DEFAULT, "loc_560A"),
    )


    label("loc_55F1")

    Jump("loc_560A")

    label("loc_55F6")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_560A")

    label("loc_5600")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_560A")

    label("loc_560A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5642")

    ChrTalk(
        0x101,
        "#3P#00005FThis sound is nothing …!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_5663")

    label("loc_5642")


    ChrTalk(
        0x101,
        "#3P#00005FThat sound was\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5663")

    Fade(500)
    OP_68(47820, 1000, 890, 0)
    MoveCamera(312, 34, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23760, 0)
    SetChrPos(0xF, 17120, 0, 24570, 135)
    SetChrPos(0x101, 16370, 0, 21380, 135)
    SetChrPos(0x102, 15090, 0, 21830, 135)
    SetChrPos(0x103, 16079, 0, 24050, 135)
    SetChrPos(0x104, 16340, 0, 22600, 135)
    SetChrPos(0x109, 14100, 0, 21100, 135)
    SetChrPos(0x105, 14900, 0, 23290, 135)
    OP_68(37310, 1000, 3570, 1000)
    MoveCamera(312, 34, 0, 1000)
    OP_6E(590, 1000)
    SetCameraDistance(24950, 1000)
    Sound(486, 0, 100, 0)
    BeginChrThread(0xE, 1, 0, 28)
    Sleep(1000)
    OP_68(24830, 1000, 19380, 1000)
    MoveCamera(311, 23, 0, 1000)
    OP_6E(590, 1000)
    SetCameraDistance(24950, 1000)
    OP_6F(0x79)
    Sound(487, 0, 100, 0)
    BeginChrThread(0xE, 3, 0, 27)
    Sleep(500)
    StopBGM(0xFA0)

    NpcTalk(
        0xC,
        "passenger",
        "Ahh!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "passenger",
        "KYAAA\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0xE,
        "Reggie",
        "Hyuu, that's dangerous!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Reggie",
        "Be careful!\x02",
    )

    CloseMessageWindow()
    OP_6B(0xE)
    BeginChrThread(0xE, 1, 0, 29)
    Sleep(3000)
    OP_6B(0xFF)
    OP_6F(0x79)
    OP_68(54850, 1000, -840, 2500)
    MoveCamera(310, 21, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(23500, 2500)
    Sound(494, 0, 100, 0)
    OP_0D()
    Sleep(4000)
    Fade(500)
    OP_68(15880, 1000, 21890, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22330, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A1E")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆ \"Crackdown on Runaway Vehicles\"? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",        # 0
            "【Are doing】\x01",        # 1
            "【not doing】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A05"),
        (1, "loc_5A0A"),
        (2, "loc_5A14"),
        (SWITCH_DEFAULT, "loc_5A1E"),
    )


    label("loc_5A05")

    Jump("loc_5A1E")

    label("loc_5A0A")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_5A1E")

    label("loc_5A14")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_5A1E")

    label("loc_5A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5A7D")

    ChrTalk(
        0x101,
        "#00001FOh, that is \"Hybrads\" …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FAnd after all … …!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AC1")

    label("loc_5A7D")


    ChrTalk(
        0x101,
        "#00001FS-so that was the race car\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FIt's so dangerous!\x02",
    )

    CloseMessageWindow()

    label("loc_5AC1")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7507", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xF, 0x104, 500)
    Sleep(100)

    ChrTalk(
        0xF,
        (
            "#07907FGet after them guys!\x02\x03",
            "I'll contact ahead!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B32():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B32)
    Sleep(50)

    def lambda_5B42():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B42)
    Sleep(50)

    def lambda_5B52():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B52)
    Sleep(50)

    def lambda_5B62():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B62)
    Sleep(50)

    def lambda_5B72():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B72)
    Sleep(50)

    def lambda_5B82():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B82)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00001FGot it!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00007FNoel, leave the navigation to me\x01",
            "Focus on driving! It is!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x109,
        "#10107FYes sir!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 3, 0, 32)
    BeginChrThread(0x101, 3, 0, 33)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 34)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 36)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 35)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 37)
    Sleep(300)

    def lambda_5C4B():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5C4B)
    Sleep(1000)
    WaitChrThread(0x109, 3)
    Sleep(500)

    def lambda_5C62():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5C62)

    def lambda_5C77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5C77)
    WaitChrThread(0x109, 2)
    Sound(461, 0, 100, 0)
    OP_71(0x5, 0x10F, 0x12C, 0x0, 0x0)
    Sleep(1500)
    OP_68(19350, 1000, 20110, 3000)
    MoveCamera(295, 33, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(22330, 3000)
    Sound(493, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 30)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)
    Sleep(1500)
    Sound(462, 0, 100, 0)
    OP_71(0x5, 0x12D, 0x14A, 0x0, 0x0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 39)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 41)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 40)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 42)
    WaitChrThread(0x102, 3)

    def lambda_5D3C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D3C)

    def lambda_5D51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5D51)
    WaitChrThread(0x104, 3)

    def lambda_5D66():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D66)

    def lambda_5D7B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5D7B)
    WaitChrThread(0x103, 3)

    def lambda_5D90():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D90)

    def lambda_5DA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5DA5)
    WaitChrThread(0x105, 3)

    def lambda_5DBA():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5DBA)

    def lambda_5DCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5DCF)
    OP_6F(0x1)
    Sleep(800)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_0D()
    Sound(461, 0, 100, 0)
    OP_71(0x5, 0x14B, 0x168, 0x1, 0x0)
    Sleep(1000)
    OP_68(29880, 1000, 3290, 2000)
    MoveCamera(295, 33, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(22330, 2000)
    Sound(493, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 31)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    Sleep(800)
    OP_68(40230, 1000, 1390, 1500)
    MoveCamera(295, 33, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(22330, 1500)
    Sound(494, 0, 100, 0)
    Sleep(3000)
    SetScenarioFlags(0x22, 0)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_4E33 end

    def Function_27_5EB0(): pass

    label("Function_27_5EB0")

    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 26730, 0, 14720, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 27000, 0, 14720, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 27700, 0, 14720, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 27000, 0, 14720, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 27000, 0, 14720, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_27_5EB0 end

    def Function_28_5FD0(): pass

    label("Function_28_5FD0")

    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    OP_9F(0x0, 0xE)
    OP_9F(0x1, 53480, 0, -180)
    OP_9F(0x1, 35030, 0, -620)
    OP_9F(0x1, 27210, 0, 9320)
    OP_9F(0x1, 26730, 0, 14720)
    OP_9F(0x1, 27000, 0, 14720)
    OP_9F(0x2, 0xE, 18000, 0x6)
    OP_9B(0x1, 0xE, 0x10E, 0x7D0, 0x4650, 0x0)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    Return()

    # Function_28_5FD0 end

    def Function_29_604B(): pass

    label("Function_29_604B")

    Sound(493, 0, 100, 0)
    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    OP_9E(0xFE, 0x7AD0, 0x212A, 0xFFFEDB08, 0x2710, 0x4)
    OP_9B(0x1, 0xE, 0xB4, 0x2AF8, 0x2EE0, 0x0)
    Sound(492, 0, 100, 0)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    Sleep(1000)
    Sound(486, 0, 100, 0)
    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    OP_9E(0xFE, 0x78BE, 0xFFFFE76E, 0x124F8, 0x2EE0, 0x1)
    OP_98(0xE, 0x9C40, 0x0, 0x0, 0x3A98, 0x0)
    Return()

    # Function_29_604B end

    def Function_30_60D2(): pass

    label("Function_30_60D2")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, 15520, 0, 21370)
    OP_9F(0x1, 19310, 0, 18600)
    OP_9F(0x2, 0xD, 5000, 0x6)
    Return()

    # Function_30_60D2 end

    def Function_31_60FC(): pass

    label("Function_31_60FC")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, 25620, 0, 9880)
    OP_9F(0x1, 30580, 0, 1500)
    OP_9F(0x1, 37950, 0, 230)
    OP_9F(0x1, 45610, 0, 160)
    OP_9F(0x2, 0xD, 10000, 0x6)
    OP_98(0xD, 0x6D60, 0x0, 0x0, 0x2710, 0x0)
    Return()

    # Function_31_60FC end

    def Function_32_6156(): pass

    label("Function_32_6156")

    OP_95(0x109, 11600, 0, 19760, 4000, 0x0)
    OP_95(0x109, 8490, 0, 19730, 4000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Sound(462, 0, 100, 0)
    OP_71(0x5, 0xF1, 0x10E, 0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_32_6156 end

    def Function_33_619B(): pass

    label("Function_33_619B")

    OP_95(0x101, 21660, 0, 22150, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_33_619B end

    def Function_34_61B7(): pass

    label("Function_34_61B7")

    OP_95(0x102, 20460, 0, 22280, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_34_61B7 end

    def Function_35_61D3(): pass

    label("Function_35_61D3")

    OP_95(0x103, 19000, 0, 23000, 2000, 0x0)
    OP_93(0x103, 0xB4, 0x1F4)
    Return()

    # Function_35_61D3 end

    def Function_36_61EF(): pass

    label("Function_36_61EF")

    OP_95(0x104, 20290, 0, 23430, 2000, 0x0)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_36_61EF end

    def Function_37_620B(): pass

    label("Function_37_620B")

    OP_95(0x105, 18030, 0, 23200, 2000, 0x0)
    OP_93(0x105, 0xB4, 0x1F4)
    Return()

    # Function_37_620B end

    def Function_38_6227(): pass

    label("Function_38_6227")

    OP_95(0x101, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x101, 0xE1, 0x1F4)

    def lambda_6247():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6247)

    def lambda_625C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_625C)
    Return()

    # Function_38_6227 end

    def Function_39_6269(): pass

    label("Function_39_6269")

    Sleep(800)
    OP_95(0x102, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x102, 0xE1, 0x1F4)
    Return()

    # Function_39_6269 end

    def Function_40_6288(): pass

    label("Function_40_6288")

    Sleep(1000)
    OP_95(0x103, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_40_6288 end

    def Function_41_62A7(): pass

    label("Function_41_62A7")

    Sleep(800)
    OP_95(0x104, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x104, 0xE1, 0x1F4)
    Return()

    # Function_41_62A7 end

    def Function_42_62C6(): pass

    label("Function_42_62C6")

    Sleep(1200)
    OP_95(0x105, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_42_62C6 end

    def Function_43_62E5(): pass

    label("Function_43_62E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63FD")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6328"),
        (1, "loc_6342"),
        (2, "loc_635C"),
        (3, "loc_6376"),
        (4, "loc_6390"),
        (5, "loc_63AA"),
        (6, "loc_63C4"),
        (SWITCH_DEFAULT, "loc_63DE"),
    )


    label("loc_6328")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_63F8")

    label("loc_6342")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_63F8")

    label("loc_635C")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_63F8")

    label("loc_6376")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_63F8")

    label("loc_6390")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_63F8")

    label("loc_63AA")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_63F8")

    label("loc_63C4")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_63F8")

    label("loc_63DE")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_63F8")

    label("loc_63F8")

    Jump("Function_43_62E5")

    label("loc_63FD")

    Return()

    # Function_43_62E5 end

    def Function_44_63FE(): pass

    label("Function_44_63FE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6470")
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_6470")

    SetMapObjFlags(0x5, 0x4)
    FadeToBright(1000, 0)
    OP_68(16650, 400, -10470, 0)
    MoveCamera(295, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22430, 0)
    OP_0D()
    Sleep(500)
    OP_68(14930, 400, 890, 5000)
    MoveCamera(280, 18, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(56040, 5000)
    PlaceName2(340, 200, "c_plac18", 0x0, 4000)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(50970, 1000, -460, 4700)
    MoveCamera(315, 30, 0, 4700)
    OP_6E(510, 4700)
    SetCameraDistance(26660, 4700)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6871")
    Sleep(2500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65AF")
    SetChrPos(0x101, 54820, 0, -130, 270)
    SetChrPos(0x102, 56020, 0, -1200, 270)
    SetChrPos(0x103, 56170, 0, 1010, 270)
    SetChrPos(0x104, 57750, 0, -1090, 270)
    SetChrPos(0x109, 57900, 0, 920, 270)
    SetChrPos(0x105, 59100, 0, -120, 270)
    Jump("loc_6604")

    label("loc_65AF")

    SetChrPos(0x101, 54820, 0, -130, 270)
    SetChrPos(0x102, 56020, 0, -1200, 270)
    SetChrPos(0x104, 56170, 0, 1010, 270)
    SetChrPos(0x109, 57750, 0, -1090, 270)
    SetChrPos(0x105, 57900, 0, 920, 270)

    label("loc_6604")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_672A")

    def lambda_6619():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6619)

    def lambda_6633():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6633)
    Sleep(100)

    def lambda_6647():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6647)

    def lambda_6661():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6661)
    Sleep(120)

    def lambda_6675():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6675)

    def lambda_668F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_668F)
    Sleep(90)

    def lambda_66A3():
        OP_95(0xFE, 53750, 0, -1090, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_66A3)

    def lambda_66BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_66BD)
    Sleep(100)

    def lambda_66D1():
        OP_95(0xFE, 53900, 0, 920, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_66D1)

    def lambda_66EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_66EB)
    Sleep(80)

    def lambda_66FF():
        OP_95(0xFE, 55100, 0, -120, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_66FF)

    def lambda_6719():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6719)
    Jump("loc_680D")

    label("loc_672A")


    def lambda_672F():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_672F)

    def lambda_6749():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6749)
    Sleep(100)

    def lambda_675D():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_675D)

    def lambda_6777():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6777)
    Sleep(120)

    def lambda_678B():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_678B)

    def lambda_67A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_67A5)
    Sleep(90)

    def lambda_67B9():
        OP_95(0xFE, 53750, 0, -1090, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_67B9)

    def lambda_67D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_67D3)
    Sleep(100)

    def lambda_67E7():
        OP_95(0xFE, 53900, 0, 920, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_67E7)

    def lambda_6801():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6801)

    label("loc_680D")

    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6835")
    WaitChrThread(0x103, 1)

    label("loc_6835")

    Fade(500)
    OP_68(52070, 1000, -280, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19600, 0)
    OP_0D()
    Sleep(1000)
    Jump("loc_6D99")

    label("loc_6871")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B22")
    ClearChrFlags(0xD, 0x80)
    OP_78(0x5, 0xD)
    OP_49()
    SetChrPos(0xD, 63820, 0, -120, 0)
    OP_D5(0xD, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_0D()
    OP_49()
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    Sleep(2200)

    def lambda_68EA():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_68EA)
    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(2500)
    Sound(492, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xD, 0x1)
    SetChrPos(0xD, 40000, 0, 5000, 0)
    OP_D5(0xD, 0x0, 0x15F90, 0x0, 0x0)
    OP_71(0x5, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x2)
    OP_66(0x2, 0x1)
    OP_68(50970, 1000, -460, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26660, 0)
    Sleep(1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A8D")
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 37700, 0, 1500, 135)
    SetChrPos(0x102, 37700, 0, -300, 45)
    SetChrPos(0x103, 38400, 0, 2000, 180)
    SetChrPos(0x104, 39000, 0, -800, 0)
    SetChrPos(0x109, 39900, 0, 1600, 225)
    SetChrPos(0x105, 39900, 0, -200, 315)
    OP_68(38860, 1200, 640, 0)
    MoveCamera(304, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19050, 0)
    Jump("loc_6B10")

    label("loc_6A8D")

    SetChrPos(0x101, 37700, 0, 900, 90)
    SetChrPos(0x102, 39000, 0, -800, 0)
    SetChrPos(0x104, 38400, 0, 2000, 180)
    SetChrPos(0x109, 39900, 0, 1600, 225)
    SetChrPos(0x105, 39900, 0, -200, 315)
    OP_68(39330, 1200, 570, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18180, 0)

    label("loc_6B10")

    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_6D99")

    label("loc_6B22")

    ClearChrFlags(0xC, 0x80)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x2)
    OP_78(0x3, 0xC)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xC, 63820, 0, -120, 0)
    OP_D5(0xC, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_49()
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)
    Sleep(1700)
    Sound(473, 0, 100, 0)
    Sleep(500)

    def lambda_6B9B():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6B9B)
    Sleep(1000)
    Sound(467, 0, 100, 0)
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    SetMapObjFlags(0x3, 0x4)
    OP_68(50970, 1000, -460, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26660, 0)
    Sleep(1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D06")
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 30000, 0, 23620, 90)
    SetChrPos(0x102, 31600, 0, 24330, 180)
    SetChrPos(0x103, 30400, 0, 24330, 135)
    SetChrPos(0x104, 30500, 0, 22130, 45)
    SetChrPos(0x109, 32200, 0, 23020, 270)
    SetChrPos(0x105, 31700, 0, 22130, 315)
    OP_68(30750, 1100, 23130, 0)
    MoveCamera(314, 26, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19050, 0)
    Jump("loc_6D89")

    label("loc_6D06")

    SetChrPos(0x101, 31110, 0, 22130, 0)
    SetChrPos(0x102, 29890, 0, 23410, 90)
    SetChrPos(0x104, 30510, 0, 24350, 135)
    SetChrPos(0x105, 32430, 0, 23120, 270)
    SetChrPos(0x109, 31750, 0, 24340, 180)
    OP_68(31460, 1400, 22950, 0)
    MoveCamera(311, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18180, 0)

    label("loc_6D89")

    Sleep(1)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()

    label("loc_6D99")


    ChrTalk(
        0x105,
        (
            "#12P#10300FI see…\x01",
            "Is this the Belgard gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FYeah, the guard's unit\x01",
            "Protecting the border towards the Empire\x01",
            "It's an important place.\x02\x03",
            "#10104FI taught to Waji before, though,\x01",
            "Sonja Belts command\x01",
            "An impressive person is under command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FI have not met him directly, but …\x01",
            "You are quite cool beauty?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7095")

    ChrTalk(
        0x104,
        (
            "#6P#00306FBeautiful woman is different …\x01",
            "Tightly\x01",
            "He is a kind of otokoe class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FCertainly, the former commander\x01",
            "With a scandal in a cult incident\x01",
            "I became a disciplinary accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FWell, originally\x01",
            "Sonya command is real top\x01",
            "It looked like it was.\x02\x03",
            "#00301FPushing work to subordinates,\x01",
            "I am doing only entertaining\x01",
            "It was a bastard not a bad guy.\x02\x03",
            "#00306FTo the refined training to do rehabilitation training\x01",
            "In addition, it is said that the former is\x01",
            "It's because of the big poka's.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_723A")

    label("loc_7095")


    ChrTalk(
        0x104,
        (
            "#00306FBeautiful woman is different …\x01",
            "Tightly\x01",
            "He is a kind of otokoe class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FCertainly, the former commander\x01",
            "With a scandal in a cult incident\x01",
            "I became a disciplinary accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, originally\x01",
            "Sonya command is real top\x01",
            "It looked like it was.\x02\x03",
            "#00301FPushing work to subordinates,\x01",
            "I am doing only entertaining\x01",
            "It was a bastard not a bad guy.\x02\x03",
            "#00306FTo the refined training to do rehabilitation training\x01",
            "In addition, it is said that the former is\x01",
            "It's because of the big poka's.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_723A")


    ChrTalk(
        0x102,
        (
            "#00108FRiding in the mastermind of the mastermind,\x01",
            "Gnostic to the members\x01",
            "I did administer it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300Fby the way……\x01",
            "The result of rehabilitation training\x01",
            "How was it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_74C6")

    ChrTalk(
        0x104,
        (
            "#6P#00300FOh, it was worth doing\x01",
            "All of us are recovering to their former now.\x02\x03",
            "#00306FAnyway, the commander is terrible\x01",
            "Because it was Sparta.\x01",
            "I became honest hesitant.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00305FOh, that's right.\x01",
            "I remembered with rehabilitation training … …\x02\x03",
            "#00300FThis time Mireille 's guy,\x01",
            "She seems to have decided to promote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FWhen I say Mr. Mireille,\x01",
            "That female officer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FOk, the credit to date\x01",
            "It seems he was admitted.\x02\x03",
            "#00309FBecause it is a corner, please look out later\x01",
            "Can you tease?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7694")

    label("loc_74C6")


    ChrTalk(
        0x104,
        (
            "#00300FOh, it was worth doing\x01",
            "All of us are recovering to their former now.\x02\x03",
            "#00306FAnyway, the commander is terrible\x01",
            "Because it was Sparta.\x01",
            "I became honest hesitant.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00305FOh, that's right.\x01",
            "I remembered with rehabilitation training … …\x02\x03",
            "#00300FThis time Mireille 's guy,\x01",
            "She seems to have decided to promote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWhen I say Mr. Mireille,\x01",
            "That female officer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FOk, the credit to date\x01",
            "It seems he was admitted.\x02\x03",
            "#00309FBecause it is a corner, please look out later\x01",
            "Can you tease?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7694")


    ChrTalk(
        0x101,
        (
            "#00006FNo, I'll celebrate it … …\x02\x03",
            "#00000FOh, and also to Sonya Commander\x01",
            "I have to say good-bye to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FThen, once in the command room on the second floor\x01",
            "Let's go.\x02\x03",
            "I am busy with the relationship of trade council\x01",
            "It may be, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, let's go.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77C7")
    SetChrPos(0x0, 50820, 0, -130, 270)
    Jump("loc_77FC")

    label("loc_77C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77EB")
    SetChrPos(0x0, 37700, 0, 900, 270)
    Jump("loc_77FC")

    label("loc_77EB")

    SetChrPos(0x0, 31110, 0, 22130, 180)

    label("loc_77FC")

    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7824")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_7824")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_44_63FE end

    def Function_45_782C(): pass

    label("Function_45_782C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(46000, -9000, -17800, 0)
    MoveCamera(305, 19, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x0, 55000, -10000, -17800, 270)
    SetChrPos(0x1, 56800, -10000, -17800, 270)
    SetChrPos(0x2, 58600, -10000, -17800, 270)
    SetChrPos(0x3, 60400, -10000, -17800, 270)
    OP_68(42000, 3000, -17800, 7000)
    SetCameraDistance(24000, 7000)

    def lambda_78C9():
        OP_97(0x0, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_78C9)
    Sleep(300)

    def lambda_78E6():
        OP_97(0x1, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_78E6)
    Sleep(300)

    def lambda_7903():
        OP_97(0x2, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_7903)
    Sleep(300)

    def lambda_7920():
        OP_97(0x3, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_7920)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0xFF)
    EndChrThread(0x1, 0xFF)
    EndChrThread(0x2, 0xFF)
    EndChrThread(0x3, 0xFF)
    EventEnd(0x5)
    NewScene("t2030", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_45_782C end

    def Function_46_7969(): pass

    label("Function_46_7969")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(46000, 3000, -17800, 0)
    MoveCamera(305, 19, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x0, 20000, -10000, -17800, 90)
    SetChrPos(0x1, 18200, -10000, -17800, 90)
    SetChrPos(0x2, 16400, -10000, -17800, 90)
    SetChrPos(0x3, 14600, -10000, -17800, 90)
    OP_68(50000, -9000, -17800, 7000)
    SetCameraDistance(24000, 7000)

    def lambda_7A06():
        OP_97(0x0, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7A06)
    Sleep(300)

    def lambda_7A23():
        OP_97(0x1, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_7A23)
    Sleep(300)

    def lambda_7A40():
        OP_97(0x2, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_7A40)
    Sleep(300)

    def lambda_7A5D():
        OP_97(0x3, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_7A5D)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0xFF)
    EndChrThread(0x1, 0xFF)
    EndChrThread(0x2, 0xFF)
    EndChrThread(0x3, 0xFF)
    EventEnd(0x5)
    NewScene("r1080", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_46_7969 end

    def Function_47_7AA6(): pass

    label("Function_47_7AA6")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Erebonia Empire Border\x01",
            "\"Belgard gate\"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_47_7AA6 end

    SaveToFile()

Try(main)
