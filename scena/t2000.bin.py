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
        "Function_6_F6C",          # 06, 6
        "Function_7_103E",         # 07, 7
        "Function_8_116B",         # 08, 8
        "Function_9_11BC",         # 09, 9
        "Function_10_1250",        # 0A, 10
        "Function_11_1358",        # 0B, 11
        "Function_12_25D4",        # 0C, 12
        "Function_13_2844",        # 0D, 13
        "Function_14_37B2",        # 0E, 14
        "Function_15_3967",        # 0F, 15
        "Function_16_3A74",        # 10, 16
        "Function_17_3DAD",        # 11, 17
        "Function_18_3E01",        # 12, 18
        "Function_19_4165",        # 13, 19
        "Function_20_44ED",        # 14, 20
        "Function_21_4540",        # 15, 21
        "Function_22_4593",        # 16, 22
        "Function_23_45AA",        # 17, 23
        "Function_24_53DC",        # 18, 24
        "Function_25_54F4",        # 19, 25
        "Function_26_5893",        # 1A, 26
        "Function_27_6986",        # 1B, 27
        "Function_28_6AA6",        # 1C, 28
        "Function_29_6B21",        # 1D, 29
        "Function_30_6BA8",        # 1E, 30
        "Function_31_6BD2",        # 1F, 31
        "Function_32_6C2C",        # 20, 32
        "Function_33_6C71",        # 21, 33
        "Function_34_6C8D",        # 22, 34
        "Function_35_6CA9",        # 23, 35
        "Function_36_6CC5",        # 24, 36
        "Function_37_6CE1",        # 25, 37
        "Function_38_6CFD",        # 26, 38
        "Function_39_6D3F",        # 27, 39
        "Function_40_6D5E",        # 28, 40
        "Function_41_6D7D",        # 29, 41
        "Function_42_6D9C",        # 2A, 42
        "Function_43_6DBB",        # 2B, 43
        "Function_44_6ED4",        # 2C, 44
        "Function_45_84B8",        # 2D, 45
        "Function_46_85F5",        # 2E, 46
        "Function_47_8732",        # 2F, 47
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F11")

    Jump("loc_F60")

    label("loc_F16")

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

    label("loc_F60")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E1A end

    def Function_6_F6C(): pass

    label("Function_6_F6C")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

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
            "Crossbell City West Exit\x01",              # 0
            "Bus Stop (Nearby Police Academy)\x01",      # 1
            "Quit\x01",                                  # 2
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

    # Function_6_F6C end

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
    Jump("loc_1354")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_128F")
    Jump("loc_1354")

    label("loc_128F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_133D")

    ChrTalk(
        0xF,
        (
            "#07900FThanks to you, we were able\x01",
            "to stop the runaway car.\x02\x03",
            "#07904FNow I'll be able to concentrate\x01",
            "on guarding the border for a while.\x01",
            "Really, thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1354")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_134B")
    Jump("loc_1354")

    label("loc_134B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1354")

    label("loc_1354")

    TalkEnd(0xFE)
    Return()

    # Function_10_1250 end

    def Function_11_1358(): pass

    label("Function_11_1358")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_18C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162E")

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Ooh, Randy and guys.\x01",
            "Been a while, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHi, Carter.\x01",
            "How's the Bellguard Gate situation?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "...Well, things have\x01",
            "become like this, so...\x01",
            "Frankly, it's a big mess.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "As per the Commander's instructions,\x01",
            "for the time being we're on the look\x01",
            "out for an Imperial Army invasion.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Although there they're right in the middle of a civil\x01",
            "war so I don't think we'll have to worry for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FI see...\x01",
            "I'm a little relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, I guess you've got many troubles, but...\x01",
            "Brace yourselves in some way.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "Yeah, leave this place to us.\x01",
            "We'll show you the spirit\x01",
            "of the State Guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 1)
    Jump("loc_18BF")

    label("loc_162E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BE")

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "The independence became invalid and  furthermore\x01",
            "the State Guard Commander in Chief disappeared...\x01",
            "The State Guard too is in a big mess.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "But you see...thanks to Commander Sonya, it seems\x01",
            "we won't lose sight of our purpose for the time being.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "As the State Guard that defends Crossbell,\x01",
            "this is the time to brace ourselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18BF")

    label("loc_17BE")


    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "The independence became invalid and  furthermore\x01",
            "the State Guard Commander in Chief disappeared...\x01",
            "The State Guard too is in a big mess.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Carter",
        (
            "As the State Guard that defends Crossbell,\x01",
            "this is the time to brace ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BF")

    Jump("loc_25D0")

    label("loc_18C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1AAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F4")

    ChrTalk(
        0x8,
        (
            "After the raid incident, the tension with\x01",
            "the two major powers has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "According to a rumor, it seems that before long\x01",
            "there're going to be large-scale maneuvers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems just like if we had gone back to before\x01",
            "the "Non-Aggression Pact" was concluded...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AA8")

    label("loc_19F4")


    ChrTalk(
        0x8,
        (
            "After the raid incident, the tension with\x01",
            "the two major powers has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems just like if we had gone back to before\x01",
            "the "Non-Aggression Pact" was concluded...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA8")

    Jump("loc_25D0")

    label("loc_1AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1CF9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC1")

    ChrTalk(
        0x8,
        (
            "Even the part of the railway repair\x01",
            "works that remained was somehow\x01",
            "taken care of during the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Still, that absurd monster that\x01",
            "we encountered yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I feared, I guess that was\x01",
            "the cause of the incident, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C56")

    label("loc_1BC1")


    ChrTalk(
        0x8,
        (
            "Frankly speaking, I was\x01",
            "relieved back then when\x01",
            "the monster ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I feared, I guess that monster\x01",
            "was the cause of the incident, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C56")

    Jump("loc_1CF4")

    label("loc_1C5B")


    ChrTalk(
        0x8,
        (
            "It seems that you caught that\x01",
            "reckless car from some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha, thanks to you, the CGF\x01",
            "big concerns decreased by one.\x01",
            "Really, thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF4")

    Jump("loc_25D0")

    label("loc_1CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1EC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E08")

    ChrTalk(
        0x8,
        (
            "Recently, a strangely reckless car\x01",
            "comes around here frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly...\x01",
            "What will happen if it cause an accident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To think there's someone who can't read the atmosphere\x01",
            "when the national border is in such a tense situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EC1")

    label("loc_1E08")


    ChrTalk(
        0x8,
        (
            "Recently, a strangely reckless car\x01",
            "comes around here frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To think there's someone who can't read the atmosphere\x01",
            "when the national border is in such a tense situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC1")

    Jump("loc_25D0")

    label("loc_1EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDD")

    ChrTalk(
        0x8,
        (
            "Since the independence proposal at the Trade Conference, \x01",
            "the national border has been in quite a state of tension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After the Mayor spoke\x01",
            "out that much, it's the\x01",
            "only obvious result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I must do my job without\x01",
            "letting my guard down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2091")

    label("loc_1FDD")


    ChrTalk(
        0x8,
        (
            "Since the independence proposal at the Trade Conference, \x01",
            "the national border has been in quite a state of tension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I must do my job without\x01",
            "letting my guard down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2091")

    Jump("loc_25D0")

    label("loc_2096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_219F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B1")
    Call(0, 12)
    Jump("loc_219A")

    label("loc_20B1")


    ChrTalk(
        0x8,
        (
            "It seems that all in a hurry it was decided\x01",
            "to improve the national border guarding\x01",
            "level during today's conference.\x02",
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

    label("loc_219A")

    Jump("loc_25D0")

    label("loc_219F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_23A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BA")
    Call(0, 12)
    Jump("loc_239F")

    label("loc_21BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E6")

    ChrTalk(
        0x8,
        (
            "For the duration of the Trade Conference\x01",
            "the national border guarding will be stricter too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that VIPs from all neighboring countries\x01",
            "have gathered in Crossbell...\x01",
            "If things don't go well, it could\x01",
            "become an international problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The CGF responsibility is grave.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_239F")

    label("loc_22E6")


    ChrTalk(
        0x8,
        (
            "Now that VIPs from all neighboring countries\x01",
            "have gathered in Crossbell...\x01",
            "If things don't go well, it could\x01",
            "become an international problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The CGF responsibility is grave.\x02",
    )

    CloseMessageWindow()

    label("loc_239F")

    Jump("loc_25D0")

    label("loc_23A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_25D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23BF")
    Call(0, 12)
    Jump("loc_25D0")

    label("loc_23BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2559")

    ChrTalk(
        0x8,
        (
            "After having been served a strange drug during the\x01",
            "Cult incident, we were really in a terrible condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For having abused our bodies to the limit,\x01",
            "they were in pieces and in a very useless state.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And that's why the Commander called\x01",
            "Randy to do live combat training \x01",
            "rehabilitation practice for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to you, we regained our senses.\x01",
            "You really have my thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25D0")

    label("loc_2559")


    ChrTalk(
        0x8,
        "Thank you for the rehabilitation practice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to you, we regained our senses.\x01",
            "You really have my thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D0")

    TalkEnd(0xFE)
    Return()

    # Function_11_1358 end

    def Function_12_25D4(): pass

    label("Function_12_25D4")


    ChrTalk(
        0x8,
        (
            "This is the border gate called Bellguard Gate.\x01",
            "If you intend to go to the Empire,\x01",
            "undergo the checks inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 500)

    ChrTalk(
        0x8,
        "...Wait, Randy and the others?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHeya, guardin' well today too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ha ha, same as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way, thanks for all you did\x01",
            "for the rehabilitation training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to you I've gone back to my senses.\x01",
            "Let me thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FEh! Don't sweat it.\x01",
            "After all, it was a direct order\x01",
            "from the new Commander.\x02\x03",
            "#00309FWell, if you wanna get worked\x01",
            "hard again, call me whenever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No...cut me some slack.\x01",
            "I've got enough for the present.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 5)
    OP_93(0x8, 0x5A, 0x0)
    Return()

    # Function_12_25D4 end

    def Function_13_2844(): pass

    label("Function_13_2844")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2970")

    NpcTalk(
        0x9,
        "Soldier Loggins",
        (
            "That giant tree that appeared\x01",
            "in the Marshlands...\x01",
            "When it appeared, my knees gave out.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Loggins",
        (
            "In any case, it seems that's too\x01",
            "much for a private like me.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Loggins",
        (
            "Now I have to carry out my\x01",
            "duty as a State Guard soldier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A15")

    label("loc_2970")


    NpcTalk(
        0x9,
        "Soldier Loggins",
        (
            "That giant tree...\x01",
            "It seems it's too much\x01",
            "for a private like me.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Loggins",
        (
            "Now I have to carry out my\x01",
            "duty as a State Guard soldier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A15")

    Jump("loc_37AE")

    label("loc_2A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B33")

    ChrTalk(
        0x9,
        (
            "In the fight in the Mainz region,\x01",
            "the 3rd Company was annihilated...\x01",
            "The rescue unit too suffered great damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even some armored vehicles were destroyed...\x01",
            "Honestly, the CFG damage\x01",
            "is inestimable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Damn jaegers...\x01",
            "I'll never forgive them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BA1")

    label("loc_2B33")


    ChrTalk(
        0x9,
        (
            "The damage in the \x01",
            "chain of raid incidents\x01",
            "is inestimable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Damn jaegers...\x01",
            "I'll never forgive them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA1")

    Jump("loc_37AE")

    label("loc_2BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D6D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7E")

    ChrTalk(
        0x9,
        (
            "I felt a terrific strength from \x01",
            "yesterday's giant ogre-like monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems it was different than\x01",
            "the reported "Cryptids"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hm, we can't let our guard down.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CEF")

    label("loc_2C7E")


    ChrTalk(
        0x9,
        (
            "I felt a terrific strength from \x01",
            "yesterday's giant ogre-like monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hm, we can't let our guard down.\x02",
    )

    CloseMessageWindow()

    label("loc_2CEF")

    Jump("loc_2D68")

    label("loc_2CF4")


    ChrTalk(
        0x9,
        (
            "Honestly...\x01",
            "What nuisances they caused, those kids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I'll pull myself together\x01",
            "and focus on guarding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D68")

    Jump("loc_37AE")

    label("loc_2D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2E77")

    ChrTalk(
        0x9,
        (
            "If the state independence becomes real,\x01",
            "we CGF will earn a proper military power\x01",
            "as a regular army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even so, the Empire and Republic are a threat, but...\x01",
            "I want it to get realized in some way or another\x01",
            "even in order to show Crossbell pride.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AE")

    label("loc_2E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC8")

    ChrTalk(
        0x9,
        (
            "Like it was said in the Trade Conference,\x01",
            "it's true that the CGF, compared to the other\x01",
            "nations armies, is a half-assed existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, it was none other than the Empire\x01",
            "and Republic that formed such a structure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To be provided that as ammunition\x01",
            "for attack, I feel quite a lot irritated.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30AC")

    label("loc_2FC8")


    ChrTalk(
        0x9,
        (
            "We CGF are only allowed the\x01",
            "minimum of armaments for consideration\x01",
            "towards the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, it was none other than the Empire\x01",
            "and Republic that formed such a structure...\x01",
            "I feel quite a lot irritated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AC")

    Jump("loc_37AE")

    label("loc_30B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3359")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A2")

    ChrTalk(
        0x9,
        (
            "Vice Commander Douglas...\x01",
            "He's one of the strongest in the\x01",
            "CGF in hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I had the chance,\x01",
            "I'd like to spar with him, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FNow that you mention it,\x01",
            "lately I did nothing but sparrin'\x01",
            "with that Douglas guy.\x02\x03",
            "#00306FMan, he was really tough.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 500)

    ChrTalk(
        0x9,
        "What...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "..Randy, wouldn't\x01",
            "you spar with me?\x01",
            "I absolutely want to test my mettle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, if you've got such free time,\x01",
            "you should give your all and be on watch.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_334D")

    label("loc_32A2")

    TurnDirection(0x9, 0x104, 0)

    ChrTalk(
        0x9,
        (
            "Mr... You've got a point, focusing on my\x01",
            "current duty is what it's most important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...Then next time, spar with me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304FYeah yeah, if I remember.\x02",
    )

    CloseMessageWindow()

    label("loc_334D")

    OP_93(0x9, 0x5A, 0x0)
    Jump("loc_37AE")

    label("loc_3359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_343C")

    ChrTalk(
        0x9,
        (
            "Who are guarding the VIPs in the\x01",
            "Michelam area are excellent men\x01",
            "for fighting abilities among the unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With them, who kept leaving high\x01",
            "records in combat training too,\x01",
            "the VIPs' safety should be solid.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AE")

    label("loc_343C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_37AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3716")

    ChrTalk(
        0x9,
        (
            "I think that after Commander Sonya\x01",
            "was assigned, it's like Bellguard\x01",
            "Gate morale has quite increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As proof, the recovery after having\x01",
            "been served that drug during the\x01",
            "Cult incident was at an odd speed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, compared to the previous Commander,\x01",
            "the difference is like between heaven and hell.\x02\x03",
            "#00300FThere aren't that many excellent superior officers\x01",
            "who can keep up with that spartan.\x01",
            "You must bring out your motivation too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah... I must apply myself\x01",
            "all the more from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I had my body taken over\x01",
            "by that Joachim Gｸnther\x01",
            "in that Cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FYeah, now that you say it,\x01",
            "such a thing happened too.\x02\x03",
            "#00300FWell, let's both do our best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hm.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_37AE")

    label("loc_3716")


    ChrTalk(
        0x9,
        (
            "I had my body taken over\x01",
            "by that Joachim Gｸnther\x01",
            "in that Cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even in such a sense,\x01",
            "I must apply myself\x01",
            "all the more from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AE")

    TalkEnd(0xFE)
    Return()

    # Function_13_2844 end

    def Function_14_37B2(): pass

    label("Function_14_37B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_37C3")
    Jump("loc_3963")

    label("loc_37C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E5")

    ChrTalk(
        0xA,
        (
            "After the freight train inspection was over, now I'm \x01",
            "doing one for the new type or armored vehicles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Uhm, as I thought, their numbers don't match.\x01",
            "It seems we're short of one unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've got the key, so where\x01",
            "the heck could it have gone...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3963")

    label("loc_38E5")


    ChrTalk(
        0xA,
        (
            "Uhhm, it's hard to think it was stolen\x01",
            "while the CGF soldiers are on watch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Where the heck could it have gone...?\x02",
    )

    CloseMessageWindow()

    label("loc_3963")

    TalkEnd(0xFE)
    Return()

    # Function_14_37B2 end

    def Function_15_3967(): pass

    label("Function_15_3967")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3978")
    Jump("loc_3A70")

    label("loc_3978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3986")
    Jump("loc_3A70")

    label("loc_3986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3994")
    Jump("loc_3A70")

    label("loc_3994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_39A2")
    Jump("loc_3A70")

    label("loc_39A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_39B0")
    Jump("loc_3A70")

    label("loc_39B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39BE")
    Jump("loc_3A70")

    label("loc_39BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A70")

    ChrTalk(
        0xB,
        (
            "Compared to Garrelia Fortress, these are\x01",
            "extremely modest national border defenses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ho ho ho, it's because the Empire\x01",
            "and Crossbell are on a different league.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A70")

    TalkEnd(0xFE)
    Return()

    # Function_15_3967 end

    def Function_16_3A74(): pass

    label("Function_16_3A74")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AA6")
    SetScenarioFlags(0x31, 2)

    label("loc_3AA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_3AE6")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3ADB")
    Sound(2499, 255, 100, 0)
    Jump("loc_3AE1")

    label("loc_3ADB")

    Sound(3537, 255, 100, 0)

    label("loc_3AE1")

    Jump("loc_3AEC")

    label("loc_3AE6")

    Sound(3344, 255, 100, 0)

    label("loc_3AEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_3B5F")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B3F"),
        (SWITCH_DEFAULT, "loc_3B50"),
    )


    label("loc_3B3F")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3B5A")

    label("loc_3B50")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B5A")

    Jump("loc_3D9A")

    label("loc_3B5F")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3B91")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_3B91")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3BC3"),
        (1, "loc_3CC7"),
        (2, "loc_3D58"),
        (SWITCH_DEFAULT, "loc_3D90"),
    )


    label("loc_3BC3")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3BF4")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_3C04")

    label("loc_3BF4")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_3C04")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C5A")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C7D")
    Sound(461, 0, 100, 0)

    label("loc_3C7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3C9D")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_3CAD")

    label("loc_3C9D")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_3CAD")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_3AEC")

    label("loc_3CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3D39")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_3CFC")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_3D14")

    label("loc_3CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3D0F")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_3D14")

    label("loc_3D0F")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_3D14")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D53")

    label("loc_3D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3D49")
    OP_AF(0xFB)
    Jump("loc_3D53")

    label("loc_3D49")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D53")

    Jump("loc_3D9A")

    label("loc_3D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D71")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D8B")

    label("loc_3D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3D81")
    OP_AF(0xFB)
    Jump("loc_3D8B")

    label("loc_3D81")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D8B")

    Jump("loc_3D9A")

    label("loc_3D90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D9A")

    Jump("loc_3AEC")

    label("loc_3D9F")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_16_3A74 end

    def Function_17_3DAD(): pass

    label("Function_17_3DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3DFD")
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

    label("loc_3DFD")

    Call(0, 6)
    Return()

    # Function_17_3DAD end

    def Function_18_3E01(): pass

    label("Function_18_3E01")

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

    def lambda_3F82():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3F82)

    def lambda_3F97():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3F97)
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

    def lambda_408A():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_408A)
    Sleep(50)

    def lambda_40A2():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_40A2)
    Sleep(50)

    def lambda_40BA():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_40BA)
    Sleep(50)

    def lambda_40D2():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_40D2)
    Sleep(50)

    def lambda_40EA():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_40EA)
    OP_93(0x106, 0x5A, 0x1F4)
    Sleep(1500)
    OP_68(34000, -7000, -18000, 6000)
    OP_93(0x106, 0x10E, 0x1F4)

    def lambda_4121():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4121)
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

    # Function_18_3E01 end

    def Function_19_4165(): pass

    label("Function_19_4165")

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
            "#10401F#12P(Bellguard Gate defense\x01",
            "system seems perfect.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12P(Yeah, honestly, there's no openings.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#6P(It seems it would be better\x01",
            "to withdraw from here for now...)\x02",
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

    # Function_19_4165 end

    def Function_20_44ED(): pass

    label("Function_20_44ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_453F")
    OP_95(0xFE, 27780, 0, 4550, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 27780, 0, 18140, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_20_44ED")

    label("loc_453F")

    Return()

    # Function_20_44ED end

    def Function_21_4540(): pass

    label("Function_21_4540")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4592")
    OP_95(0xFE, 30910, 0, -3330, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 30910, 0, 2200, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_21_4540")

    label("loc_4592")

    Return()

    # Function_21_4540 end

    def Function_22_4593(): pass

    label("Function_22_4593")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    Return()

    # Function_22_4593 end

    def Function_23_45AA(): pass

    label("Function_23_45AA")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51DF")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xF,
        (
            "Randy...and everyone from\x01",
            "the Special Support Section.\x02\x03",
            "Good morning, and\x01",
            "thank you for coming.\x02",
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
            "#00000FGood morning, 2nd Lt. Mireille.\x02\x03",
            "#00004FThank you very much for all the hard work you\x01",
            "did for yesterday's railway reparation works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07902FYes, I'm glad that we\x01",
            "managed somehow, but...\x02\x03",
            "#07903FIn the end, we couldn't catch\x01",
            "that giant monster trail.\x02\x03",
            "#07908FToday too I have ordered a search for it\x01",
            "to the units patrolling the autonomous state,\x01",
            "but frankly I wonder if there'll be good results...\x02",
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
            "#00303F...Well, what should've gotten the most priority\x01",
            "was the railway restoration, right?\x02\x03",
            "#00300FWouldn't it be alright to forget\x01",
            "the monster for now and focus\x01",
            "on your current job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#07903F...Yes, that's true too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FEehm, we saw a request\x01",
            "today and came to enquire.\x02\x03",
            "I know it's sudden, but could you\x01",
            "tell us the request content?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07900FYes, understood.\x02\x03",
            "#07903FLately, reckless driving is happening on\x01",
            "the West Crossbell Highway... A so-to-\x01",
            "speak runaway car is appearing frequently.\x02\x03",
            "#07900FIt's causing great troubles for the\x01",
            "Empire travellers and the regular buses.\x02\x03",
            "I want to ask you\x01",
            "to cooperate in\x01",
            "its crackdown.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA2")
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
            "#1K◆ About the [Runaway Vehicle Crackdown], you... (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",         # 0
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
        (0, "loc_4C89"),
        (1, "loc_4C8E"),
        (2, "loc_4C98"),
        (SWITCH_DEFAULT, "loc_4CA2"),
    )


    label("loc_4C89")

    Jump("loc_4CA2")

    label("loc_4C8E")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_4CA2")

    label("loc_4C98")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_4CA2")

    label("loc_4CA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4D7E")

    ChrTalk(
        0x109,
        (
            "#10103FA runaway car...\x01",
            "It seems a story I've heard somewhere.\x02\x03",
            "#10101FCould it be...\x01",
            "That team of young boys we\x01",
            "caught before in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FThe "High Bloods"?\x01",
            "It could be very likely...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DB2")

    label("loc_4D7E")


    ChrTalk(
        0x109,
        (
            "#10103FUhhm... That doesn't\x01",
            "sound good at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DB2")


    ChrTalk(
        0xF,
        (
            "#07901FYes, it's been seen as a problem of declined \x01",
            "public order from the Empire and Republic...\x02\x03",
            "#07903FIf an accident were to happen and foreigners\x01",
            "got involved, it would turn into a big trouble.\x02\x03",
            "#07901FIn addition, the train derailment\x01",
            "accident just happened yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FIndeed, Crossbell position\x01",
            "seems to be very critical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07900FAlso, in regard to this case, we're\x01",
            "proceeding cooperating with the police\x01",
            "District Crime Prevention Section.\x02\x03",
            "We accepted this case since\x01",
            "the runaway car route is\x01",
            "often the highway.\x02",
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
            "#00205FHow should we crack\x01",
            "it down concretely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07903FIt goes through the West Crossbell Highway\x01",
            "and turns back at Bellguard Gate...\x01",
            "It's using this route.\x02\x03",
            "#07900FYou'll stakeout at the gate and, after\x01",
            "confirming the runaway car appearance,\x01",
            "you'll pursue it with your orbal car.\x02\x03",
            "In the meantime, I'll call the District\x01",
            "Crime Prevention Section and have\x01",
            "them on standby at the west exit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FI see...a pincer attack then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07900FYes, precisely.\x01",
            "...So, can I count on you?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8B, 0x1, 0x0)
    Jump("loc_5393")

    label("loc_51DF")


    ChrTalk(
        0xF,
        (
            "#07900FThe runaway car goes through the West Crossbell \x01",
            "Highway and turns back at Bellguard Gate...\x01",
            "It's using this route.\x02\x03",
            "#07903FYou'll stakeout at the gate and, after\x01",
            "confirming the runaway car appearance,\x01",
            "you'll pursue it with your orbal car.\x02\x03",
            "#07900FLike that, you'll trap the runaway car\x01",
            "together with the District Crime\x01",
            "Prevention Section on standby at\x01",
            "Crossbell City west exit. That's the plan.\x02\x03",
            "...So, can I count on you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5393")

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

    # Function_23_45AA end

    def Function_24_53DC(): pass

    label("Function_24_53DC")

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
            "[Quit]\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_543D")
    Call(0, 25)
    Jump("loc_54F3")

    label("loc_543D")


    ChrTalk(
        0x101,
        (
            "#00006F...I'm sorry, 2nd Lt. Mireille.\x01",
            "We're busy at present...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07903FI see...\x01",
            "That's too bad.\x02\x03",
            "#07900FThen, speak to me if \x01",
            "you free yourselves.\x02\x03",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x178, 1)

    label("loc_54F3")

    Return()

    # Function_24_53DC end

    def Function_25_54F4(): pass

    label("Function_25_54F4")


    ChrTalk(
        0x101,
        (
            "#00000FGot it.\x01",
            "Allow us to accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#07902FThank you, you really help me.\x02\x03",
            "#07903FThen, I'll contact the District\x01",
            "Crime Prevention Section\x01",
            "immediately to start the operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, please.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00300FWe'll go to prepare\x01",
            "the orbal car too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568A")
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
            "#1KIs the SSS car is parked at Bellguard Gate?\x07\x00\x02",
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

    label("loc_568A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5718")
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
        "#10102FRoger!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jump("loc_5822")

    label("loc_5718")

    TurnDirection(0x101, 0x104, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FOh, right.\x01",
            "Let's go get it later.\x02",
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
        "#10102FRoger!\x02",
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
            "The car that was parked in another location \x01",
            "has been moved to Bellguard Gate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5822")

    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Runaway Vehicle Pursuit]\x07\x00",
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

    # Function_25_54F4 end

    def Function_26_5893(): pass

    label("Function_26_5893")

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
            "#00301F...No sign of the runaway\x01",
            "vehicle to be appearin' yet.\x02\x03",
            "#00306FWill it really come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI...wonder.\x02\x03",
            "#00003FIt was said it's travelling\x01",
            "route was the West Crossbell\x01",
            "Highway, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat's exactly why miss Kate and the others from the\x01",
            "District Crime Prevention Section can't catch it.\x02\x03",
            "The police's jurisdiction is\x01",
            "generally inside Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FAnd in that sense, such a\x01",
            "request was turned to us\x01",
            "who're an irregular existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FWell, it is right that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FAt any rate, whether it's\x01",
            "inside or outside the city, we\x01",
            "can't allow reckless driving.\x02\x03",
            "We'll catch that car no matter what!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#07902FUh uh, I'm counting on you.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D4")
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
            "#1K◆ About the [Runaway Vehicle Crackdown], you... (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",         # 0
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
        (0, "loc_60BB"),
        (1, "loc_60C0"),
        (2, "loc_60CA"),
        (SWITCH_DEFAULT, "loc_60D4"),
    )


    label("loc_60BB")

    Jump("loc_60D4")

    label("loc_60C0")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_60D4")

    label("loc_60CA")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_60D4")

    label("loc_60D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6111")

    ChrTalk(
        0x101,
        "#3P#00005FThat sound, could it be...!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_6138")

    label("loc_6111")


    ChrTalk(
        0x101,
        "#3P#00005FWhat's that sound...!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6138")

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
        "*phew*, watch out!\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64ED")
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
            "#1K◆ About the [Runaway Vehicle Crackdown], you... (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",         # 0
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
        (0, "loc_64D4"),
        (1, "loc_64D9"),
        (2, "loc_64E3"),
        (SWITCH_DEFAULT, "loc_64ED"),
    )


    label("loc_64D4")

    Jump("loc_64ED")

    label("loc_64D9")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_64ED")

    label("loc_64E3")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_64ED")

    label("loc_64ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6547")

    ChrTalk(
        0x101,
        "#00001FT-That's the "High Bloods"'s...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FI-I knew it...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_658E")

    label("loc_6547")


    ChrTalk(
        0x101,
        "#00001FT-That's the runaway car...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FHow dangerous...!\x02",
    )

    CloseMessageWindow()

    label("loc_658E")

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
            "I'll call the District Crime Prevention Section!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6605():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6605)
    Sleep(50)

    def lambda_6615():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6615)
    Sleep(50)

    def lambda_6625():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6625)
    Sleep(50)

    def lambda_6635():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6635)
    Sleep(50)

    def lambda_6645():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6645)
    Sleep(50)

    def lambda_6655():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6655)
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
            "#00007FNoｱl, leave the navigation to me\x01",
            "and concentrate on driving!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x109,
        "#10107FYessir!\x02",
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

    def lambda_6721():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6721)
    Sleep(1000)
    WaitChrThread(0x109, 3)
    Sleep(500)

    def lambda_6738():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6738)

    def lambda_674D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_674D)
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

    def lambda_6812():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6812)

    def lambda_6827():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6827)
    WaitChrThread(0x104, 3)

    def lambda_683C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_683C)

    def lambda_6851():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6851)
    WaitChrThread(0x103, 3)

    def lambda_6866():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6866)

    def lambda_687B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_687B)
    WaitChrThread(0x105, 3)

    def lambda_6890():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6890)

    def lambda_68A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_68A5)
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

    # Function_26_5893 end

    def Function_27_6986(): pass

    label("Function_27_6986")

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

    # Function_27_6986 end

    def Function_28_6AA6(): pass

    label("Function_28_6AA6")

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

    # Function_28_6AA6 end

    def Function_29_6B21(): pass

    label("Function_29_6B21")

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

    # Function_29_6B21 end

    def Function_30_6BA8(): pass

    label("Function_30_6BA8")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, 15520, 0, 21370)
    OP_9F(0x1, 19310, 0, 18600)
    OP_9F(0x2, 0xD, 5000, 0x6)
    Return()

    # Function_30_6BA8 end

    def Function_31_6BD2(): pass

    label("Function_31_6BD2")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, 25620, 0, 9880)
    OP_9F(0x1, 30580, 0, 1500)
    OP_9F(0x1, 37950, 0, 230)
    OP_9F(0x1, 45610, 0, 160)
    OP_9F(0x2, 0xD, 10000, 0x6)
    OP_98(0xD, 0x6D60, 0x0, 0x0, 0x2710, 0x0)
    Return()

    # Function_31_6BD2 end

    def Function_32_6C2C(): pass

    label("Function_32_6C2C")

    OP_95(0x109, 11600, 0, 19760, 4000, 0x0)
    OP_95(0x109, 8490, 0, 19730, 4000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Sound(462, 0, 100, 0)
    OP_71(0x5, 0xF1, 0x10E, 0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_32_6C2C end

    def Function_33_6C71(): pass

    label("Function_33_6C71")

    OP_95(0x101, 21660, 0, 22150, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_33_6C71 end

    def Function_34_6C8D(): pass

    label("Function_34_6C8D")

    OP_95(0x102, 20460, 0, 22280, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_34_6C8D end

    def Function_35_6CA9(): pass

    label("Function_35_6CA9")

    OP_95(0x103, 19000, 0, 23000, 2000, 0x0)
    OP_93(0x103, 0xB4, 0x1F4)
    Return()

    # Function_35_6CA9 end

    def Function_36_6CC5(): pass

    label("Function_36_6CC5")

    OP_95(0x104, 20290, 0, 23430, 2000, 0x0)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_36_6CC5 end

    def Function_37_6CE1(): pass

    label("Function_37_6CE1")

    OP_95(0x105, 18030, 0, 23200, 2000, 0x0)
    OP_93(0x105, 0xB4, 0x1F4)
    Return()

    # Function_37_6CE1 end

    def Function_38_6CFD(): pass

    label("Function_38_6CFD")

    OP_95(0x101, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x101, 0xE1, 0x1F4)

    def lambda_6D1D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D1D)

    def lambda_6D32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6D32)
    Return()

    # Function_38_6CFD end

    def Function_39_6D3F(): pass

    label("Function_39_6D3F")

    Sleep(800)
    OP_95(0x102, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x102, 0xE1, 0x1F4)
    Return()

    # Function_39_6D3F end

    def Function_40_6D5E(): pass

    label("Function_40_6D5E")

    Sleep(1000)
    OP_95(0x103, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_40_6D5E end

    def Function_41_6D7D(): pass

    label("Function_41_6D7D")

    Sleep(800)
    OP_95(0x104, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x104, 0xE1, 0x1F4)
    Return()

    # Function_41_6D7D end

    def Function_42_6D9C(): pass

    label("Function_42_6D9C")

    Sleep(1200)
    OP_95(0x105, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_42_6D9C end

    def Function_43_6DBB(): pass

    label("Function_43_6DBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6ED3")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6DFE"),
        (1, "loc_6E18"),
        (2, "loc_6E32"),
        (3, "loc_6E4C"),
        (4, "loc_6E66"),
        (5, "loc_6E80"),
        (6, "loc_6E9A"),
        (SWITCH_DEFAULT, "loc_6EB4"),
    )


    label("loc_6DFE")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6ECE")

    label("loc_6E18")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_6ECE")

    label("loc_6E32")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_6ECE")

    label("loc_6E4C")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6ECE")

    label("loc_6E66")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_6ECE")

    label("loc_6E80")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_6ECE")

    label("loc_6E9A")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6ECE")

    label("loc_6EB4")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6ECE")

    label("loc_6ECE")

    Jump("Function_43_6DBB")

    label("loc_6ED3")

    Return()

    # Function_43_6DBB end

    def Function_44_6ED4(): pass

    label("Function_44_6ED4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F46")
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_6F46")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7347")
    Sleep(2500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7085")
    SetChrPos(0x101, 54820, 0, -130, 270)
    SetChrPos(0x102, 56020, 0, -1200, 270)
    SetChrPos(0x103, 56170, 0, 1010, 270)
    SetChrPos(0x104, 57750, 0, -1090, 270)
    SetChrPos(0x109, 57900, 0, 920, 270)
    SetChrPos(0x105, 59100, 0, -120, 270)
    Jump("loc_70DA")

    label("loc_7085")

    SetChrPos(0x101, 54820, 0, -130, 270)
    SetChrPos(0x102, 56020, 0, -1200, 270)
    SetChrPos(0x104, 56170, 0, 1010, 270)
    SetChrPos(0x109, 57750, 0, -1090, 270)
    SetChrPos(0x105, 57900, 0, 920, 270)

    label("loc_70DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7200")

    def lambda_70EF():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70EF)

    def lambda_7109():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7109)
    Sleep(100)

    def lambda_711D():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_711D)

    def lambda_7137():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7137)
    Sleep(120)

    def lambda_714B():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_714B)

    def lambda_7165():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7165)
    Sleep(90)

    def lambda_7179():
        OP_95(0xFE, 53750, 0, -1090, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7179)

    def lambda_7193():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7193)
    Sleep(100)

    def lambda_71A7():
        OP_95(0xFE, 53900, 0, 920, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_71A7)

    def lambda_71C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_71C1)
    Sleep(80)

    def lambda_71D5():
        OP_95(0xFE, 55100, 0, -120, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_71D5)

    def lambda_71EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_71EF)
    Jump("loc_72E3")

    label("loc_7200")


    def lambda_7205():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7205)

    def lambda_721F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_721F)
    Sleep(100)

    def lambda_7233():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7233)

    def lambda_724D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_724D)
    Sleep(120)

    def lambda_7261():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7261)

    def lambda_727B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_727B)
    Sleep(90)

    def lambda_728F():
        OP_95(0xFE, 53750, 0, -1090, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_728F)

    def lambda_72A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_72A9)
    Sleep(100)

    def lambda_72BD():
        OP_95(0xFE, 53900, 0, 920, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_72BD)

    def lambda_72D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_72D7)

    label("loc_72E3")

    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_730B")
    WaitChrThread(0x103, 1)

    label("loc_730B")

    Fade(500)
    OP_68(52070, 1000, -280, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19600, 0)
    OP_0D()
    Sleep(1000)
    Jump("loc_786F")

    label("loc_7347")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75F8")
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

    def lambda_73C0():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_73C0)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7563")
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
    Jump("loc_75E6")

    label("loc_7563")

    SetChrPos(0x101, 37700, 0, 900, 90)
    SetChrPos(0x102, 39000, 0, -800, 0)
    SetChrPos(0x104, 38400, 0, 2000, 180)
    SetChrPos(0x109, 39900, 0, 1600, 225)
    SetChrPos(0x105, 39900, 0, -200, 315)
    OP_68(39330, 1200, 570, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18180, 0)

    label("loc_75E6")

    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_786F")

    label("loc_75F8")

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

    def lambda_7671():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7671)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77DC")
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
    Jump("loc_785F")

    label("loc_77DC")

    SetChrPos(0x101, 31110, 0, 22130, 0)
    SetChrPos(0x102, 29890, 0, 23410, 90)
    SetChrPos(0x104, 30510, 0, 24350, 135)
    SetChrPos(0x105, 32430, 0, 23120, 270)
    SetChrPos(0x109, 31750, 0, 24340, 180)
    OP_68(31460, 1400, 22950, 0)
    MoveCamera(311, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18180, 0)

    label("loc_785F")

    Sleep(1)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()

    label("loc_786F")


    ChrTalk(
        0x105,
        (
            "#12P#10300FI see...\x01",
            "This is Bellguard Gate, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FYes, it's an important place where\x01",
            "a CGF unit protects the national \x01",
            "border with the Empire region.\x02\x03",
            "#10104FI told this to you too Wazy, but\x01",
            "the place is directed by an amazing\x01",
            "person: Commander Sonya Bｴlz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, I haven't meet her in person, but...\x01",
            "Don't they say it's quite the cool beauty?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C13")

    ChrTalk(
        0x104,
        (
            "#6P#00306FShe's a beauty for sure, but...\x01",
            "If pushed, I'd say she's in\x01",
            "the scary category.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI think the previous Commander\x01",
            "was disciplinarily dismissed due\x01",
            "to the Cult incident scandal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FWell, Commander Sonya\x01",
            "seemed to be the real\x01",
            "top from the very start.\x02\x03",
            "#00301FThat guy was a good for nothing who kept\x01",
            "pushin' his work onto his subordinates\x01",
            "and did nothing but winin' and dinin'.\x02\x03",
            "#00306FWhat started the fact that I got\x01",
            "stucked with doin' rehabilitation\x01",
            "training was due to that guy's big mistakes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E21")

    label("loc_7C13")


    ChrTalk(
        0x104,
        (
            "#00306FShe's a beauty for sure, but...\x01",
            "If pushed, I'd say she's in\x01",
            "the scary category.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI think the previous Commander\x01",
            "was disciplinarily dismissed due\x01",
            "to the Cult incident scandal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, Commander Sonya\x01",
            "seemed to be the real\x01",
            "top from the very start.\x02\x03",
            "#00301FThat guy was a good for nothing who kept\x01",
            "pushin' his work onto his subordinates\x01",
            "and did nothing but winin' and dinin'.\x02\x03",
            "#00306FWhat started the fact that I got\x01",
            "stucked with doin' rehabilitation\x01",
            "training was due to that guy's big mistakes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E21")


    ChrTalk(
        0x102,
        (
            "#00108FHe cajoled with the ringleader\x01",
            "and prescribed Gnosis to the\x01",
            "CGF members...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FBy the way...\x01",
            "How were the rehabilitation\x01",
            "training results?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8102")

    ChrTalk(
        0x104,
        (
            "#6P#00300FWell, they had their effect and now\x01",
            "all the guys have recovered back.\x02\x03",
            "#00306FAfter all, the Commander\x01",
            "was crazily spartan.\x01",
            "Honestly, they were totally exhausted.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00305FOh, yeah.\x01",
            "It came to me while thinkin' about the\x01",
            "rehabilitation training, but...\x02\x03",
            "#00300FIt seems that this time they\x01",
            "decided a promotion for Mireille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FMiss Mireille was...\x01",
            "That female officer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FYeah, seems her merits 'til\x01",
            "now have been recognised.\x02\x03",
            "#00309FSince we're here, let's go see\x01",
            "her later and tease her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8322")

    label("loc_8102")


    ChrTalk(
        0x104,
        (
            "#00300FWell, they had their effect and now\x01",
            "all the guys have recovered back.\x02\x03",
            "#00306FAfter all, the Commander\x01",
            "was crazily spartan.\x01",
            "Honestly, they were totally exhausted.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00305FOh, yeah.\x01",
            "It came to me while thinkin' about the\x01",
            "rehabilitation training, but...\x02\x03",
            "#00300FIt seems that this time they\x01",
            "decided a promotion for Mireille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FMiss Mireille was...\x01",
            "That female officer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah, seems her merits 'til\x01",
            "now have been recognised.\x02\x03",
            "#00309FSince we're here, let's go see\x01",
            "her later and tease her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8322")


    ChrTalk(
        0x101,
        (
            "#00006FNo, we should congratulate her...\x02\x03",
            "#00000FOh, we also must go\x01",
            "greet Commander Sonya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FThen, let's try to go to the\x01",
            "Commander Room at 2F now.\x02\x03",
            "She could be busy due to the\x01",
            "Trade Conference, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's try to go there.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8453")
    SetChrPos(0x0, 50820, 0, -130, 270)
    Jump("loc_8488")

    label("loc_8453")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8477")
    SetChrPos(0x0, 37700, 0, 900, 270)
    Jump("loc_8488")

    label("loc_8477")

    SetChrPos(0x0, 31110, 0, 22130, 180)

    label("loc_8488")

    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84B0")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_84B0")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_44_6ED4 end

    def Function_45_84B8(): pass

    label("Function_45_84B8")

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

    def lambda_8555():
        OP_97(0x0, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8555)
    Sleep(300)

    def lambda_8572():
        OP_97(0x1, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_8572)
    Sleep(300)

    def lambda_858F():
        OP_97(0x2, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_858F)
    Sleep(300)

    def lambda_85AC():
        OP_97(0x3, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_85AC)
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

    # Function_45_84B8 end

    def Function_46_85F5(): pass

    label("Function_46_85F5")

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

    def lambda_8692():
        OP_97(0x0, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8692)
    Sleep(300)

    def lambda_86AF():
        OP_97(0x1, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_86AF)
    Sleep(300)

    def lambda_86CC():
        OP_97(0x2, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_86CC)
    Sleep(300)

    def lambda_86E9():
        OP_97(0x3, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_86E9)
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

    # Function_46_85F5 end

    def Function_47_8732(): pass

    label("Function_47_8732")

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
            "   [Bellguard Gate]\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_47_8732 end

    SaveToFile()

Try(main)
