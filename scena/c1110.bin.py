from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1110.bin",                # FileName
        "c1110",                    # MapName
        "c1110",                    # Location
        0x0017,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 23, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1110",                  # 0
        "Receptionist Shion",     # 1
        "Chief Clip",             # 2
        "Shipping Employee",      # 3
        "Trader Rizel",           # 4
        "Citizen",                # 5
        "Citizen",                # 6
        "Citizen",                # 7
        "Citizen",                # 8
        "Bond",                   # 9
        "Creil",                  # 10
        "Sunita",                 # 11
        "Mary",                   # 12
        "Old Man Mors",           # 13
        "Roy",                    # 14
        "Alm",                    # 15
        "Aerie",                  # 16
        "Mrs. Margaret",          # 17
        "Chroma",                 # 18
        "Otto",                   # 19
    ))

    AddCharChip((
        "chr/ch34600.itc",                   # 00
        "chr/ch28000.itc",                   # 01
        "chr/ch23600.itc",                   # 02
        "chr/ch27800.itc",                   # 03
        "chr/ch21900.itc",                   # 04
        "chr/ch20400.itc",                   # 05
        "chr/ch21300.itc",                   # 06
        "chr/ch20800.itc",                   # 07
        "chr/ch27600.itc",                   # 08
        "chr/ch33300.itc",                   # 09
        "chr/ch34400.itc",                   # 0A
        "chr/ch39000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch21200.itc",                   # 0D
        "chr/ch46300.itc",                   # 0E
        "chr/ch46200.itc",                   # 0F
        "chr/ch44000.itc",                   # 10
        "chr/ch24900.itc",                   # 11
        "chr/ch20800.itc",                   # 12
    ))

    DeclNpc(0,       0,       7400,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(3529,    4000,    16209,   315,  261,  0x0, 0,   1,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(2720,    4000,    17000,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294962867, 0,       4460,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294922306, 250,     14710,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294953786, 4000,    14529,   135,  389,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4294962867, 0,       4460,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       7400,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(389,     0,       4960,    360,  389,  0x0, 0,   8,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(1879,    0,       3369,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3019,    0,       3369,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(3849,    0,       3089,    270,  389,  0x0, 0,   11,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   13,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(5760,    0,       4294964937, 90,   389,  0x0, 0,   14,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(6760,    0,       4294964937, 270,  389,  0x0, 0,   15,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(4294953786, 4000,    14529,   135,  389,  0x0, 0,   16,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294964687, 4000,    18750,   180,  389,  0x0, 0,   17,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294962916, 4000,    17329,   180,  389,  0x0, 0,   18,  0,   0,   0,   0,   18,  255,  0)

    DeclActor(0,       0,       6000,    1500,    0,       1500,    7460,    0x007E, 0,  4,  0x0000)
    DeclActor(0,       4000,    17600,   1500,    0,       5500,    18450,   0x007C, 0,  38, 0x0000)
    DeclActor(4294959196, 4000,    19780,   1500,    4294959196, 5500,    19780,   0x007C, 0,  36, 0x0000)
    DeclActor(8000,    4120,    19640,   1500,    8000,    5520,    19640,   0x007C, 0,  37, 0x0000)

    ChipFrameInfo(1060, 0)                                       # 0

    ScpFunction((
        "Function_0_424",          # 00, 0
        "Function_1_4DC",          # 01, 1
        "Function_2_507",          # 02, 2
        "Function_3_7E1",          # 03, 3
        "Function_4_893",          # 04, 4
        "Function_5_897",          # 05, 5
        "Function_6_172C",         # 06, 6
        "Function_7_17AF",         # 07, 7
        "Function_8_1809",         # 08, 8
        "Function_9_1830",         # 09, 9
        "Function_10_1843",        # 0A, 10
        "Function_11_1A8B",        # 0B, 11
        "Function_12_28A5",        # 0C, 12
        "Function_13_2976",        # 0D, 13
        "Function_14_2C01",        # 0E, 14
        "Function_15_2CCE",        # 0F, 15
        "Function_16_2D98",        # 10, 16
        "Function_17_2DF3",        # 11, 17
        "Function_18_2E40",        # 12, 18
        "Function_19_2EAA",        # 13, 19
        "Function_20_3403",        # 14, 20
        "Function_21_348E",        # 15, 21
        "Function_22_34D7",        # 16, 22
        "Function_23_3546",        # 17, 23
        "Function_24_37C4",        # 18, 24
        "Function_25_3A46",        # 19, 25
        "Function_26_3ABE",        # 1A, 26
        "Function_27_3AF6",        # 1B, 27
        "Function_28_5834",        # 1C, 28
        "Function_29_5EA1",        # 1D, 29
        "Function_30_6501",        # 1E, 30
        "Function_31_65F9",        # 1F, 31
        "Function_32_708C",        # 20, 32
        "Function_33_7497",        # 21, 33
        "Function_34_75B1",        # 22, 34
        "Function_35_7821",        # 23, 35
        "Function_36_83BE",        # 24, 36
        "Function_37_8452",        # 25, 37
        "Function_38_850C",        # 26, 38
        "Function_39_86A0",        # 27, 39
    ))


    def Function_0_424(): pass

    label("Function_0_424")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_464"),
        (1, "loc_470"),
        (2, "loc_47C"),
        (3, "loc_488"),
        (4, "loc_494"),
        (5, "loc_4A0"),
        (6, "loc_4AC"),
        (SWITCH_DEFAULT, "loc_4B8"),
    )


    label("loc_464")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_470")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_47C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_488")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_494")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4DB")

    Return()

    # Function_0_424 end

    def Function_1_4DC(): pass

    label("Function_1_4DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_506")
    OP_94(0xFE, 0x193C, 0x3B1A, 0x672, 0x41BE, 0x3E8)
    Sleep(300)
    Jump("Function_1_4DC")

    label("loc_506")

    Return()

    # Function_1_4DC end

    def Function_2_507(): pass

    label("Function_2_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_515")
    Jump("loc_77C")

    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_549")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x9, 1120, 0, 5240, 315)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_77C")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_557")
    Jump("loc_77C")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_591")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 1000, 0, 5100, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2500, 0, 5100, 270)
    Jump("loc_77C")

    label("loc_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5B3")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x17, 0x10)
    Jump("loc_77C")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C1")
    Jump("loc_77C")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5F5")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 390, 0, 5090, 360)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_77C")

    label("loc_5F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_603")
    Jump("loc_77C")

    label("loc_603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_611")
    Jump("loc_77C")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0x9, 1880, 0, 5490, 180)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xD, 670, 0, 3710, 360)
    SetChrPos(0xE, -180, 0, 3700, 360)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_77C")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_77C")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6BF")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 2380, 4000, 15840, 90)
    SetChrPos(0x9, 3790, 4000, 15840, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x9, 0x10)
    Jump("loc_77C")

    label("loc_6BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_70E")
    SetChrPos(0xB, 2380, 4000, 15840, 90)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x9, 3790, 4000, 15840, 270)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_709")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_709")

    Jump("loc_77C")

    label("loc_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_77C")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2380, 4000, 15840, 90)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0x9, 3790, 4000, 15840, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x10)

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_790")
    ClearScenarioFlags(0x22, 1)
    Event(0, 35)
    Jump("loc_7E0")

    label("loc_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_7E0")
    ClearScenarioFlags(0x22, 2)
    SetChrPos(0x0, -13650, 4000, 12700, 45)
    SetChrPos(0x1, -13650, 4000, 12700, 45)
    SetChrPos(0x2, -13650, 4000, 12700, 45)
    SetChrPos(0x3, -13650, 4000, 12700, 45)

    label("loc_7E0")

    Return()

    # Function_2_507 end

    def Function_3_7E1(): pass

    label("Function_3_7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FA")
    OP_10(0x0, 0x0)
    OP_10(0x6, 0x1)
    Jump("loc_800")

    label("loc_7FA")

    OP_10(0x0, 0x1)
    OP_10(0x6, 0x0)

    label("loc_800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_830")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_856")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)

    label("loc_856")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_870")
    SetMapObjFlags(0x3, 0x4)

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_892")
    SetMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 6)), scpexpr(EXPR_END)), "loc_892")
    OP_1B(0x2, 0x0, 0x27)

    label("loc_892")

    Return()

    # Function_3_7E1 end

    def Function_4_893(): pass

    label("Function_4_893")

    Call(0, 5)
    Return()

    # Function_4_893 end

    def Function_5_897(): pass

    label("Function_5_897")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D1")
    Call(0, 28)
    Return()

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF")
    Call(0, 27)
    Return()

    label("loc_8DF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2D")

    ChrTalk(
        0x8,
        (
            "The staff split up and confirmed\x01",
            "the safety of the citizens under\x01",
            "this martial law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Other than the minor injuries of ten-odd\x01",
            "citizens who got involved in disturbances,\x01",
            "there has been hardly any serious ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I arranged for ambulances\x01",
            "for those needing treatment...\x01",
            "For now, I am relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B00")

    label("loc_A2D")


    ChrTalk(
        0x8,
        (
            "Other than ten-odd citizens who received\x01",
            "minor injuries under this martial law,\x01",
            "there has been hardly any serious ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I arranged for ambulances\x01",
            "for those needing treatment...\x01",
            "For now, I am relieved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B00")

    Jump("loc_1728")

    label("loc_B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCD")

    ChrTalk(
        0x8,
        (
            "For now, we have accepted\x01",
            "citizens who can't return home\x01",
            "here at the City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something bothering you,\x01",
            "please don't hesitate to let me know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C71")

    label("loc_BCD")


    ChrTalk(
        0x8,
        (
            "We have emergency supplies of food and\x01",
            "blankets here at City Meeting Hall too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something bothering you,\x01",
            "please don't hesitate to let me know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C71")

    Jump("loc_1728")

    label("loc_C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D05")

    ChrTalk(
        0x8,
        (
            "You can clearly hear the chants\x01",
            "of "hooray" even from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel like it is a little scary. \x01",
            "I wonder why that is...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1728")

    label("loc_D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D88")

    ChrTalk(
        0x8,
        (
            "Thank you for attending\x01",
            "today's charity event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are planning to\x01",
            "participate, please\x01",
            "ask me about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1728")

    label("loc_D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED4")

    ChrTalk(
        0x8,
        (
            "A large number of citizens are\x01",
            "asking me about the armed group\x01",
            "that attacked Mainz, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am troubled because I have nothing\x01",
            "resembling an answer regarding the objective\x01",
            "of the criminals or their actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Many are saying it's an Imperial plot,\x01",
            "but... In the end, what is the real truth?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F2B")

    label("loc_ED4")


    ChrTalk(
        0x8,
        (
            "Many are saying it's an Imperial plot,\x01",
            "but... In the end, what is the real truth?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2B")

    Jump("loc_1728")

    label("loc_F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FE5")

    ChrTalk(
        0x8,
        (
            "Welcome. In the hall on my left,\x01",
            "a civic forum with the theme of\x01",
            "state independence is being held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is open to the public, so\x01",
            "please stop by, if you like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1728")

    label("loc_FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1056")

    ChrTalk(
        0x8,
        (
            "Let's see, auditing\x01",
            "itself is possible, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm terribly sorry,\x01",
            "the seats are full...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1728")

    label("loc_1056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10E5")

    ChrTalk(
        0x8,
        (
            "Welcome to Crossbell\x01",
            "City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are thinking of using\x01",
            "the City Meeting Hall,\x01",
            "please fill out this form.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1728")

    label("loc_10E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_12E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1209")

    ChrTalk(
        0x8,
        (
            "Inquiries regarding study\x01",
            "groups for accepting state\x01",
            "independence have increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To answer them, the city and CNS\x01",
            "are jointly holding a civic forum\x01",
            "the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We are now fine tuning\x01",
            "things such that everyone\x01",
            "will find the forum useful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12DB")

    label("loc_1209")


    ChrTalk(
        0x8,
        (
            "The day after tomorrow, we are going to\x01",
            "hold a civic forum here at City Meeting Hall\x01",
            "with state independence as the theme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We are now fine tuning\x01",
            "things such that everyone\x01",
            "will find the forum useful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DB")

    Jump("loc_1728")

    label("loc_12E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1396")

    ChrTalk(
        0x8,
        (
            "I-I am terribly sorry.\x01",
            "I thought the notice had been\x01",
            "there for awhile, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From the standpoint of security\x01",
            "guarantee, we cannot let pass\x01",
            "average citizens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1728")

    label("loc_1396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_150B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1479")

    ChrTalk(
        0x8,
        (
            "Each country's heads of state\x01",
            "have finally come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They will be talking about various\x01",
            "things starting this afternoon, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder what everyone\x01",
            "will do to pass the time?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1506")

    label("loc_1479")


    ChrTalk(
        0x8,
        (
            "The heads of state will talk about various\x01",
            "things starting this afternoon, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder what everyone\x01",
            "will do to pass the time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1506")

    Jump("loc_1728")

    label("loc_150B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_15B4")

    ChrTalk(
        0x8,
        (
            "The City Meeting Hall is\x01",
            "reserved for the duration\x01",
            "of the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because it is near Orchis Tower,\x01",
            "it can be used if anything happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1728")

    label("loc_15B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_171C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1657")

    ChrTalk(
        0x8,
        (
            "Everyone, thank you for\x01",
            "your investigation today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We here at City Meeting Hall look forward\x01",
            "to working with you in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1717")

    label("loc_1657")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1717")

    ChrTalk(
        0x8,
        (
            "We would like you all to confirm a\x01",
            "total of three suspicious addresses\x01",
            "as well as the previous residents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once you have confirmed them\x01",
            "all, please come report here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1717")

    label("loc_1717")

    Jump("loc_1728")

    label("loc_171C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1728")
    Call(0, 10)

    label("loc_1728")

    TalkEnd(0x8)
    Return()

    # Function_5_897 end

    def Function_6_172C(): pass

    label("Function_6_172C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_17AB")

    ChrTalk(
        0xFE,
        (
            "I hope we find some\x01",
            "good property.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, I'd like\x01",
            "somewhere with lots of\x01",
            "blooming flowers, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17AB")

    TalkEnd(0xFE)
    Return()

    # Function_6_172C end

    def Function_7_17AF(): pass

    label("Function_7_17AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1805")

    ChrTalk(
        0xFE,
        "It's all right, mother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure father will\x01",
            "find a nice place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1805")

    TalkEnd(0xFE)
    Return()

    # Function_7_17AF end

    def Function_8_1809(): pass

    label("Function_8_1809")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_182C")

    ChrTalk(
        0xFE,
        "Nyaon.[I'm tired]\x02",
    )

    CloseMessageWindow()

    label("loc_182C")

    TalkEnd(0xFE)
    Return()

    # Function_8_1809 end

    def Function_9_1830(): pass

    label("Function_9_1830")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_183F")
    Call(0, 10)

    label("loc_183F")

    TalkEnd(0xFE)
    Return()

    # Function_9_1830 end

    def Function_10_1843(): pass

    label("Function_10_1843")

    OP_4B(0x10, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B9")

    ChrTalk(
        0x10,
        (
            "Yes, I'm looking for a place that's\x01",
            "as cheap as possible, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "A small place is fine, but the\x01",
            "three of us have to live there...\x01",
            "Is there a place like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... Please\x01",
            "have a look at\x01",
            "these materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I remember correctly,\x01",
            "the previous residents\x01",
            "moved out some months ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmm, so this is the\x01",
            "property. What to do...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A82")

    label("loc_19B9")


    ChrTalk(
        0x10,
        (
            "Ah, and...\x01",
            "Pets have to be allowed.\x01",
            "That's the minimum condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, I think that's okay for\x01",
            "this particular property.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Oh, that's great!\x01",
            "In that case, I'd like to\x01",
            "check it out ASAP...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A82")

    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_10_1843 end

    def Function_11_1A8B(): pass

    label("Function_11_1A8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB5")

    ChrTalk(
        0xFE,
        (
            "We are now preparing a place to\x01",
            "give a formal explanation to the\x01",
            "citizens regarding this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Later, citizens would probably\x01",
            "seek official explanation about\x01",
            "what may happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is chaos everywhere. \x01",
            "We have to hurry and get ready.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C5F")

    label("loc_1BB5")


    ChrTalk(
        0xFE,
        (
            "We are now preparing a place to\x01",
            "give a formal explanation to the\x01",
            "citizens regarding this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is chaos everywhere. \x01",
            "We have to hurry and get ready.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5F")

    Jump("loc_28A1")

    label("loc_1C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1E5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9F")

    ChrTalk(
        0xFE,
        (
            "Regarding this matter, the\x01",
            "President had no choice but\x01",
            "to hand down "martial law".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But even so, a situation like this... \x01",
            "There are probably a lot of\x01",
            "people who are unprepared for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...While waiting on a conclusion,\x01",
            "we must once again confirm\x01",
            "the safety of the citizens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E59")

    label("loc_1D9F")


    ChrTalk(
        0xFE,
        (
            "A situation like this... There\x01",
            "are probably a lot of people\x01",
            "who are unprepared for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...While waiting on a conclusion,\x01",
            "we must once again confirm\x01",
            "the safety of the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E59")

    Jump("loc_28A1")

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F35")

    ChrTalk(
        0xFE,
        (
            "Crossbell independence, and the\x01",
            "President's assumption of office...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given these, our organizational\x01",
            "structure will likely change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Things are getting more tense, day by day.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FA8")

    label("loc_1F35")


    ChrTalk(
        0xFE,
        (
            "Given these, our organizational\x01",
            "structure will likely change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Things are getting more tense, day by day.\x02",
    )

    CloseMessageWindow()

    label("loc_1FA8")

    Jump("loc_28A1")

    label("loc_1FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1FEE")

    ChrTalk(
        0xFE,
        (
            "Come now, please\x01",
            "enjoy today's\x01",
            "charity event.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A1")

    label("loc_1FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_21F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2157")

    ChrTalk(
        0xFE,
        (
            "We got a directive from City\x01",
            "Hall to "devote ourselves to\x01",
            "handling minor disputes"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, it seems like there're a lot of\x01",
            "things we're not seeing, and I'm worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, but if city staff such as\x01",
            "ourselves are worried, all the\x01",
            "citizens will be even more worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We've got to hold ourselves together, somehow.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21F2")

    label("loc_2157")


    ChrTalk(
        0xFE,
        (
            "If city staff such as ourselves\x01",
            "are worried, all the citizens will\x01",
            "be even more worried, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We've got to hold ourselves together, somehow.\x02",
    )

    CloseMessageWindow()

    label("loc_21F2")

    Jump("loc_28A1")

    label("loc_21F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2290")

    ChrTalk(
        0xFE,
        (
            "The civic forum we're now\x01",
            "holding is proceeding smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that things continue like this\x01",
            "and no particular uproar occurs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A1")

    label("loc_2290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_22DC")

    ChrTalk(
        0xFE,
        (
            "Hmm, I want to get good at\x01",
            "operating a keyboard somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A1")

    label("loc_22DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_24A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E6")

    ChrTalk(
        0xFE,
        (
            "Lately, even General Affairs\x01",
            "Section Two has started to use\x01",
            "orbal mail more and more, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mastering something\x01",
            "new at my age is a\x01",
            "bit of a challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The input device called a keyboard\x01",
            "in particular is a formidable enemy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24A1")

    label("loc_23E6")


    ChrTalk(
        0xFE,
        (
            "In addition, I get eye strain when I\x01",
            "look at the display no matter what I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, the print medium...\x01",
            "Well, I'm saying it like this,\x01",
            "but it'll probably be left behind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A1")

    Jump("loc_28A1")

    label("loc_24A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2589")

    ChrTalk(
        0xFE,
        (
            "I feel like our workload has doubled ever since\x01",
            "this was redesignated as the City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the civic forum, preparations\x01",
            "for the referendum... Lately, I feel\x01",
            "all of this is reaching a climax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A1")

    label("loc_2589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_25D4")

    ChrTalk(
        0xFE,
        (
            "Umm, as she said, security\x01",
            "is the number one problem...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A1")

    label("loc_25D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_267B")

    ChrTalk(
        0xFE,
        (
            "I saw the unveiling\x01",
            "ceremony from the window.\x01",
            "Wow, what a spectacle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "City Hall was finally relocated.\x01",
            "The reality of it is finally setting in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A1")

    label("loc_267B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2713")

    ChrTalk(
        0xFE,
        (
            "Yes, the resident registration office\x01",
            "hasn't moved. We still handle that here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please ask about it at the reception desk on 1F.\x02",
    )

    CloseMessageWindow()
    Jump("loc_28A1")

    label("loc_2713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_27D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2733")
    Call(0, 13)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_27D0")

    label("loc_2733")


    ChrTalk(
        0xFE,
        (
            "It seems the reason for\x01",
            "today's cancellation was\x01",
            "mainly due to the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, if we had set a\x01",
            "cancellation fee, maybe\x01",
            "this wouldn't have happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D0")

    Jump("loc_28A1")

    label("loc_27D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_28A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F8")
    Call(0, 12)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_28A1")

    label("loc_27F8")


    ChrTalk(
        0xFE,
        (
            "*sigh*, it seems all the relocation\x01",
            "paperwork has been given to \x01",
            "General Affairs Section Two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought each section\x01",
            "was going to do their\x01",
            "own... *grumble*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A1")

    TalkEnd(0xFE)
    Return()

    # Function_11_1A8B end

    def Function_12_28A5(): pass

    label("Function_12_28A5")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xA,
        (
            "Umm, then can you check\x01",
            "the shipping label?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm, let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, there's no mistake. Please\x01",
            "take care of the delivery, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, please leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_28A5 end

    def Function_13_2976(): pass

    label("Function_13_2976")

    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "It'll be time to start the\x01",
            "seminar soon, but... Should I\x01",
            "postpone the program a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "O-Of course. With less than\x01",
            "half my staff here, there'd\x01",
            "be no meaning in starting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But to think they cancelled... \x01",
            "This is why I hate working with amateurs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because of things like this, the business chance\x01",
            "I was thinking of seizing was a big mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "R-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A-Anyway, I'll wait only\x01",
            "a little while longer.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BEB")

    ChrTalk(
        0x102,
        (
            "#00105F(Hey Lloyd.\x01",
            "Could he be...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Yeah. One of those Gnosis\x01",
            "patients from the Cult incident.)\x02\x03",
            "#00000F(It looks like he has it tough,\x01",
            "but I'm glad he's all right.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BEB")

    SetScenarioFlags(0x12E, 5)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_13_2976 end

    def Function_14_2C01(): pass

    label("Function_14_2C01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C24")
    Call(0, 12)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2CCA")

    label("loc_2C24")


    ChrTalk(
        0xFE,
        (
            "Umm, this belongs to General\x01",
            "Affairs Section One, and this\x01",
            "belongs to the Finance Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The new City Hall is close by,\x01",
            "so these will be there shortly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCA")

    TalkEnd(0xFE)
    Return()

    # Function_14_2C01 end

    def Function_15_2CCE(): pass

    label("Function_15_2CCE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF1")
    Call(0, 13)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_2D94")

    label("loc_2CF1")


    ChrTalk(
        0xFE,
        (
            "Hmm. Even if I collect participation fees, it\x01",
            "won't even cover half of the hall reservation fee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to get some new\x01",
            "capital no matter what, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D94")

    TalkEnd(0xFE)
    Return()

    # Function_15_2CCE end

    def Function_16_2D98(): pass

    label("Function_16_2D98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2DEF")

    ChrTalk(
        0xFE,
        (
            "Umm, I'm here to ask about the citizen\x01",
            "registration procedure, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DEF")

    TalkEnd(0xFE)
    Return()

    # Function_16_2D98 end

    def Function_17_2DF3(): pass

    label("Function_17_2DF3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm worried about my mother who\x01",
            "works in the department store...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2DF3 end

    def Function_18_2E40(): pass

    label("Function_18_2E40")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Mrr... My goodness.\x01",
            "To think this would happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President Dieter...\x01",
            "I believed in him.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2E40 end

    def Function_19_2EAA(): pass

    label("Function_19_2EAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_32B5")

    ChrTalk(
        0xFE,
        (
            "My, you all are... \x01",
            "Policemen, if I recall right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You helped me back there, you know.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FD0")

    ChrTalk(
        0x101,
        (
            "#00005FAh... Could you be Vice\x01",
            "Chief Pierre's wife...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, it's been awhile, madame. \x01",
            "Are you sheltering here in City Meeting Hall?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_2FD0")


    ChrTalk(
        0x101,
        (
            "#00005FAh... Could you be Vice\x01",
            "Chief Pierre's wife...?\x02\x03",
            "#00001FUmm... Are you sheltering\x01",
            "here in City Meeting Hall?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3049")


    ChrTalk(
        0xFE,
        (
            "Yes, that's right, but... Umm,\x01",
            "have you seen my husband?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He hasn't returned since he said\x01",
            "he was going to Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FNo, we haven't...\x02\x03",
            "What is the Vice Chief\x01",
            "doing at Orchis Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who knows...\x01",
            "I too didn't ask him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. For him to needlessly\x01",
            "worry me at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to give him a severe\x01",
            "scolding when he gets back.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F...Please wait here\x01",
            "for now, madam.\x02\x03",
            "He might\x01",
            "suddenly return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yes, I'll do so. Please\x01",
            "contact me if you do see him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3373")

    label("loc_32B5")


    ChrTalk(
        0xFE,
        (
            "My husband went to Orchis\x01",
            "Tower and hasn't returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. For him to needlessly\x01",
            "worry me at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to give him a severe\x01",
            "scolding when he gets back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3373")

    SetScenarioFlags(0x1CC, 2)
    Jump("loc_33FF")

    label("loc_337B")


    ChrTalk(
        0xFE,
        (
            "Goodness. For him to needlessly\x01",
            "worry me at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to give him a severe\x01",
            "scolding when he gets back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FF")

    TalkEnd(0xFE)
    Return()

    # Function_19_2EAA end

    def Function_20_3403(): pass

    label("Function_20_3403")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_348A")

    ChrTalk(
        0xFE,
        (
            "Hey, why can't we go\x01",
            "to Orchis Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can we come and go freely at least\x01",
            "to the square in front of Orchis Tower?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_348A")

    TalkEnd(0xFE)
    Return()

    # Function_20_3403 end

    def Function_21_348E(): pass

    label("Function_21_348E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34D3")

    ChrTalk(
        0xFE,
        (
            "Yeah, yeah! \x01",
            "You tell us suddenly\x01",
            "such a thing now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D3")

    TalkEnd(0xFE)
    Return()

    # Function_21_348E end

    def Function_22_34D7(): pass

    label("Function_22_34D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3542")

    ChrTalk(
        0xFE,
        (
            "I want to participate in\x01",
            "tomorrow's civic forum, but...\x01",
            "I wonder if there are open seats.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3542")

    TalkEnd(0xFE)
    Return()

    # Function_22_34D7 end

    def Function_23_3546(): pass

    label("Function_23_3546")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_358E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3580")
    Call(0, 32)
    Return()

    label("loc_3580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358E")
    Call(0, 29)
    Return()

    label("loc_358E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_366C")

    ChrTalk(
        0xFE,
        (
            "Sorry, everyone. Roy\x01",
            "is wasting your time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we can hold the pageant,\x01",
            "it'll be a good way for\x01",
            "the citizens to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please do your best\x01",
            "searching for participants.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_36F1")

    label("loc_366C")


    ChrTalk(
        0xFE,
        (
            "If we can hold the pageant,\x01",
            "it'll be a good way for\x01",
            "the citizens to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please do your best\x01",
            "searching for participants.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F1")

    Jump("loc_37C0")

    label("loc_36F6")


    ChrTalk(
        0xFE,
        (
            "It seems the citizens had a chance to\x01",
            "relax, and a lot of reconstruction support\x01",
            "funds were collected after the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although the pageant was Roy's idea...\x01",
            "Hu hu, it turned out all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C0")

    TalkEnd(0xFE)
    Return()

    # Function_23_3546 end

    def Function_24_37C4(): pass

    label("Function_24_37C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_380C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37FE")
    Call(0, 32)
    Return()

    label("loc_37FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_380C")
    Call(0, 29)
    Return()

    label("loc_380C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393C")

    ChrTalk(
        0x15,
        (
            "I want all of you to scout\x01",
            ""working women" who will\x01",
            "participate in the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "A "waitress", a "craftsman", \x01",
            "a "maid" and a "Sister"...\x01",
            "I'm looking for these four types.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I think this set of\x01",
            "occupations will\x01",
            "give a good balance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I'm counting on you!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_39CD")

    label("loc_393C")


    ChrTalk(
        0x15,
        (
            ""Waitress", "craftsman",\x01",
            ""maid", "Sister"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I want you to scout four "working\x01",
            "women" of those types for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I'm counting on you!\x02",
    )

    CloseMessageWindow()

    label("loc_39CD")

    Jump("loc_3A42")

    label("loc_39D2")


    ChrTalk(
        0x15,
        (
            "Thanks to your help, the\x01",
            "pageant was a huge success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Thank you for\x01",
            "gathering the\x01",
            "participants for me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A42")

    TalkEnd(0xFE)
    Return()

    # Function_24_37C4 end

    def Function_25_3A46(): pass

    label("Function_25_3A46")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "This address in Downtown is my father's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is great, Aerie! We just\x01",
            "have to go there to meet him.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_3A46 end

    def Function_26_3ABE(): pass

    label("Function_26_3ABE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Uh uh, we finally found\x01",
            "his location, Alm㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_3ABE end

    def Function_27_3AF6(): pass

    label("Function_27_3AF6")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    StopBGM(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-190, 1300, 5510, 0)
    MoveCamera(34, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20640, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x109, -700, 0, 3600, 0)
    SetChrPos(0x105, 700, 0, 3600, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    ChrTalk(
        0x8,
        (
            "Welcome to Crossbell\x01",
            "City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, thank you for coming,\x01",
            "members of the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FWe're here for the request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWe have some new members\x01",
            "helping out as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FNice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FPleased to make your acquaintance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, nice to meet\x01",
            "both of you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FCity Meeting Hall, eh?\x01",
            "The name has a weird ring to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FYeah. It's finally\x01",
            "hitting me that this\x01",
            "isn't City Hall anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F*giggle*, well the new\x01",
            "City Hall will be in\x01",
            "the new building.\x02\x03",
            "#00100FFor now, this place is still\x01",
            "functioning as a "branch office".\x02\x03",
            "So in that sense it'll be\x01",
            "just as useful for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10103FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. And this reception counter will\x01",
            "continue to serve as the point of\x01",
            "contact for various city services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, notice about this resource has yet\x01",
            "to spread among the citizens, causing the\x01",
            "number of public inquiries to skyrocket.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "I-I am sorry, this not\x01",
            "something regarding you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo problem. It sounds like you\x01",
            "have your work cut out for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, the things government\x01",
            "officials think up sure are boring.\x02\x03",
            "If it were me, I would have made it an \x01",
            ""adult hall" near the Entertainment District.\x02\x03",
            "#10309FA nightclub to entertain public servants...\x01",
            "It goes without saying that the SSS would be even\x01",
            "more popular than it's now if there was such a thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FPopular you say...\x01",
            "What kind of support requests we'd do?\x02\x03",
            "#00001FI mean, from the very start that\x01",
            "kind of "night work" is\x01",
            "unthinkable for public servants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FA-Ahaha... \x01",
            "(I pictured it a little in my head.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F*a-ahem*... Anyway, Lloyd, aren't you\x01",
            "forgetting the main reason why we're here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00011FO-Oh, that's right.\x02\x03",
            "#00000FUhmm, sorry. About that\x01",
            "support request then...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Y-Yes, let me explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "──I am sure you are all aware of\x01",
            "the "Residence Change Notice".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is submitted at\x01",
            "the time of residence\x01",
            "change, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Recently, we found\x01",
            "suspicious names on\x01",
            "some of these forms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FSuspicious names?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes... They were "names\x01",
            "not registered within the\x01",
            "city" to be precise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We found a few of them, and in each\x01",
            "case they had names not found on any\x01",
            "citizen or corporate registration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So I was hoping you could confirm\x01",
            "the real situation at the addresses\x01",
            "those notices are from...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And just to be safe, I would\x01",
            "also like you to check on\x01",
            "the prior residents as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FI see. So basically we have to\x01",
            "confirm the new and old residents\x01",
            "at those addresses, right?\x02\x03",
            "#00003FWe can't ignore any crime related\x01",
            "activities that might be occurring.\x02\x03",
            "#00000FAnd we'll report all of what\x01",
            "we find back to you then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYes, that's the gist of it.\x02\x03",
            "#00100FIt's only natural that you'd have\x01",
            "a list of suspicious addresses...\x02\x03",
            "But do you have any idea of the\x01",
            "whereabouts of the previous residents?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, we only know the\x01",
            "location of one of\x01",
            "the people who moved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We have no idea about\x01",
            "any of the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FI see. So an investigation\x01",
            "is needed, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FBut first, we'll need to\x01",
            "go to each address to\x01",
            "verify who lives there.\x02\x03",
            "We should even be able to find\x01",
            "about the previous residents\x01",
            "through the investigation process.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYeah, that should work.\x02\x03",
            "#00000FDo you have the\x01",
            "list of places?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, I have a duplicate\x01",
            "report ready for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOk, we'll hold onto this.\x02",
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x258, 0x3E8, 0x0)
    Sleep(800)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_97(0x101, 0x0, 0x0, 0xFFFFFDA8, 0x3E8, 0x0)
    Sleep(50)

    def lambda_49E2():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49E2)

    def lambda_49EF():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_49EF)

    def lambda_49FC():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_49FC)

    def lambda_4A09():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4A09)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00000FHmm, so it looks like there're a\x01",
            "total of three places of interest.\x02\x03",
            "First is a place near Elie's\x01",
            "house in Residential Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FLet's see... Oh that's next\x01",
            "to my parents' house.\x02\x03",
            "#00105FThe "High Bloods" is the resident...\x01",
            "...Is it the name of some company?\x02\x03",
            "#00103FThe family of Mr. Bond,\x01",
            "a securities salesman, \x01",
            "should be living there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FYeah, he's recorded on the\x01",
            "list as the previous resident.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5P#00003FA securities salesmanr named Bond...\x02\x03",
            "#00001FWasn't he one of the Gnosis\x01",
            "victims from the Cult incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FYes, I'm certain he was.\x02\x03",
            "#00108FI heard various things\x01",
            "happened to the family\x01",
            "after the incident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FYou think they got caught up\x01",
            "in some trouble because of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FI don't know... \x01",
            "But Mr. Bond did submit a\x01",
            "residence change notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FThe next one is on East Street, on the\x01",
            "second floor of Acacia Apartments.\x02\x03",
            "Oh yeah, that's the place just\x01",
            "to the left of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FResidential Street and East Street... We've\x01",
            "got to make sure to investigate both of them.\x02\x03",
            "#00001FAnd the last address is also on East\x01",
            "Street... The Fisherman's Guild...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00011F──Wait... What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FW-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00008FWell, the form says the current resident\x01",
            "is the "Fishing Emperor Club", but...\x02\x03",
            "It's a name I don't think I've ever heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00105FYou were a member of the\x01",
            "Fisherman's Guild, right?\x02\x03",
            "Have you heard anything about\x01",
            "this from the other members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FW-Well, I've been busy lately and\x01",
            "haven't had time for fishing.\x02\x03",
            "#00001FAnd we don't know the location of the\x01",
            ""Fisherman's Guild", the previous resident,\x01",
            "either... Could they have changed their name?\x02\x03",
            "#00003F...Anyway, we'll need to\x01",
            "investigate this, too.\x02\x03",
            "#00001FThe last address is on the first\x01",
            "floor of Lotus Heights in Downtown.\x02\x03",
            "Mr. Geithner was the previous resident.\x01",
            "It seems he's gone missing.\x02\x03",
            "And the current resident is...\x01",
            ""Sean Alnam".\x02\x03",
            "#00005F...That name kind of\x01",
            "sounds familiar...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10304FHu hu, he's a famous fairytale author, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00011FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FHe wrote "Mark and the Witch of the\x01",
            "Deep Forest." They're some of the\x01",
            "most popular books at the library.\x02\x03",
            "#00100FYou've heard it too, Lloyd.\x01",
            "Remember, back when we raided\x01",
            "the Revache hideout...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00005FYeah, now that you mention it...\x01",
            "That was the password to\x01",
            "unlock a door there, wasn't it.\x02\x03",
            "#00008FBut I can't believe an author that famous\x01",
            "would choose to live in Downtown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FYes, well for starters,\x01",
            "Mr. Alnam should be already dead.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006FY-You don't say... \x01",
            "I'm getting a bad feeling about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, well it looks like\x01",
            "we have our investigative\x01",
            "work cut out for us then.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "I am so sorry.\x02",
    )

    CloseMessageWindow()

    def lambda_5569():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5569)
    Sleep(50)

    def lambda_5579():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5579)
    Sleep(50)

    def lambda_5589():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5589)
    Sleep(50)

    def lambda_5599():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5599)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "We staff members will try to be \x01",
            "more careful in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FOh, don't worry about it... This must\x01",
            "be a busy time for City Meeting Hall staff\x01",
            "with the new mayor and the system's reform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FYes. The citizens who submitted the faulty\x01",
            "notices are the ones to blame here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "T-Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FOk, we'll get started\x01",
            "with our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe'll give you our report once\x01",
            "we've confirmed them all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Y-Yes, please, I am\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Suspicious Housing Units Investigation]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x131, 4)
    OP_29(0x6A, 0x1, 0x0)
    SetChrPos(0x0, 0, 0, 4000, 180)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    EventEnd(0x5)
    Return()

    # Function_27_3AF6 end

    def Function_28_5834(): pass

    label("Function_28_5834")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-190, 1300, 5510, 0)
    MoveCamera(34, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20640, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x109, -700, 0, 3600, 0)
    SetChrPos(0x105, 700, 0, 3600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#12P#1PHow is your investigation\x01",
            "of the suspicious housing\x01",
            "units going, everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FActually, we just\x01",
            "finished and we're here\x01",
            "to deliver our report.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Handed over the duplicate report\x01",
            "with corrected resident names.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#12P#1PI see. You did a great\x01",
            "job investigating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PHmm, interesting. So Republicans have\x01",
            "moved into Residential Street and\x01",
            "Imperials have moved into East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12P#1PAnd as for Downtown... Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PNo, I just didn't expect to\x01",
            "see Mr. Geval's name here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PI have seen him here\x01",
            "a few times so I have\x01",
            "some mixed feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PI am not sure how to say this, but\x01",
            "even though he has done bad things,\x01",
            "I cannot bring myself to hate him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYes, somehow I\x01",
            "know the feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FHe seems easy to read whether\x01",
            "in a good or bad sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, if he was a little\x01",
            "more upstanding, everyone\x01",
            "too would like him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, I guess that is true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, that is all I needed\x01",
            "for this investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All that is left is for the Residential Affairs Section\x01",
            "personnel to do all the paperwork to sort this out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thank you so much\x01",
            "for your help today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FWell I'm glad we were\x01",
            "able to be of service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FPlease let us know if\x01",
            "you ever need anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Suspicious Housing Units Investigation]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6A, 0x1, 0x7)
    OP_29(0x6A, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0xF)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 0, 0, 4000, 180)
    EventEnd(0x5)
    Return()

    # Function_28_5834 end

    def Function_29_5EA1(): pass

    label("Function_29_5EA1")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A4")
    Fade(500)
    OP_68(1560, 1500, 3500, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 1810, 0, 3530, 0)
    SetChrPos(0x102, 620, 0, 3130, 0)
    SetChrPos(0x104, 1610, 0, 2310, 0)
    SetChrPos(0x103, 2860, 0, 2990, 0)
    SetChrPos(0x105, 2700, 0, 1650, 0)
    SetChrPos(0x109, 570, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_0D()

    ChrTalk(
        0x14,
        "Mmm... So they're not coming after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Say, Roy. How\x01",
            "about giving up\x01",
            "on this program.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "What're you saying, grandpa!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "This is the centerpiece of the\x01",
            "charity event to cheer up the\x01",
            "citizens we're talking about here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "If we don't do it,\x01",
            "just what will we do!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "B-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me. I'm\x01",
            "terribly sorry for\x01",
            "interrupting, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_60FB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_60FB)
    Sleep(50)
    OP_93(0x15, 0xB4, 0x1F4)

    ChrTalk(
        0x15,
        "You guys are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Oh, so you came for us after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Are you here for\x01",
            "today's charity event?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm, if I'm not mistaken, the\x01",
            "Merchants Association requested our\x01",
            "assistance with the charity event, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        "Huh? I don't remember that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "──I was the one who submitted the request.\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x14, 0x15, 500)
    Sleep(500)

    ChrTalk(
        0x14,
        (
            "W-What?\x01",
            "Roy, just when did you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Ha ha, I did it secretly,\x01",
            "a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'll get right to\x01",
            "explaining the job.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6380():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6380)

    ChrTalk(
        0x15,
        "Do you have time?\x02",
    )

    CloseMessageWindow()
    Jump("loc_64B6")

    label("loc_63A4")

    Fade(500)
    OP_68(1560, 1500, 3500, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 1810, 0, 3530, 0)
    SetChrPos(0x102, 620, 0, 3130, 0)
    SetChrPos(0x104, 1610, 0, 2310, 0)
    SetChrPos(0x103, 2860, 0, 2990, 0)
    SetChrPos(0x105, 2700, 0, 1650, 0)
    SetChrPos(0x109, 570, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_93(0x14, 0xB4, 0x0)
    OP_93(0x15, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x15,
        (
            "I want to get right to\x01",
            "explaining the job, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Do you have time?\x02",
    )

    CloseMessageWindow()

    label("loc_64B6")

    Call(0, 30)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0x14, 0x5A, 0x0)
    OP_93(0x15, 0x10E, 0x0)
    BeginChrThread(0x14, 0, 0, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1750, 0, 4000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_29_5EA1 end

    def Function_30_6501(): pass

    label("Function_30_6501")

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
            "Accept\x01",      # 0
            "Quit\x01",        # 1
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
        (0, "loc_655D"),
        (1, "loc_6565"),
        (SWITCH_DEFAULT, "loc_65F8"),
    )


    label("loc_655D")

    Call(0, 31)
    Jump("loc_65F8")

    label("loc_6565")


    ChrTalk(
        0x101,
        (
            "#00006F...S-Sorry. \x01",
            "Now is a little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I see... Too bad, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "If by chance you get free, \x01",
            "it'd be great if you could help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 3)
    Jump("loc_65F8")

    label("loc_65F8")

    Return()

    # Function_30_6501 end

    def Function_31_65F9(): pass

    label("Function_31_65F9")


    ChrTalk(
        0x101,
        "#00000FYes, we accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Alright! Then, let me explain\x01",
            "the support request content.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You all are aware that we are\x01",
            "holding a charity event in\x01",
            "the City Meeting Hall today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We have a piano performance\x01",
            "and buffet lined up already.\x01",
            "There's just one problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FAnd that is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You see, I had planned\x01",
            "a special program\x01",
            "afterwards, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The participants haven't shown up,\x01",
            "and the program can't move forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FI remember reading that in your request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSo, what is this\x01",
            "program, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "It's the "Miss Crossbell Contest\x01",
            "-Working Women Forever-".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012FS-So, a pageant,\x01",
            "then. Right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FWow, lookin' forward to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FThat subtitle cheapness\x01",
            "really bothers me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "It's a pageant directed\x01",
            "at Crossbell's working\x01",
            "women, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "But... Hardly any of the\x01",
            "participants have shown up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Three people agreed\x01",
            "to participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The program can't proceed\x01",
            "like this. We're talking\x01",
            "cancellation here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FHmm, I could see why a lot\x01",
            "of people would be hesitant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, I think I\x01",
            "understand the problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "It's just like you're thinking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I want all of you to scout\x01",
            ""working women" who will\x01",
            "participate in the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see... I understand the\x01",
            "basics of your request.\x02\x03",
            "#00000FBy the way, you said there\x01",
            "were three participants...\x01",
            "Who are they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Let's see, the first is Miss Cynthia,\x01",
            "a department store receptionist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Next is Miss Iris, \x01",
            "a Back Street hostess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Finally, I got the OK\x01",
            "from officer Kate\x01",
            "of Crossbell Police.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012FEven senior Kate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FA receptionist, a hostess and a policewoman.\x01",
            "Hu hu, that's a nice variety.\x02\x03",
            "#10302FWhat other sorts of occupations\x01",
            "were you looking for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Hmm, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "A "waitress", a "craftsman", \x01",
            "a "maid" and a "Sister"...\x01",
            "I'm looking for these four types.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I think this set of\x01",
            "occupations will\x01",
            "give a good balance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Ideally, I'd like a nurse\x01",
            "or Arc-en-ciel member to\x01",
            "participate as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI think it is impossible.\x01",
            "Arc-en-ciel, with the recent\x01",
            "Miss Ilya incident, is right out.\x02\x03",
            "And St. Ursula Hospital has their\x01",
            "hands full dealing with patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FRight...\x02\x03",
            "#00000FAnyway, we have the general idea.\x02\x03",
            "We'll go find a "waitress", \x01",
            ""craftman", "maid" and\x01",
            "a "Sister" for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "After you've gathered enough\x01",
            "participants, we'll start\x01",
            "the event ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I'm counting on you!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Charity Event Assistance]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x198, 4)
    OP_29(0x8F, 0x1, 0x0)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0x14, 0x5A, 0x0)
    OP_93(0x15, 0x10E, 0x0)
    BeginChrThread(0x14, 0, 0, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1750, 0, 4000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_65F9 end

    def Function_32_708C(): pass

    label("Function_32_708C")

    EventBegin(0x0)
    Fade(500)
    OP_68(1560, 1500, 3500, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 1810, 0, 3530, 0)
    SetChrPos(0x102, 620, 0, 3130, 0)
    SetChrPos(0x104, 1610, 0, 2310, 0)
    SetChrPos(0x103, 2860, 0, 2990, 0)
    SetChrPos(0x105, 2700, 0, 1650, 0)
    SetChrPos(0x109, 570, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_93(0x14, 0xB4, 0x0)
    OP_93(0x15, 0xB4, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_740E")

    ChrTalk(
        0x14,
        "Oh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Did you find pageant participants?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I wanted a "waitress",\x01",
            ""craftman", "maid" and\x01",
            "a "Sister". Those four.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, we managed to find all of them.\x02\x03",
            "The ladies wanted us to contact\x01",
            "them prior to the event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Oh, that's great news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "On our end, the piano concert\x01",
            "is just about to finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Wow, you managed to make it in time! \x01",
            "We'll be able to hold the event after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, thank goodness.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 500)

    ChrTalk(
        0x14,
        (
            "Mmm. You worked\x01",
            "very hard too, Roy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It's so nice to see\x01",
            "my lazy grandson\x01",
            "finally grow up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x14, 500)

    ChrTalk(
        0x15,
        "Tch, what was that?\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)

    ChrTalk(
        0x15,
        (
            "Well anyway, the\x01",
            "pageant is starting.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_73E8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_73E8)

    ChrTalk(
        0x15,
        "Are you guys ready?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7452")

    label("loc_740E")


    ChrTalk(
        0x15,
        (
            "Well anyway, the\x01",
            "pageant is starting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Are you guys ready?\x02",
    )

    CloseMessageWindow()

    label("loc_7452")

    Call(0, 33)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0x14, 0x5A, 0x0)
    OP_93(0x15, 0x10E, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1750, 0, 4000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_32_708C end

    def Function_33_7497(): pass

    label("Function_33_7497")

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
            "Already Prepared\x01",      # 0
            "Not Yet Prepared\x01",      # 1
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
        (0, "loc_7509"),
        (1, "loc_7511"),
        (SWITCH_DEFAULT, "loc_75B0"),
    )


    label("loc_7509")

    Call(0, 34)
    Jump("loc_75B0")

    label("loc_7511")


    ChrTalk(
        0x101,
        (
            "#00006FCan you wait a bit? \x01",
            "We aren't quite ready for this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Hey now, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Then, once you are\x01",
            "ready, come speak to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19A, 0)
    Jump("loc_75B0")

    label("loc_75B0")

    Return()

    # Function_33_7497 end

    def Function_34_75B1(): pass

    label("Function_34_75B1")


    ChrTalk(
        0x101,
        (
            "#00000FYes, all good here.\x02\x03",
            "Then, we'll contact\x01",
            "the participants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Yeah, please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FMan, time for the main\x01",
            "event. I can't wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FThat is all you ever think,\x01",
            "about, Mr. Randy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 500)

    ChrTalk(
        0x14,
        (
            "On my end, I've got to\x01",
            "get the venue ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I'm leaving the\x01",
            "MCing to you, Roy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x14, 500)

    ChrTalk(
        0x15,
        "Sure. Leave it to me, grandpa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FI guess all we can do now is pray to the\x01",
            "Goddess for the success of this event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, this is a good\x01",
            "chance for us to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FYes, I agree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FLet's contact the participants\x01",
            "and then enter the venue.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    StopBGM(0xFA0)
    OP_0D()
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_75B1 end

    def Function_35_7821(): pass

    label("Function_35_7821")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1560, 1500, 3500, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 1810, 0, 3530, 0)
    SetChrPos(0x102, 620, 0, 3130, 0)
    SetChrPos(0x104, 1610, 0, 2310, 0)
    SetChrPos(0x103, 2860, 0, 2990, 0)
    SetChrPos(0x105, 2700, 0, 1650, 0)
    SetChrPos(0x109, 570, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_93(0x14, 0xB4, 0x0)
    OP_93(0x15, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x15,
        (
            "Thanks to your help, the\x01",
            "pageant was a huge success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Thank you for\x01",
            "gathering the\x01",
            "participants for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHa ha, you're welcome.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_7C42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7A76")

    ChrTalk(
        0x102,
        (
            "#00104F*giggle*, I feel like\x01",
            "we enjoyed it too.\x02\x03",
            "#00102FI never expected to win the\x01",
            "special award, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FBecause it's you Miss Elie,\x01",
            "that's the expected result!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FYou were cool.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xE)
    Jump("loc_7C3D")

    label("loc_7A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7B6B")

    ChrTalk(
        0x103,
        (
            "#00204F...It was a lot of\x01",
            "fun for us, too.\x02\x03",
            "#00202FI never expected to win the\x01",
            "special award, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, it's because it's you,\x01",
            "Tio. It was only natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FI know, right?\x01",
            "You were so cute!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xF)
    Jump("loc_7C3D")

    label("loc_7B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7C3D")

    ChrTalk(
        0x109,
        (
            "#10104FWe enjoyed it too.\x02\x03",
            "#10100FI never expected to win\x01",
            "the special award, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FBecause it is you Miss Noｱl, \x01",
            "I think it was to be expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FYou were very cool.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x10)

    label("loc_7C3D")

    Jump("loc_7E89")

    label("loc_7C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7D05")

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, I feel like\x01",
            "we enjoyed it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI thought Miss Elie could have\x01",
            "done better, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FWell, it can't be helped\x01",
            "if we don't have uniforms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E89")

    label("loc_7D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7DCA")

    ChrTalk(
        0x103,
        (
            "#00202F...It was a lot of\x01",
            "fun for us, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FThough I thought you could have\x01",
            "done a little better, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWell, it can't be helped\x01",
            "if we don't have uniforms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E89")

    label("loc_7DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7E89")

    ChrTalk(
        0x109,
        (
            "#10100FWe enjoyed\x01",
            "it a lot too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FThough I thought you could have\x01",
            "done a little better, Miss Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, it can't be helped\x01",
            "if we don't have uniforms.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E89")


    ChrTalk(
        0x14,
        (
            "It seems the citizens had a chance to\x01",
            "relax, and a lot of reconstruction support\x01",
            "funds were collected after the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Today, I can't help but\x01",
            "compliment your idea, Roy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Tch, you're supposed to say\x01",
            ""nice idea!" in this situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "That's right. Since it's\x01",
            "a special occasion, I'll\x01",
            "give you guys this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You guys are winners\x01",
            "too, after all.\x01",
            "Please, take it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_8076")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x76, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_81DD")

    label("loc_8076")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_80D1")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x72, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_81DD")

    label("loc_80D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_812C")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_81DD")

    label("loc_812C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_8187")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x82, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_81DD")

    label("loc_8187")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_81DD")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x66),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x66, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_81DD")


    ChrTalk(
        0x101,
        (
            "#00005FAre you sure?\x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, well you showed\x01",
            "us a good time too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FI hope you hold this kind of event again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, definitely.\x02\x03",
            "#00000F──Alright then, we'll\x01",
            "excuse ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Yeah, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'll be counting on your\x01",
            "help again in the future!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Charity Event Assistance]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8F, 0x1, 0x11)
    OP_29(0x8F, 0x4, 0x10)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0x14, 0x5A, 0x0)
    OP_93(0x15, 0x10E, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1750, 0, 4000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_35_7821 end

    def Function_36_83BE(): pass

    label("Function_36_83BE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell City Meeting Hall\x01",
            "    Reception Office\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_36_83BE end

    def Function_37_8452(): pass

    label("Function_37_8452")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell City Meeting Hall\x01",
            "Multipurpose Communications Room\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8508")

    ChrTalk(
        0x101,
        (
            "#00000FSeems like we've got\x01",
            "no reason to enter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_8508")

    TalkEnd(0xFF)
    Return()

    # Function_37_8452 end

    def Function_38_850C(): pass

    label("Function_38_850C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Saint's Prayer]\x01",
            "Magnus Hector\x01\x01",
            "S1134. A work of Magnus Hector's final years\x01",
            "praising the founding of the autonomous state\x01",
            "of Crossbell. After the former City Hall was built,\x01",
            "it was popular among the citizens for many years\x01",
            "as the symbol of the building itself.\x01",
            "S1204. Following the City Hall transfer,\x01",
            "it was handed over to City Meeting Hall.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_850C end

    def Function_39_86A0(): pass

    label("Function_39_86A0")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Heated arguments can be\x01",
            "heard coming from the hall...\x02\x03",
            "Let's refrain from disturbing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -13650, 4000, 12700, 225)
    EventEnd(0x4)
    Return()

    # Function_39_86A0 end

    SaveToFile()

Try(main)
