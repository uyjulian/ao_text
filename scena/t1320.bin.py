from ScenarioHelper import *

def main():
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
        "Receptionist Carmina",         # 1
        "tourist",                 # 2
        "tourist",                 # 3
        "tourist",                 # 4
        "Watcher Wave",         # 5
        "tourist",                 # 6
        "tourist",                 # 7
        "Swimsuit catalog",           # 8
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
        "Function_5_843",          # 05, 5
        "Function_6_894",          # 06, 6
        "Function_7_8D9",          # 07, 7
        "Function_8_A03",          # 08, 8
        "Function_9_B78",          # 09, 9
        "Function_10_CB6",         # 0A, 10
        "Function_11_DC2",         # 0B, 11
        "Function_12_E34",         # 0C, 12
        "Function_13_1009",        # 0D, 13
        "Function_14_218A",        # 0E, 14
        "Function_15_21AF",        # 0F, 15
        "Function_16_21D4",        # 10, 16
        "Function_17_3D69",        # 11, 17
        "Function_18_40D1",        # 12, 18
        "Function_19_4A5B",        # 13, 19
        "Function_20_4BBE",        # 14, 20
        "Function_21_7357",        # 15, 21
        "Function_22_7B96",        # 16, 22
        "Function_23_7BD3",        # 17, 23
        "Function_24_7C10",        # 18, 24
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_836")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A1")

    ChrTalk(
        0x8,
        (
            "It repels the swimsuit ripping demon,\x01",
            "I'm really thankful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because the opponent is a monster,\x01",
            "It is said that it came out completely\x01",
            "It may not be possible to say … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the future, the Michelam Business Division\x01",
            "I have to take countermeasures.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_831")

    label("loc_7A1")


    ChrTalk(
        0x8,
        (
            "It repels the swimsuit ripping demon,\x01",
            "I'm really thankful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the future, the Michelam Business Division\x01",
            "I have to take countermeasures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_831")

    Jump("loc_83F")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_83F")

    label("loc_83F")

    TalkEnd(0x8)
    Return()

    # Function_4_68A end

    def Function_5_843(): pass

    label("Function_5_843")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Now I'm picking a swimsuit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… I hope he decides quickly.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_843 end

    def Function_6_894(): pass

    label("Function_6_894")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Yeah, there are so many cute swimsuits.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what to do ~.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_894 end

    def Function_7_8D9(): pass

    label("Function_7_8D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_999")
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Wow ah! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, in a men's changing room\x01",
            "Do not put in girls! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FThat's right.\x01",
            "… …. I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105FWow?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_9FF")

    label("loc_999")


    ChrTalk(
        0xFE,
        (
            "Well, totally …\x01",
            "There is no disconnection and skiing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In danger, ass to a girl\x01",
            "It was almost seen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FF")

    TalkEnd(0xFE)
    Return()

    # Function_7_8D9 end

    def Function_8_A03(): pass

    label("Function_8_A03")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Attention on enjoying a lake bath\x01",
            "─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\x01",
            "· Be sure to prepare exercise.\x01",
            "· Please do not enter water while wearing clothes.\x01",
            "(Swimwear is available for rent at the reception desk)\x01",
            "· Follow the instructions of the observer.\x01",
            "─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\x01",
            "Let's keep good manners and have fun.\x01",
            "─ ─ From the Michelam Division\x07\x00\x02",
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

    # Function_8_A03 end

    def Function_9_B78(): pass

    label("Function_9_B78")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCA")

    ChrTalk(
        0x101,
        (
            "#12500F…… This is a girls changing room.\x01",
            "Let's not get misunderstood inside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C66")

    ChrTalk(
        0x101,
        (
            "#00000F…… っ て.\x01",
            "This is a girls changing room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105FLloyd, are you going in?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FNo, no, I will not enter.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CA2")

    label("loc_C66")


    ChrTalk(
        0x101,
        (
            "#00000FThis is a girls changing room.\x01",
            "…… Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA2")

    SetChrPos(0x0, 104470, 0, 2310, 180)
    EventEnd(0x4)
    Return()

    # Function_9_B78 end

    def Function_10_CB6(): pass

    label("Function_10_CB6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1E")

    ChrTalk(
        0x101,
        (
            "#00000FI have not borrowed bathing suit yet\x01",
            "I can not go on ahead.\x02\x03",
            "Let 's finish the reception first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAE")

    ChrTalk(
        0x101,
        (
            "#00003FI do not have time to enter the beach again.\x02\x03",
            "#00000FShall I head for a theme park soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYeah, it's getting stuck! It is!\x02",
    )

    CloseMessageWindow()

    label("loc_DAE")

    SetChrPos(0x0, 7010, 0, 1020, 270)
    EventEnd(0x4)
    Return()

    # Function_10_CB6 end

    def Function_11_DC2(): pass

    label("Function_11_DC2")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FOops, this dress is not so much\x01",
            "I can not afford to do it.\x02\x03",
            "Let's go to the beach quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 91160, 0, 690, 90)
    EventEnd(0x4)
    Return()

    # Function_11_DC2 end

    def Function_12_E34(): pass

    label("Function_12_E34")

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
            "#00002F#5POh\x01",
            "Is this the beach reception?\x02\x03",
            "#00000FHere as well as swimsuits\x01",
            "I think I can borrow it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#5PNo, this place is\x01",
            "Why is it made?\x01",
            "I never thought of dreaming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHuff, immediately,\x01",
            "Shall I accept my reception?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -8000, 0, 1130, 90)
    SetScenarioFlags(0x144, 6)
    EventEnd(0x5)
    Return()

    # Function_12_E34 end

    def Function_13_1009(): pass

    label("Function_13_1009")

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
            "#11PHello,\x01",
            "Welcome Lake Baths#8RLake beach#What.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe people of the mission support department\x01",
            "Do you Come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6POh, yes we are\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PMaria Bell's girlfriend\x01",
            "You told me to tell it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes, until today's afternoon\x01",
            "It is a reservation.\x02",
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
            "#11PAbout bathing suits, this direction\x01",
            "Photo#4Rsample#We prepared\x01",
            "Please choose your favorite one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6POh, well in that case\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PWell then, which one is ruined.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F#6PHmm.\x02",
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
            "#00316F#11PBut Lloyd\x02\x03",
            "#00315FAfter entering the Special Affairs Support Division\x01",
            "It's the biggest reward! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PTh-that's an exaggeration\x02\x03",
            "#00002FSurely everyone,\x01",
            "What kind of clothes will you come up with?\x01",
            "I am looking forward for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PThat's right, yeah.\x02\x03",
            "#00301FAnd Iria and\x01",
            "Cecil's swimsuit! Is it?\x02\x03",
            "#00307FIn addition, it looks like Lisa-chan\x01",
            "There are super promising stocks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PC-calm down\x02\x03",
            "#00006F…… Hmm, but what do you care?\x01",
            "Surrounding us\x01",
            "Many women with good style.\x02\x03",
            "#00002FEven Cecil's older sister and Leisha\x01",
            "Ellie is also quite glamorous … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PIria seems to be a model,\x01",
            "Noel and Franan also\x01",
            "I'm getting out of Toko.\x02\x03",
            "#00302FWell Tio Suzuki and Shri Elephant\x01",
            "By doing what you expect from now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PThat's rude, Randy\x02\x03",
            "#00005FOh, that's right.\x01",
            "Can I swim with Ka'a?\x02\x03",
            "#00001FI didn't ask her \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11POh, it's a long time ago,\x01",
            "I do not remember him or her.\x02\x03",
            "#00300FFor once, do not get drowned\x01",
            "It might be better to see someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, lets check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2434, 255, 80, 0)
    Sleep(800)

    ChrTalk(
        0x105,
        "#1PEhe, you guys are really overly concerned parents\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_187B():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_187B)
    Sleep(50)

    def lambda_188B():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_188B)
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
        "#00005FWazy…?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 140, -1, -1)

    AnonymousTalk(
        0x104,
        "#00305FYou already changed?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x105,
        "Yeah. I'll be waiting outside\x02",
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

    def lambda_19D9():

        label("loc_19D9")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_19D9")

    QueueWorkItem2(0x101, 2, lambda_19D9)

    def lambda_19EB():

        label("loc_19EB")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_19EB")

    QueueWorkItem2(0x104, 2, lambda_19EB)

    def lambda_19FD():
        OP_95(0xFE, 104270, 0, 97380, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_19FD)
    WaitChrThread(0x105, 1)

    def lambda_1A1B():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A1B)
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
        "#00301F#5PSuspicious…\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#6PSuspicious? Wazy?\x02\x03",
            "#00012FWell, basically\x01",
            "I think it is a suspicious guy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00306F#11PNo not that\x02\x03",
            "#00303FWhile we are talking\x01",
            "Beautiful things to change quickly.\x02\x03",
            "And it also becomes unisex\x01",
            "Separate type swimsuit …\x02\x03",
            "#00301FIsn't it suspicious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PWhere is it suspicious?\x01",
            "I do not understand Sappari ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PWell, Park#6RBokunenjin#Me\x02\x03",
            "#00300FWell, whatever.\x01",
            "Let 's change clothes soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PRight, we shouldn't make him wait\x02",
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
        "Wazy, sorry for the wait\x02",
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
        "Yo, ok let's go\x02",
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
        "#12905F#6P….\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12505F#5PW-what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12805F#11PIs something the matter?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2429, 255, 100, 0)
    Sleep(600)

    ChrTalk(
        0x105,
        (
            "#12904F#6PNo, the man's swimming suit appearance\x01",
            "I thought that it was not fun.\x02\x03",
            "#12902FWell, for both of you, your physique is good\x01",
            "Do you think you are disappointed?\x02",
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
        "#12513F#5PYou know…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12801F#11PNo need for that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12909F#6PHuh, then\x01",
            "Shall I go out to the beach?\x02",
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

    # Function_13_1009 end

    def Function_14_218A(): pass

    label("Function_14_218A")


    def lambda_218F():
        OP_9B(0x1, 0xFE, 0xA, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_218F)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_218A end

    def Function_15_21AF(): pass

    label("Function_15_21AF")


    def lambda_21B4():
        OP_9B(0x1, 0xFE, 0xFFF6, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21B4)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_21AF end

    def Function_16_21D4(): pass

    label("Function_16_21D4")

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
            "#12809F#11PNo, I was tired.\x01",
            "Absolutely proficient#4RAge#I let you know.\x02\x03",
            "#12801FWell, if you want a greed\x01",
            "Also for Cecil and Lisha\x01",
            "I wanted you to participate in the beach volleyball!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12505F#6PHuh, why\x02",
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
        "#12513F#6PCome on Randy\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12802F#11PHmm, Lloyd's Kun\x01",
            "What did you imagine?\x02\x03",
            "#12806FWant to be with you\x01",
            "Shut up lady and Cecil's\x01",
            "I'm painting sunscreen.\x02\x03",
            "#12801FSo how was it\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512F#6PNo~……\x02\x03",
            "I was only amazing\x01",
            "I can not say it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12807F#11PAnd ~! Is it?\x02\x03",
            "#12810FThis ~, only one person\x01",
            "Have fun with delicious eyes!\x02",
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
        "#12511F#6PAhh, I give up I give up!\x02",
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

    def lambda_25E6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25E6)
    OP_9B(0x1, 0x104, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    WaitChrThread(0x101, 2)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12803F#11PSo Lloyd\x02\x03",
            "#12802FWhose swimwear figure\x01",
            "You got the biggest thing?\x02",
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
            "#12511F#6PHUH!?\x02\x03",
            "#12508F(Well ….\x01",
            "Even if someone told me …).\x02",
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
            "#1KWhose swimwear figure was the best?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        100,
        0,
        (
            "Erie\x01",        # 0
            "Tio\x01",        # 1
            "Noel\x01",        # 2
            "Franc\x01",        # 3
            "Keya\x01",        # 4
            "Cecil\x01",        # 5
            "Ilia\x01",        # 6
            "Lisha\x01",      # 7
            "Shuri\x01",        # 8
            "Randy\x01",      # 9
            "Waji\x01",          # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27BB"),
        (1, "loc_290E"),
        (2, "loc_2A4C"),
        (3, "loc_2BA3"),
        (4, "loc_2CEA"),
        (5, "loc_2E6D"),
        (6, "loc_2FB4"),
        (7, "loc_30FE"),
        (8, "loc_324C"),
        (9, "loc_3418"),
        (10, "loc_355A"),
        (SWITCH_DEFAULT, "loc_36A6"),
    )


    label("loc_27BB")

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
            "#3C(Well, what is style?\x01",
            "I thought it from before … …)\x02\x03",
            "(troubled……\x01",
            "From now on at the same time at work\x01",
            "I hope not to be conscious. )\x02",
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
    Jump("loc_36A6")

    label("loc_290E")

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
            "#3C(Although it was a modest swim suit,\x01",
            "It was a pretty feeling … …)\x02\x03",
            "(Black dress on fair skin\x01",
            "It was shining … …)\x02",
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
    Jump("loc_36A6")

    label("loc_2A4C")

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
            "#3C(Noel is as imagined\x01",
            "It was sporty feeling. )\x02\x03",
            "(And yet what is it?\x01",
            "The charm that was usually suppressed\x01",
            "I mean playing … …)\x02",
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
    Jump("loc_36A6")

    label("loc_2BA3")

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
            "#3C(Well, after all\x01",
            "When I say pretty swimsuit\x01",
            "Is it frank? )\x02\x03",
            "(Pink polka dots ……\x01",
            "It fits the atmosphere of her. )\x02",
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
    Jump("loc_36A6")

    label("loc_2CEA")

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
            "#3CYeah yeah, after all\x01",
            "Ka'a's swimsuit shape is the best. )\x02\x03",
            "(That swimwear, Eli and Tio are\x01",
            "Did you make it look? )\x02\x03",
            "(It's easy to move and simple, but\x01",
            "I mean something stylish … …)\x02",
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
    Jump("loc_36A6")

    label("loc_2E6D")

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
            "#3C(Cecil elder sister ….\x01",
            "That is a bit irregular … …)\x02\x03",
            "(Up to now\x01",
            "Cecil's older sister's style and\x01",
            "I was not conscious … …)\x02",
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
    Jump("loc_36A6")

    label("loc_2FB4")

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
            "#3C(Mr. Ilya … ….\x01",
            "After all I feel like a star. )\x02\x03",
            "(Shine glittering at any time … …\x01",
            "I am convinced that everyone admires. )\x02",
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
    Jump("loc_36A6")

    label("loc_30FE")

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
            "#3C(Well, with Lisha's height\x01",
            "That style is irregular … …)\x02\x03",
            "(If you think about it, the degree of exposure close to that\x01",
            "I am wearing a stage costume … …)\x02",
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
    Jump("loc_36A6")

    label("loc_324C")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_335B")

    AnonymousTalk(
        0x101,
        (
            "#3C(Hey, like a boy, but\x01",
            "After all it is a girl. )\x02\x03",
            "(When it is first time face, in an unexpected form\x01",
            "I made a mistake … ….)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D0")

    label("loc_335B")


    AnonymousTalk(
        0x101,
        (
            "#3C(Hey, like a boy, but\x01",
            "After all it is a girl. )\x02\x03",
            "(When first introduced,\x01",
            "Although it seemed to be wrong. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D0")

    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_3418")

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
            "#3C(But Randy … ….\x01",
            "As expected after all, you can do it. )\x02\x03",
            "(If you look closely, there are many old wounds ……\x01",
            "I wonder if it hit the hunting era? )\x02",
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
    Jump("loc_36A6")

    label("loc_355A")

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
            "#3C(Was it … Well if I were told\x01",
            "It is some swimsuit you care about. )\x02\x03",
            "(Separate unisex dual use ……\x01",
            "I think that it is just a hobby. )\x02",
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
    Jump("loc_36A6")

    label("loc_36A6")

    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#1PWhew, two men\x01",
            "What do you mean by jar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12511F#6PAh\x02",
    )

    CloseMessageWindow()

    def lambda_36FA():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_36FA)
    Sleep(50)

    def lambda_370A():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_370A)
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
        "#12505F#5PWazy\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12805F#5PCome on.\x01",
            "Did you change your clothes already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12PWell, because I am young\x01",
            "Inflating the delusion is\x01",
            "I think that it can not be helped.\x02\x03",
            "#10302FWho could afford a little more\x01",
            "Is not it good for girls' uke?\x02\x03",
            "#10309FOn top of that, if you are interested in the other party\x01",
            "It is perfect if it makes me think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12511F#5PNo!\x01",
            "I was talking about that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12801F#5PGenerally agree … …\x01",
            "It is quite a line of sight from the top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#12PYeah well I'm popular\x02",
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
            "#10304F#12PHuff, one step ahead\x01",
            "I am back in the hotel room.\x02\x03",
            "#10300FBefore going to the theme park\x01",
            "I want to take a break.\x02\x03",
            "#10302FAdeu#8RWell then#.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xB4, 0x1F4)
    MoveCamera(325, 18, 0, 4000)

    def lambda_39E3():

        label("loc_39E3")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_39E3")

    QueueWorkItem2(0x101, 2, lambda_39E3)

    def lambda_39F5():

        label("loc_39F5")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_39F5")

    QueueWorkItem2(0x104, 2, lambda_39F5)

    def lambda_3A07():
        OP_95(0xFE, 104270, 0, 97380, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A07)
    WaitChrThread(0x105, 1)

    def lambda_3A25():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A25)
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
            "#12807F#11POHH I CAN'T HANDLE IT!\x02\x03",
            "#12806FI did not check the change of clothes\x01",
            "What is this defeat feeling! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12506F#5PWell it's probably the people he deals with\x02\x03",
            "#12500FIf I still feel like it\x01",
            "In the evening, I went to a host byte\x01",
            "He seems to be out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12801F#11PHow envious ----\x01",
            "Rather than Quecharan!\x02\x03",
            "#12803FWell, once in a while\x01",
            "I have to check the rows!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12512F#5P(He seems totally jealous)\x02",
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
            "After that, Lloyd's\x01",
            "After returning to the hotel and taking a rest … ….\x02\x03",
            "After enjoying shopping etc. respectively\x01",
            "I decided to gather before the theme park.\x07\x00\x02",
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

    # Function_16_21D4 end

    def Function_17_3D69(): pass

    label("Function_17_3D69")

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

    def lambda_3E3E():
        OP_97(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E3E)
    Sleep(500)

    def lambda_3E5B():
        OP_97(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3E5B)
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
            "#11P#01105FIn Lloyd and theme park\x01",
            "Are not you going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FNo we are but\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        "#6P#00005FWhat's going on here?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#6P#00003FThere are no people at the reception desk ……\x01",
            "Where the hell did you go?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6090, 1600, 50, 4000)
    OP_6F(0x1)
    Sleep(100)

    NpcTalk(
        0xE,
        "Female voice",
        "#4P#N#2SWhat is this!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "Female voice",
        "#4P#N#2SI-I'm so sorry!\x02",
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
        "#11P#01105FI hear someone\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FOh, somehow\x01",
            "It looks like I'm tormenting … ….\x02",
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

    # Function_17_3D69 end

    def Function_18_40D1(): pass

    label("Function_18_40D1")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C6")
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
            "On the beach we came\x01",
            "I do not see such an eye …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As for this beach management\x01",
            "What's going on! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm terribly sorry\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PI am well watched\x01",
            "He was not there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, alright.\x01",
            "I apologize for it.\x01",
            "It's fine, is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even though I was injured\x01",
            "I do not understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Is not it, such a thing\x01",
            "I do not feel disappointed!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        "Uh, what's wrong?\x02",
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

    def lambda_43D3():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43D3)
    Sleep(200)

    def lambda_43F0():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_43F0)
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
            "#12PYou came to the beach,\x01",
            "Mary Bell's invited guest … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, I'm sorry!\x01",
            "I left the reception open …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FNo, that's fine, but ….\x01",
            "what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Not just something!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I was swimming at the beach earlier,\x01",
            "My swimming suit has been cut by someone!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00005FY-your swim suit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, since the opening of the beach\x01",
            "A case where a female swimsuit is torn down\x01",
            "It happened a couple of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this time morning, at the time of charter\x01",
            "It seems that it did not appear, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PWe heard about rumors, too,\x01",
            "That is becoming a party.\x02",
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
            "She was swimsuited,\x01",
            "An embarrassing feeling in the presence of the public\x01",
            "I was made to do! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Even if you complain,\x01",
            "Say it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        "#6PWell, I told you such a thing ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "Anyways……\x01",
            "On your side Michelam\x01",
            "Capture the perpetrator!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If it is not a responsibility problem\x01",
            "I will appeal!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47C4():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_47C4)
    Sleep(100)

    def lambda_47D4():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_47D4)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5PT-that is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PIt seems difficult\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PUntil now even the appearance of the criminal\x01",
            "It is not confirmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#5P#01111FBarking ……\x01",
            "It seems to be hard for some reason. )\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        "#11P#01100F(Lloyd, should we help out?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A35")

    label("loc_48C6")

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
            "I quickly broke my swimsuit\x01",
            "Capture the perpetrator!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If it is not a responsibility problem\x01",
            "I will appeal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PT-that is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PIt seems difficult\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PUntil now even the appearance of the criminal\x01",
            "It is not confirmed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        "#11P#01100F(Lloyd, should we help out?)\x02",
    )

    CloseMessageWindow()

    label("loc_4A35")

    Call(0, 19)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 7230, 0, 790, 270)
    EventEnd(0x5)
    Return()

    # Function_18_40D1 end

    def Function_19_4A5B(): pass

    label("Function_19_4A5B")


    ChrTalk(
        0x101,
        (
            "#5P#00003F(what will you do……?\x01",
            "I am heading towards the theme park\x01",
            "It was on the way … …)\x02",
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
            "【Assist in finding a criminal】\x01",      # 0
            "【I will stop it】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B22")
    Call(0, 20)
    Jump("loc_4BBD")

    label("loc_4B22")


    ChrTalk(
        0x101,
        (
            "#5P#00003FAt the theme park\x01",
            "I'm meeting you … ….\x01",
            "It is not the curtain we are going out. )\x02\x03",
            "#00000F(This is Michelam Business Division\x01",
            "Let's leave it. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15B, 5)

    label("loc_4BBD")

    Return()

    # Function_19_4A5B end

    def Function_20_4BBE(): pass

    label("Function_20_4BBE")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00000F…… Everyone, if possible about the case\x01",
            "Could you tell me more in detail?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4C8A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4C8A)
    Sleep(100)

    def lambda_4C9A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4C9A)
    Sleep(100)

    def lambda_4CAA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4CAA)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5P#00004FAs a police person,\x01",
            "This sneaky crime\x01",
            "I can not overlook it.\x02\x03",
            "#00000FAbout the identity of the culprit\x01",
            "It may be possible,\x01",
            "Could you cooperate with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "oh dear……\x01",
            "Thank you for your consideration!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#12PHe will search for the perpetrator.\x01",
            "Was not it good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hmm, we're counting on you\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PIf so, what about talking in the hallway\x01",
            "Let's move the place to the change room once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FYes let's\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#11P#01109FLet's do our best, Lloyd!\x02",
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
            "Quest 【Investigation of Swimsuit Swear Case】\x07\x00",
            "I started!\x02",
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
            "#6P#00001FFirst of all, when the incident occurred\x01",
            "Could you tell me the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Sure\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "…… I, with my boyfriend,\x01",
            "I was playing water at the beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Tossing the beach ball,\x01",
            "I practice swimming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "After a while,\x01",
            "I have a drink in a kiosk\x01",
            "I decided to go buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "So, if you take your eyes off for a while,\x01",
            "I heard her scream ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When you come back,\x01",
            "She was swimsuited\x01",
            "I was crouching at the lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "People around me gather,\x01",
            "I was already suprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "A watchman there went in a hurry\x01",
            "I brought a towel … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FI see\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00001FThe watchman says something\x01",
            "Did not you witness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I was watching the whole lake,\x01",
            "I did not see anything interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Until you rush to hear screams\x01",
            "Even swim suit has been cut off\x01",
            "I did not notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Since becoming a fuss\x01",
            "I tried asking tourists around me,\x01",
            "There was no one who saw the culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I am a victim too\x01",
            "I do not see the culprit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "Since my boyfriend went to buy it\x01",
            "I casually looked around,\x01",
            "Nobody was approaching … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The moment when it was cut was surprised,\x01",
            "I cried in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FThat's … …\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00001FEven in the case of a torn up to now\x01",
            "Is there no witnesses?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, both like this time\x01",
            "I was awake on the beach,\x01",
            "Nobody is watching the criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just swimwear always\x01",
            "It is cut with things like a knife,\x01",
            "It is hard to think of an accident ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Besides, in a similar way\x01",
            "More than nothing is happening\x01",
            "It is natural to think that it is the same criminal … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even looking at the customer's list, at the time of the incident\x01",
            "There is no person who is coming in common.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wonder if it was an accident\x01",
            "When I was forgotten,\x01",
            "It has happened again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FI see\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        "#12P#01111FLloyd, do you know who did it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "Hey, my daughter.\x01",
            "You should not hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No matter how much you say the police,\x01",
            "About hearing the story\x01",
            "That's why … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F…… No, in the image of the culprit\x01",
            "A star has arrived.\x02",
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
        "S-seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if site verification is not done\x01",
            "Are you sure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FOf course it is necessary, but …\x01",
            "Probably, I do not think much evidence will come out.\x02\x03",
            "#00001FSince the site is a beach,\x01",
            "Now that time has passed since its occurrence\x01",
            "There is a high possibility that it was erased by the waves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I-I see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But even after considering it\x01",
            "You know the culprit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, I will talk about all of you\x01",
            "In combination,\x01",
            "You will naturally see the image of the culprit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#12P#01109FYou're so cool, Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    ChrTalk(
        0xE,
        (
            "Do not waste it,\x01",
            "Let's have an answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "My swimming suit\x01",
            "The criminal who tore it … ….\x01",
            "Who the heck is she saying?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00001F(That there are no witnesses,\x01",
            "The crime so far is on the waterside\x01",
            "What is being done ……)\x02\x03",
            "(And swim suit\x01",
            "With a thing like a knife\x01",
            "Being torn up. )\x02\x03",
            "#00003F(From these,\x01",
            "Probably the culprit … …)\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D48")
    Sleep(500)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThe criminal of swimsuit riot incident?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "The victim himself\x01",        # 0
            "Victim's boyfriend\x01",      # 1
            "A watchman\x01",            # 2
            "Entirely someone else\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C1A")

    ChrTalk(
        0x101,
        (
            "#6P#00003FThinking from the situation,\x01",
            "The culprit is here\x01",
            "It can not be any other tourist.\x02\x03",
            "#00001FProbably this time the culprit,\x01",
            "Lying on the beach ……\x01",
            "I think that it is some kind of \"demon\".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C15")
    OP_2C(0x7E, 0x1)

    label("loc_5C15")

    Jump("loc_5D43")

    label("loc_5C1A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#6P#00003F(No, that person in circumstances\x01",
            "It can not be the culprit.\x01",
            "…… Let's think over. )\x02\x03",
            "#00001F(That there are no witnesses,\x01",
            "The crime so far is on the waterside\x01",
            "What is being done ……)\x02\x03",
            "(And swim suit\x01",
            "With a thing like a knife\x01",
            "Being torn up. )\x02\x03",
            "#00003F(From these,\x01",
            "Probably the culprit … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D43")

    Jump("loc_5AC2")

    label("loc_5D48")

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
        "M-monster?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Demon beast swimsuit her\x01",
            "You mean she tore it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No matter how much\x01",
            "Is not it a story that goes too far?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "You're saying there are monsters here?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FLet's go to the actual scene\x02\x03",
            "#00003FFirst it was torn.\x01",
            "About bathing suits ……\x02\x03",
            "#00001FThis is like a knife\x01",
            "You seem to have been cut?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, yeah ….\x01",
            "It was the same also in the case up to now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell, I will ask …\x01",
            "Such things on this beach\x01",
            "Is it possible to \"bring in\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No……\x01",
            "It should be difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also call at reception,\x01",
            "I am strictly checking … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, our officials too, on security,\x01",
            "A compact simple metal detector\x01",
            "I carry it around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's why,\x01",
            "How did you bring in?\x01",
            "I do not understand it at all …………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ah…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000F… … That's right, that is …\x01",
            "The culprit \"brought a knife\"\x01",
            "I do not mean that.\x02\x03",
            "#00003FProbably, to the criminal's own body\x01",
            "Weapons to cut through swimsuits\x01",
            "\"Prepared\" … …\x02\x03",
            "#00001Fperhaps……\x01",
            "Sharp claws and things like teeth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, that makes a criminal a demonic beast\x01",
            "Is it reasonable …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FNo, if only this\x01",
            "It is simply a strange idea.\x02\x03",
            "#00000FHowever, when combined with other elements ……\x01",
            "It should gradually increase the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Alternatives?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FOriginally this incident,\x01",
            "The incidents that have happened so far and\x01",
            "That seems to have many things in common.\x02\x03",
            "#00003FWhat there are no witnesses ……\x01",
            "That the crime is being done at the waterside …\x01",
            "The same thing as the trick … …\x02\x03",
            "#00001FFrom that point of view,\x01",
            "The criminal has a high likelihood of the same criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, even though\x01",
            "In the customer's roster at the time of the incident\x01",
            "Those who have come consistently …\x02",
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
            "#12P#00003FThat's right.\x01",
            "I entered by regular means\x01",
            "There are no culprits among the customers.\x02\x03",
            "#00000FAnd, as long as there are observers\x01",
            "It is also impossible to enter through the lake … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, that kind of person on a falling stone\x01",
            "I think you will notice it if you misunderstand … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FIf you think so …\x01",
            "The route that the criminal appears on the scene\x01",
            "There is only one.\x02\x03",
            "Off the coast of Elm ……\x01",
            "Have a habitation around that\x01",
            "It is possible if it is aquatic monsters.\x02\x03",
            "#00003FAnd if it is a small aquarium monster\x01",
            "Without being noticed by the observer by swimming underwater\x01",
            "It should be close to the beach human being.\x02\x03",
            "#00001FConversely……\x01",
            "In other ways, this incident\x01",
            "You can not wake it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "One, that is,\x01",
            "I could only raise it to a devil … …\x01",
            "Is that something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Although it's still speculation\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "Wait a moment, please.\x01",
            "Do not you remember important things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Why the devil something,\x01",
            "Slit the girls swimsuit\x01",
            "Is that necessary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, it certainly has it too ……\x01",
            "How are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As expected after all …\x01",
            "Somewhere hentai man's\x01",
            "Is not it a matter of work?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FSurely, motivation is\x01",
            "I do not know but …\x02\x03",
            "#00001FOnly the demon this time incident\x01",
            "I can not raise it\x01",
            "The fact remains unchanged.\x02\x03",
            "#00003FAnd at this point\x01",
            "\"Monster with such a habit\"\x01",
            "There is no choice but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But …\x01",
            "Then what shall we do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When a monster comes into and out,\x01",
            "Michelam Division's credit also\x01",
            "I will be connected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Somehow on this occasion\x01",
            "I hope I can get rid of it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "But the opponents are monsters\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Waiting until it appears,\x01",
            "Very beach, etc\x01",
            "I can not operate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, I also suffered damage\x01",
            "Would you be comfortable with that?\x01",
            "As expected it is not.\x02",
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
            "#12P#01100FIf it's the case\x01",
            "Is Ka'a to Otori?\x02",
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

    def lambda_6AB5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AB5)
    Sleep(100)

    def lambda_6AC5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6AC5)
    Sleep(100)

    def lambda_6AD5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6AD5)
    Sleep(100)

    def lambda_6AE5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6AE5)
    Sleep(100)

    def lambda_6AF5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6AF5)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00011FK-KeA, what are you saying?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01105FBecause that monster is\x01",
            "You want to cut girls' swimsuits, is not it?\x02\x03",
            "#01103FWhen Ka'a was playing on the waterside,\x01",
            "It may come out again.\x02\x03",
            "#01109FAt that time, if Lloyd protects you\x01",
            "Ka'aa is fine as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FOh, that …\x01",
            "Koea to such a dangerous eye\x01",
            "Can not you let me meet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "That's right, little girl\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Although only swimsuits have been cut so far,\x01",
            "I do not know what will happen next time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108FHmm, but …\x01",
            "If there are monsters as it is\x01",
            "Bell is in trouble, is not it?\x02\x03",
            "#01106FTo thank you for inviting me\x01",
            "I want to get rid of it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FWe-well that's true but\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00003FGot it\x02\x03",
            "#00001FThat strategy of Kia,\x01",
            "I do not know if it will succeed\x01",
            "Let's do it as much as we can.\x02\x03",
            "#00003FHowever, the role of the decoy is not Ka - a,\x01",
            "I will ask someone else in us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01101FRight!\x02",
    )

    CloseMessageWindow()

    def lambda_6E5B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6E5B)
    Sleep(100)

    def lambda_6E6B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6E6B)
    Sleep(100)

    def lambda_6E7B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6E7B)
    Sleep(100)

    def lambda_6E8B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6E8B)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "Something like that ….\x01",
            "Are you okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, if you are a member of the support department\x01",
            "I am used to battle with monsters … …\x01",
            "I think that it will not be important.\x02\x03",
            "#00003FThe problem is,\x01",
            "Who will you ask for it … ….\x02\x03",
            "#00000FIt seems to be asking for cooperation,\x01",
            "Eli, Tio, Noel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01105FWho are you gonna choose, Lloyd?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00003FHmm\x02",
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
            "#1KWho will ask the role of a decoy?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Erie】\x01",      # 0
            "[Tio]\x01",      # 1
            "[Noel]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7075"),
        (1, "loc_70B0"),
        (2, "loc_70EB"),
        (SWITCH_DEFAULT, "loc_7126"),
    )


    label("loc_7075")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x15B, 6)

    ChrTalk(
        0x101,
        "#6P#00000F… … Let's ask Ellie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7126")

    label("loc_70B0")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x15B, 7)

    ChrTalk(
        0x101,
        "#6P#00000FLet's call Tio\x02",
    )

    CloseMessageWindow()
    Jump("loc_7126")

    label("loc_70EB")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C4, 5)

    ChrTalk(
        0x101,
        "#6P#00000F… … Let's ask Noel.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7126")

    label("loc_7126")


    ChrTalk(
        0x153,
        "#12P#01109FGot it!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00003Fso……\x01",
            "From the moment to the devastation of devil on the beach\x01",
            "I want to start.\x02\x03",
            "#00000FEveryone,\x01",
            "Can you pay attrition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, got it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Let me say the inspection time\x01",
            "For tourists for a while\x01",
            "Let me evacuate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "You guys, be careful ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The monsters that slit my swimsuit\x01",
            "Please beat me up!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00000FYes, leave it to us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01109FOK then Let's Go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_7328")
    AddParty(0x1, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x1)
    Jump("loc_734A")

    label("loc_7328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_7340")
    AddParty(0x2, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x2)
    Jump("loc_734A")

    label("loc_7340")

    AddParty(0x8, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x3)

    label("loc_734A")

    SetScenarioFlags(0x22, 3)
    NewScene("t1310", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_4BBE end

    def Function_21_7357(): pass

    label("Function_21_7357")

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
        "Everyone thank you so much\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to Michelam Division's\x01",
            "It seems to be lost without losing credibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHah, glad we could be of assistance\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm really thankful to you.\x01",
            "Why can I say thank you … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, in the relationship of development demons\x01",
            "Regarding the matter that was out,\x01",
            "I will report to Mr. Maria Bell.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_75CC")

    ChrTalk(
        0x102,
        "#00100FYeah, that would be better.\x02",
    )

    CloseMessageWindow()
    Jump("loc_762F")

    label("loc_75CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_75FD")

    ChrTalk(
        0x103,
        "#00200FThat would be good\x02",
    )

    CloseMessageWindow()
    Jump("loc_762F")

    label("loc_75FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_762F")

    ChrTalk(
        0x109,
        "#10100FYes, thank you.\x02",
    )

    CloseMessageWindow()

    label("loc_762F")


    ChrTalk(
        0x101,
        (
            "#00000FHaha, if you are Mary Bell\x01",
            "It seems to think about some measures.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        "#12PHuhu, cheers for good work\x02",
    )

    CloseMessageWindow()

    def lambda_76A2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76A2)
    Sleep(100)

    def lambda_76B2():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_76B2)
    Sleep(100)

    def lambda_76C2():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_76C2)
    Sleep(100)

    def lambda_76D2():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_76D2)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#12PTentatively, the swimsuit splitting case\x01",
            "The monster who was the culprit was able to get rid of it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#12PWell, if you do not mind\x01",
            "Let's go to the beach play continuation!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#6PWell, I am going to go again! Is it?\x01",
            "I thought he was discouraged … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PTosen right?\x01",
            "Because I came all the way\x01",
            "I have to play.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#12PHuhu, then\x01",
            "We are in this.\x02",
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
            "#12PSorry then I\x01",
            "I will return to the job of monitoring.\x01",
            "Thank you very much.\x02",
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
            "#00000FOkay, then, we\x01",
            "I suppose I should go soon.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        "#6P#01100FRight!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_7996")

    ChrTalk(
        0x102,
        (
            "#00104FI am a little more\x01",
            "After seeing the boutiques go.\x02\x03",
            "#00100FHuhuu, see you later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A7C")

    label("loc_7996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_7A18")

    ChrTalk(
        0x103,
        (
            "#00204FI go ahead\x01",
            "I am going to a theme park.\x02\x03",
            "#00202FTsite and Shuri\x01",
            "Because I am keeping it, with this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A7C")

    label("loc_7A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_7A7C")

    ChrTalk(
        0x109,
        (
            "#10100FI am a little more frank\x01",
            "I will go watch the jewelry store.\x02\x03",
            "#10109FWell then, see you later!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A7C")


    def lambda_7A81():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A81)
    Sleep(200)

    def lambda_7A91():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7A91)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FOk see you later then\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01109FBye!\x02",
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
            "Quest 【Investigation of Swimsuit Swear Case】\x07\x00",
            "Achieved!\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_7B6A")
    RemoveParty(0x1, 0xFF)
    Jump("loc_7B87")

    label("loc_7B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_7B7B")
    RemoveParty(0x2, 0xFF)
    Jump("loc_7B87")

    label("loc_7B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_7B87")
    RemoveParty(0x8, 0xFF)

    label("loc_7B87")

    EventEnd(0x5)
    SetScenarioFlags(0x22, 1)
    NewScene("t1020", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_21_7357 end

    def Function_22_7B96(): pass

    label("Function_22_7B96")

    OP_95(0xE, 4990, 0, 50, 2000, 0x0)
    OP_95(0xE, 6570, 0, 1030, 2000, 0x0)
    OP_95(0xE, 10000, 0, 1020, 2000, 0x0)
    Return()

    # Function_22_7B96 end

    def Function_23_7BD3(): pass

    label("Function_23_7BD3")

    OP_95(0xD, 4990, 0, 50, 2000, 0x0)
    OP_95(0xD, 6570, 0, 1030, 2000, 0x0)
    OP_95(0xD, 10000, 0, 1020, 2000, 0x0)
    Return()

    # Function_23_7BD3 end

    def Function_24_7C10(): pass

    label("Function_24_7C10")

    EventBegin(0x2)
    ClearMapFlags(0x20)
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
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_24_7C10 end

    SaveToFile()

Try(main)
