from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Carter",                 # 1
        "Loggins ",               # 2
        "Romeo ",                 # 3
        "Tourist",                # 4
        "バス",                   # 5
        "Special Support Vehicle",# 6
        "暴走車",                 # 7
        "2nd Lt. Mireille",       # 8
        "Traveler",               # 9
        "Traveler",               # 10
        "Traveler",               # 11
        "Traveler",               # 12
        "Traveler",               # 13
        "Traveler",               # 14
        "State Guard Soldier",    # 15
        "State Guard Soldier",    # 16
        "State Guard Soldier",    # 17
        "State Guard Soldier",    # 18
        "新型装甲車",             # 19
        "West Crossbell HIghway", # 20
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

    PlaceName(73.0, 0.0, -4.0, 0x0000, 0x0000, "West Crossbell HIghway")
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
        "Function_7_103E",         # 07, 7
        "Function_8_116B",         # 08, 8
        "Function_9_11BC",         # 09, 9
        "Function_10_1250",        # 0A, 10
        "Function_11_1362",        # 0B, 11
        "Function_12_2584",        # 0C, 12
        "Function_13_27E7",        # 0D, 13
        "Function_14_36A9",        # 0E, 14
        "Function_15_3853",        # 0F, 15
        "Function_16_395F",        # 10, 16
        "Function_17_3C9C",        # 11, 17
        "Function_18_3CF0",        # 12, 18
        "Function_19_4054",        # 13, 19
        "Function_20_43C0",        # 14, 20
        "Function_21_4413",        # 15, 21
        "Function_22_4466",        # 16, 22
        "Function_23_447D",        # 17, 23
        "Function_24_51EE",        # 18, 24
        "Function_25_52FF",        # 19, 25
        "Function_26_566B",        # 1A, 26
        "Function_27_671E",        # 1B, 27
        "Function_28_683E",        # 1C, 28
        "Function_29_68B9",        # 1D, 29
        "Function_30_6940",        # 1E, 30
        "Function_31_696A",        # 1F, 31
        "Function_32_69C4",        # 20, 32
        "Function_33_6A09",        # 21, 33
        "Function_34_6A25",        # 22, 34
        "Function_35_6A41",        # 23, 35
        "Function_36_6A5D",        # 24, 36
        "Function_37_6A79",        # 25, 37
        "Function_38_6A95",        # 26, 38
        "Function_39_6AD7",        # 27, 39
        "Function_40_6AF6",        # 28, 40
        "Function_41_6B15",        # 29, 41
        "Function_42_6B34",        # 2A, 42
        "Function_43_6B53",        # 2B, 43
        "Function_44_6C6C",        # 2C, 44
        "Function_45_8128",        # 2D, 45
        "Function_46_8265",        # 2E, 46
        "Function_47_83A2",        # 2F, 47
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F16")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x2D, 1)"), scpexpr(EXPR_END)), "loc_E9F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_F11")

    label("loc_E9F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D),
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
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F11")

    Jump("loc_F5F")

    label("loc_F16")

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
            "#1KIt's a bus stop. Ride the bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City West Entrance\x01",        # 0
            "Bus Stop (Near Police Academy)\x01",      # 1
            "Cancel\x01",                              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1016")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1036")

    label("loc_1016")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1036")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()

    label("loc_1036")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_F6B end

    def Function_7_103E(): pass

    label("Function_7_103E")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1167")
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

    def lambda_111E():
        OP_95(0xFE, 27000, 0, 23850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_111E)
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

    label("loc_1167")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_103E end

    def Function_8_116B(): pass

    label("Function_8_116B")

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

    # Function_8_116B end

    def Function_9_11BC(): pass

    label("Function_9_11BC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1217")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_120C")
    Sound(2502, 255, 100, 0)
    Jump("loc_1212")

    label("loc_120C")

    Sound(2503, 255, 100, 0)

    label("loc_1212")

    Jump("loc_123B")

    label("loc_1217")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1235")
    Sound(3347, 255, 100, 0)
    Jump("loc_123B")

    label("loc_1235")

    Sound(3348, 255, 100, 0)

    label("loc_123B")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_11BC end

    def Function_10_1250(): pass

    label("Function_10_1250")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1270")
    Call(0, 23)
    Return()

    label("loc_1270")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1281")
    Jump("loc_135E")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_128F")
    Jump("loc_135E")

    label("loc_128F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1347")

    ChrTalk(
        0xF,
        (
            "#07900FThanks to you, we were able to\x01",
            "stop the recklessly driven car.\x02\x03",
            "#07904FNow I'll be able to concentrate\x01",
            "on guarding the border for a\x01",
            "while. Really, thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_135E")

    label("loc_1347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1355")
    Jump("loc_135E")

    label("loc_1355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_135E")

    label("loc_135E")

    TalkEnd(0xFE)
    Return()

    # Function_10_1250 end

    def Function_11_1362(): pass

    label("Function_11_1362")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_18D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1661")

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Ohh, Randy and friends.\x01",
            "Been a while, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHi, Carter. How's the\x01",
            "situation at Bellguard\x01",
            "Gate?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "...Well, things got like\x01",
            "this, after all. Honestly,\x01",
            "it's a big mess.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Per the commander's instructions,\x01",
            "we're on the look out for an Imperial\x01",
            "army invasion for the time being.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Although they're in the middle of a civil\x01",
            "war so I don't think we have anything to\x01",
            "worry about for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FI see... That's a\x01",
            "relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, things are probably tough for you\x01",
            "guys in a lot of different ways, but...\x01",
            "Do what you can to brace yourself.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Yeah, leave this place to\x01",
            "us. We'll show you the\x01",
            "spirit of the State Guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 1)
    Jump("loc_18CF")

    label("loc_1661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E0")

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "The independence became invalid and also\x01",
            "the Secretary of Defense disappeared...\x01",
            "The State Guard is in too big a mess.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "But you see... thanks to Commander\x01",
            "Sonya, it seems we won't lose sight\x01",
            "of our purpose for the time being.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "As the State Guard that\x01",
            "defends Crossbell, this is\x01",
            "the time to brace ourselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18CF")

    label("loc_17E0")


    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "The independence became invalid and also\x01",
            "the Secretary of Defense disappeared...\x01",
            "The State Guard is in too big a mess.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "As the State Guard that\x01",
            "defends Crossbell, this is\x01",
            "the time to brace ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CF")

    Jump("loc_2580")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D6")

    ChrTalk(
        0x8,
        (
            "After that attack,\x01",
            "tensions with the major\x01",
            "powers have increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "According to rumor,\x01",
            "there'll be large-scale\x01",
            "exercises before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's almost as if we've gone\x01",
            "back to before the Non-\x01",
            "Aggression Pact was signed...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A75")

    label("loc_19D6")


    ChrTalk(
        0x8,
        (
            "After that attack,\x01",
            "tensions with the major\x01",
            "powers have increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's almost as if we've gone\x01",
            "back to before the Non-\x01",
            "Aggression Pact was signed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A75")

    Jump("loc_2580")

    label("loc_1A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1CBA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B85")

    ChrTalk(
        0x8,
        (
            "Even the remaining portion of the\x01",
            "railway repair work was taken\x01",
            "care of last night somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Still, that absurd\x01",
            "monster that we\x01",
            "encountered yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I feared, I guess it\x01",
            "was the cause of the\x01",
            "incident, huh.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C12")

    label("loc_1B85")


    ChrTalk(
        0x8,
        (
            "Honestly speaking, I was\x01",
            "relieved when the\x01",
            "monster ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I feared, I guess that\x01",
            "monster was the cause of\x01",
            "the incident, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C12")

    Jump("loc_1CB5")

    label("loc_1C17")


    ChrTalk(
        0x8,
        (
            "It seems that you caught\x01",
            "the recklessly driven\x01",
            "car some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, thanks to you, the\x01",
            "CGF's concerns have decreased\x01",
            "by one. Really, thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB5")

    Jump("loc_2580")

    label("loc_1CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCD")

    ChrTalk(
        0x8,
        (
            "Recently, a strange\x01",
            "recklessly driven car has\x01",
            "been stopping by frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly... What will\x01",
            "happen if it causes an\x01",
            "accident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To think there's someone who can't\x01",
            "read the atmosphere when the national\x01",
            "border is so tense like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E89")

    label("loc_1DCD")


    ChrTalk(
        0x8,
        (
            "Recently, a strange\x01",
            "recklessly driven car has\x01",
            "been stopping by frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To think there's someone who can't\x01",
            "read the atmosphere when the national\x01",
            "border is so tense like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E89")

    Jump("loc_2580")

    label("loc_1E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB7")

    ChrTalk(
        0x8,
        (
            "Since the independence proposal at\x01",
            "the trade conference, tensions at\x01",
            "the border have been rather high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's obvious this would happen\x01",
            "after the mayor spoke out against\x01",
            "the major powers that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I've got to do my\x01",
            "job without letting my\x01",
            "guard down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2063")

    label("loc_1FB7")


    ChrTalk(
        0x8,
        (
            "Since the independence proposal at\x01",
            "the trade conference, tensions at\x01",
            "the border have been rather high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I've got to do my\x01",
            "job without letting my\x01",
            "guard down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2063")

    Jump("loc_2580")

    label("loc_2068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2164")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2083")
    Call(0, 12)
    Jump("loc_215F")

    label("loc_2083")


    ChrTalk(
        0x8,
        (
            "It seems it was hurriedly decided to\x01",
            "improve the national border security\x01",
            "level for today's conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that Vice Commander Douglas\x01",
            "came from Tangram Gate and he's in a\x01",
            "meeting with the commander now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215F")

    Jump("loc_2580")

    label("loc_2164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_236F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217F")
    Call(0, 12)
    Jump("loc_236A")

    label("loc_217F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22AB")

    ChrTalk(
        0x8,
        (
            "For the duration of the trade\x01",
            "conference, national border\x01",
            "security will be increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that VIPs from all neighboring countries\x01",
            "have gathered in Crossbell... If things don't go\x01",
            "well, it could become an international incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The CGF bears a heavy\x01",
            "responsibility.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_236A")

    label("loc_22AB")


    ChrTalk(
        0x8,
        (
            "Now that VIPs from all neighboring countries\x01",
            "have gathered in Crossbell... If things don't go\x01",
            "well, it could become an international incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The CGF bears a heavy\x01",
            "responsibility.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_236A")

    Jump("loc_2580")

    label("loc_236F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2580")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238A")
    Call(0, 12)
    Jump("loc_2580")

    label("loc_238A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2509")

    ChrTalk(
        0x8,
        (
            "After being dosed with a strange\x01",
            "drug in the cult incident, we\x01",
            "were really in terrible shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For having abused our bodies\x01",
            "to the limit, they were in\x01",
            "tattered and useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And that's why the Commander called\x01",
            "Randy to help us with live combat\x01",
            "rehabilitation training for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to you, we\x01",
            "regained our senses. You\x01",
            "really have my thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2580")

    label("loc_2509")


    ChrTalk(
        0x8,
        (
            "Thank you for the\x01",
            "rehabilitation training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to you, we\x01",
            "regained our senses. You\x01",
            "really have my thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2580")

    TalkEnd(0xFE)
    Return()

    # Function_11_1362 end

    def Function_12_2584(): pass

    label("Function_12_2584")


    ChrTalk(
        0x8,
        (
            "This is the Bellguard border gate.\x01",
            "If you intend to go to the Empire,\x01",
            "go through the checks inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 500)

    ChrTalk(
        0x8,
        (
            "...Wait, Randy and the\x01",
            "others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHeya, guardin' well\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, same as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way, thanks for\x01",
            "the rehabilitation\x01",
            "training you gave us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to you I've gotten\x01",
            "back to my senses. Allow\x01",
            "me to thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHey, don't sweat it. After\x01",
            "all, it was a direct order\x01",
            "from the new commander.\x02\x03",
            "#00309FWell, if you ever wanna\x01",
            "get worked hard again,\x01",
            "call me anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No... Cut me some slack.\x01",
            "I've had enough for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 5)
    OP_93(0x8, 0x5A, 0x0)
    Return()

    # Function_12_2584 end

    def Function_13_27E7(): pass

    label("Function_13_27E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_29A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2907")

    NpcTalk(
        0x9,
        "Soldier Loggins",
        (
            "That huge tree that appeared\x01",
            "in the Marshlands... When it\x01",
            "appeared, my knees gave out.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Loggins",
        (
            "In any case, it's too\x01",
            "much for a private like\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Loggins",
        (
            "Now I have to carry out\x01",
            "my duty as a State Guard\x01",
            "soldier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29A3")

    label("loc_2907")


    NpcTalk(
        0x9,
        "Soldier Loggins",
        (
            "That giant tree... It's\x01",
            "too much for a private\x01",
            "like me.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Loggins",
        (
            "Now I have to carry out\x01",
            "my duty as a State Guard\x01",
            "soldier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A3")

    Jump("loc_36A5")

    label("loc_29A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AC4")

    ChrTalk(
        0x9,
        (
            "In the fight in the Mainz region, 3rd\x01",
            "Company was annihilated... The relief\x01",
            "unit suffered great damage as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even some armored cars were\x01",
            "destroyed... Honestly, the damage\x01",
            "to the CGF is inestimable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Damn jaegers... I'll\x01",
            "never forgive them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B2C")

    label("loc_2AC4")


    ChrTalk(
        0x9,
        (
            "The damage from the\x01",
            "chain of attacks is\x01",
            "inestimable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Damn jaegers... I'll\x01",
            "never forgive them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B2C")

    Jump("loc_36A5")

    label("loc_2B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2CEE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C07")

    ChrTalk(
        0x9,
        (
            "I felt a terrific\x01",
            "strength from yesterday's\x01",
            "giant ogre-like monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems it was\x01",
            "different than the\x01",
            "reported Cryptids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, we can't let our\x01",
            "guard down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C78")

    label("loc_2C07")


    ChrTalk(
        0x9,
        (
            "I felt a terrific\x01",
            "strength from yesterday's\x01",
            "giant ogre-like monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, we can't let our\x01",
            "guard down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C78")

    Jump("loc_2CE9")

    label("loc_2C7D")


    ChrTalk(
        0x9,
        (
            "Honestly... What\x01",
            "nuisances those kids\x01",
            "were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I'll pull myself\x01",
            "together and focus on\x01",
            "guarding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CE9")

    Jump("loc_36A5")

    label("loc_2CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2DEA")

    ChrTalk(
        0x9,
        (
            "If state independence is\x01",
            "realized, we CGF will earn proper\x01",
            "military power as a regular army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even so, the Empire and Republic are threats,\x01",
            "but... I want it to be realized in somehow or\x01",
            "other even just to show Crossbell's pride.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A5")

    label("loc_2DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_300B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F24")

    ChrTalk(
        0x9,
        (
            "As was said at the trade conference,\x01",
            "it's true that the CGF is half-baked\x01",
            "compared to the other nations' armies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, it was none other than\x01",
            "the Empire and Republic that\x01",
            "set up that very structure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I feel irritated that\x01",
            "they used that fact as\x01",
            "ammunition against us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3006")

    label("loc_2F24")


    ChrTalk(
        0x9,
        (
            "We CGF are only allowed the minimum\x01",
            "of armaments out of consideration\x01",
            "towards the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, it was none other than the\x01",
            "Empire and Republic that set up such a\x01",
            "structure... I feel rather irritated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3006")

    Jump("loc_36A5")

    label("loc_300B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31F2")

    ChrTalk(
        0x9,
        (
            "Vice Commander Douglas... He's\x01",
            "one of the strongest in the\x01",
            "CGF in hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I had the chance, I'd\x01",
            "like to spar with him,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FNow that you mention it,\x01",
            "lately I've done nothing but\x01",
            "spar with that Douglas guy.\x02\x03",
            "#00306FMan, he was really tough.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 500)

    ChrTalk(
        0x9,
        "What...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Randy, won't you spar\x01",
            "with me? I want to test\x01",
            "my mettle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, if you've got so much\x01",
            "free time, you should give\x01",
            "your all and stay on guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32A4")

    label("loc_31F2")

    TurnDirection(0x9, 0x104, 0)

    ChrTalk(
        0x9,
        (
            "Mrr... You've got a point.\x01",
            "Focusing on my current duties\x01",
            "is what it's most important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Then spar with me\x01",
            "next time, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah, yeah, if I\x01",
            "remember.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32A4")

    OP_93(0x9, 0x5A, 0x0)
    Jump("loc_36A5")

    label("loc_32B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3353")

    ChrTalk(
        0x9,
        (
            "Our strongest guardsmen\x01",
            "are guarding VIPs at\x01",
            "Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They've got a great record in\x01",
            "combat. The VIPs should be\x01",
            "safe if they're with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A5")

    label("loc_3353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3613")

    ChrTalk(
        0x9,
        (
            "After Commander Sonya was\x01",
            "assigned, I feel that morale at\x01",
            "Bellguard Gate greatly increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As proof, our recovery after\x01",
            "being dosed with that drug in the\x01",
            "cult incident was oddly speedy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, compared to the previous commander,\x01",
            "the difference is like that between\x01",
            "heaven and hell.\x02\x03",
            "#00300FThere aren't that many excellent superior\x01",
            "officers on the same level as that\x01",
            "spartan. We've got to get motivated too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah... I've got to\x01",
            "apply myself even more\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I had my body taken over\x01",
            "by that Joachim Gｸnther\x01",
            "in the cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FYeah, that happened, now\x01",
            "that you mention it.\x02\x03",
            "#00300FWell, let's both do our\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_36A5")

    label("loc_3613")


    ChrTalk(
        0x9,
        (
            "I had my body taken over\x01",
            "by that Joachim Gｸnther\x01",
            "in the cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In that sense, I've got\x01",
            "to apply myself even\x01",
            "more from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A5")

    TalkEnd(0xFE)
    Return()

    # Function_13_27E7 end

    def Function_14_36A9(): pass

    label("Function_14_36A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_36BA")
    Jump("loc_384F")

    label("loc_36BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_384F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D2")

    ChrTalk(
        0xA,
        (
            "After finishing the freight train\x01",
            "inspection, I'm now doing one for\x01",
            "our new armored cars, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, as I thought, their\x01",
            "numbers don't match. It\x01",
            "seems we're short one unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've got the key here,\x01",
            "so where the heck could\x01",
            "it have gone...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_384F")

    label("loc_37D2")


    ChrTalk(
        0xA,
        (
            "Hmm, it's hard to think it\x01",
            "was stolen while we CGF\x01",
            "soldiers were on watch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Where the heck could it\x01",
            "have gone...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384F")

    TalkEnd(0xFE)
    Return()

    # Function_14_36A9 end

    def Function_15_3853(): pass

    label("Function_15_3853")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3864")
    Jump("loc_395B")

    label("loc_3864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3872")
    Jump("loc_395B")

    label("loc_3872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3880")
    Jump("loc_395B")

    label("loc_3880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_388E")
    Jump("loc_395B")

    label("loc_388E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_389C")
    Jump("loc_395B")

    label("loc_389C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_38AA")
    Jump("loc_395B")

    label("loc_38AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_395B")

    ChrTalk(
        0xB,
        (
            "Compared to Garrelia\x01",
            "Fortress, these are extremely\x01",
            "modest border defenses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hohoho, it's because the\x01",
            "Empire and Crossbell are in\x01",
            "completely different leagues.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_395B")

    TalkEnd(0xFE)
    Return()

    # Function_15_3853 end

    def Function_16_395F(): pass

    label("Function_16_395F")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3991")
    SetScenarioFlags(0x31, 2)

    label("loc_3991")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_39D1")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39C6")
    Sound(2499, 255, 100, 0)
    Jump("loc_39CC")

    label("loc_39C6")

    Sound(3537, 255, 100, 0)

    label("loc_39CC")

    Jump("loc_39D7")

    label("loc_39D1")

    Sound(3344, 255, 100, 0)

    label("loc_39D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_3A4C")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A2C"),
        (SWITCH_DEFAULT, "loc_3A3D"),
    )


    label("loc_3A2C")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3A47")

    label("loc_3A3D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A47")

    Jump("loc_3C89")

    label("loc_3A4C")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3A7E")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_3A7E")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3AB2"),
        (1, "loc_3BB6"),
        (2, "loc_3C47"),
        (SWITCH_DEFAULT, "loc_3C7F"),
    )


    label("loc_3AB2")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3AE3")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_3AF3")

    label("loc_3AE3")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_3AF3")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B49")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B49")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B6C")
    Sound(461, 0, 100, 0)

    label("loc_3B6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3B8C")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_3B9C")

    label("loc_3B8C")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_3B9C")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_39D7")

    label("loc_3BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3C28")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_3BEB")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_3C03")

    label("loc_3BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3BFE")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_3C03")

    label("loc_3BFE")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_3C03")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C42")

    label("loc_3C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3C38")
    OP_AF(0xFB)
    Jump("loc_3C42")

    label("loc_3C38")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C42")

    Jump("loc_3C89")

    label("loc_3C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C60")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C7A")

    label("loc_3C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3C70")
    OP_AF(0xFB)
    Jump("loc_3C7A")

    label("loc_3C70")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C7A")

    Jump("loc_3C89")

    label("loc_3C7F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C89")

    Jump("loc_39D7")

    label("loc_3C8E")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_16_395F end

    def Function_17_3C9C(): pass

    label("Function_17_3C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3CEC")
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

    label("loc_3CEC")

    Call(0, 6)
    Return()

    # Function_17_3C9C end

    def Function_18_3CF0(): pass

    label("Function_18_3CF0")

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

    def lambda_3E71():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3E71)

    def lambda_3E86():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3E86)
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

    def lambda_3F79():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F79)
    Sleep(50)

    def lambda_3F91():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3F91)
    Sleep(50)

    def lambda_3FA9():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3FA9)
    Sleep(50)

    def lambda_3FC1():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3FC1)
    Sleep(50)

    def lambda_3FD9():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3FD9)
    OP_93(0x106, 0x5A, 0x1F4)
    Sleep(1500)
    OP_68(34000, -7000, -18000, 6000)
    OP_93(0x106, 0x10E, 0x1F4)

    def lambda_4010():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4010)
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

    # Function_18_3CF0 end

    def Function_19_4054(): pass

    label("Function_19_4054")

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
            "#10401F#12P(Bellguard Gate's\x01",
            "security seems perfect.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P(Yeah, honestly, there's\x01",
            "no openings.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#6P(It seems best to\x01",
            "withdraw for now...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11P(Yeah, let's.)\x02",
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

    # Function_19_4054 end

    def Function_20_43C0(): pass

    label("Function_20_43C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4412")
    OP_95(0xFE, 27780, 0, 4550, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 27780, 0, 18140, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_20_43C0")

    label("loc_4412")

    Return()

    # Function_20_43C0 end

    def Function_21_4413(): pass

    label("Function_21_4413")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4465")
    OP_95(0xFE, 30910, 0, -3330, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 30910, 0, 2200, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_21_4413")

    label("loc_4465")

    Return()

    # Function_21_4413 end

    def Function_22_4466(): pass

    label("Function_22_4466")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    Return()

    # Function_22_4466 end

    def Function_23_447D(): pass

    label("Function_23_447D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5015")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xF,
        (
            "Randy... and the rest of the\x01",
            "Special Support Section.\x02\x03",
            "Good morning, and thank you for\x01",
            "coming.\x02",
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
            "#00000FLt. Mireille, good\x01",
            "morning.\x02\x03",
            "#00004FThat was great work on\x01",
            "the railway repair\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07902FYes, I'm glad we somehow managed it,\x01",
            "but...\x02\x03",
            "#07903FIn the end, we couldn't catch that\x01",
            "giant monster's trail.\x02\x03",
            "#07908FI ordered our patrol units to look\x01",
            "for it today as well, but I honestly\x01",
            "don't know if they'll find it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, you did have to\x01",
            "prioritize those repairs.\x02\x03",
            "#00300FShouldn't you forget the\x01",
            "monster for now and focus\x01",
            "on your current work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07903F...Yes, you're probably\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUmm, we're here today to\x01",
            "ask about your support\x01",
            "request.\x02\x03",
            "I know it's sudden, but\x01",
            "could you tell us the\x01",
            "details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07900FYes, understood.\x02\x03",
            "#07903FThere's a problem on West Crossbell\x01",
            "Highway... A certain recklessly driven car\x01",
            "has been showing up more often lately.\x02\x03",
            "#07900FIt's causing a lot of trouble for buses\x01",
            "and people travelling to and from the\x01",
            "Empire.\x02\x03",
            "I want to ask for your cooperation in\x01",
            "putting a stop to it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0E")
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
            "#1K◆ About [Stopping a\x01",
            "Recklessly Driven Car],\x01",
            "you... (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",         # 0
            "[Did it]\x01",            # 1
            "[Didn't do it]\x01",      # 2
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
        (0, "loc_4AF5"),
        (1, "loc_4AFA"),
        (2, "loc_4B04"),
        (SWITCH_DEFAULT, "loc_4B0E"),
    )


    label("loc_4AF5")

    Jump("loc_4B0E")

    label("loc_4AFA")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_4B0E")

    label("loc_4B04")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_4B0E")

    label("loc_4B0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4BE9")

    ChrTalk(
        0x109,
        (
            "#10103FA recklessly driven\x01",
            "car... I feel like I've\x01",
            "heard that somewhere.\x02\x03",
            "#10101FCould it be... those\x01",
            "young boys we caught\x01",
            "before in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FThe High Bloods? I'd say\x01",
            "that's likely...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C1C")

    label("loc_4BE9")


    ChrTalk(
        0x109,
        (
            "#10103FHmm... That doesn't\x01",
            "sound good at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C1C")


    ChrTalk(
        0xF,
        (
            "#07901FYes, and now that security in\x01",
            "Crossbell is seen as lacking\x01",
            "by the Empire and Republic...\x02\x03",
            "#07903FIf an accident involving\x01",
            "foreigners occurred, there'd\x01",
            "be big trouble.\x02\x03",
            "#07901FThat train derailment\x01",
            "occurred just yesterday as it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FIndeed, Crossbell seems\x01",
            "to be in a precarious\x01",
            "position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07900FAlso, in regard to this case,\x01",
            "we're cooperating with the\x01",
            "police's Patrol Division.\x02\x03",
            "We accepted this case since\x01",
            "the recklessly driven car's\x01",
            "route is often the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FHow are we going to stop\x01",
            "it, specifically?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07903FThey take West Crossbell Highway and\x01",
            "double-back at Bellguard gate... That's\x01",
            "their route.\x02\x03",
            "#07900FYou'll standby at the gate. When appearance\x01",
            "of the recklessly driven car is confirmed,\x01",
            "you'll pursue it in your orbal car.\x02\x03",
            "In the meantime, I'll call the Patrol\x01",
            "Division and have them on standby at\x01",
            "Crossbell City's west entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... A pincer attack\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07900FYes, precisely. ...So,\x01",
            "can I count on you?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8B, 0x1, 0x0)
    Jump("loc_51A5")

    label("loc_5015")


    ChrTalk(
        0xF,
        (
            "#07900FThe recklessly driven car uses West\x01",
            "Crossbell Highway and doubles back at\x01",
            "Bellguard gate... That's its route.\x02\x03",
            "#07903FYou'll standby at the gate. When appearance\x01",
            "of the recklessly driven car is confirmed,\x01",
            "you'll pursue it in your orbal car.\x02\x03",
            "#07900FThe plan is to perform a pincer attack with\x01",
            "the Patrol Division standing by at\x01",
            "Crossbell City's west entrance.\x02\x03",
            "...So, can I count on you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51A5")

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

    # Function_23_447D end

    def Function_24_51EE(): pass

    label("Function_24_51EE")

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
            "[Accept]\x01",      # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5251")
    Call(0, 25)
    Jump("loc_52FE")

    label("loc_5251")


    ChrTalk(
        0x101,
        (
            "#00006F...I'm sorry, Lt.\x01",
            "Mireille. Our hands are\x01",
            "full right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07903FI see... That's too bad.\x02\x03",
            "#07900FThen, tell me if you get\x01",
            "free.\x02\x03",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x178, 1)

    label("loc_52FE")

    Return()

    # Function_24_51EE end

    def Function_25_52FF(): pass

    label("Function_25_52FF")


    ChrTalk(
        0x101,
        (
            "#00000FGot it. Allow us to\x01",
            "accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07902FThanks, this is a big help.\x02\x03",
            "#07903FThen, I'll contact the\x01",
            "Patrol Division immediately\x01",
            "to start the operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, please do.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00300FLet's prepare our orbal\x01",
            "car too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_547D")
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
            "#1KIs the SSS car is parked\x01",
            "at Bellguard Gate?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_547D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5510")
    TurnDirection(0x101, 0x104, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00000FOh, right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FNoｱl, I'll leave the\x01",
            "driving to you.\x02",
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
    Jump("loc_55FA")

    label("loc_5510")

    TurnDirection(0x101, 0x104, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FOh, right. Let's go get\x01",
            "it later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FNoｱl, I'll leave the\x01",
            "driving to you.\x02",
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
            "The car has been moved\x01",
            "to Bellguard Gate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55FA")

    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Reckless Driver\x01",
            "Pursuit]\x07\x00",
            " started!\x02",
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

    # Function_25_52FF end

    def Function_26_566B(): pass

    label("Function_26_566B")

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
            "#00301F...There's no sign of\x01",
            "the car just yet.\x02\x03",
            "#00306FWill it really come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHmm... I wonder.\x02\x03",
            "#00003FShe said its travel\x01",
            "route is West Crossbell\x01",
            "Highway, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat's exactly why Kate and\x01",
            "the others from the Patrol\x01",
            "Division can't catch it.\x02\x03",
            "The police's jurisdiction\x01",
            "is generally inside\x01",
            "Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FAnd for that reason,\x01",
            "this request came to us,\x01",
            "an irregular existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWell, it's probably\x01",
            "something along those\x01",
            "lines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FAnyway, whether it's inside\x01",
            "or outside the city, we can't\x01",
            "allow reckless driving.\x02\x03",
            "We'll catch that car no\x01",
            "matter what!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07902FHaha, I'm counting on\x01",
            "you.\x02",
        )
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E88")
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
            "#1K◆ About [Stopping a\x01",
            "Recklessly Driven Car],\x01",
            "you... (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",         # 0
            "[Did it]\x01",            # 1
            "[Didn't do it]\x01",      # 2
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
        (0, "loc_5E6F"),
        (1, "loc_5E74"),
        (2, "loc_5E7E"),
        (SWITCH_DEFAULT, "loc_5E88"),
    )


    label("loc_5E6F")

    Jump("loc_5E88")

    label("loc_5E74")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_5E88")

    label("loc_5E7E")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_5E88")

    label("loc_5E88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5EC3")

    ChrTalk(
        0x101,
        (
            "#3P#00005FThis sound, could it\x01",
            "be!?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_5EE6")

    label("loc_5EC3")


    ChrTalk(
        0x101,
        "#3P#00005FThis sound is...!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5EE6")

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
        "Passenger",
        "Uwaaah!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Passenger",
        "Eeeeek!!\x02",
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
        "Whoa, watch out!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Reggie",
        "Be careful, damn!\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629C")
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
            "#1K◆ About [Stopping a\x01",
            "Recklessly Driven Car],\x01",
            "you... (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",         # 0
            "[Did it]\x01",            # 1
            "[Didn't do it]\x01",      # 2
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
        (0, "loc_6283"),
        (1, "loc_6288"),
        (2, "loc_6292"),
        (SWITCH_DEFAULT, "loc_629C"),
    )


    label("loc_6283")

    Jump("loc_629C")

    label("loc_6288")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_629C")

    label("loc_6292")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_629C")

    label("loc_629C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_62F0")

    ChrTalk(
        0x101,
        (
            "#00001FT-That's the High\x01",
            "Bloods'...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FI-I knew it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6340")

    label("loc_62F0")


    ChrTalk(
        0x101,
        (
            "#00001FT-That's the recklessly\x01",
            "driven car, huh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FHow dangerous!\x02",
    )

    CloseMessageWindow()

    label("loc_6340")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7507", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xF, 0x104, 500)
    Sleep(100)

    ChrTalk(
        0xF,
        (
            "#07907FGuys, start pursuing it!\x02\x03",
            "I'll call the Patrol\x01",
            "Division!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_63A5():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63A5)
    Sleep(50)

    def lambda_63B5():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63B5)
    Sleep(50)

    def lambda_63C5():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_63C5)
    Sleep(50)

    def lambda_63D5():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_63D5)
    Sleep(50)

    def lambda_63E5():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63E5)
    Sleep(50)

    def lambda_63F5():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_63F5)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00001FUnderstood!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00007FNoｱl, leave navigation\x01",
            "to me and focus on\x01",
            "driving!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x109,
        "#10107FYes, sir!\x02",
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

    def lambda_64B9():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_64B9)
    Sleep(1000)
    WaitChrThread(0x109, 3)
    Sleep(500)

    def lambda_64D0():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_64D0)

    def lambda_64E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_64E5)
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

    def lambda_65AA():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_65AA)

    def lambda_65BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_65BF)
    WaitChrThread(0x104, 3)

    def lambda_65D4():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_65D4)

    def lambda_65E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_65E9)
    WaitChrThread(0x103, 3)

    def lambda_65FE():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_65FE)

    def lambda_6613():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6613)
    WaitChrThread(0x105, 3)

    def lambda_6628():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6628)

    def lambda_663D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_663D)
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

    # Function_26_566B end

    def Function_27_671E(): pass

    label("Function_27_671E")

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

    # Function_27_671E end

    def Function_28_683E(): pass

    label("Function_28_683E")

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

    # Function_28_683E end

    def Function_29_68B9(): pass

    label("Function_29_68B9")

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

    # Function_29_68B9 end

    def Function_30_6940(): pass

    label("Function_30_6940")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, 15520, 0, 21370)
    OP_9F(0x1, 19310, 0, 18600)
    OP_9F(0x2, 0xD, 5000, 0x6)
    Return()

    # Function_30_6940 end

    def Function_31_696A(): pass

    label("Function_31_696A")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, 25620, 0, 9880)
    OP_9F(0x1, 30580, 0, 1500)
    OP_9F(0x1, 37950, 0, 230)
    OP_9F(0x1, 45610, 0, 160)
    OP_9F(0x2, 0xD, 10000, 0x6)
    OP_98(0xD, 0x6D60, 0x0, 0x0, 0x2710, 0x0)
    Return()

    # Function_31_696A end

    def Function_32_69C4(): pass

    label("Function_32_69C4")

    OP_95(0x109, 11600, 0, 19760, 4000, 0x0)
    OP_95(0x109, 8490, 0, 19730, 4000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Sound(462, 0, 100, 0)
    OP_71(0x5, 0xF1, 0x10E, 0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_32_69C4 end

    def Function_33_6A09(): pass

    label("Function_33_6A09")

    OP_95(0x101, 21660, 0, 22150, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_33_6A09 end

    def Function_34_6A25(): pass

    label("Function_34_6A25")

    OP_95(0x102, 20460, 0, 22280, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_34_6A25 end

    def Function_35_6A41(): pass

    label("Function_35_6A41")

    OP_95(0x103, 19000, 0, 23000, 2000, 0x0)
    OP_93(0x103, 0xB4, 0x1F4)
    Return()

    # Function_35_6A41 end

    def Function_36_6A5D(): pass

    label("Function_36_6A5D")

    OP_95(0x104, 20290, 0, 23430, 2000, 0x0)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_36_6A5D end

    def Function_37_6A79(): pass

    label("Function_37_6A79")

    OP_95(0x105, 18030, 0, 23200, 2000, 0x0)
    OP_93(0x105, 0xB4, 0x1F4)
    Return()

    # Function_37_6A79 end

    def Function_38_6A95(): pass

    label("Function_38_6A95")

    OP_95(0x101, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x101, 0xE1, 0x1F4)

    def lambda_6AB5():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AB5)

    def lambda_6ACA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6ACA)
    Return()

    # Function_38_6A95 end

    def Function_39_6AD7(): pass

    label("Function_39_6AD7")

    Sleep(800)
    OP_95(0x102, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x102, 0xE1, 0x1F4)
    Return()

    # Function_39_6AD7 end

    def Function_40_6AF6(): pass

    label("Function_40_6AF6")

    Sleep(1000)
    OP_95(0x103, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_40_6AF6 end

    def Function_41_6B15(): pass

    label("Function_41_6B15")

    Sleep(800)
    OP_95(0x104, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x104, 0xE1, 0x1F4)
    Return()

    # Function_41_6B15 end

    def Function_42_6B34(): pass

    label("Function_42_6B34")

    Sleep(1200)
    OP_95(0x105, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_42_6B34 end

    def Function_43_6B53(): pass

    label("Function_43_6B53")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C6B")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6B96"),
        (1, "loc_6BB0"),
        (2, "loc_6BCA"),
        (3, "loc_6BE4"),
        (4, "loc_6BFE"),
        (5, "loc_6C18"),
        (6, "loc_6C32"),
        (SWITCH_DEFAULT, "loc_6C4C"),
    )


    label("loc_6B96")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6C66")

    label("loc_6BB0")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_6C66")

    label("loc_6BCA")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_6C66")

    label("loc_6BE4")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6C66")

    label("loc_6BFE")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_6C66")

    label("loc_6C18")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_6C66")

    label("loc_6C32")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6C66")

    label("loc_6C4C")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6C66")

    label("loc_6C66")

    Jump("Function_43_6B53")

    label("loc_6C6B")

    Return()

    # Function_43_6B53 end

    def Function_44_6C6C(): pass

    label("Function_44_6C6C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CDE")
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_6CDE")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70DF")
    Sleep(2500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E1D")
    SetChrPos(0x101, 54820, 0, -130, 270)
    SetChrPos(0x102, 56020, 0, -1200, 270)
    SetChrPos(0x103, 56170, 0, 1010, 270)
    SetChrPos(0x104, 57750, 0, -1090, 270)
    SetChrPos(0x109, 57900, 0, 920, 270)
    SetChrPos(0x105, 59100, 0, -120, 270)
    Jump("loc_6E72")

    label("loc_6E1D")

    SetChrPos(0x101, 54820, 0, -130, 270)
    SetChrPos(0x102, 56020, 0, -1200, 270)
    SetChrPos(0x104, 56170, 0, 1010, 270)
    SetChrPos(0x109, 57750, 0, -1090, 270)
    SetChrPos(0x105, 57900, 0, 920, 270)

    label("loc_6E72")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F98")

    def lambda_6E87():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E87)

    def lambda_6EA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6EA1)
    Sleep(100)

    def lambda_6EB5():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6EB5)

    def lambda_6ECF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6ECF)
    Sleep(120)

    def lambda_6EE3():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6EE3)

    def lambda_6EFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6EFD)
    Sleep(90)

    def lambda_6F11():
        OP_95(0xFE, 53750, 0, -1090, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F11)

    def lambda_6F2B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6F2B)
    Sleep(100)

    def lambda_6F3F():
        OP_95(0xFE, 53900, 0, 920, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6F3F)

    def lambda_6F59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6F59)
    Sleep(80)

    def lambda_6F6D():
        OP_95(0xFE, 55100, 0, -120, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F6D)

    def lambda_6F87():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6F87)
    Jump("loc_707B")

    label("loc_6F98")


    def lambda_6F9D():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F9D)

    def lambda_6FB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6FB7)
    Sleep(100)

    def lambda_6FCB():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6FCB)

    def lambda_6FE5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6FE5)
    Sleep(120)

    def lambda_6FF9():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6FF9)

    def lambda_7013():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7013)
    Sleep(90)

    def lambda_7027():
        OP_95(0xFE, 53750, 0, -1090, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7027)

    def lambda_7041():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7041)
    Sleep(100)

    def lambda_7055():
        OP_95(0xFE, 53900, 0, 920, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7055)

    def lambda_706F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_706F)

    label("loc_707B")

    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70A3")
    WaitChrThread(0x103, 1)

    label("loc_70A3")

    Fade(500)
    OP_68(52070, 1000, -280, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19600, 0)
    OP_0D()
    Sleep(1000)
    Jump("loc_7607")

    label("loc_70DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7390")
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

    def lambda_7158():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7158)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72FB")
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
    Jump("loc_737E")

    label("loc_72FB")

    SetChrPos(0x101, 37700, 0, 900, 90)
    SetChrPos(0x102, 39000, 0, -800, 0)
    SetChrPos(0x104, 38400, 0, 2000, 180)
    SetChrPos(0x109, 39900, 0, 1600, 225)
    SetChrPos(0x105, 39900, 0, -200, 315)
    OP_68(39330, 1200, 570, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18180, 0)

    label("loc_737E")

    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_7607")

    label("loc_7390")

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

    def lambda_7409():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7409)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7574")
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
    Jump("loc_75F7")

    label("loc_7574")

    SetChrPos(0x101, 31110, 0, 22130, 0)
    SetChrPos(0x102, 29890, 0, 23410, 90)
    SetChrPos(0x104, 30510, 0, 24350, 135)
    SetChrPos(0x105, 32430, 0, 23120, 270)
    SetChrPos(0x109, 31750, 0, 24340, 180)
    OP_68(31460, 1400, 22950, 0)
    MoveCamera(311, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18180, 0)

    label("loc_75F7")

    Sleep(1)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()

    label("loc_7607")


    ChrTalk(
        0x105,
        (
            "#12P#10300FSo this is Bellguard\x01",
            "gate, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FYeah. It's base of the Guardian\x01",
            "Force unit that protects\x01",
            "Crossbell's border with the Empire.\x02\x03",
            "#10104FI told you about her before, but\x01",
            "this place is under the skilled\x01",
            "command of Commander Sonya Bｴlz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe. I've never met her in\x01",
            "person, but she seems like\x01",
            "quite the cool beauty.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7946")

    ChrTalk(
        0x104,
        (
            "#6P#00306FShe's definitely a babe\x01",
            "but... She's one scary\x01",
            "lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI think the previous commander was\x01",
            "given a dishonorable discharge\x01",
            "after that cult incident scandal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FCommander Sonya was more skilled than\x01",
            "him from the start.\x02\x03",
            "#00301FThat guy was a good-for-nothing who\x01",
            "pushed work onto his subordinates. He\x01",
            "himself only entertained dignitaries.\x02\x03",
            "#00306FIn a way, that rehabilitation\x01",
            "training we had to do was his fault,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B05")

    label("loc_7946")


    ChrTalk(
        0x104,
        (
            "#00306FShe's definitely a babe\x01",
            "but... She's one scary\x01",
            "lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI think the previous commander was\x01",
            "given a dishonorable discharge\x01",
            "after that cult incident scandal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FCommander Sonya was more skilled than\x01",
            "him from the start.\x02\x03",
            "#00301FThat guy was a good-for-nothing who\x01",
            "pushed work onto his subordinates. He\x01",
            "himself only entertained dignitaries.\x02\x03",
            "#00306FIn a way, that rehabilitation\x01",
            "training we had to do was his fault,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B05")


    ChrTalk(
        0x102,
        (
            "#00108FHe was persuaded by the\x01",
            "mastermind... and dosed\x01",
            "the troops with the drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FAbout that... How did\x01",
            "the rehabilitation\x01",
            "training go?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D95")

    ChrTalk(
        0x104,
        (
            "#6P#00300FIt was great. All troops\x01",
            "are back to normal.\x02\x03",
            "#00306FBut that commander is a\x01",
            "slave driver. I'm\x01",
            "completely exhausted.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00305FOh, right. I thought about\x01",
            "it during rehabilitation\x01",
            "training, but...\x02\x03",
            "#00300FMirelle should have gotten\x01",
            "her promotion by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FMireille... That female\x01",
            "officer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FYeah. Looks like they\x01",
            "finally recognized her\x01",
            "achievements.\x02\x03",
            "#00309FSince we're here, I was\x01",
            "thinking of teasing her\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F7C")

    label("loc_7D95")


    ChrTalk(
        0x104,
        (
            "#00300FIt was great. All troops\x01",
            "are back to normal.\x02\x03",
            "#00306FBut that commander is a\x01",
            "slave driver. I'm\x01",
            "completely exhausted.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00305FOh, right. I thought about\x01",
            "it during rehabilitation\x01",
            "training, but...\x02\x03",
            "#00300FMirelle should have gotten\x01",
            "her promotion by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FMirelle is that officer\x01",
            "lady we met before\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah. Looks like they\x01",
            "finally recognized her\x01",
            "achievements.\x02\x03",
            "#00309FSince we're here, I was\x01",
            "thinking of teasing her\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F7C")


    ChrTalk(
        0x101,
        (
            "#00006FYou should congratulate\x01",
            "her instead.\x02\x03",
            "#00000FBut anyway, we should\x01",
            "also check in with\x01",
            "Commander Sonya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FIn that case, let's head\x01",
            "to the commander's room\x01",
            "on 2F.\x02\x03",
            "She may be busy with\x01",
            "trade conference\x01",
            "preparations, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAlright, let's head\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80C3")
    SetChrPos(0x0, 50820, 0, -130, 270)
    Jump("loc_80F8")

    label("loc_80C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80E7")
    SetChrPos(0x0, 37700, 0, 900, 270)
    Jump("loc_80F8")

    label("loc_80E7")

    SetChrPos(0x0, 31110, 0, 22130, 180)

    label("loc_80F8")

    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8120")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_8120")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_44_6C6C end

    def Function_45_8128(): pass

    label("Function_45_8128")

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

    def lambda_81C5():
        OP_97(0x0, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_81C5)
    Sleep(300)

    def lambda_81E2():
        OP_97(0x1, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_81E2)
    Sleep(300)

    def lambda_81FF():
        OP_97(0x2, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_81FF)
    Sleep(300)

    def lambda_821C():
        OP_97(0x3, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_821C)
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

    # Function_45_8128 end

    def Function_46_8265(): pass

    label("Function_46_8265")

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

    def lambda_8302():
        OP_97(0x0, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8302)
    Sleep(300)

    def lambda_831F():
        OP_97(0x1, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_831F)
    Sleep(300)

    def lambda_833C():
        OP_97(0x2, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_833C)
    Sleep(300)

    def lambda_8359():
        OP_97(0x3, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_8359)
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

    # Function_46_8265 end

    def Function_47_83A2(): pass

    label("Function_47_83A2")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Erebonian Empire Region National Border\x01",
            "    Bellguard Gate\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_47_83A2 end

    SaveToFile()

Try(main)
