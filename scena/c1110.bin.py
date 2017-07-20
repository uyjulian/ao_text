from ScenarioHelper import *

def main():
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
        "Receptionist Sion",           # 1
        "Clip leader",           # 2
        "A carrier",                 # 3
        "Trade quotient rezero",           # 4
        "Citizen",                   # 5
        "Citizen",                   # 6
        "Citizen",                   # 7
        "Citizen",                   # 8
        "bond",                 # 9
        "Craig",               # 10
        "Sanita",               # 11
        "Mary",                 # 12
        "Mols old man",             # 13
        "Roy",                   # 14
        "Almu",                 # 15
        "Airy",               # 16
        "Mrs. Margaret",       # 17
        "Chroma",                 # 18
        "Otto",               # 19
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
        "Function_6_1647",         # 06, 6
        "Function_7_16C4",         # 07, 7
        "Function_8_1727",         # 08, 8
        "Function_9_1747",         # 09, 9
        "Function_10_175A",        # 0A, 10
        "Function_11_1984",        # 0B, 11
        "Function_12_25F4",        # 0C, 12
        "Function_13_26D1",        # 0D, 13
        "Function_14_291A",        # 0E, 14
        "Function_15_29BC",        # 0F, 15
        "Function_16_2A71",        # 10, 16
        "Function_17_2AC4",        # 11, 17
        "Function_18_2AFA",        # 12, 18
        "Function_19_2B77",        # 13, 19
        "Function_20_308E",        # 14, 20
        "Function_21_310C",        # 15, 21
        "Function_22_316A",        # 16, 22
        "Function_23_31CC",        # 17, 23
        "Function_24_3417",        # 18, 24
        "Function_25_36A9",        # 19, 25
        "Function_26_370D",        # 1A, 26
        "Function_27_374D",        # 1B, 27
        "Function_28_5170",        # 1C, 28
        "Function_29_5746",        # 1D, 29
        "Function_30_5D83",        # 1E, 30
        "Function_31_5E79",        # 1F, 31
        "Function_32_6944",        # 20, 32
        "Function_33_6D76",        # 21, 33
        "Function_34_6E84",        # 22, 34
        "Function_35_70E9",        # 23, 35
        "Function_36_7C1D",        # 24, 36
        "Function_37_7CAB",        # 25, 37
        "Function_38_7D47",        # 26, 38
        "Function_39_7F2A",        # 27, 39
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F5")

    ChrTalk(
        0x8,
        (
            "With the staff members,\x01",
            "Citizen's in a riot under martial law\x01",
            "I confirmed my safety … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Caught up in a fuss\x01",
            "Apart from more than ten citizens who suffered minor injuries,\x01",
            "It seems that there was hardly any damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To those who need treatment\x01",
            "We also arranged an ambulance … ….\x01",
            "It is safe in this for the moment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AA3")

    label("loc_9F5")


    ChrTalk(
        0x8,
        (
            "In the riot under martial law,\x01",
            "Apart from more than ten citizens who suffered minor injuries,\x01",
            "It seems that there was hardly any damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To those who need treatment\x01",
            "We also arranged an ambulance … ….\x01",
            "It is safe in this for the moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA3")

    Jump("loc_1643")

    label("loc_AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5C")

    ChrTalk(
        0x8,
        (
            "Currently, at the city hall\x01",
            "People of citizens who can not return home\x01",
            "I am taking an accepting attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have any problems\x01",
            "Please do not hesitate to contact us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BE2")

    label("loc_B5C")


    ChrTalk(
        0x8,
        (
            "Also at the municipal hall, food, blankets, etc.\x01",
            "We prepare for emergency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have any problems\x01",
            "Please do not hesitate to contact us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE2")

    Jump("loc_1643")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C65")

    ChrTalk(
        0x8,
        (
            "A voice to chant the harmony,\x01",
            "I will definitely arrive here as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel a bit scary\x01",
            "I wonder why ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D02")

    ChrTalk(
        0x8,
        (
            "Today I went to a charity event\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I definitely want to participate\x01",
            "If you have any plan\x01",
            "Please contact us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E36")

    ChrTalk(
        0x8,
        (
            "About the armed group that struck Mainz,\x01",
            "So many people from citizens\x01",
            "I have received an inquiry … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When it comes to the story of the criminal or the incident,\x01",
            "Because I can not answer to you\x01",
            "It is very troubling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There are also many people who say that it is the work of the empire … …\x01",
            "Where is the truth?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E87")

    label("loc_E36")


    ChrTalk(
        0x8,
        (
            "There are also many people who say that it is the work of the empire … …\x01",
            "Where is the truth?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E87")

    Jump("loc_1643")

    label("loc_E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F35")

    ChrTalk(
        0x8,
        (
            "Now, at the multipurpose hall on the left\x01",
            "The theme of national independence\x01",
            "A citizen forum is underway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since anyone can listen\x01",
            "If you like, please drop in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_FA9")

    ChrTalk(
        0x8,
        (
            "Well, even on the day\x01",
            "It is possible to listen to itself … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Unfortunately the seat is\x01",
            "It is buried … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1050")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "Welcome to the Crossbell Municipal Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those who think about using the city hall\x01",
            "First of all, aside from reception, this\x01",
            "Please fill in the application form.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_1050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_124C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1185")

    ChrTalk(
        0x8,
        (
            "Following the advocacy of national independence,\x01",
            "I would like to hold a study group here\x01",
            "Inquiries have increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In response to such a voice, the city and communications company\x01",
            "Collaborate with the citizen forum on the day after tomorrow\x01",
            "It was decided to hold it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it is currently being adjusted variously,\x01",
            "Surely meaningful for you\x01",
            "I think that a forum can be held.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1247")

    label("loc_1185")


    ChrTalk(
        0x8,
        (
            "The day after tomorrow, at this city hall\x01",
            "Cross Bell's theme of national independence\x01",
            "We are planning to hold a citizen forum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it is currently being adjusted variously,\x01",
            "Surely meaningful for you\x01",
            "I think that a forum can be held.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1247")

    Jump("loc_1643")

    label("loc_124C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_12F2")

    ChrTalk(
        0x8,
        (
            "I am sorry, too.\x01",
            "The notification from before\x01",
            "I think that it was … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From a security perspective absolutely\x01",
            "In order to pass the general public\x01",
            "I do not go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_12F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_144B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C2")

    ChrTalk(
        0x8,
        (
            "The leaders of the countries finally\x01",
            "You made it into the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From the afternoon in each\x01",
            "I also heard the story of acting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, what kind of\x01",
            "Will you spend your time?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1446")

    label("loc_13C2")


    ChrTalk(
        0x8,
        (
            "From the afternoon, the leaders\x01",
            "I also heard the story of acting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, what kind of\x01",
            "Will you spend your time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1446")

    Jump("loc_1643")

    label("loc_144B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_14F8")

    ChrTalk(
        0x8,
        (
            "During the period before and after the trade meeting\x01",
            "Use of Municipal Hall\x01",
            "We are refraining from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is also close to the Orkis Tower,\x01",
            "If something happens that's it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_14F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1637")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_158C")

    ChrTalk(
        0x8,
        (
            "Everyone, today's survey,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We will continue the Cross Bell City Hall\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1632")

    label("loc_158C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1632")

    ChrTalk(
        0x8,
        (
            "I would like to ask everyone\x01",
            "A total of three suspicious houses, and\x01",
            "It is confirmation of the previous owner who is unknown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once all are confirmed,\x01",
            "Please report to this person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1632")

    label("loc_1632")

    Jump("loc_1643")

    label("loc_1637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1643")
    Call(0, 10)

    label("loc_1643")

    TalkEnd(0x8)
    Return()

    # Function_5_897 end

    def Function_6_1647(): pass

    label("Function_6_1647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_16C0")

    ChrTalk(
        0xFE,
        (
            "A nice property\x01",
            "I hope you find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you can, flowers are full\x01",
            "As a place of bloom\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C0")

    TalkEnd(0xFE)
    Return()

    # Function_6_1647 end

    def Function_7_16C4(): pass

    label("Function_7_16C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1723")

    ChrTalk(
        0xFE,
        "It's all right, mother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If your father, surely a good room\x01",
            "You find me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1723")

    TalkEnd(0xFE)
    Return()

    # Function_7_16C4 end

    def Function_8_1727(): pass

    label("Function_8_1727")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1743")

    ChrTalk(
        0xFE,
        "Nyan.\x02",
    )

    CloseMessageWindow()

    label("loc_1743")

    TalkEnd(0xFE)
    Return()

    # Function_8_1727 end

    def Function_9_1747(): pass

    label("Function_9_1747")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1756")
    Call(0, 10)

    label("loc_1756")

    TalkEnd(0xFE)
    Return()

    # Function_9_1747 end

    def Function_10_175A(): pass

    label("Function_10_175A")

    OP_4B(0x10, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18BC")

    ChrTalk(
        0x10,
        (
            "Yeah, I want a room as cheap as possible\x01",
            "I am looking for … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Because it may be somewhat narrow,\x01",
            "A place where three families can live … …\x01",
            "Is there something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I agree……\x01",
            "Because there are such materials,\x01",
            "Why do not you check it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Certainly, a few months ago\x01",
            "The property for which a transfer report was accepted\x01",
            "I think that it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmm, that kind of property.\x01",
            "let's see……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_197B")

    label("loc_18BC")


    ChrTalk(
        0x10,
        (
            "Oh, and … …\x01",
            "It is a petable property\x01",
            "It is the minimum condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, if that property\x01",
            "I think that it was OK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Oh, that was nice!\x01",
            "Even so soon\x01",
            "I want to check …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197B")

    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_10_175A end

    def Function_11_1984(): pass

    label("Function_11_1984")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8A")

    ChrTalk(
        0xFE,
        (
            "Regarding this incident,\x01",
            "A place of official explanation for citizens\x01",
            "I am preparing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About future events\x01",
            "Crossbell citizens also\x01",
            "You will be asking for an explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are confusion everywhere,\x01",
            "We must proceed with preparations as soon as possible\x01",
            "You can not do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B1E")

    label("loc_1A8A")


    ChrTalk(
        0xFE,
        (
            "Regarding this incident,\x01",
            "A place of official explanation for citizens\x01",
            "I am preparing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are confusion everywhere,\x01",
            "We must proceed with preparations as soon as possible\x01",
            "You can not do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1E")

    Jump("loc_25F0")

    label("loc_1B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1CD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C32")

    ChrTalk(
        0xFE,
        (
            "Regarding this case,\x01",
            "Only from the President is \"martial law\"\x01",
            "It was not reported.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is such a situation ……\x01",
            "Even those who are not prepared\x01",
            "There should be many.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Now waiting for convergence,\x01",
            "Safety of citizens again\x01",
            "You have to check it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CD0")

    label("loc_1C32")


    ChrTalk(
        0xFE,
        (
            "Such a situation …\x01",
            "Even those who are not prepared\x01",
            "There should be many.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Now waiting for convergence,\x01",
            "Safety of citizens again\x01",
            "You have to check it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD0")

    Jump("loc_25F0")

    label("loc_1CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1DEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D84")

    ChrTalk(
        0xFE,
        (
            "Crossbell independent country,\x01",
            "And what is the president's inauguration ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way, of course\x01",
            "Even the regime will change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyday from today I feel nervous days.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DE7")

    label("loc_1D84")


    ChrTalk(
        0xFE,
        (
            "In this way, of course\x01",
            "Even the regime will change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyday from today I feel nervous days.\x02",
    )

    CloseMessageWindow()

    label("loc_1DE7")

    Jump("loc_25F0")

    label("loc_1DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E40")

    ChrTalk(
        0xFE,
        (
            "Come now, Today\x01",
            "Charity event\x01",
            "Please enjoy and go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_1E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7A")

    ChrTalk(
        0xFE,
        (
            "From the city hall, \"Toward a solution\x01",
            "I am doing my best.\x01",
            "I have received a notice ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, various things\x01",
            "It is too invisible, it makes me uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, but we are the staff of the city\x01",
            "I was worried that everyone in the citizen\x01",
            "It makes me more uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must hold my mind somehow.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FFC")

    label("loc_1F7A")


    ChrTalk(
        0xFE,
        (
            "We are the staff of the city\x01",
            "I was worried that everyone in the citizen\x01",
            "It makes me more uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must hold my mind somehow.\x02",
    )

    CloseMessageWindow()

    label("loc_1FFC")

    Jump("loc_25F0")

    label("loc_2001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2087")

    ChrTalk(
        0xFE,
        (
            "For now, the citizen forum\x01",
            "It seems that it is progressing smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As usual, there is a lot of noise\x01",
            "I pray for not happening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_2087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_20DA")

    ChrTalk(
        0xFE,
        (
            "Umm, somehow, I got a keyboard\x01",
            "I want to be able to manipulate well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_20DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_225C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BE")

    ChrTalk(
        0xFE,
        (
            "Recently, at the General Affairs Division 2\x01",
            "Demand mail\x01",
            "I am gradually using it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this year\x01",
            "Challenging new things is\x01",
            "It is rather difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially that keyboard\x01",
            "The input device is terribly difficult.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2257")

    label("loc_21BE")


    ChrTalk(
        0xFE,
        (
            "And when I look at the display\x01",
            "Eyes get tired all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Again paper medium is better …\x01",
            "If you are saying this\x01",
            "It will be left behind from the surroundings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2257")

    Jump("loc_25F0")

    label("loc_225C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_22FB")

    ChrTalk(
        0xFE,
        (
            "Since it became a city hall\x01",
            "I feel that the busyness has doubled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the citizen forum\x01",
            "There is preparation for referendum … …\x01",
            "Recently the mountain is going on something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_22FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2342")

    ChrTalk(
        0xFE,
        (
            "Er, as she says\x01",
            "The security problem is the best …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_23E7")

    ChrTalk(
        0xFE,
        (
            "From the window the state of the unveiling ceremony\x01",
            "I had you see it,\x01",
            "Wow, that was exactly spectacular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally, the town hall was relocated,\x01",
            "I feel I could feel it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_23E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2460")

    ChrTalk(
        0xFE,
        (
            "Yes, if you are a resident registrar, you do not have to go to the city agency\x01",
            "You can proceed here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please tell us at the reception desk on the 1st floor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_2460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2543")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2480")
    Call(0, 13)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_253E")

    label("loc_2480")


    ChrTalk(
        0xFE,
        (
            "Most of the reasons for cancellation on the day\x01",
            "Apparently it is in the rain.\x01",
            "It is reasonable for Rizero to get angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, for example cancellation fee\x01",
            "If it is structured to take,\x01",
            "Perhaps it did not work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253E")

    Jump("loc_25F0")

    label("loc_2543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_25F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2566")
    Call(0, 12)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_25F0")

    label("loc_2566")


    ChrTalk(
        0xFE,
        (
            "Well, what is it?\x01",
            "All administrative processing is to the general affairs department 2\x01",
            "I wonder if it will come around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is for each person\x01",
            "I think it should be done … …\x01",
            "Grumbling ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F0")

    TalkEnd(0xFE)
    Return()

    # Function_11_1984 end

    def Function_12_25F4(): pass

    label("Function_12_25F4")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xA,
        (
            "Well, then that's the delivery voucher\x01",
            "Can I ask for confirmation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, yeah, how long … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, that's no mistake.\x01",
            "Then we asked for delivery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Well, please leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_25F4 end

    def Function_13_26D1(): pass

    label("Function_13_26D1")

    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "It's about the seminar\x01",
            "It's the start time ……\x01",
            "Can you delay the schedule for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Of course, of course.\x01",
            "It is less than half of the capacity\x01",
            "It does not make sense to start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But it was canceled on the day …\x01",
            "That's why amateurs do not like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "With such a thing, business opportunities\x01",
            "If you think you can grasp it is a big mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway,\x01",
            "I will make you stick a little more.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2904")

    ChrTalk(
        0x102,
        (
            "#00105F(Hey, Lloyd.\x01",
            "Perhaps this person … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Oh, the case of the case of the example\x01",
            "It is one of Gnostic victims. )\x02\x03",
            "#00000F(Something seems to be tough,\x01",
            "It was nice to be healthy anyway. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2904")

    SetScenarioFlags(0x12E, 5)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_13_26D1 end

    def Function_14_291A(): pass

    label("Function_14_291A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_293D")
    Call(0, 12)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_29B8")

    label("loc_293D")


    ChrTalk(
        0xFE,
        (
            "Well, this baggage\x01",
            "To the general affairs department 1,\x01",
            "Is this meant for finance section …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The new city hall is nearby,\x01",
            "I wonder if it will come quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B8")

    TalkEnd(0xFE)
    Return()

    # Function_14_291A end

    def Function_15_29BC(): pass

    label("Function_15_29BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DF")
    Call(0, 13)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_2A6D")

    label("loc_29DF")


    ChrTalk(
        0xFE,
        (
            "Hmmm, even if you collect the participation fee\x01",
            "Even the facility usage fee is not enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything, as new\x01",
            "I have to increase the original hand … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6D")

    TalkEnd(0xFE)
    Return()

    # Function_15_29BC end

    def Function_16_2A71(): pass

    label("Function_16_2A71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AC0")

    ChrTalk(
        0xFE,
        (
            "Um, even here is the resident registration\x01",
            "I heard that you can do procedures … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC0")

    TalkEnd(0xFE)
    Return()

    # Function_16_2A71 end

    def Function_17_2AC4(): pass

    label("Function_17_2AC4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I am working in a department store\x01",
            "I am worried about my mother ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2AC4 end

    def Function_18_2AFA(): pass

    label("Function_18_2AFA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Umu … It's kind of strange.\x01",
            "Well, it probably will be such a situation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President Dieter ……\x01",
            "I believed him.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2AFA end

    def Function_19_2B77(): pass

    label("Function_19_2B77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F65")

    ChrTalk(
        0xFE,
        (
            "Oh, you guys …\x01",
            "I wonder if he was a police officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That passage took care of me.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C82")

    ChrTalk(
        0x101,
        (
            "#00005FOh … maybe,\x01",
            "Mrs. Pierre's wife ……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, for the first time in a while, Madame.\x01",
            "You evacuated to the city hall?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF0")

    label("loc_2C82")


    ChrTalk(
        0x101,
        (
            "#00005FOh, maybe\x01",
            "Mrs. Pierre's wife ……?\x02\x03",
            "#00001FEr …\x01",
            "Did you evacuate to the city hall?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF0")


    ChrTalk(
        0xFE,
        (
            "Yeah, that's right ……\x01",
            "… … did not you see that master?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just said I'd go to the Orkis Tower,\x01",
            "Do not come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FNo, I have not seen it ….\x02\x03",
            "The deputy director, what on earth do you do?\x01",
            "To the Orkis Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "here we go……\x01",
            "I have not heard of it either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Totally, that person\x01",
            "In such a time worrying about extra … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When coming back,\x01",
            "I have to scold him a lot.\x02",
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
            "#00000FTentatively, my wife is here\x01",
            "Please wait.\x02\x03",
            "Perhaps it is a little\x01",
            "It may come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Yes, I will.\x01",
            "Please contact me if you see it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3014")

    label("loc_2F65")


    ChrTalk(
        0xFE,
        (
            "My husband to the Orkis Tower\x01",
            "I did not return after I went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Totally, that person\x01",
            "In such a time worrying about extra … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When coming back,\x01",
            "I have to scold him a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3014")

    SetScenarioFlags(0x1CC, 2)
    Jump("loc_308A")

    label("loc_301C")


    ChrTalk(
        0xFE,
        (
            "Totally, that person\x01",
            "In such a time worrying about extra … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When coming back,\x01",
            "I have to scold him a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308A")

    TalkEnd(0xFE)
    Return()

    # Function_19_2B77 end

    def Function_20_308E(): pass

    label("Function_20_308E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3108")

    ChrTalk(
        0xFE,
        (
            "Hey, why?\x01",
            "You can not go to the Orkist Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About the square in front of the tower\x01",
            "Can I freely go in and out?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3108")

    TalkEnd(0xFE)
    Return()

    # Function_20_308E end

    def Function_21_310C(): pass

    label("Function_21_310C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3166")

    ChrTalk(
        0xFE,
        (
            "Sure.\x01",
            "Almost such a story, even if suddenly told\x01",
            "I heard that I have not heard this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3166")

    TalkEnd(0xFE)
    Return()

    # Function_21_310C end

    def Function_22_316A(): pass

    label("Function_22_316A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_31C8")

    ChrTalk(
        0xFE,
        (
            "Citizens' Forum tomorrow\x01",
            "I would like to participate in …\x01",
            "Are there any vacant seats yet?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C8")

    TalkEnd(0xFE)
    Return()

    # Function_22_316A end

    def Function_23_31CC(): pass

    label("Function_23_31CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3206")
    Call(0, 32)
    Return()

    label("loc_3206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3214")
    Call(0, 29)
    Return()

    label("loc_3214")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_336A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E8")

    ChrTalk(
        0xFE,
        (
            "Sorry, you guys.\x01",
            "Roy makes time and effort ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you can open Miscon,\x01",
            "For citizens as well\x01",
            "Let's get a good breath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, do your best\x01",
            "Please collect participants.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3365")

    label("loc_32E8")


    ChrTalk(
        0xFE,
        (
            "If you can open Miscon,\x01",
            "For citizens as well\x01",
            "Let's get a good breath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, do your best\x01",
            "Please collect participants.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3365")

    Jump("loc_3413")

    label("loc_336A")


    ChrTalk(
        0xFE,
        (
            "The citizens seemed to be able to relax,\x01",
            "We also donate to donation money for reconstruction assistance\x01",
            "After Miscon, it gathers quite a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Misccon was Roy's idea … …\x01",
            "Huhuu, I thought I was fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3413")

    TalkEnd(0xFE)
    Return()

    # Function_23_31CC end

    def Function_24_3417(): pass

    label("Function_24_3417")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_345F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3451")
    Call(0, 32)
    Return()

    label("loc_3451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345F")
    Call(0, 29)
    Return()

    label("loc_345F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3638")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A5")

    ChrTalk(
        0x15,
        (
            "To you, to Miscon\x01",
            "A \"working woman\" to participate\x01",
            "I want you to scout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "\"Waitress\" \"Craftsman\"\x01",
            "\"Maid\" \"Sister\" …\x01",
            "I'd like to go with these 4 frames.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "If these people participate\x01",
            "The occupation of the contest participants\x01",
            "It will be well balanced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "We're counting on you!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3633")

    label("loc_35A5")


    ChrTalk(
        0x15,
        (
            "\"Waitress\" \"Craftsman\"\x01",
            "\"Maid\" \"Sister\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "This 4-frame \"working woman\"\x01",
            "Please come and scout me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "We're counting on you!\x02",
    )

    CloseMessageWindow()

    label("loc_3633")

    Jump("loc_36A5")

    label("loc_3638")


    ChrTalk(
        0x15,
        (
            "Thanks to you\x01",
            "Miscon is a huge success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You are a participant\x01",
            "Thanks for collecting it,\x01",
            "Thank you very much!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A5")

    TalkEnd(0xFE)
    Return()

    # Function_24_3417 end

    def Function_25_36A9(): pass

    label("Function_25_36A9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Old city, father in this address … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You did it, Airy!\x01",
            "I will only go here and meet again.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_36A9 end

    def Function_26_370D(): pass

    label("Function_26_370D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Huhu, finally I know whereabouts\x01",
            "I'm glad, Alm Ju\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_370D end

    def Function_27_374D(): pass

    label("Function_27_374D")

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
            "Welcome.\x01",
            "Welcome to the Crossbell Municipal Hall.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Please come welcome.\x01",
            "You are a member of the Special Affairs Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, I came to confirm the request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FNew members together\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FNice to meet you, my older sister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FThanking you in advance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, this is it.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F…… But is it a city hall?\x01",
            "I feel something strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FYeah, this building is\x01",
            "I do not think it's a city hall\x01",
            "Somewhat lacking feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FHuhu, the new city hall is\x01",
            "In the new city hall building to be completed this time\x01",
            "Since I entered in advance … …\x02\x03",
            "#00100FBut, once in a while,\x01",
            "The \"branch office\" of the city hall remains.\x02\x03",
            "In that sense, it will not change in the future\x01",
            "I think it will be helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10103FIndeed, was that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, even at this reception\x01",
            "Citizen's window service such as various residents procedures\x01",
            "It is supposed to continue to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… But the public notice about it\x01",
            "Whether it has not penetrated everyone of citizens,\x01",
            "In a situation where there are very many inquiries ……\x02",
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
            "I am sorry, too.\x01",
            "It was an unrelated story to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FNo, it is … it seems tough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, but thinking of officials\x01",
            "It's boring.\x02\x03",
            "If I am referring to the area around the entertainment district\x01",
            "I made it as an \"adult social gathering place\".\x02\x03",
            "#10309FNightclub held by public servant ……\x01",
            "The mission support department is surely more than ever\x01",
            "I guess it got pulled out?\x02",
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
            "#12P#00006FPull it … …\x01",
            "I'm asking for any assistance.\x02\x03",
            "#00001FI mean,\x01",
            "In the first place public officials work at night\x01",
            "It is impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FOh, haha ….\x01",
            "(I imagined a bit.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FKo, Kohon ……\x01",
            "Better still Lloyd, do not you forget the subject?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00011FOh, yes.\x02\x03",
            "#00000FEr, I'm sorry.\x01",
            "About the request for assistance … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Yes, I will explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "- Everyone is notified of \"change of resident\"\x01",
            "Do you know what you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is moving etc\x01",
            "When a resident changes\x01",
            "It is a notification I will submit to the city … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, recently, in this notice\x01",
            "A thing with a suspicious name written\x01",
            "It was found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FSuspicious name, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah … exactly\x01",
            "\"Name not registered in city\"\x01",
            "It will be said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have found some,\x01",
            "For both residents and corporate residents of the city\x01",
            "It was a name that does not exist at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, to you all\x01",
            "It was delivered with that suspicious name\x01",
            "Confirmation of actual condition of dwelling … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In addition,\x01",
            "Confirm the status of the original residents\x01",
            "I would like you to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FI see.\x01",
            "The old and new residents of that suspicious house\x01",
            "You should check it.\x02\x03",
            "#00003FIf you were involved in some kind of crime\x01",
            "I can not leave it alone … ….\x02\x03",
            "#00000FCertainly, the neighborhood\x01",
            "You should investigate all the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYeah, well.\x02\x03",
            "#00100FHowever, the place of the suspicious house is\x01",
            "Of course I think that … …\x02\x03",
            "Regarding the location of the original resident\x01",
            "Are you grasping by the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, that is the only one\x01",
            "Because I am accepting a transfer\x01",
            "I understand ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For other people\x01",
            "It is a situation I can not grasp at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FIndeed, when it comes to\x01",
            "That is why we need search activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FBut first, with that suspicious house\x01",
            "Investigation of residents whose location is known\x01",
            "It seems better to have done it.\x02\x03",
            "Even if the residents of the unknown location,\x01",
            "Some thing in the process of investigation\x01",
            "I will come to understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FOh, yes.\x02\x03",
            "#00000FBy the way, those\x01",
            "Is there something like a list?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, a copy of the notice\x01",
            "Please check it because it is prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000Ftake into custody.\x02",
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x258, 0x3E8, 0x0)
    Sleep(800)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_97(0x101, 0x0, 0x0, 0xFFFFFDA8, 0x3E8, 0x0)
    Sleep(50)

    def lambda_4528():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4528)

    def lambda_4535():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4535)

    def lambda_4542():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4542)

    def lambda_454F():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_454F)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00000FWell, ohh ……\x01",
            "Is there a problem house in 3 places in all?\x02\x03",
            "First of all, one residential area ……\x01",
            "Do you know where Elly is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100Flet's see……\x01",
            "Oh, this is next to my parents house.\x02\x03",
            "#00105FResident \"Hybrads\" ……\x01",
            "What is this, corporate name?\x02\x03",
            "#00103FHere is the securities man's\x01",
            "Bond's family\x01",
            "I should have lived … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FOh, as a former resident\x01",
            "It is also listed in the list.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5P#00003FMr. Bond of securities man … …\x02\x03",
            "#00001FCertainly due to a cult incident\x01",
            "It is one of Gnostic victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FWell, there is no doubt.\x02\x03",
            "#00108FAfter the incident,\x01",
            "Just if your family had a lot\x01",
            "I was listening ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FNo way … … something's wrong\x01",
            "Was it involved?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00001FI do not know but …\x01",
            "Apparently I gave out the move notification\x01",
            "It looks like Bond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FEntrance is East Street,\x01",
            "\"Acacia - so\" on the second floor.\x02\x03",
            "It is next to the left of the Association of Association\x01",
            "I have written buildings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FResidential area and east street ……\x01",
            "I have to investigate both reliably.\x02\x03",
            "#00001FThe next residence is also Higashi dori.\x01",
            "Is this address the headquarters of the fishing public division ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00011F- Well, yeah! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FWell, what happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00008FNo, if the name of the resident is \"#4RAfternoon tea#club\"\x01",
            "I'm supposed to be ……\x02\x03",
            "I thought that it was a group name that I never heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00105FLloyd, certainly you\x01",
            "You were a member of \"Fishing public division\", are not you?\x02\x03",
            "From other members\x01",
            "Are not you hearing anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FOh, oh, recently busy\x01",
            "Because it was not fishing.\x02\x03",
            "#00001FBefore you resident\x01",
            "\"Fishing public division\" is unknown … …\x01",
            "Well, have you changed your name?\x02\x03",
            "#00003F… Well good.\x01",
            "As you can find this properly.\x02\x03",
            "#00001FThe last residence is the Old Town,\x01",
            "\"Lotus Heights\" on the first floor?\x02\x03",
            "Mr. Geithner ……\x01",
            "It seems that the location is still unknown.\x02\x03",
            "And the current residents ……\x01",
            "\"Sean Alnam\".\x02\x03",
            "#00005F…… that, this name somewhere\x01",
            "You've heard of it … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10304FHe is the author of a famous fairy tale.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00011FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FPopular fairy tales in the library,\x01",
            "\"Mark and Deep Forest Witch\"\x01",
            "People who wrote it.\x02\x03",
            "#00100FDo not you remember Lloyd?\x01",
            "Hey, previously Rubathe's\x01",
            "When entering the hide … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00005FOh, by the way it's a door\x01",
            "To unlock password\x01",
            "Was it being used?\x02\x03",
            "#00008FBut, no wonder such a writer\x01",
            "Old city …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FWell, rather than in the first place\x01",
            "The author should have already been a deceased person.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006FWell, maybe ….\x01",
            "Somewhat anxious it came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuhu, whatever the other\x01",
            "This is the time to accept the receipt\x01",
            "It seems to be good to notice.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "I am sorry, too.\x02",
    )

    CloseMessageWindow()

    def lambda_4F0E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F0E)
    Sleep(50)

    def lambda_4F1E():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F1E)
    Sleep(50)

    def lambda_4F2E():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4F2E)
    Sleep(50)

    def lambda_4F3E():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F3E)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "All the staff, to be careful\x01",
            "I am keeping in mind … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FNo, such a thing ….\x01",
            "Now the city hall is also organized and taken over\x01",
            "It's a pretty busy time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FYeah, that's bad for anything else\x01",
            "This is the person who submitted this notification!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell, that's why\x01",
            "We are going to investigate immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAfter checking all\x01",
            "I will ask the report again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes.\x01",
            "Thank you.\x02",
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
            "Quest 【Request for investigation of suspicious house】\x07\x00",
            "I started!\x02",
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

    # Function_27_374D end

    def Function_28_5170(): pass

    label("Function_28_5170")

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
            "#12P#1Peveryone.\x01",
            "Those who confirm the suspicious house\x01",
            "Are you progressing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, one thing\x01",
            "Since confirmation is over\x01",
            "I will report it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I added the correct resident name\x01",
            "I handed out a copy of the notice.\x07\x00\x02",
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
            "#12P#1PIndeed, until a fine place\x01",
            "You have examined it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PIn the residential area, Republic,\x01",
            "For the eastern street the empire is better\x01",
            "You had it in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12P#1PThe person in the old town … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FDid you have something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PNo, Gebal's name is\x01",
            "It was too surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PI also here several times\x01",
            "Just as I have seen you\x01",
            "I feel a little complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#1PWhat is that,\x01",
            "Even if you do bad things\x01",
            "Because it was a person who can not hate somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYes, somehow\x01",
            "I feel like understanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FIndeed it's a good or bad way\x01",
            "It seemed like an easy-to-understand person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, that's a while more\x01",
            "When you are in a victory\x01",
            "There are also pretties, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Huhu, maybe so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Anyway, as a survey\x01",
            "I think that it is a result that is no more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Afterwards, if you follow various procedures at the residents'\x01",
            "It seems that it can be handled without any problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Today everyone,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FNo, this is it.\x01",
            "It seems that it was useful, nothing more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FAlso, if something happens\x01",
            "Please call me anytime.\x02",
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
            "Quest 【Request for investigation of suspicious house】\x07\x00",
            "Achieved!\x02",
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

    # Function_28_5170 end

    def Function_29_5746(): pass

    label("Function_29_5746")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C31")
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
        "Hmm. They really aren't showing up\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Hey, Roy.\x01",
            "Again this program\x01",
            "I should not give up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "What are you saying now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "To cheer everyone in the city\x01",
            "Charity event,\x01",
            "That 's the eyeball program.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Without doing this,\x01",
            "What on earth do you say! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "B-but…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "Inquiries\x01",
            "I am sorry but …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_599F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_599F)
    Sleep(50)
    OP_93(0x15, 0xB4, 0x1F4)

    ChrTalk(
        0x15,
        "You guys are\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "OH you came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Today is a charity event\x01",
            "Did he come to visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, certainly from the Chamber of Commerce\x01",
            "Cooperation with charity events\x01",
            "I was asked … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        "Yes, that's it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I'm the one who submitted the request\x02",
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
            "Why not?\x01",
            "Roy, you … before you …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Haha, in fact\x01",
            "I asked for a secret request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Well then,\x01",
            "Shall I explain the work immediately?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C08():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5C08)

    ChrTalk(
        0x15,
        "Do you have time?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D38")

    label("loc_5C31")

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
            "Instantly explain the work\x01",
            "I would like to ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Do you have time?\x02",
    )

    CloseMessageWindow()

    label("loc_5D38")

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

    # Function_29_5746 end

    def Function_30_5D83(): pass

    label("Function_30_5D83")

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
            "Choice 1: Accept\x01",      # 0
            "quit\x01",          # 1
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
        (0, "loc_5DE5"),
        (1, "loc_5DED"),
        (SWITCH_DEFAULT, "loc_5E78"),
    )


    label("loc_5DE5")

    Call(0, 31)
    Jump("loc_5E78")

    label("loc_5DED")


    ChrTalk(
        0x101,
        (
            "#00006FSorry, I'm sorry.\x01",
            "Now a bit … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Oh yeah … I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "If you have time\x01",
            "I will be saved if you help me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 3)
    Jump("loc_5E78")

    label("loc_5E78")

    Return()

    # Function_30_5D83 end

    def Function_31_5E79(): pass

    label("Function_31_5E79")


    ChrTalk(
        0x101,
        "#00000FYes, we'll accept\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "That's right!\x01",
            "Well, I will explain the content of the request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Today, in the hall of this city hall\x01",
            "The charity event is held in\x01",
            "You know too, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Now, just playing the piano\x01",
            "Eating party is held, but,\x01",
            "Only one problem has occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FA problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Actually, after my planning\x01",
            "An eyeball program is held\x01",
            "It was a schedule ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Participants did not gather,\x01",
            "The program itself seems to be torn down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FYou did send the request to them though/\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSo, what is that program?\x01",
            "What exactly is that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "\"Miss Crossbell Contest\x01",
            "~ Working woman, forever ~ '.\x02",
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
            "#00012FYes, so-called\x01",
            "Do you mean Miscon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FOh wow that sounds great\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FThe subtitle's cheapness\x01",
            "I am worried … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Well, in short\x01",
            "For women working in Crossbell\x01",
            "In Miscon with a spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Just … … so far participants\x01",
            "We have hardly gathered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Offer was\x01",
            "Only three people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It is truly\x01",
            "I do not form the body of the program,\x01",
            "Please tell me to stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FWell, after all many people\x01",
            "I guess I will not hold back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FGhost, apparently\x01",
            "You seem to be able to talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "It's as you guess\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "To you, to Miscon\x01",
            "A \"working woman\" to participate\x01",
            "I want you to scout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see……\x01",
            "I understood the outline of the request.\x02\x03",
            "#00000FBy the way, participants are currently\x01",
            "They seem to have three people, but ….\x01",
            "What kind of people are they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Well, first\x01",
            "Ms. Cynthia, a receptionist at a department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Next, the hostess of the back street\x01",
            "Iris.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "And from Crossbell Police\x01",
            "Mr. Kate to the police officer\x01",
            "I got an OK.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012FKate-senpai\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FA lady guard at the receptionist and a hostess?\x01",
            "Huff, there are lots of variations.\x02\x03",
            "#10302FWhat kind of occupation child is there after?\x01",
            "Should I invite him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Hmm, right…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "\"Waitress\" \"Craftsman\"\x01",
            "\"Maid\" \"Sister\" …\x01",
            "I'd like to go with these 4 frames.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "If these people participate\x01",
            "The occupation of the contest participants\x01",
            "It will be well balanced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "…… If true, nurses and others\x01",
            "A member of the alkane shell\x01",
            "I wanted to invite you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI guess it can not be helped.\x01",
            "Alcan Shell is Mr. Ilya's case\x01",
            "I guess it is not so far … …\x02\x03",
            "Ursula hospital, too, in patient response\x01",
            "It should be handy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FRight…\x02\x03",
            "#00000FOk then I think we get it\x02\x03",
            "\"Waitress\" \"Craftsman\"\x01",
            "\"Maid\" \"Sister\" …\x01",
            "Let's look for women in these occupations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Participants gathered\x01",
            "Events even soon\x01",
            "I am going to start.\x02",
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
            "Quest 【Cooperation for Charity Event】\x07\x00",
            "I started!\x02",
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

    # Function_31_5E79 end

    def Function_32_6944(): pass

    label("Function_32_6944")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CE2")

    ChrTalk(
        0x14,
        "Oh you guys\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "How is the search for the pagent participants going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The participation frame I was asking was\x01",
            "\"Waitress\" \"Craftsman\"\x01",
            "\"Maid\" \"Sister\" are four.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, we found all of them\x02\x03",
            "To them, before the program starts\x01",
            "I am getting in touch with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Oh fantastic!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "This is almost time.\x01",
            "It is around the end of the piano performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Well, I managed to make it in time!\x01",
            "I can manage to hold it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHehe, great\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 500)

    ChrTalk(
        0x14,
        (
            "Well, for Roy\x01",
            "Those who did a lot of hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "That unwilling grandson is\x01",
            "I thought that I grew up properly\x01",
            "There is a deep emotion.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x14, 500)

    ChrTalk(
        0x15,
        "What now?\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)

    ChrTalk(
        0x15,
        (
            "Well, anyway,\x01",
            "Miscon is about to start.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6CB3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_6CB3)

    ChrTalk(
        0x15,
        "Are you all prepared?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D31")

    label("loc_6CE2")


    ChrTalk(
        0x15,
        (
            "Well, anyway,\x01",
            "Miscon is about to start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Are you ready for them too?\x02",
    )

    CloseMessageWindow()

    label("loc_6D31")

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

    # Function_32_6944 end

    def Function_33_6D76(): pass

    label("Function_33_6D76")

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
            "Choice 1: All set\x01",      # 0
            "I have not done it yet\x01",      # 1
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
        (0, "loc_6DE8"),
        (1, "loc_6DF0"),
        (SWITCH_DEFAULT, "loc_6E83"),
    )


    label("loc_6DE8")

    Call(0, 34)
    Jump("loc_6E83")

    label("loc_6DF0")


    ChrTalk(
        0x101,
        (
            "#00006FCan you wait for a while?\x01",
            "Ready for a moment … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Hey hey, let's do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Then, when you are ready\x01",
            "Please give me a voice again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19A, 0)
    Jump("loc_6E83")

    label("loc_6E83")

    Return()

    # Function_33_6D76 end

    def Function_34_6E84(): pass

    label("Function_34_6E84")


    ChrTalk(
        0x101,
        (
            "#00000FYes, all good here\x02\x03",
            "Well, from here\x01",
            "I will contact the participants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Yes, please do\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FWell, it is time to go.\x01",
            "I'm starting to look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FRandy is\x01",
            "It is really only that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 500)

    ChrTalk(
        0x14,
        (
            "Well, if you are\x01",
            "Let's go to prepare the venue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The direction of Miscon's progress is Roy,\x01",
            "I will leave it to you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x14, 500)

    ChrTalk(
        0x15,
        "Yes, see you then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FWell, for the time being\x01",
            "I only pray for success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHehe, it's a good opportunity\x01",
            "Let me relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FWe also contact the participants as soon as possible\x01",
            "Shall I enter the hall?\x02",
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

    # Function_34_6E84 end

    def Function_35_70E9(): pass

    label("Function_35_70E9")

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
            "Thanks to you\x01",
            "Miscon is a huge success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You are a participant\x01",
            "Thanks for collecting it,\x01",
            "Thank you very much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHaha, you are welcome.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_74E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7333")

    ChrTalk(
        0x102,
        (
            "#00104FHehe, we also\x01",
            "I feel I enjoyed it much.\x02\x03",
            "#00102FNo way to receive a special prize\x01",
            "I did not expect it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FIf you were Ellie\x01",
            "It is a natural result!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202Fit was cool.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xE)
    Jump("loc_74DB")

    label("loc_7333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7417")

    ChrTalk(
        0x103,
        (
            "#00204F……we also\x01",
            "It was pretty fun.\x02\x03",
            "#00202FNo way to receive a special prize\x01",
            "I did not think that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHuhu, if it was Tio\x01",
            "I think it's a natural result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FTrue!\x01",
            "It was lovely ~.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xF)
    Jump("loc_74DB")

    label("loc_7417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_74DB")

    ChrTalk(
        0x109,
        (
            "#10104FWe also enjoyed it much.\x02\x03",
            "#10100FNo way to receive a special prize\x01",
            "It was unexpected though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204FIf Noel is a natural result.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FIt was awesome.\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x10)

    label("loc_74DB")

    Jump("loc_76E1")

    label("loc_74E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7592")

    ChrTalk(
        0x102,
        (
            "#00102FHehe, we also\x01",
            "I feel I enjoyed it much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FErie was also one step behind\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FWell, it's not a uniform\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76E1")

    label("loc_7592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7646")

    ChrTalk(
        0x103,
        (
            "#00202F……we also\x01",
            "It was pretty fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FTio was also one step behind\x01",
            "I think, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWell, it's not a uniform\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76E1")

    label("loc_7646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_76E1")

    ChrTalk(
        0x109,
        (
            "#10100FUs too\x01",
            "I enjoyed it much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FNoel also\x01",
            "I think that it was a step after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHeh he is not a uniform\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76E1")


    ChrTalk(
        0x14,
        (
            "The citizens seemed to be able to relax,\x01",
            "We also donate to donation money for reconstruction assistance\x01",
            "After Miscon, it gathers quite a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Today is Roy 's thought\x01",
            "She is obliged to compliment her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Well, it's not my thought\x01",
            "Please tell me a nice idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "That's right.\x01",
            "I will give this to you\x01",
            "I'll give you a present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I imagined the winner this time\x01",
            "It's like a memento.\x01",
            "Please accept it if you do not mind.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_78C7")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got Quartz\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('精神３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7A3E")

    label("loc_78C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_7926")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got Quartz\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('防御３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7A3E")

    label("loc_7926")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_7985")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got Quartz\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('攻击３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7A3E")

    label("loc_7985")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_79E4")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got Quartz\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回避３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7A3E")

    label("loc_79E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_7A3E")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got Quartz\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＨＰ３', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7A3E")


    ChrTalk(
        0x101,
        (
            "#00005FIs that ok?\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, anyway\x01",
            "I enjoyed it thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FThis kind of thing is fun once in a while\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYep, definitely \x02\x03",
            "#00000F── Well then,\x01",
            "This will be rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Yes, thanks again\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "If there is something again\x01",
            "Nice to meet you!\x02",
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
            "Quest 【Cooperation for Charity Event】\x07\x00",
            "Achieved!\x02",
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

    # Function_35_70E9 end

    def Function_36_7C1D(): pass

    label("Function_36_7C1D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell Civic Center\x01",
            "Reception room\x07\x00\x02",
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
            "There is a lock on the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_36_7C1D end

    def Function_37_7CAB(): pass

    label("Function_37_7CAB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell Civic Center\x01",
            "Various facilities contact port\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D43")

    ChrTalk(
        0x101,
        (
            "#00000FIt is necessary to enter this place\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7D43")

    TalkEnd(0xFF)
    Return()

    # Function_37_7CAB end

    def Function_38_7D47(): pass

    label("Function_38_7D47")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Saint's Prayer\"\x01",
            "Magnus Hector\x01",
            "In the case of\x01",
            "S1134, was created to honor the establishment of autonomous state\x01",
            "Sculptor Magnus · Hector His last masterpiece. In the case of\x01",
            "After the Old Town Hall is built, as a symbol of the same building\x01",
            "It has been familiar to citizens for many years. In the case of\x01",
            "In the case of\x01",
            "S 1204, with the relocation of the city hall,\x01",
            "It is handed over to the city hall as it is. In the case of\x07\x00\x02",
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

    # Function_38_7D47 end

    def Function_39_7F2A(): pass

    label("Function_39_7F2A")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From the hall\x01",
            "I can hear a hot debate … …\x02\x03",
            "Let's stop disturbing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -13650, 4000, 12700, 225)
    EventEnd(0x4)
    Return()

    # Function_39_7F2A end

    SaveToFile()

Try(main)
