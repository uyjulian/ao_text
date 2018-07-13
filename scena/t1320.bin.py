from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1320.bin",                # FileName
        "t1320",                    # MapName
        "t1320",                    # Location
        0x00BC,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 188, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1320",                  # 0
        "Receptionist Carmina",   # 1
        "Tourist",                # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Watchman Wave",          # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "水着カタログ",           # 8
    ))

    AddCharChip((
        "chr/ch34600.itc",                   # 00
        "chr/ch24402.itc",                   # 01
        "chr/ch44200.itc",                   # 02
        "chr/ch48200.itc",                   # 03
        "chr/ch23600.itc",                   # 04
        "chr/ch48200.itc",                   # 05
        "chr/ch48300.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(4294965296, 0,       5150,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294966977, 200,     4294962246, 90,   389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1750,    0,       3230,    45,   385,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(106769,  0,       102819,  0,    385,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   104.0,                 4.5,                   -1.0,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -26.0,                 -2.25,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 10,  8.850000381469727,     1.0,                   -1.0,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.425000190734863,    -0.25,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 11,  88.52999877929688,     1.0,                   -1.0,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -44.26499938964844,    -0.25,                 0.20000000298023224,   1.0])

    DeclActor(4294965296, 0,       4650,    2000,    4294965296, 1500,    5150,    0x007E, 0,  3,  0x0000)
    DeclActor(99280,   0,       3850,    1200,    99070,   1500,    4220,    0x007C, 0,  8,  0x0000)
    DeclActor(104000,  0,       4600,    1200,    104000,  1500,    4600,    0x007C, 0,  24, 0x0000)
    DeclActor(94000,   0,       4600,    1200,    94000,   1500,    4600,    0x007C, 0,  24, 0x0000)

    ChipFrameInfo(1024, 0)                                       # 0

    ScpFunction((
        "Function_0_400",          # 00, 0
        "Function_1_4B0",          # 01, 1
        "Function_2_5AD",          # 02, 2
        "Function_3_686",          # 03, 3
        "Function_4_68A",          # 04, 4
        "Function_5_87D",          # 05, 5
        "Function_6_8D5",          # 06, 6
        "Function_7_923",          # 07, 7
        "Function_8_A6D",          # 08, 8
        "Function_9_C33",          # 09, 9
        "Function_10_D97",         # 0A, 10
        "Function_11_EC2",         # 0B, 11
        "Function_12_F34",         # 0C, 12
        "Function_13_1112",        # 0D, 13
        "Function_14_2331",        # 0E, 14
        "Function_15_2356",        # 0F, 15
        "Function_16_237B",        # 10, 16
        "Function_17_405D",        # 11, 17
        "Function_18_43E2",        # 12, 18
        "Function_19_4DD1",        # 13, 19
        "Function_20_4F32",        # 14, 20
        "Function_21_7BFE",        # 15, 21
        "Function_22_84CA",        # 16, 22
        "Function_23_8507",        # 17, 23
        "Function_24_8544",        # 18, 24
    ))


    def Function_0_400(): pass

    label("Function_0_400")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_438"),
        (1, "loc_444"),
        (2, "loc_450"),
        (3, "loc_45C"),
        (4, "loc_468"),
        (5, "loc_474"),
        (6, "loc_480"),
        (SWITCH_DEFAULT, "loc_48C"),
    )


    label("loc_438")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_444")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_450")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_45C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_468")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_474")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_48C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_498")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_4AF")

    Return()

    # Function_0_400 end

    def Function_1_4B0(): pass

    label("Function_1_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_END)), "loc_4BE")
    SetChrFlags(0x8, 0x80)

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EC")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52E")
    SetChrPos(0x8, 96490, 0, 1360, 90)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_542")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)
    Jump("loc_551")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_551")
    ClearScenarioFlags(0x22, 3)
    Event(0, 21)

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B")
    SetMapFlags(0x10000000)
    Event(0, 18)

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AC")
    Event(0, 12)

    label("loc_5AC")

    Return()

    # Function_1_4B0 end

    def Function_2_5AD(): pass

    label("Function_2_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BF")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EA")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F8")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_5F8")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_END)), "loc_61D")
    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_61D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_635")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_64B")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_663")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_678")
    OP_65(0x0, 0x1)

    label("loc_678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_END)), "loc_685")
    OP_65(0x0, 0x1)

    label("loc_685")

    Return()

    # Function_2_5AD end

    def Function_3_686(): pass

    label("Function_3_686")

    Call(0, 4)
    Return()

    # Function_3_686 end

    def Function_4_68A(): pass

    label("Function_4_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A1")
    Call(0, 13)
    Return()

    label("loc_6A1")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C3")

    ChrTalk(
        0x8,
        (
            "Thank you very much for having\x01",
            "repelled the swimsuit ripping monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because they are monsters,\x01",
            "maybe we can't say for sure\x01",
            "that they won't appear again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, the Michelam Management Division\x01",
            "will have to ready some countermeasures.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_86B")

    label("loc_7C3")


    ChrTalk(
        0x8,
        (
            "Thank you very much for having\x01",
            "repelled the swimsuit ripping monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, the Michelam Management Division\x01",
            "will have to ready some countermeasures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86B")

    Jump("loc_879")

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_879")

    label("loc_879")

    TalkEnd(0x8)
    Return()

    # Function_4_68A end

    def Function_5_87D(): pass

    label("Function_5_87D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "My girlfriend is choosing a swimsuit now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Can't she choose fast...?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_87D end

    def Function_6_8D5(): pass

    label("Function_6_8D5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Wooow, so many cute swimsuits.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Which one should I choose...?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_8D5 end

    def Function_7_923(): pass

    label("Function_7_923")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EC")
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "EeeeeeK!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "D-Don't bring a little girl\x01",
            "in the men changing room!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FN-Now that you mention it...\x01",
            "...I'm very sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105FHoee?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A69")

    label("loc_9EC")


    ChrTalk(
        0xFE,
        (
            "H-Honestly...\x01",
            "I can't let my guard down at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was almost on the verge of having\x01",
            "my butt seen by a little girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A69")

    TalkEnd(0xFE)
    Return()

    # Function_7_923 end

    def Function_8_A6D(): pass

    label("Function_8_A6D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Advises on how to Enjoy the Lake Beach\x01",
            "─────────────────────────────\x01",
            "・Please, absolutely warm up.\x01",
            "・Please, do not enter dressed into the water.\x01",
            "  (We loan swimsuits at the reception)\x01",
            "・Please, observe the watchman's indications.\x01",
            "─────────────────────────────\x01",
            " Let's mind our manners and have fun.\x01",
            "  　──Michelam Management Division\x07\x00\x02",
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

    # Function_8_A6D end

    def Function_9_C33(): pass

    label("Function_9_C33")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA0")

    ChrTalk(
        0x101,
        (
            "#12500F...The women changing room is this way.\x01",
            "Let's leave before we get misunderstood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3E")

    ChrTalk(
        0x101,
        (
            "#00000F...Oops.\x01",
            "The women changing room is this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105FLloyd, are we going in?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FN-No no, we aren't.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D83")

    label("loc_D3E")


    ChrTalk(
        0x101,
        (
            "#00000FThe women changing room is this way.\x01",
            "...Let's not enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D83")

    SetChrPos(0x0, 104470, 0, 2310, 180)
    EventEnd(0x4)
    Return()

    # Function_9_C33 end

    def Function_10_D97(): pass

    label("Function_10_D97")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E21")

    ChrTalk(
        0x101,
        (
            "#00000FSince we haven't borrowed swimsuits yet,\x01",
            "we can't proceed ahead.\x02\x03",
            "Let's report to the reception first of all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EAE")

    ChrTalk(
        0x101,
        (
            "#00003FWe don't have time to enter the beach again.\x02\x03",
            "#00000FLet's head to the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYes, let's gooo!\x02",
    )

    CloseMessageWindow()

    label("loc_EAE")

    SetChrPos(0x0, 7010, 0, 1020, 270)
    EventEnd(0x4)
    Return()

    # Function_10_D97 end

    def Function_11_EC2(): pass

    label("Function_11_EC2")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FWhoops, we can't loiter around\x01",
            "too much dressed like this.\x02\x03",
            "Let's go the beach.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 91160, 0, 690, 90)
    EventEnd(0x4)
    Return()

    # Function_11_EC2 end

    def Function_12_F34(): pass

    label("Function_12_F34")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -9000, 0, 1000, 90)
    SetChrPos(0x104, -9500, 0, 2130, 90)
    SetChrPos(0x105, -9500, 0, 130, 90)
    OP_68(2400, 1600, 1130, 0)
    MoveCamera(315, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    OP_68(-5400, 1600, 1130, 5000)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(-9350, 3500, 1480, 0)
    MoveCamera(316, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18050, 0)
    OP_68(-9350, 1500, 1480, 2000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00002F#5PEeh...\x01",
            "This is the beach reception?\x02\x03",
            "#00000FIt seems we can borrow\x01",
            "swimsuits here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#5PMaaan, I would've never\x01",
            "dreamt a place like this\x01",
            "could be built.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHu hu, let's report to\x01",
            "the reception now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -8000, 0, 1130, 90)
    SetScenarioFlags(0x144, 6)
    EventEnd(0x5)
    Return()

    # Function_12_F34 end

    def Function_13_1112(): pass

    label("Function_13_1112")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51090.itc", 0x1E)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x9)
    SetChrPos(0xF, -1500, 1000, 3500, 0)
    SetChrFlags(0xF, 0x8)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, -2000, 0, 2500, 0)
    SetChrPos(0x104, -3000, 0, 2350, 0)
    SetChrPos(0x105, -1000, 0, 2450, 0)
    SetMapObjFlags(0x0, 0x1000)
    FadeToBright(1000, 0)
    OP_68(-2000, 1000, 3850, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18500, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11PGood morning,\x01",
            "welcome to the Lake Beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou are the people from the\x01",
            "Special Support Section, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6POh, yes we're.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PHave you been informed\x01",
            "by Milady Mariabell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes, you have a reservation\x01",
            "until today's noon.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x0, 0x8, 0x0, 0xC8, 0x3E8, 0x0)
    Sleep(300)
    Sound(18, 0, 100, 0)
    Fade(250)
    ClearChrFlags(0xF, 0x8)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11PAs for the swimsuits, we have\x01",
            "prepared some samples, so\x01",
            "please choose the ones you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PEeh, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PLet's see, which should I go with...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F#6P.........Hm.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xF, 0x80)
    OP_49()
    OP_D7(0x1E)
    Sleep(1000)
    LoadChrToIndex("chr/ch15000.itc", 0x1E)
    LoadChrToIndex("chr/ch15300.itc", 0x1F)
    LoadChrToIndex("chr/ch15400.itc", 0x20)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12900.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12500.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12800.itp")
    SetChrPos(0x101, 100000, 0, 100300, 0)
    SetChrPos(0x104, 100000, 0, 101700, 180)
    SetChrPos(0x105, 109000, 0, 101000, 270)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    OP_68(94020, 1500, 4870, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(22000, 4000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(100000, 2200, 101000, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18520, 0)
    OP_68(100000, 1200, 101000, 2000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00316F#11PStill, Lloyd...\x02\x03",
            "#00315FDon't you feel this is our biggest reward\x01",
            "since we've joined the SSS!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PT-That's really an exaggeration.\x02\x03",
            "#00002FAlthough it's true that\x01",
            "I'm anticipating a little\x01",
            "how everyone will look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PI know, I know㈱\x02\x03",
            "#00301FFurthermore, Miss Ilya and\x01",
            "Miss Cecil in a swimsuit!?\x02\x03",
            "#00307FAnd we also have to add\x01",
            "the promising dear Rixia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PC-Calm down.\x02\x03",
            "#00006F...Uhhm, but unexpectedly,\x01",
            "there're many women with\x01",
            "nice figures around us.\x02\x03",
            "#00002FSister Cecil, Rixia, but\x01",
            "Elie is pretty glamor too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PMiss Ilya looks like a model,\x01",
            "and Noｱl and sweet Fran\x01",
            "have their good points.\x02\x03",
            "#00302FWell, as for peTiote and Sullboy,\x01",
            "we can expect things in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PThat's rude, Randy.\x02\x03",
            "#00005FAh...by the way,\x01",
            "can KeA swim?\x02\x03",
            "#00001FI didn't ask her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PHmm, it's something so in the past that\x01",
            "probably she doesn't even remember.\x02\x03",
            "#00300FWell, I guess someone should keep\x01",
            "an eye on her so she doesn't drown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, let's do that.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2434, 255, 80, 0)
    Sleep(800)

    ChrTalk(
        0x105,
        "#1PHu hu, you really are doting parents.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_19CC():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19CC)
    Sleep(50)

    def lambda_19DC():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_19DC)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    SetCameraDistance(19500, 3000)
    OP_68(102000, 1000, 101000, 3000)
    Sleep(500)
    OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(40, 120, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005FWazy...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 140, -1, -1)

    AnonymousTalk(
        0x104,
        "#00305FD-Did you already change?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x105,
        "Yeah, I'll wait outside.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_93(0x105, 0xB4, 0x1F4)
    Sound(2424, 255, 100, 0)
    Sleep(500)
    MoveCamera(325, 18, 0, 4000)

    def lambda_1B2B():

        label("loc_1B2B")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_1B2B")

    QueueWorkItem2(0x101, 2, lambda_1B2B)

    def lambda_1B3D():

        label("loc_1B3D")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_1B3D")

    QueueWorkItem2(0x104, 2, lambda_1B3D)

    def lambda_1B4F():
        OP_95(0xFE, 104270, 0, 97380, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B4F)
    WaitChrThread(0x105, 1)

    def lambda_1B6D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B6D)
    Sound(121, 0, 100, 0)
    Sleep(500)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x105, 1)
    Sound(890, 0, 100, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Fade(500)
    OP_68(100410, 1000, 101610, 0)
    MoveCamera(320, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16640, 0)
    OP_68(100240, 1000, 101490, 0)
    MoveCamera(311, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#00301F#5P──Suspicious.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#6PSuspicious...who, Wazy?\x02\x03",
            "#00012FWell, I think he always\x01",
            "is basically suspicious.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00306F#11PNo, that's not that.\x02\x03",
            "#00303FI mean how he cleverly and quickly\x01",
            "changed while we were chattin'.\x02\x03",
            "Also, that two-piece type swimmin' suit\x01",
            "that can be used both by men and women...\x02\x03",
            "#00301F...Isn't that suspicious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PI don't get at all where\x01",
            "that should be suspicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PJeez, you blockhead.\x02\x03",
            "#00300F...Well, whatever.\x01",
            "Let's change quick too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PRight, it's bad making him wait.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(94150, 1200, 1070, 0)
    MoveCamera(316, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18520, 0)
    SetChrPos(0x101, 94020, 0, 5870, 180)
    SetChrPos(0x104, 94020, 0, 5870, 180)
    SetChrPos(0x105, 94020, 0, 370, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(121, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x8)
    Sleep(300)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_79(0x0)
    OP_68(94380, 1200, 1630, 3500)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(1500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x8)
    Sleep(300)
    Sound(890, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Sound(2088, 255, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "Wazy, sorry for the wait.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sound(2364, 255, 100, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x104,
        "Alright, let's go then.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x105,
        "#12905F#6P............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12505F#5PHuh, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12805F#11PSomething weird?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2429, 255, 100, 0)
    Sleep(600)

    ChrTalk(
        0x105,
        (
            "#12904F#6PWell, I think that there's nothing of\x01",
            "special interest in men's swimsuits.\x02\x03",
            "#12902FWell, your physiques are good,\x01",
            "so I think I wasn't disappointed...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12513F#5PHey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12801F#11PIt's none of your business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12909F#6PHu hu, then, shall we\x01",
            "go to the beach?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_CC(0x1, 0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    ClearMapObjFlags(0x0, 0x1000)
    SetChrChipPat(0x0, 0x1, 0x60)
    LoadChrChipPat()
    SetChrChipPat(0x3, 0x1, 0x61)
    LoadChrChipPat()
    SetChrChipPat(0x4, 0x1, 0x62)
    LoadChrChipPat()
    OP_C7(0x1, 0x17)
    SetChrPos(0x0, 94020, 0, 1060, 90)
    SetScenarioFlags(0x144, 7)
    OP_29(0xA5, 0x1, 0x2)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_13_1112 end

    def Function_14_2331(): pass

    label("Function_14_2331")


    def lambda_2336():
        OP_9B(0x1, 0xFE, 0xA, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2336)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_2331 end

    def Function_15_2356(): pass

    label("Function_15_2356")


    def lambda_235B():
        OP_9B(0x1, 0xFE, 0xFFF6, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_235B)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_2356 end

    def Function_16_237B(): pass

    label("Function_16_237B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03000.itc", 0x1E)
    LoadChrToIndex("apl/ch51322.itc", 0x1F)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrPos(0x101, 100000, 0, 100300, 0)
    SetChrPos(0x104, 100000, 0, 101700, 180)
    SetChrPos(0x105, 109000, 0, 101000, 270)
    SetChrChipByIndex(0x105, 0x1E)
    SetChrSubChip(0x105, 0x0)
    OP_68(100000, 2200, 101000, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18520, 0)
    FadeToBright(1000, 0)
    OP_68(100000, 1200, 101000, 3000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12809F#11PMaaan, I'm beat but I've\x01",
            "appreciated everything a lot.\x02\x03",
            "#12801FHmm, if I were allowed to hope for more,\x01",
            "I would've wished for Miss Cecil and\x01",
            "dear Rixia to join the beach volley!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12505F#6POh, and why is...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1300)
    OP_64(0x101)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#12513F#6PH-Hey, Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12802F#11PHmm, I wonder what little\x01",
            "Lloyd has just imagined...?\x02\x03",
            "#12806FJeez, when it comes to you,\x01",
            "you even shrewdly got to put suntan\x01",
            "on milady, Miss Cecil and Miss Rixia.\x02\x03",
            "#12801FSo, so, how was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512F#6PW-Well...\x02\x03",
            "I can only describe it\x01",
            "as it was amazing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12807F#11PWHAT!?\x02\x03",
            "#12810FDamn you, havin' a\x01",
            "good time all alone, huh!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x0, 0x104, 0x0, 0x3E8, 0xBB8, 0x0)
    Fade(350)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    OP_A1(0x101, 0x3E8, 0x2, 0x0, 0x1)
    OP_63(0x101, 0x96, 1400, 0x28, 0x2B, 0x64, 0x0)
    Sound(908, 0, 70, 0)
    OP_A1(0x101, 0x1F4, 0x6, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3)
    OP_64(0x101)
    OP_0D()

    ChrTalk(
        0x101,
        "#12511F#6PWaah, stop, stop!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 100000, 0, 100300, 90)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 100000, 0, 101000, 180)

    def lambda_27AA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27AA)
    OP_9B(0x1, 0x104, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    WaitChrThread(0x101, 2)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12803F#11P──So, Lloyd?\x02\x03",
            "#12802FWhose swimsuit\x01",
            "struck you the most?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(4131, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#12511F#6PEeeh!?\x02\x03",
            "#12508F(Hmm...\x01",
            "If I had to pick someone...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhose swimsuit was the best?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        100,
        0,
        (
            "Elie\x01",       # 0
            "Tio\x01",        # 1
            "Noｱl\x01",      # 2
            "Fran\x01",       # 3
            "KeA\x01",        # 4
            "Cecil\x01",      # 5
            "Ilya\x01",       # 6
            "Rixia\x01",      # 7
            "Sully\x01",      # 8
            "Randy\x01",      # 9
            "Wazy\x01",       # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2966"),
        (1, "loc_2AD7"),
        (2, "loc_2C12"),
        (3, "loc_2D55"),
        (4, "loc_2EB6"),
        (5, "loc_3045"),
        (6, "loc_3191"),
        (7, "loc_32EB"),
        (8, "loc_345F"),
        (9, "loc_3648"),
        (10, "loc_3798"),
        (SWITCH_DEFAULT, "loc_38F2"),
    )


    label("loc_2966")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12600.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#3C(Hmm, I thought she had\x01",
            "a nice figure before, but...)\x02\x03",
            "(This is troublesome...  I should\x01",
            "pretend I'm not aware of that from\x01",
            "now on when I'm with her for work.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_2AD7")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12700.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#3C(It was a modest swimsuit,\x01",
            "but it was cute....)\x02\x03",
            "(The black one piece looked\x01",
            "pretty on her light skin...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_2C12")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13001.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#3C(As her figure is,\x01",
            "Noｱl was sporty.)\x02\x03",
            "(And yet, how to put it...\x01",
            "She had a charm that\x01",
            "she normally suppresses...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_2D55")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13100.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#3C(Hmm, as I thought, if we're\x01",
            "talking about a lovely figure in\x01",
            "a swimsuit, that would be Fran's.)\x02\x03",
            "(Pink with polka dots...\x01",
            "It matched her air.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_2EB6")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13200.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#3C(Yes, yes, as expected, KeA was\x01",
            "the number one in a swimsuit.)\x02\x03",
            "(Could that swimsuit have been\x01",
            "chosen by Elie and Tio...?)\x02\x03",
            "(It was easy to move and simple,\x01",
            "but stylish in some respects...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_3045")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13300.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#3C(Sister Cecil...\x01",
            "That was probably\x01",
            "a little foul play...)\x02\x03",
            "(I wasn't conscious\x01",
            "of sister Cecil's figure\x01",
            "until now, but...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_3191")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13400.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#3C(Miss Ilya...\x01",
            "As expected, she\x01",
            "looked like a star.)\x02\x03",
            "(Sparkling brilliantly in every\x01",
            "situation... I can understand\x01",
            "why all admires her.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_32EB")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13500.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#3C(Hmm, due to Rixia's stature, that\x01",
            "style was against the rules...)\x02\x03",
            "(Thinking about it, it was like she\x01",
            "was wearing an almost scantily-clad\x01",
            "theatrical costume...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_345F")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13600.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_356A")

    AnonymousTalk(
        0x101,
        (
            "#3C(Ha ha, she acts like a boy,\x01",
            "but she's really a girl.)\x02\x03",
            "(The first time we met \x01",
            "I made an incredible blunder...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3600")

    label("loc_356A")


    AnonymousTalk(
        0x101,
        (
            "#3C(Ha ha, she acts like a boy,\x01",
            "but she's really a girl.)\x02\x03",
            "(When I was introduced to her\x01",
            "the first time, she seemed to be\x01",
            "the opposite, though.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3600")

    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_3648")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12800.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#3C(Still, Randy...\x01",
            "He's really well built.)\x02\x03",
            "(At a closer look, he has many old\x01",
            "scars... Could those be from his\x01",
            "jaeger period?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_3798")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12900.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#3C(Wazy, eh? ...Now that Randy said\x01",
            "that, somehow his swimsuit was\x01",
            "concerning me.)\x02\x03",
            "(A unisex two-piece...\x01",
            "I think it was a simple style.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_38F2")

    label("loc_38F2")

    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#1POh boy, what're you two\x01",
            "bickering about, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12511F#6P!\x02",
    )

    CloseMessageWindow()

    def lambda_3940():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3940)
    Sleep(50)

    def lambda_3950():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3950)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    SetCameraDistance(19500, 3000)
    OP_68(102000, 1000, 101000, 3000)
    Sleep(500)
    OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12505F#5PWazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12805F#5PHey there.\x01",
            "Already changed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12PWell, because you're young\x01",
            "I think there's no helping\x01",
            "getting caught in wild fantasies.\x02\x03",
            "#10302FIf you can afford it a little, a\x01",
            ""remissive" girl is nice, you know?\x02\x03",
            "#10309FSo, I believe it would be perfect if you\x01",
            "made her think you're interested in her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12511F#5PN-No!\x01",
            "We weren't having such a conversation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12801F#5PI mostly agree, but...\x01",
            "Isn't that quite a condescendin' attitude?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#12PYes, that's why I'm popular.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10304F#12PHu hu, I'll go ahead and\x01",
            "return to the hotel room.\x02\x03",
            "#10300FI'd like to take a rest before\x01",
            "going to the theme park.\x02\x03",
            "#10302FAdieu.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xB4, 0x1F4)
    MoveCamera(325, 18, 0, 4000)

    def lambda_3C78():

        label("loc_3C78")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_3C78")

    QueueWorkItem2(0x101, 2, lambda_3C78)

    def lambda_3C8A():

        label("loc_3C8A")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_3C8A")

    QueueWorkItem2(0x104, 2, lambda_3C8A)

    def lambda_3C9C():
        OP_95(0xFE, 104270, 0, 97380, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C9C)
    WaitChrThread(0x105, 1)

    def lambda_3CBA():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CBA)
    Sound(121, 0, 100, 0)
    Sleep(500)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x105, 1)
    Sound(890, 0, 100, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)
    OP_63(0x104, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(100410, 1000, 101610, 0)
    MoveCamera(320, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16640, 0)
    OP_68(100240, 1000, 101490, 0)
    MoveCamera(311, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12807F#11POoh, I can't accept it!\x02\x03",
            "#12806FI failed to check when he was changin'...\x01",
            "What's with this sense of defeat!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12506F#5PWell, maybe he's a too tough opponent.\x02\x03",
            "#12500FIt seems that even now he\x01",
            "goes out at night to do his host\x01",
            "side job when he feels like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12801F#11PHow enviab──\x01",
            "No, that's outrageous!!\x02\x03",
            "#12803FWe must tail him once\x01",
            "and check his behavior!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12512F#5P(That had no persuasive power at all...)\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17720, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Later, after Lloyd and the others returned\x01",
            "to the hotel and had a rest...\x02\x03",
            "They decided to gather at the theme park\x01",
            "after everyone enjoyed their shopping.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrChipPat(0x0, 0x1, 0x0)
    LoadChrChipPat()
    SetChrChipPat(0x3, 0x1, 0x3)
    LoadChrChipPat()
    SetChrChipPat(0x4, 0x1, 0x4)
    LoadChrChipPat()
    OP_C7(0x1, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1080", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_237B end

    def Function_17_405D(): pass

    label("Function_17_405D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5720, 1600, 1240, 0)
    MoveCamera(312, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25730, 0)
    SetChrPos(0x101, -12960, 0, 640, 90)
    SetChrPos(0x153, -12960, 0, 1770, 90)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    LoadChrToIndex("chr/ch48300.itc", 0x20)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 98840, 0, 1140, 270)
    OP_68(-9290, 1100, 1300, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x2, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)

    def lambda_4132():
        OP_97(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4132)
    Sleep(500)

    def lambda_414F():
        OP_97(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_414F)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_71(0x2, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)
    Sleep(500)
    TurnDirection(0x153, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x153,
        (
            "#11P#01105FLloyd, we aren't going\x01",
            "to the theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FWell, that's not that, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        "#6P#00005FSomehow it's quiet...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#6P#00003FEven the receptionist is not here...\x01",
            "Where could she have gone?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6090, 1600, 50, 4000)
    OP_6F(0x1)
    Sleep(100)

    NpcTalk(
        0xE,
        "Woman's Voice",
        "#4P#N#2S...What does this mean...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "Woman's Voice",
        "#4P#N#2S...I-I'm terribly sorry...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x153, 0x5A, 0x0)
    Fade(500)
    OP_68(-9290, 1100, 1300, 0)
    MoveCamera(312, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25730, 0)
    OP_0D()

    ChrTalk(
        0x153,
        "#11P#01105FI can hear some voices...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, it seems they're\x01",
            "quarreling somehow...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x15B, 4)
    SetChrPos(0x0, -9420, 0, 610, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_17_405D end

    def Function_18_43E2(): pass

    label("Function_18_43E2")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch48200.itc", 0x1F)
    LoadChrToIndex("chr/ch48300.itc", 0x20)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0x8, 96490, 0, 1360, 90)
    SetChrPos(0xC, 96150, 0, 60, 90)
    SetChrPos(0xD, 99300, 0, -400, 315)
    SetChrPos(0xE, 98840, 0, 1140, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C27")
    OP_68(96990, 1600, 210, 0)
    MoveCamera(44, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    SetChrPos(0x101, 90240, 0, 570, 90)
    SetChrPos(0x153, 90020, 0, 1390, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "I've finally come to the beach\x01",
            "and I have to go through this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What's this beach\x01",
            "management doing!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I am really sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PI wasn't watching\x01",
            "thoroughly too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "N-Now, now.\x01",
            "They have apologized,\x01",
            "so isn't it fine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You didn't even\x01",
            "get hurt, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No! That won't\x01",
            "satisfy me!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "Excuse me, is something wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(96820, 1700, -360, 0)
    MoveCamera(308, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    TurnDirection(0xD, 0x101, 0)
    TurnDirection(0xC, 0x101, 0)
    TurnDirection(0x8, 0x101, 0)

    def lambda_46E2():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46E2)
    Sleep(200)

    def lambda_46FF():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_46FF)
    Sleep(500)
    WaitChrThread(0x153, 1)

    ChrTalk(
        0x153,
        "#5P#01100FAre you fighting?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PYou're the guests who Miss Mariabell\x01",
            "invited to come to the beach...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, I'm sorry!\x01",
            "I left the reception unattended...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FNo, that's not a problem...\x01",
            "Has something happened here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Of course it has!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When I was swimming at the beach just now,\x01",
            "someone torn my swimsuit!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00005FYour swimsuit was...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, two or three cases of\x01",
            "women swimsuits getting torn have\x01",
            "happened since the beach opening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems it didn't happen this morning\x01",
            "during your reserved time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PWe had heard the rumors too,\x01",
            "but to think it happened to us...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(100)
    TurnDirection(0xE, 0xD, 500)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "A girl had her swimsuit torn and\x01",
            "was given an embarrassing\x01",
            "experience in public, you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Say at least one\x01",
            "complaint too!!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        "#6PE-Even if you tell me that...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "At any rate...\x01",
            "You from Michelam have\x01",
            "to catch the culprit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Or else, I'll sue you\x01",
            "for being responsible!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4B14():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4B14)
    Sleep(100)

    def lambda_4B24():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4B24)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5PT-That would be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PHonestly, it seems hard to do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWe didn't even confirm the\x01",
            "culprit's figure until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#5P#01111F(Hoee...\x01",
            "Somehow it seems terrible.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        "#11P#01100F(Lloyd, why don't you help them?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DAB")

    label("loc_4C27")

    OP_68(96820, 1700, -360, 0)
    MoveCamera(308, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 91240, 0, 570, 90)
    SetChrPos(0x153, 91020, 0, 1390, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "Catch the culprit who has\x01",
            "torn my swimsuit at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Or else, I'll sue you\x01",
            "for being responsible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PT-That would be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PHonestly, it seems hard to do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWe didn't even confirm the\x01",
            "culprit's figure until now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        "#11P#01100F(Lloyd, why don't you help them?)\x02",
    )

    CloseMessageWindow()

    label("loc_4DAB")

    Call(0, 19)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 7230, 0, 790, 270)
    EventEnd(0x5)
    Return()

    # Function_18_43E2 end

    def Function_19_4DD1(): pass

    label("Function_19_4DD1")


    ChrTalk(
        0x101,
        (
            "#5P#00003F(What to do...?\x01",
            "We were heading\x01",
            "to the theme park...)\x02",
        )
    )

    CloseMessageWindow()
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
            "[Help to Look for the Culprit]\x01",      # 0
            "[Quit]\x01",                              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E8D")
    Call(0, 20)
    Jump("loc_4F31")

    label("loc_4E8D")


    ChrTalk(
        0x101,
        (
            "#5P#00003F(We have an appointment\x01",
            "at the theme park...\x01",
            "It's probably none of our business.)\x02\x03",
            "#00000F(Let's leave this to the Michelam\x01",
            "Management Division.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15B, 5)

    label("loc_4F31")

    Return()

    # Function_19_4DD1 end

    def Function_20_4F32(): pass

    label("Function_20_4F32")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00000F...Everyone, could you tell me more\x01",
            "in detail about the incident, if possible?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_500D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_500D)
    Sleep(100)

    def lambda_501D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_501D)
    Sleep(100)

    def lambda_502D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_502D)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5P#00004FAs a policeman,\x01",
            "I can't overlook such \x01",
            "a mean crime.\x02\x03",
            "#00000FI would be able to narrow it\x01",
            "down to a criminal profile...\x01",
            "Will you allow me to help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My...\x01",
            "By all means, please!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#12PHa ha, he says he'll look for the culprit.\x01",
            "Aren't you glad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hmph, break two legs, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PThen, talking in the corridor is not good.\x01",
            "Let's move to the changing room for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FYes, let's do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#11P#01109FDo your best, Lloyd!\x02",
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
            "Quest [The Torn Swimsuit Case]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7E, 0x4, 0x2)
    OP_29(0x7E, 0x1, 0x0)
    OP_68(3220, 1500, 100150, 0)
    MoveCamera(318, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16620, 0)
    SetChrPos(0x101, 3570, 0, 99420, 0)
    SetChrPos(0x153, 4410, 0, 100170, 315)
    SetChrPos(0x8, 1210, 0, 101710, 135)
    SetChrPos(0xC, 840, 0, 100620, 135)
    SetChrPos(0xD, 2970, 0, 102410, 180)
    SetChrPos(0xE, 3930, 0, 102440, 180)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00001FCould you tell me the situation\x01",
            "at the time the incident happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...I was playing in the water at\x01",
            "the beach with my boyfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Tossing the beach ball to each other,\x01",
            "practicing swimming and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then, after some time,\x01",
            "I went to buy something\x01",
            "to drink at the stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "So, while I wasn't watching,\x01",
            "I heard her screams...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When I got back, she\x01",
            "had her swimsuit torn\x01",
            "and was leaning in the lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The people nearby gathered and...\x01",
            "Oh, it was the worst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The watchman there came in a\x01",
            "hurry bringing a towel, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FI understand...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00001FMr. watchman, did you\x01",
            "witness anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I was observing the whole lake, but I\x01",
            "didn't notice anything suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Until I ran after hearing the screams,\x01",
            "I didn't even notice that her swimsuit\x01",
            "had been torn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because there was a commotion,\x01",
            "I tried asking the nearby tourists,\x01",
            "but no one saw the culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Even I, the victim,\x01",
            "didn't see the culprit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "After my boyfriend went to buy something,\x01",
            "I casually walked around but I didn't\x01",
            "notice anyone approaching me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The moment it got cut, I was shocked,\x01",
            "panicked and leaned in the water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FWell, you know...\x01",
            "That can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00001FHave there been any eyewitnesses\x01",
            "of the torn incidents until now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No. They all happened on the\x01",
            "foreshore like this time, but\x01",
            "nobody saw any culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is just that every time the swimsuits\x01",
            "are torn by something like an edged tool...\x01",
            "It is hard to think they are accidents...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Also, it's natural to think it's the\x01",
            "same culprit since every time it\x01",
            "happens it uses the same method...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But even looking at the register of the customers' names, \x01",
            "the same people never come during the incidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "When you start forgetting that\x01",
            "it may have been an accident,\x01",
            "it ends up happening again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FI see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        "#12P#01111FLloyd, do you think you can figure out the culprit?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "Now now, little miss,\x01",
            "it's not good urging him on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even if he's a policeman, there's\x01",
            "no way he could figure that out\x01",
            "just by listening to those stor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...No, I've got an idea\x01",
            "about the criminal profile.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        "S-Seriously!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You can without even\x01",
            "inspecting the site?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FNaturally there would normally be the need, but...\x01",
            "I think there won't be any important evidence.\x02\x03",
            "#00001FSince the site is the foreshore, now that\x01",
            "time has passed from when it happened, it's very\x01",
            "likely evidence has been cancelled by the waves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I-Indeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, you say you figured out the\x01",
            "culprit only based on those stories?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes. If I combine all the stories I heard \x01",
            "from you all until now and think about them, \x01",
            "a criminal profile comes to my mind naturally.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#12P#01109FLloyd, you're cool!\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    ChrTalk(
        0xE,
        (
            "Don't give yourself such\x01",
            "airs and answer me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Who in the world is \x01",
            "the culprit that...\x01",
            "Torn my swimsuit?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00001F(There're no eyewitnesses\x01",
            "and all the criminal acts until now\x01",
            "have been done on the waterside...)\x02\x03",
            "(And also, the swimsuits\x01",
            "have been torn by an\x01",
            "edged-tool-like thing.)\x02\x03",
            "#00003F(All this considered,\x01",
            "the culprit probably is...)\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6366")
    Sleep(500)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThe culprit of the Torn Swimsuits Case is?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "The Victim Herself\x01",           # 0
            "The Victim's Boyfriend\x01",       # 1
            "The Watchman\x01",                 # 2
            "Someone Else Completely\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6201")

    ChrTalk(
        0x101,
        (
            "#6P#00003FJudging from the situation,\x01",
            "the culprit isn't anyone here\x01",
            "nor one of the other tourists.\x02\x03",
            "#00001FMost likely, the culprit\x01",
            "is lurking on the beach...\x01",
            "I think it's some kind of "monster".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61FC")
    OP_2C(0x7E, 0x1)

    label("loc_61FC")

    Jump("loc_6361")

    label("loc_6201")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#6P#00003F(No, situation wise, that person\x01",
            "can't be the culprit. \x01",
            "...Let's try to think things over.)\x02\x03",
            "#00001F(There're no eyewitnesses\x01",
            "and all the criminal acts until now\x01",
            "have been done on the waterside...)\x02\x03",
            "(And also, the swimsuits\x01",
            "have been torn by an\x01",
            "edged-tool-like thing.)\x02\x03",
            "#00003F(Thinking about this,\x01",
            "the culprit is probably...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6361")

    Jump("loc_6056")

    label("loc_6366")

    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "A m-monster...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You want to say that a monster has\x01",
            "torn my girlfriend's swimsuit!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I-Isn't it too much of\x01",
            "an offbeat story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Where's the proofs, the proofs!!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FI'll tell you in order.\x02\x03",
            "#00003FFirst of all, the\x01",
            "torn swimsuit...\x02\x03",
            "#00001FIt seems it was torn by an\x01",
            "edged-tool-like thing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Y-Yes...\x01",
            "It seemed so in all the incidents until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FThen, I'll ask you...\x01",
            "Is it possible to "bring in"\x01",
            "something like that at this beach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "N-No...\x01",
            "That would be hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I advise that at the reception\x01",
            "and I strictly check...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, for security reasons\x01",
            "we staff too carry a portable\x01",
            "simple metal detector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's why I can't really\x01",
            "get it how something like\x01",
            "that could've been brought...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "............Ah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000F...Exactly, in other words...\x01",
            "The culprit didn't "bring\x01",
            "in an edged-tool".\x02\x03",
            "#00003FProbably, the body of the culprit\x01",
            "itself is "equipped beforehand"\x01",
            "with a weapon that tears swmisuits...\x02\x03",
            "#00001FProbably... Something like\x01",
            "sharp claws or teeth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "A-And that would be the argument\x01",
            "to make a monster the culprit...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FNo, this is solely a very\x01",
            "strange conceptualization.\x02\x03",
            "#00000FHowever, combining together other elements...\x01",
            "It will start to gradually gain authenticity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Other elements...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FFirst of all, this incident seems\x01",
            "to have many features in common\x01",
            "with the torn incidents up to now.\x02\x03",
            "#00003FThe fact that there're no eyewitnesses...\x01",
            "The fact the crime happened by the shore...\x01",
            "The method being completely the same...\x02\x03",
            "#00001FJudging from those too,\x01",
            "it's highly possible the culprit is the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, nevertheless, in the register of names \x01",
            "there is no guest who consistently comes\x01",
            "at the time of the incidents...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00003FRight, and that means that...\x01",
            "The culprit isn't among the customers\x01",
            "who entered via regular means.\x02\x03",
            "#00000FAlso, since a watchman is present,\x01",
            "it can't even enter via the lake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, as you can imagine, I'd notice if\x01",
            "there were such a guy who tried to slip in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FAll that considered...\x01",
            "The culprit has only one route\x01",
            "it can use to show up on the site.\x02\x03",
            "The Elm Lake's offing...\x01",
            "It's possible it's an aquatic monster\x01",
            "whose habitat is nearby there.\x02\x03",
            "#00003FThen, in case of a small type aquatic monster,\x01",
            "it should be able to approach the people\x01",
            "at the beach without the watchman \x01",
            "noticing it by swimming underwater.\x02\x03",
            "#00001FIn other words...\x01",
            "This incident couldn't have\x01",
            "happened in any other way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "S-So this incident was\x01",
            "only caused by a monster...\x01",
            "Is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It seems it makes sense...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "W-Wait a moment.\x01",
            "Aren't you forgetting anything important?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Why the likes of a monster\x01",
            "have the need to tear a\x01",
            "girl's swimsuit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "T-That's true too...\x01",
            "What do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Couldn't it be really...\x01",
            "The act of a maniac?\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FA-As you'd expect I don't\x01",
            "know its motive, but...\x02\x03",
            "#00001FIt doesn't change the fact\x01",
            "that it was a monster that\x01",
            "caused the incident.\x02\x03",
            "#00003FAnd that leaves us at\x01",
            "present with a "monster\x01",
            "that has such trait"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But...\x01",
            "What should we do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If a monster appears frequently,\x01",
            "it will be tied with the credit of the\x01",
            "Michelam Management Division too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish we could somehow exterminate\x01",
            "it with this occasion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "But our opponent is an elusive one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If we wait until it shows up,\x01",
            "we won't be able to operate\x01",
            "the beach at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uhhm, I am a victim too, so\x01",
            "I don't really want to come\x01",
            "again until it's safe.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x153)
    Sleep(500)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#12P#01100FThen...\x01",
            "Should KeA be a bait?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_72C6():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72C6)
    Sleep(100)

    def lambda_72D6():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_72D6)
    Sleep(100)

    def lambda_72E6():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_72E6)
    Sleep(100)

    def lambda_72F6():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_72F6)
    Sleep(100)

    def lambda_7306():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7306)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00011FK-KeA, what're you saying!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01105FBut, that monster tears\x01",
            "girls' swimsuits, right?\x02\x03",
            "#01103FIf KeA plays by the shore,\x01",
            "maybe it will come out again.\x02\x03",
            "#01109FAnd if when that happens Lloyd\x01",
            "protects KeA, it'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FH-Hey, listen...\x01",
            "There's no way I'd have you go\x01",
            "through such danger, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "H-He's right, little miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Only swimsuits were torn until now,\x01",
            "but we don't know what will happen next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108FHmm, but...\x01",
            "If the monster keeps being around like this,\x01",
            "it'll put Bell in trouble, right?\x02\x03",
            "#01106FI want to exterminate it in some way\x01",
            "as thanks for having invited us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FI-I get your point, but still...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00003F...All right.\x02\x03",
            "#00001FI don't know if your plan\x01",
            "will succeed or not, but\x01",
            "we can only try doing it.\x02\x03",
            "#00003FHowever, KeA, you won't be the bait,\x01",
            "we'll rely on someone else among us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01101FYes!\x02",
    )

    CloseMessageWindow()

    def lambda_76B3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_76B3)
    Sleep(100)

    def lambda_76C3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_76C3)
    Sleep(100)

    def lambda_76D3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_76D3)
    Sleep(100)

    def lambda_76E3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_76E3)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "No way...\x01",
            "Will she be fine?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, the Support Section's members\x01",
            "are used to fight against monsters too...\x01",
            "It won't be anything serious.\x02\x03",
            "#00003FThe problem is, \x01",
            "who will do the bait...\x02\x03",
            "#00000FIt seems I could rely on Elie,\x01",
            "Tio or Noｱl's help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01105FLloyd, who will you call?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00003FLet's see...\x02",
    )

    CloseMessageWindow()
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
            "#1KWho will you rely on to be the bait?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Elie]\x01",       # 0
            "[Tio]\x01",        # 1
            "[Noｱl]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_78E9"),
        (1, "loc_791F"),
        (2, "loc_7954"),
        (SWITCH_DEFAULT, "loc_798A"),
    )


    label("loc_78E9")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x15B, 6)

    ChrTalk(
        0x101,
        "#6P#00000F...I'll rely on Elie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_798A")

    label("loc_791F")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x15B, 7)

    ChrTalk(
        0x101,
        "#6P#00000F...I'll rely on Tio.\x02",
    )

    CloseMessageWindow()
    Jump("loc_798A")

    label("loc_7954")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C4, 5)

    ChrTalk(
        0x101,
        "#6P#00000F...I'll rely on Noｱl.\x02",
    )

    CloseMessageWindow()
    Jump("loc_798A")

    label("loc_798A")


    ChrTalk(
        0x153,
        "#12P#01109FYes, in this case, everything should be all right!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00003FFor these reasons...\x01",
            "I would like to start the monster\x01",
            "extermination at the beach now.\x02\x03",
            "#00000FEveryone from the staff, could you\x01",
            "please clear out the people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Let's make it a temporary\x01",
            "inspection and have the\x01",
            "tourists evacuate for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Be careful you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "See that you beat to a pulp the\x01",
            "monster that tore my swimsuit!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00000FYes, please leave it to us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01109FThen, let's gooo!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_7BCF")
    AddParty(0x1, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x1)
    Jump("loc_7BF1")

    label("loc_7BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_7BE7")
    AddParty(0x2, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x2)
    Jump("loc_7BF1")

    label("loc_7BE7")

    AddParty(0x8, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x3)

    label("loc_7BF1")

    SetScenarioFlags(0x22, 3)
    NewScene("t1310", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_4F32 end

    def Function_21_7BFE(): pass

    label("Function_21_7BFE")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1330, 3100, 1380, 0)
    MoveCamera(318, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch48200.itc", 0x1F)
    LoadChrToIndex("chr/ch48300.itc", 0x20)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0x101, -3160, 0, 1570, 45)
    SetChrPos(0x153, -2960, 0, -40, 45)
    SetChrPos(0xEF, -4480, 0, 1090, 45)
    SetChrPos(0xC, 490, 0, 1750, 270)
    SetChrPos(0xD, -570, 0, -680, 315)
    SetChrPos(0xE, -390, 0, 320, 315)
    SetChrPos(0x8, -2000, 0, 5150, 180)
    OP_68(-1330, 1600, 1380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x8,
        "Thank you for your hard work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because of you, it seems that it ended without\x01",
            "Michelam Management Division losing credit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHa ha, we're honored to have been of help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thank you very much.\x01",
            "I don't know how we should thank you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Furthermore, I will report to Lady\x01",
            "Mariabell about the developments\x01",
            "and the monster appearances.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_7EB4")

    ChrTalk(
        0x102,
        "#00100FYes, that would be fine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F07")

    label("loc_7EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_7EE5")

    ChrTalk(
        0x103,
        "#00200FThat is probably fine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F07")

    label("loc_7EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_7F07")

    ChrTalk(
        0x109,
        "#10100FYes, please.\x02",
    )

    CloseMessageWindow()

    label("loc_7F07")


    ChrTalk(
        0x101,
        (
            "#00000FHa ha, I think that Miss Mariabell will\x01",
            "come up with a countermeasure or another.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        "#12PUh uh, thank you for hard work㈱\x02",
    )

    CloseMessageWindow()

    def lambda_7F9E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F9E)
    Sleep(100)

    def lambda_7FAE():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7FAE)
    Sleep(100)

    def lambda_7FBE():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_7FBE)
    Sleep(100)

    def lambda_7FCE():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7FCE)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#12PYou were able to exterminate the monster that\x01",
            "was the culprit of the torn swimsuit incidents.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#12PAlright, being that the case, let's go\x01",
            "to continue with our beach fun!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#6PEeeh, do you want to go again!?\x01",
            "I thought you learned your lesson...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PIsn't it obvious!?\x01",
            "We've come all the way here,\x01",
            "we have to have fun.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#12PUh uh, then, we will\x01",
            "excuse ourselves here.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 3, 0, 22)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 23)
    Sleep(2000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)
    TurnDirection(0xC, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#12PThen, I'll go back to my\x01",
            "watchman work too.\x01",
            "Thanks guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0xC, 0xB4, 0x1388, 0x7D0, 0x0)
    Sleep(1000)
    OP_68(-3510, 1300, 960, 3000)
    OP_6F(0x1)
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000FAlright, should\x01",
            "we go too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        "#6P#01100FYes!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_82C8")

    ChrTalk(
        0x102,
        (
            "#00104FI'll go have a look at the\x01",
            "boutique a little more.\x02\x03",
            "#00100F*giggle*, see you later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83BE")

    label("loc_82C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_8354")

    ChrTalk(
        0x103,
        (
            "#00204FI will go on ahead\x01",
            "to the theme park.\x02\x03",
            "#00202FI am making Zeit and Miss Sully wait,\x01",
            "so I will excuse myself here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83BE")

    label("loc_8354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_83BE")

    ChrTalk(
        0x109,
        (
            "#10100FI'll go looking at the jewelry\x01",
            "a little more with Fran.\x02\x03",
            "#10109FThen, see you later!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83BE")


    def lambda_83C3():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_83C3)
    Sleep(200)

    def lambda_83D3():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_83D3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FYeah, later then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01109FSee you!\x02",
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
            "Quest [The Torn Swimsuit Case]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7E, 0x1, 0x4)
    OP_29(0x7E, 0x1, 0x5)
    OP_29(0x7E, 0x4, 0x10)
    OP_32(0xFF, 0xFE, 0x0)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_849E")
    RemoveParty(0x1, 0xFF)
    Jump("loc_84BB")

    label("loc_849E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_84AF")
    RemoveParty(0x2, 0xFF)
    Jump("loc_84BB")

    label("loc_84AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_84BB")
    RemoveParty(0x8, 0xFF)

    label("loc_84BB")

    EventEnd(0x5)
    SetScenarioFlags(0x22, 1)
    NewScene("t1020", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_21_7BFE end

    def Function_22_84CA(): pass

    label("Function_22_84CA")

    OP_95(0xE, 4990, 0, 50, 2000, 0x0)
    OP_95(0xE, 6570, 0, 1030, 2000, 0x0)
    OP_95(0xE, 10000, 0, 1020, 2000, 0x0)
    Return()

    # Function_22_84CA end

    def Function_23_8507(): pass

    label("Function_23_8507")

    OP_95(0xD, 4990, 0, 50, 2000, 0x0)
    OP_95(0xD, 6570, 0, 1030, 2000, 0x0)
    OP_95(0xD, 10000, 0, 1020, 2000, 0x0)
    Return()

    # Function_23_8507 end

    def Function_24_8544(): pass

    label("Function_24_8544")

    EventBegin(0x2)
    ClearMapFlags(0x20)
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
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_24_8544 end

    SaveToFile()

Try(main)
