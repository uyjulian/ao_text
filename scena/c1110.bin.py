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
        "Function_6_1740",         # 06, 6
        "Function_7_17C3",         # 07, 7
        "Function_8_1823",         # 08, 8
        "Function_9_184B",         # 09, 9
        "Function_10_185E",        # 0A, 10
        "Function_11_1A86",        # 0B, 11
        "Function_12_28B4",        # 0C, 12
        "Function_13_2985",        # 0D, 13
        "Function_14_2C10",        # 0E, 14
        "Function_15_2CDE",        # 0F, 15
        "Function_16_2DA8",        # 10, 16
        "Function_17_2E03",        # 11, 17
        "Function_18_2E4D",        # 12, 18
        "Function_19_2EB6",        # 13, 19
        "Function_20_3407",        # 14, 20
        "Function_21_347D",        # 15, 21
        "Function_22_34CD",        # 16, 22
        "Function_23_353F",        # 17, 23
        "Function_24_3797",        # 18, 24
        "Function_25_3A0E",        # 19, 25
        "Function_26_3A83",        # 1A, 26
        "Function_27_3ABA",        # 1B, 27
        "Function_28_57C5",        # 1C, 28
        "Function_29_5E0B",        # 1D, 29
        "Function_30_6455",        # 1E, 30
        "Function_31_654D",        # 1F, 31
        "Function_32_6F99",        # 20, 32
        "Function_33_739E",        # 21, 33
        "Function_34_7490",        # 22, 34
        "Function_35_76F6",        # 23, 35
        "Function_36_8219",        # 24, 36
        "Function_37_82AD",        # 25, 37
        "Function_38_8361",        # 26, 38
        "Function_39_84F6",        # 27, 39
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A27")

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
            "Other than the minor injuries of 10-odd\x01",
            "citizens who got involved in disturbances,\x01",
            "there's been hardly any injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I arranged for an ambulance\x01",
            "for those needing treatment...\x01",
            "For now, I'm relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AF4")

    label("loc_A27")


    ChrTalk(
        0x8,
        (
            "Other than 10-odd citizens who received\x01",
            "minor injuries under this martial law,\x01",
            "there's been hardly any injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I arranged for an ambulance\x01",
            "for those needing treatment...\x01",
            "For now, I'm relieved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF4")

    Jump("loc_173C")

    label("loc_AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBA")

    ChrTalk(
        0x8,
        (
            "For now, we've accepted\x01",
            "citizens who can't return home\x01",
            "here at City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there's something\x01",
            "bothering you, please don't\x01",
            "hesitate to let me know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C61")

    label("loc_BBA")


    ChrTalk(
        0x8,
        (
            "We have emergency supplies\x01",
            "of food and blankets here at\x01",
            "City Meeting Hall as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there's something\x01",
            "bothering you, please don't\x01",
            "hesitate to let me know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C61")

    Jump("loc_173C")

    label("loc_C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CF3")

    ChrTalk(
        0x8,
        (
            "You can clearly hear the\x01",
            "chants of "hooray" even\x01",
            "from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel like it's a\x01",
            "little scary. I wonder\x01",
            "why that is...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173C")

    label("loc_CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D76")

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
            "participate, please ask\x01",
            "me about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173C")

    label("loc_D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB9")

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
            "I have nothing resembling an answer\x01",
            "regarding the objective of the criminals\x01",
            "or their actions to give them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Many are saying it's an\x01",
            "Imperial plot, but... In the\x01",
            "end, what is the real truth?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F10")

    label("loc_EB9")


    ChrTalk(
        0x8,
        (
            "Many are saying it's an\x01",
            "Imperial plot, but... In the\x01",
            "end, what is the real truth?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F10")

    Jump("loc_173C")

    label("loc_F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FCE")

    ChrTalk(
        0x8,
        (
            "Welcome. In the hall on my left, a\x01",
            "citizen's forum with the theme of\x01",
            "state independence is being held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is open to the\x01",
            "public, so please stop\x01",
            "by, if you like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173C")

    label("loc_FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1053")

    ChrTalk(
        0x8,
        (
            "That's right, the audit\x01",
            "itself can be done\x01",
            "today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm terribly sorry, but\x01",
            "the seats are all\x01",
            "filled...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173C")

    label("loc_1053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10ED")

    ChrTalk(
        0x8,
        (
            "Hello, and welcome to\x01",
            "Crossbell City Meeting\x01",
            "Hall.\x02",
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
    Jump("loc_173C")

    label("loc_10ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_12F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121F")

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
            "To answer them, the city and Crossbell\x01",
            "News are jointly holding a citizen's\x01",
            "forum the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're now fine tuning\x01",
            "things such that everyone\x01",
            "will find the forum useful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12ED")

    label("loc_121F")


    ChrTalk(
        0x8,
        (
            "The day after tomorrow, we're holding a\x01",
            "citizen's forum here at City Meeting Hall\x01",
            "with state independence as the theme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're now fine tuning\x01",
            "things such that everyone\x01",
            "will find the forum useful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12ED")

    Jump("loc_173C")

    label("loc_12F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13B0")

    ChrTalk(
        0x8,
        (
            "I-I'm terribly sorry. I\x01",
            "thought the notice had been\x01",
            "there for a while, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From the standpoint of security\x01",
            "guarantees, it'll never pass\x01",
            "with the average citizens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173C")

    label("loc_13B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1522")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148E")

    ChrTalk(
        0x8,
        (
            "Each country's head of\x01",
            "state has finally come\x01",
            "to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They'll be talking about\x01",
            "various things starting\x01",
            "this afternoon, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder what you all\x01",
            "will do to pass the\x01",
            "time?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_151D")

    label("loc_148E")


    ChrTalk(
        0x8,
        (
            "The heads of state will talking\x01",
            "about various things starting\x01",
            "this afternoon, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder what you all\x01",
            "will do to pass the\x01",
            "time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151D")

    Jump("loc_173C")

    label("loc_1522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_15CB")

    ChrTalk(
        0x8,
        (
            "The City Meeting Hall is\x01",
            "reserved for the duration\x01",
            "of the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because it is near Orchis\x01",
            "Tower, it can be used if\x01",
            "anything happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173C")

    label("loc_15CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1730")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_166E")

    ChrTalk(
        0x8,
        (
            "Everyone, thank you for\x01",
            "your investigation\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We here at City Meeting Hall\x01",
            "look forward to working with\x01",
            "you in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_172B")

    label("loc_166E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_172B")

    ChrTalk(
        0x8,
        (
            "We would like you all to confirm a\x01",
            "total of three suspicious addresses\x01",
            "as well as the previous owners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once you have confirmed\x01",
            "them all, please come\x01",
            "report here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_172B")

    label("loc_172B")

    Jump("loc_173C")

    label("loc_1730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_173C")
    Call(0, 10)

    label("loc_173C")

    TalkEnd(0x8)
    Return()

    # Function_5_897 end

    def Function_6_1740(): pass

    label("Function_6_1740")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_17BF")

    ChrTalk(
        0xFE,
        (
            "I hope we find some good\x01",
            "property.\x02",
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

    label("loc_17BF")

    TalkEnd(0xFE)
    Return()

    # Function_6_1740 end

    def Function_7_17C3(): pass

    label("Function_7_17C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_181F")

    ChrTalk(
        0xFE,
        "It's all right, mom.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure dad will find a\x01",
            "great apartment for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181F")

    TalkEnd(0xFE)
    Return()

    # Function_7_17C3 end

    def Function_8_1823(): pass

    label("Function_8_1823")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1847")

    ChrTalk(
        0xFE,
        "Nyaon. [I'm tired]\x02",
    )

    CloseMessageWindow()

    label("loc_1847")

    TalkEnd(0xFE)
    Return()

    # Function_8_1823 end

    def Function_9_184B(): pass

    label("Function_9_184B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_185A")
    Call(0, 10)

    label("loc_185A")

    TalkEnd(0xFE)
    Return()

    # Function_9_184B end

    def Function_10_185E(): pass

    label("Function_10_185E")

    OP_4B(0x10, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D2")

    ChrTalk(
        0x10,
        (
            "Yes, I'm looking for a\x01",
            "room that's as cheap as\x01",
            "possible, but...\x02",
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
            "Hmm... Please have a\x01",
            "look at these materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I remember correctly,\x01",
            "the previous resident\x01",
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
    Jump("loc_1A7D")

    label("loc_19D2")


    ChrTalk(
        0x10,
        (
            "Ah, and... Pets have to\x01",
            "be allowed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, I think that's okay\x01",
            "for this particular\x01",
            "property.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Oh, that's great! In\x01",
            "that case, I'd like to\x01",
            "check it out ASAP...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7D")

    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_10_185E end

    def Function_11_1A86(): pass

    label("Function_11_1A86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB3")

    ChrTalk(
        0xFE,
        (
            "We're now preparing a place to\x01",
            "give a formal explanation to the\x01",
            "citizens regarding this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Later, I want to give the citizens\x01",
            "an official explanation regarding\x01",
            "what may happen in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's chaos\x01",
            "everywhere. I've got to\x01",
            "hurry and get ready.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C5A")

    label("loc_1BB3")


    ChrTalk(
        0xFE,
        (
            "We're now preparing a place to\x01",
            "give a formal explanation to the\x01",
            "citizens regarding this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's chaos\x01",
            "everywhere. I've got to\x01",
            "hurry and get ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5A")

    Jump("loc_28B0")

    label("loc_1C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1E5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9A")

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
            "But even so, a situation like\x01",
            "this... There are probably a lot of\x01",
            "people who are unprepared for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...While waiting for a conclusion,\x01",
            "we must once again confirm the\x01",
            "safety of the citizens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E55")

    label("loc_1D9A")


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
            "...While waiting for a conclusion,\x01",
            "we must once again confirm the\x01",
            "safety of the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E55")

    Jump("loc_28B0")

    label("loc_1E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2E")

    ChrTalk(
        0xFE,
        (
            "Crossbell independence,\x01",
            "and the President's\x01",
            "inauguration, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given these, our\x01",
            "organizational structure\x01",
            "will likely change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things are getting more\x01",
            "tense, day by day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FA1")

    label("loc_1F2E")


    ChrTalk(
        0xFE,
        (
            "Given these, our\x01",
            "organizational structure\x01",
            "will likely change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things are getting more\x01",
            "tense, day by day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA1")

    Jump("loc_28B0")

    label("loc_1FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1FE7")

    ChrTalk(
        0xFE,
        (
            "Come now, please enjoy\x01",
            "today's charity event.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B0")

    label("loc_1FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_21ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214D")

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
            "Somehow, it seems like there\x01",
            "a lot of things we're not\x01",
            "seeing, and I'm worried.\x02",
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
        (
            "We've got to hold\x01",
            "ourselves together,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21E8")

    label("loc_214D")


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
        (
            "We've got to hold\x01",
            "ourselves together,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E8")

    Jump("loc_28B0")

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_228F")

    ChrTalk(
        0xFE,
        (
            "The citizen's forum\x01",
            "we're now holding is\x01",
            "proceeding smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that things continue\x01",
            "like this and no particular\x01",
            "disturbances occur.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B0")

    label("loc_228F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_22DB")

    ChrTalk(
        0xFE,
        (
            "Hmm, I want to get good\x01",
            "at operating a keyboard\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B0")

    label("loc_22DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E5")

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
            "Mastering something new\x01",
            "at my age is a bit of a\x01",
            "challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The input device called\x01",
            "a keyboard in particular\x01",
            "is a formidable enemy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2493")

    label("loc_23E5")


    ChrTalk(
        0xFE,
        (
            "In addition, I get eye\x01",
            "strain when I look at the\x01",
            "display no matter what I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always knew paper was... Well\x01",
            "if I say things like this, I'll\x01",
            "get left behind, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2493")

    Jump("loc_28B0")

    label("loc_2498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_25A1")

    ChrTalk(
        0xFE,
        (
            "I feel like our workload has\x01",
            "doubled ever since this was\x01",
            "redesignated the City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the citizens' forum, there's preparations for\x01",
            "the referendum to attend to... Lately, I've been\x01",
            "feeling like all of this is reaching a climax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B0")

    label("loc_25A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_25EC")

    ChrTalk(
        0xFE,
        (
            "Umm, as she said,\x01",
            "security is the number\x01",
            "one problem...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B0")

    label("loc_25EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2693")

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
            "City Hall was finally\x01",
            "relocated. The reality of\x01",
            "it is finally setting in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B0")

    label("loc_2693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_272B")

    ChrTalk(
        0xFE,
        (
            "Yes, the resident registration\x01",
            "office hasn't moved. We still\x01",
            "handle that here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please ask about it at\x01",
            "the reception desk on\x01",
            "1F.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B0")

    label("loc_272B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_27E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274B")
    Call(0, 13)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_27E0")

    label("loc_274B")


    ChrTalk(
        0xFE,
        (
            "It seems the reason for\x01",
            "today's cancellation was\x01",
            "mainly due the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, if we set a\x01",
            "cancellation fee, maybe\x01",
            "this wouldn't be a problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E0")

    Jump("loc_28B0")

    label("loc_27E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_28B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2808")
    Call(0, 12)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_28B0")

    label("loc_2808")


    ChrTalk(
        0xFE,
        (
            "*sigh*, it seems all the relocation\x01",
            "paperwork has been given to General\x01",
            "Affairs Section Two.\x02",
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

    label("loc_28B0")

    TalkEnd(0xFE)
    Return()

    # Function_11_1A86 end

    def Function_12_28B4(): pass

    label("Function_12_28B4")

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
            "Yeah, there's no mistake.\x01",
            "Please take care of the\x01",
            "delivery, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, please leave it to\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_28B4 end

    def Function_13_2985(): pass

    label("Function_13_2985")

    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "It'll be time to start the\x01",
            "seminar soon, but... Shall I\x01",
            "postpone the program a bit?\x02",
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
            "But to think they\x01",
            "cancelled... This is why I\x01",
            "hate working with amateurs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because of things like this, the\x01",
            "business chance I was thinking\x01",
            "of seizing was a big mistake.\x02",
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
            "A-Anyway, I'll wait just\x01",
            "a little while longer.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BFA")

    ChrTalk(
        0x102,
        (
            "#00105F(Hey Lloyd. Could he\x01",
            "be...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Yeah. He's one of those\x01",
            "Gnosis patients from the\x01",
            "cult incident.)\x02\x03",
            "#00000F(It looks like he has it\x01",
            "tough, but I'm glad he's\x01",
            "all right.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BFA")

    SetScenarioFlags(0x12E, 5)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_13_2985 end

    def Function_14_2C10(): pass

    label("Function_14_2C10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C33")
    Call(0, 12)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2CDA")

    label("loc_2C33")


    ChrTalk(
        0xFE,
        (
            "Umm, this belongs to General\x01",
            "Affairs Section One, and this\x01",
            "belongs to the Finance Division...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The new City Hall is\x01",
            "close by, so these will\x01",
            "be there shortly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDA")

    TalkEnd(0xFE)
    Return()

    # Function_14_2C10 end

    def Function_15_2CDE(): pass

    label("Function_15_2CDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D01")
    Call(0, 13)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_2DA4")

    label("loc_2D01")


    ChrTalk(
        0xFE,
        (
            "Hmm. Even if I collect participation\x01",
            "fees, it won't even cover half of\x01",
            "the hall reservation fee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to get some new\x01",
            "capital no matter what,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA4")

    TalkEnd(0xFE)
    Return()

    # Function_15_2CDE end

    def Function_16_2DA8(): pass

    label("Function_16_2DA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2DFF")

    ChrTalk(
        0xFE,
        (
            "Umm, I'm here to ask about\x01",
            "the citizen registration\x01",
            "procedure, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFF")

    TalkEnd(0xFE)
    Return()

    # Function_16_2DA8 end

    def Function_17_2E03(): pass

    label("Function_17_2E03")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm worried about my mom\x01",
            "who works at the\x01",
            "department store...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2E03 end

    def Function_18_2E4D(): pass

    label("Function_18_2E4D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm... What is this?\x01",
            "Surely this situation\x01",
            "is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President Dieter... I\x01",
            "believed in him.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2E4D end

    def Function_19_2EB6(): pass

    label("Function_19_2EB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_32B9")

    ChrTalk(
        0xFE,
        (
            "My, you all are...\x01",
            "You're those police if I\x01",
            "recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You helped me back\x01",
            "there, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FDA")

    ChrTalk(
        0x101,
        (
            "#00005FAh... Could you be Vice\x01",
            "Chief Pierre's wife?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, it's been a while,\x01",
            "madame. Are you sheltering\x01",
            "here at City Meeting Hall?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3050")

    label("loc_2FDA")


    ChrTalk(
        0x101,
        (
            "#00005FAh... Could you be Vice\x01",
            "Chief Pierre's wife?\x02\x03",
            "#00001FUmm... Are you\x01",
            "sheltering here at City\x01",
            "Meeting Hall?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3050")


    ChrTalk(
        0xFE,
        (
            "Yes, that's right,\x01",
            "but... Umm, have you\x01",
            "seen my husband?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He hasn't returned since\x01",
            "he said he was going to\x01",
            "Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FNo, we haven't...\x02\x03",
            "What is the vice chief\x01",
            "doing at Orchis Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heck if I know... I\x01",
            "didn't even ask him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. For him to\x01",
            "needlessly worry me at a\x01",
            "time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to give him a\x01",
            "severe scolding when he\x01",
            "gets back.\x02",
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
            "#00000F...For now, please wait\x01",
            "here.\x02\x03",
            "He might suddenly\x01",
            "return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yes, I'll do so.\x01",
            "Please contact me if you\x01",
            "see him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3377")

    label("loc_32B9")


    ChrTalk(
        0xFE,
        (
            "My husband went to\x01",
            "Orchis Tower and hasn't\x01",
            "returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. For him to\x01",
            "needlessly worry me at a\x01",
            "time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to give him a\x01",
            "severe scolding when he\x01",
            "gets back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3377")

    SetScenarioFlags(0x1CC, 2)
    Jump("loc_3403")

    label("loc_337F")


    ChrTalk(
        0xFE,
        (
            "Goodness. For him to\x01",
            "needlessly worry me at a\x01",
            "time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to give him a\x01",
            "severe scolding when he\x01",
            "gets back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3403")

    TalkEnd(0xFE)
    Return()

    # Function_19_2EB6 end

    def Function_20_3407(): pass

    label("Function_20_3407")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3479")

    ChrTalk(
        0xFE,
        (
            "Hey, can we go to Orchis\x01",
            "Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can we come and go\x01",
            "freely at least from\x01",
            "Orchis Tower plaza?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3479")

    TalkEnd(0xFE)
    Return()

    # Function_20_3407 end

    def Function_21_347D(): pass

    label("Function_21_347D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34C9")

    ChrTalk(
        0xFE,
        (
            "Yeah, yeah! I was told\x01",
            "that, but I haven't\x01",
            "heard anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C9")

    TalkEnd(0xFE)
    Return()

    # Function_21_347D end

    def Function_22_34CD(): pass

    label("Function_22_34CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_353B")

    ChrTalk(
        0xFE,
        (
            "I want to participate in tomorrow's\x01",
            "citizen's forum... I wonder if\x01",
            "there are any open seats.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_353B")

    TalkEnd(0xFE)
    Return()

    # Function_22_34CD end

    def Function_23_353F(): pass

    label("Function_23_353F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3587")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3579")
    Call(0, 32)
    Return()

    label("loc_3579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3587")
    Call(0, 29)
    Return()

    label("loc_3587")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3661")

    ChrTalk(
        0xFE,
        (
            "Sorry, everyone. Roy\x01",
            "wasted your time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we can hold the pageant,\x01",
            "it'll be a good way for the\x01",
            "citizens to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please do your best\x01",
            "searching for\x01",
            "participants.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_36E6")

    label("loc_3661")


    ChrTalk(
        0xFE,
        (
            "If we can hold the pageant,\x01",
            "it'll be a good way for the\x01",
            "citizens to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please do your best\x01",
            "searching for\x01",
            "participants.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E6")

    Jump("loc_3793")

    label("loc_36EB")


    ChrTalk(
        0xFE,
        (
            "The citizens were able to relax\x01",
            "too. Also, we got a lot of\x01",
            "donations after the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although the pageant was\x01",
            "Roy's idea... Haha, it\x01",
            "turned out all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3793")

    TalkEnd(0xFE)
    Return()

    # Function_23_353F end

    def Function_24_3797(): pass

    label("Function_24_3797")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37D1")
    Call(0, 32)
    Return()

    label("loc_37D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37DF")
    Call(0, 29)
    Return()

    label("loc_37DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_399A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3907")

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
            "A waitress, a worker, a maid\x01",
            "and a sister... Those are\x01",
            "the four I'm looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I think this set of\x01",
            "occupations will give a\x01",
            "good balance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "We're counting on you!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3995")

    label("loc_3907")


    ChrTalk(
        0x15,
        (
            "A waitress, worker,\x01",
            "maid, and sister...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I want you to scout\x01",
            ""working girls" of those\x01",
            "four types for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "We're counting on you!\x02",
    )

    CloseMessageWindow()

    label("loc_3995")

    Jump("loc_3A0A")

    label("loc_399A")


    ChrTalk(
        0x15,
        (
            "Thanks to your help, the\x01",
            "pageant was a huge\x01",
            "success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Thank you for gathering\x01",
            "the participants for me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0A")

    TalkEnd(0xFE)
    Return()

    # Function_24_3797 end

    def Function_25_3A0E(): pass

    label("Function_25_3A0E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This address in Downtown\x01",
            "is my dad's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is great, Aerie! We\x01",
            "just have to go there to\x01",
            "meet him.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_3A0E end

    def Function_26_3A83(): pass

    label("Function_26_3A83")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Haha, we finally found\x01",
            "his location, Alm㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_3A83 end

    def Function_27_3ABA(): pass

    label("Function_27_3ABA")

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
            "Hello, and welcome to\x01",
            "Crossbell City Meeting\x01",
            "Hall.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, thank you for\x01",
            "coming, members of the\x01",
            "SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FGood afternoon. We're\x01",
            "here for the request.\x02",
        )
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
        (
            "#12P#10100FPleased to make your\x01",
            "acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, nice to meet both\x01",
            "of you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FCity Meeting Hall, huh?\x01",
            "The name has a weird\x01",
            "ring to it.\x02",
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
            "#00104FHaha, well the new City\x01",
            "Hall will be in the new\x01",
            "building.\x02\x03",
            "#00100FFor now, this place is\x01",
            "still functioning as a\x01",
            ""branch office".\x02\x03",
            "So in that sense it'll\x01",
            "be just as useful for\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FI see. So that's what's\x01",
            "going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. And this reception counter will\x01",
            "continue to serve as a point of\x01",
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
            "I'm sorry, that isn't\x01",
            "why you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo problem. It sounds\x01",
            "like you have your work\x01",
            "cut out for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha, the things government officials\x01",
            "think up sure are boring.\x02\x03",
            "If it were me, I would have made it an\x01",
            ""adult hall" near the Entertainment\x01",
            "District.\x02\x03",
            "#10309FA nightclub to entertain public\x01",
            "servants... It goes without saying that\x01",
            "SSS would be even more popular than we\x01",
            "are now if there was such a thing.\x02",
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
            "#12P#00006FWe would most certainly not.\x02\x03",
            "#00001FI mean, from the very start that\x01",
            "kind of "night work" is\x01",
            "unthinkable for public servants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FAhaha... (I can't get it\x01",
            "out of my head.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FAhem. Anyway, can we get\x01",
            "back on topic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00011FO-Oh, that's right.\x02\x03",
            "#00000FSorry about that. About\x01",
            "that support request\x01",
            "then...\x02",
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
            "─I'm sure you're all\x01",
            "aware of "Residence\x01",
            "Change Notices".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They're submitted at the\x01",
            "time of residence\x01",
            "change, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Recently, we found\x01",
            "suspicious names on some\x01",
            "of the forms.\x02",
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
            "not registered with the\x01",
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
            "And just to be safe, I'd\x01",
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
            "#00003FWe can't ignore any crime-related\x01",
            "activities that might be\x01",
            "occurring.\x02\x03",
            "#00000FAnd we'll report all of what we\x01",
            "find back to you then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYes, that's the gist of\x01",
            "it.\x02\x03",
            "#00100FIt's only natural that\x01",
            "you'd have a list of\x01",
            "suspicious addresses...\x02\x03",
            "But do you have any idea\x01",
            "of the whereabouts of\x01",
            "the previous residents?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, we only know the\x01",
            "location of one of the\x01",
            "people who moved.\x02",
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
            "#12P#10300FI see. So an\x01",
            "investigation is needed,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FBut first, we'll need to go to\x01",
            "each address to verify who lives\x01",
            "there.\x02\x03",
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
            "#00000FDo you have the list of\x01",
            "places?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, I have duplicate\x01",
            "report ready for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FAlright, we'll hang on\x01",
            "to this.\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x258, 0x3E8, 0x0)
    Sleep(800)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_97(0x101, 0x0, 0x0, 0xFFFFFDA8, 0x3E8, 0x0)
    Sleep(50)

    def lambda_4979():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4979)

    def lambda_4986():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4986)

    def lambda_4993():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4993)

    def lambda_49A0():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_49A0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00000FHmm, so it looks like\x01",
            "there are a total of\x01",
            "three places of interest.\x02\x03",
            "First is a place near\x01",
            "Elie's house in\x01",
            "Residential District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FLet's see... Oh that's\x01",
            "next to my parents'\x01",
            "house.\x02\x03",
            "#00105FThe Highbloods are the\x01",
            "residents. ...Is it the\x01",
            "name of some company?\x02\x03",
            "#00103FThe family of Mr. Bond,\x01",
            "an investor, should be\x01",
            "living there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FYeah, he's recorded on\x01",
            "the list as the previous\x01",
            "resident.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5P#00003FAn investor named Bond...\x02\x03",
            "#00001FIf I remember correctly,\x01",
            "he was one of the victims\x01",
            "in the Gnosis incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FYes, I'm certain he was.\x02\x03",
            "#00108FI heard various things\x01",
            "happened to his family members\x01",
            "after the incident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FYou think they got\x01",
            "caught up in some\x01",
            "trouble because of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FI don't know... But Mr.\x01",
            "Bond did submit a\x01",
            "residence change notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FThe next one is on East\x01",
            "Street, on the second floor\x01",
            "of Acacia Apartments.\x02\x03",
            "Oh yeah, that's the place\x01",
            "just to the left of the\x01",
            "Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FResidential District and East\x01",
            "Street... We've got to make sure\x01",
            "to investigate both of them.\x02\x03",
            "#00001FAnd the next address is also on\x01",
            "East Street... The Fisherman's'\x01",
            "Guild...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00011F─Wait... What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FW-what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00008FWell, the form says the\x01",
            "current resident is the\x01",
            "Imperial Fishing Club, but...\x02\x03",
            "I don't think I've ever heard\x01",
            "that name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00105FYou were a member of the\x01",
            "Fisherman's Guild,\x01",
            "right?\x02\x03",
            "Have you heard anything\x01",
            "from the other members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FW-Well, I've been busy lately and haven't had\x01",
            "time for fishing.\x02\x03",
            "#00001FAnd we don't know the location of the\x01",
            "Fisherman's Guild, the previous resident,\x01",
            "either... Could they have changed their name?\x02\x03",
            "#00003F...Anyway, we'll need to investigate this,\x01",
            "too.\x02\x03",
            "#00001FThe last address is on Lotus Heights 1F in\x01",
            "Downtown.\x02\x03",
            "Geithner was the previous resident. I'm not\x01",
            "surprised he's gone missing.\x02\x03",
            "And the current resident is... Sean Alnam.\x02\x03",
            "#00005F...The name kind of sounds familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHehe, he's the famous\x01",
            "fairy tale author,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00011FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FHe wrote "Mark and the Witch of\x01",
            "the Deep Forest". It's one of the\x01",
            "most popular books at the library.\x02\x03",
            "#00100FYou should remember it too, Lloyd.\x01",
            "Remember when we raided the\x01",
            "Revache hideout?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00005FYeah, now that you mention\x01",
            "it... It was the password to\x01",
            "unlock a door there, wasn't it.\x02\x03",
            "#00008FBut I can't believe an author\x01",
            "that famous would choose to\x01",
            "live in Downtown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FYes, well for starters,\x01",
            "Mr. Alnam is already\x01",
            "dead.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006FY-You don't say... I'm\x01",
            "getting a bad feeling\x01",
            "about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe. All of that aside, it would have\x01",
            "been better if you noticed when accepting\x01",
            "these residence change notices, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "I-I'm so sorry to push\x01",
            "this on you all.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5514():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5514)
    Sleep(50)

    def lambda_5524():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5524)
    Sleep(50)

    def lambda_5534():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5534)
    Sleep(50)

    def lambda_5544():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5544)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "We'll try to be more\x01",
            "careful in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FOh, don't worry about it... This must\x01",
            "be a busy time for City Hall staff with\x01",
            "the new mayor and control transfer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FYes. The citizens who\x01",
            "submitted the faulty notices\x01",
            "are the ones to blame here!\x02",
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
            "#00100FWe'll give you our\x01",
            "report once we've\x01",
            "confirmed them all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright, I'm counting on\x01",
            "you.\x02",
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
            "Quest [Suspicious\x01",
            "Suspicious Housing Units\x01",
            "Investigation]\x07\x00",
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

    # Function_27_3ABA end

    def Function_28_57C5(): pass

    label("Function_28_57C5")

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
            "of the suspicious\x01",
            "addresses going, everyone?\x02",
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
            "Handed over the duplicate\x01",
            "report with corrected\x01",
            "resident names.\x02",
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
            "moved in to Residential District and\x01",
            "Imperials have moved in to East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PAnd as for Downtown...\x01",
            "Huh?\x02",
        )
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
            "#12P#1PNo, I just didn't expect\x01",
            "to see Geval's name\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PI've seen him here a few\x01",
            "times so I thought he\x01",
            "was doing ok.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PI'm not sure how to say this, but\x01",
            "even though he's done bad things,\x01",
            "I can't bring myself to hate him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FYes, I know the feeling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FHe seems easy to read\x01",
            "whether in a good or bad\x01",
            "mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHaha, if he was a little\x01",
            "more upstanding,\x01",
            "everyone would love him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, I guess that's\x01",
            "true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, that's all I\x01",
            "needed for this\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All that's left is for the Citizens\x01",
            "Division personnel to do the\x01",
            "paperwork to sort out this mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thank you so much for\x01",
            "your help today.\x02",
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
            "Quest [Suspicious Housing\x01",
            "Units Investigation]\x07\x00\x01",
            "completed!\x02",
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

    # Function_28_57C5 end

    def Function_29_5E0B(): pass

    label("Function_29_5E0B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F8")
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
        (
            "Mmm... So they're not\x01",
            "coming after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Say, Roy. How about\x01",
            "giving up on this\x01",
            "program.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "What are you saying!?\x02",
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
            "If we don't do it, just\x01",
            "what WILL we do!?\x02",
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
            "#00000FExcuse me. I'm terribly\x01",
            "sorry for interrupting,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_605D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_605D)
    Sleep(50)
    OP_93(0x15, 0xB4, 0x1F4)

    ChrTalk(
        0x15,
        "You guys are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Oh, so you came for us\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Are you here for today's\x01",
            "charity event?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm, if I'm not mistaken, the\x01",
            "Merchants Association requested our\x01",
            "help with the charity event, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "Huh? I don't remember\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "─I was the one who\x01",
            "submitted the request.\x02",
        )
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
            "W-What? Just when did\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Haha, I did it secretly,\x01",
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

    def lambda_62D4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_62D4)

    ChrTalk(
        0x15,
        "Do you have time?\x02",
    )

    CloseMessageWindow()
    Jump("loc_640A")

    label("loc_62F8")

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
            "explaining the job,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Do you have time?\x02",
    )

    CloseMessageWindow()

    label("loc_640A")

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

    # Function_29_5E0B end

    def Function_30_6455(): pass

    label("Function_30_6455")

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
            "Cancel\x01",      # 1
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
        (0, "loc_64B3"),
        (1, "loc_64BB"),
        (SWITCH_DEFAULT, "loc_654C"),
    )


    label("loc_64B3")

    Call(0, 31)
    Jump("loc_654C")

    label("loc_64BB")


    ChrTalk(
        0x101,
        (
            "#00006F...S-Sorry. Now is a\x01",
            "little...\x02",
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
            "If by chance you get\x01",
            "free, it'd be great if\x01",
            "you could help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 3)
    Jump("loc_654C")

    label("loc_654C")

    Return()

    # Function_30_6455 end

    def Function_31_654D(): pass

    label("Function_31_654D")


    ChrTalk(
        0x101,
        "#00000FYes, we accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Alright! Then, let me\x01",
            "explain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You all are aware that we're\x01",
            "holding a charity event at\x01",
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
            "You see, I had planned a\x01",
            "special program\x01",
            "afterwards...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "But the participants\x01",
            "haven't shown up, and the\x01",
            "program can't move forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FI remember reading that\x01",
            "in your request.\x02",
        )
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
            "It's the "Miss Crossbell\x01",
            "Contest ~Working Women\x01",
            "Forever~".\x02",
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
        "#00012FSo, a pageant, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FWow, sounds great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FThat subtitle sounds\x01",
            "really cheap, though.\x02",
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
            "participants have shown\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Three people agreed to\x01",
            "participate.\x02",
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
            "#00106FHmm, I could see why a\x01",
            "lot of people would be\x01",
            "hesitant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, I think I\x01",
            "understand the problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "It's just like you're\x01",
            "thinking.\x02",
        )
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
            "Let's see, the first is\x01",
            "Cynthia, the department\x01",
            "store receptionist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Next is Iris, a Back\x01",
            "Street hostess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Finally, I got the OK\x01",
            "from Officer Kate of\x01",
            "Crossbell Police.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012FEven Officer Kate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FA receptionist, a hostess\x01",
            "and a policewoman. That's\x01",
            "a nice variety.\x02\x03",
            "#10302FWhat other sorts of\x01",
            "occupations were you\x01",
            "looking for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Hmm, let's see, that\x01",
            "person was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "A waitress, a worker, a maid\x01",
            "and a sister... Those are\x01",
            "the four I'm looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I think this set of\x01",
            "occupations will give a\x01",
            "good balance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Ideally, I'd like a nurse\x01",
            "or Arc-en-Ciel artist to\x01",
            "participate as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIt can't be helped. Arc-\x01",
            "en-Ciel, with their recent\x01",
            "incident, is right out.\x02\x03",
            "And St. Ursula Hospital\x01",
            "has their hands full\x01",
            "dealing with patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FRight...\x02\x03",
            "#00000FAnyway, we have the\x01",
            "general idea.\x02\x03",
            "We'll go find a\x01",
            "waitress, worker, maid,\x01",
            "and sister for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "After you've gathered enough\x01",
            "participants, we'll start\x01",
            "the event immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "We're counting on you!\x02",
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
            "Quest [Charity Event\x01",
            "Assistance]\x07\x00",
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

    # Function_31_654D end

    def Function_32_6F99(): pass

    label("Function_32_6F99")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7316")

    ChrTalk(
        0x14,
        "Oh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Did you find the pageant\x01",
            "participants?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I wanted a waitress,\x01",
            "mechanic, maid and\x01",
            "sister. Those four.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, we managed to find\x01",
            "all of them.\x02\x03",
            "The ladies wanted us to\x01",
            "contact them prior to\x01",
            "the event.\x02",
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
            "On our end, the piano\x01",
            "concert is just about to\x01",
            "finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Wow, you managed to make it\x01",
            "in time! We'll be able to\x01",
            "hold the event after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHaha, thank goodness.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 500)

    ChrTalk(
        0x14,
        (
            "Mmm. You've got to work\x01",
            "hard now too, Roy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It's so nice to see my\x01",
            "lazy grandson finally\x01",
            "grow up.\x02",
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
            "Well anyway, I'll begin\x01",
            "the pageant.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_72F0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_72F0)

    ChrTalk(
        0x15,
        "Are you guys ready?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7359")

    label("loc_7316")


    ChrTalk(
        0x15,
        (
            "Well anyway, I'll begin\x01",
            "the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Are you guys ready?\x02",
    )

    CloseMessageWindow()

    label("loc_7359")

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

    # Function_32_6F99 end

    def Function_33_739E(): pass

    label("Function_33_739E")

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
            "Ready\x01",        # 0
            "Not yet\x01",      # 1
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
        (0, "loc_73FC"),
        (1, "loc_7404"),
        (SWITCH_DEFAULT, "loc_748F"),
    )


    label("loc_73FC")

    Call(0, 34)
    Jump("loc_748F")

    label("loc_7404")


    ChrTalk(
        0x101,
        (
            "#00006FCan you wait a bit? I'm\x01",
            "not quite ready for\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Hey, take your time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Come speak to me once\x01",
            "you're ready.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19A, 0)
    Jump("loc_748F")

    label("loc_748F")

    Return()

    # Function_33_739E end

    def Function_34_7490(): pass

    label("Function_34_7490")


    ChrTalk(
        0x101,
        (
            "#00000FYes, all good here.\x02\x03",
            "Then, we'll contact the\x01",
            "participants.\x02",
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
            "#00211FThat's all you ever\x01",
            "think about, Randy.\x02",
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
            "I'm leaving the MCing to\x01",
            "you, Roy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x14, 500)

    ChrTalk(
        0x15,
        (
            "Sure. Leave it to me,\x01",
            "grandpa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FI guess all we can do now\x01",
            "is pray to the Goddess for\x01",
            "the success of this event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha, this is a good\x01",
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
            "#00002FLet's contact the\x01",
            "participants and then\x01",
            "enter the venue.\x02",
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

    # Function_34_7490 end

    def Function_35_76F6(): pass

    label("Function_35_76F6")

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
            "pageant was a huge\x01",
            "success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Thank you for gathering\x01",
            "the participants for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYou're welcome.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_7AF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7935")

    ChrTalk(
        0x102,
        (
            "#00104FI feel like we enjoyed\x01",
            "it too.\x02\x03",
            "#00102FI never expected to win\x01",
            "the special award,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FBecause it's you Elie,\x01",
            "that's the expected\x01",
            "result!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FYou were cool.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xE)
    Jump("loc_7AF0")

    label("loc_7935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7A20")

    ChrTalk(
        0x103,
        (
            "#00204F...It was a lot of fun\x01",
            "for us, too.\x02\x03",
            "#00202FI can't believe you had\x01",
            "a special award just for\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FIt's because it's you,\x01",
            "Tio. It was only\x01",
            "natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FI know, right? You were\x01",
            "so cute!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xF)
    Jump("loc_7AF0")

    label("loc_7A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7AF0")

    ChrTalk(
        0x109,
        (
            "#10104FWe enjoyed it too.\x02\x03",
            "#10100FI never expected to win\x01",
            "the special award,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FBecause it's you Noｱl, I\x01",
            "think that's the\x01",
            "expected result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FYou were very cool.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x10)

    label("loc_7AF0")

    Jump("loc_7D1E")

    label("loc_7AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7BA9")

    ChrTalk(
        0x102,
        (
            "#00102FI feel like we enjoyed\x01",
            "it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI thought Elie could\x01",
            "have done better,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FWell, it can't be helped\x01",
            "if we don't have\x01",
            "uniforms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D1E")

    label("loc_7BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7C6E")

    ChrTalk(
        0x103,
        (
            "#00202F...It was a lot of fun\x01",
            "for us, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FThough I thought you\x01",
            "could have done a little\x01",
            "better, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWell, it can't be helped\x01",
            "if we don't have\x01",
            "uniforms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D1E")

    label("loc_7C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7D1E")

    ChrTalk(
        0x109,
        "#10100FWe enjoyed it too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FThough I thought you\x01",
            "could have done a little\x01",
            "better, Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha, it can't be helped\x01",
            "if we don't have\x01",
            "uniforms.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D1E")


    ChrTalk(
        0x14,
        (
            "The citizens were able to relax\x01",
            "too. Also, we got a lot of\x01",
            "donations after the pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I can't help but admire\x01",
            "your idea, Roy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Tch, you're supposed to\x01",
            "say "nice idea!" in this\x01",
            "situation.\x02",
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
            "too, after all. Please,\x01",
            "take it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_7EDF")
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
    Jump("loc_8046")

    label("loc_7EDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_7F3A")
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
    Jump("loc_8046")

    label("loc_7F3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_7F95")
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
    Jump("loc_8046")

    label("loc_7F95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_7FF0")
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
    Jump("loc_8046")

    label("loc_7FF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_8046")
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

    label("loc_8046")


    ChrTalk(
        0x101,
        (
            "#00005FAre you sure? Thank you\x01",
            "so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FWell, you showed us a\x01",
            "good time too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FI hope you hold this\x01",
            "kind of event again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, definitely.\x02\x03",
            "#00000F─Alright then, we'll\x01",
            "excuse ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Yeah, thanks again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'll be counting on your\x01",
            "help in the future!\x02",
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
            "Quest [Charity Event\x01",
            "Support]\x07\x00",
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

    # Function_35_76F6 end

    def Function_36_8219(): pass

    label("Function_36_8219")

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

    # Function_36_8219 end

    def Function_37_82AD(): pass

    label("Function_37_82AD")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_835D")

    ChrTalk(
        0x101,
        (
            "#00000FIt seems we've no reason\x01",
            "to enter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_835D")

    TalkEnd(0xFF)
    Return()

    # Function_37_82AD end

    def Function_38_8361(): pass

    label("Function_38_8361")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Saint's Prayer\x01",
            "Magnus Hector\x01",
            "S1134. A work of Magnus Hector's final years praising\x01",
            "the founding of the autonomous state of Crossbell.\x01",
            "After the former City Hall was built, it was popular\x01",
            "among the citizens for many years as the symbol of\x01",
            "the building itself. S1204. Following the City Hall\x01",
            "transfer, it was handed over to City Meeting Hall.\x07\x00\x02",
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

    # Function_38_8361 end

    def Function_39_84F6(): pass

    label("Function_39_84F6")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Heated arguments can be\x01",
            "heard coming from the\x01",
            "hall...\x02\x03",
            "Let's refrain from\x01",
            "disturbing them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -13650, 4000, 12700, 225)
    EventEnd(0x4)
    Return()

    # Function_39_84F6 end

    SaveToFile()

Try(main)
