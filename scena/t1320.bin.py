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
        "Function_5_869",          # 05, 5
        "Function_6_8D2",          # 06, 6
        "Function_7_920",          # 07, 7
        "Function_8_A56",          # 08, 8
        "Function_9_C25",          # 09, 9
        "Function_10_D9C",         # 0A, 10
        "Function_11_EC0",         # 0B, 11
        "Function_12_F38",         # 0C, 12
        "Function_13_1133",        # 0D, 13
        "Function_14_2317",        # 0E, 14
        "Function_15_233C",        # 0F, 15
        "Function_16_2361",        # 10, 16
        "Function_17_3F47",        # 11, 17
        "Function_18_42B6",        # 12, 18
        "Function_19_4C49",        # 13, 19
        "Function_20_4DAE",        # 14, 20
        "Function_21_7806",        # 15, 21
        "Function_22_8096",        # 16, 22
        "Function_23_80D3",        # 17, 23
        "Function_24_8110",        # 18, 24
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_85C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B1")

    ChrTalk(
        0x8,
        (
            "Thank you very much for\x01",
            "driving off the swimsuit\x01",
            "ripping monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because they are monsters,\x01",
            "we can't be sure they\x01",
            "won't appear again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, the Michelam\x01",
            "Operations Department will ready\x01",
            "countermeasures against them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_857")

    label("loc_7B1")


    ChrTalk(
        0x8,
        (
            "Thank you very much for\x01",
            "driving off the swimsuit\x01",
            "ripping monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, the Michelam\x01",
            "Operations Department will ready\x01",
            "countermeasures against them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_857")

    Jump("loc_865")

    label("loc_85C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_865")

    label("loc_865")

    TalkEnd(0x8)
    Return()

    # Function_4_68A end

    def Function_5_869(): pass

    label("Function_5_869")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My girlfriend is\x01",
            "choosing a swimsuit\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Can't she choose a\x01",
            "little faster...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_869 end

    def Function_6_8D2(): pass

    label("Function_6_8D2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Wooow, so many cute\x01",
            "swimsuits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which one should I\x01",
            "choose...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_8D2 end

    def Function_7_920(): pass

    label("Function_7_920")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EC")
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Eeeeeek!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "D-Don't bring a little\x01",
            "girl in the men's\x01",
            "changing room!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FR-Right, now that you\x01",
            "mention it. ...I'm\x01",
            "sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105FHuuuh?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A52")

    label("loc_9EC")


    ChrTalk(
        0xFE,
        (
            "H-Honestly... I can't\x01",
            "let my guard down at\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I almost had my butt\x01",
            "seen by a little girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A52")

    TalkEnd(0xFE)
    Return()

    # Function_7_920 end

    def Function_8_A56(): pass

    label("Function_8_A56")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Cautions When Enjoying Lake Beach\x01",
            "─────────────────────────────\x01",
            "・Please be sure to warm up.\x01",
            "・Please, do not enter the water in street clothes.\x01",
            "  (We loan swimsuits at the reception desk)\x01",
            "・Please, observe the lifeguard's instructions.\x01",
            "─────────────────────────────\x01",
            "  Let's mind our manners and have fun.\x01",
            "  　──Michelam Operations Department\x07\x00\x02",
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

    # Function_8_A56 end

    def Function_9_C25(): pass

    label("Function_9_C25")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9F")

    ChrTalk(
        0x101,
        (
            "#12500F...The women's changing room is\x01",
            "this way. Let's leave before\x01",
            "there are any misunderstandings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D41")

    ChrTalk(
        0x101,
        (
            "#00000F...Whoops. The women's\x01",
            "changing room is this\x01",
            "way.\x02",
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
    Jump("loc_D88")

    label("loc_D41")


    ChrTalk(
        0x101,
        (
            "#00000FThe women's changing\x01",
            "room is this way.\x01",
            "...Let's not enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D88")

    SetChrPos(0x0, 104470, 0, 2310, 180)
    EventEnd(0x4)
    Return()

    # Function_9_C25 end

    def Function_10_D9C(): pass

    label("Function_10_D9C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E1E")

    ChrTalk(
        0x101,
        (
            "#00000FSince we haven't rented\x01",
            "swimsuits yet, we can't\x01",
            "proceed.\x02\x03",
            "Let's first check in at\x01",
            "the reception desk.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EAC")

    ChrTalk(
        0x101,
        (
            "#00003FWe don't have time to go\x01",
            "to the beach again.\x02\x03",
            "#00000FLet's head to the theme\x01",
            "park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109FYeah, let's gooo!\x02",
    )

    CloseMessageWindow()

    label("loc_EAC")

    SetChrPos(0x0, 7010, 0, 1020, 270)
    EventEnd(0x4)
    Return()

    # Function_10_D9C end

    def Function_11_EC0(): pass

    label("Function_11_EC0")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#12500FWhoops, we can't loiter\x01",
            "around too long dressed\x01",
            "like this.\x02\x03",
            "Let's hurry to the\x01",
            "beach.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 91160, 0, 690, 90)
    EventEnd(0x4)
    Return()

    # Function_11_EC0 end

    def Function_12_F38(): pass

    label("Function_12_F38")

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
            "#00002F#5PWow... So this is the\x01",
            "beach reception desk,\x01",
            "huh.\x02\x03",
            "#00000FIt looks like we can\x01",
            "rent swimsuits here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#5PMaaan. Never in my wildest\x01",
            "dreams did I think a place\x01",
            "like this could be built.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHehe. Let's check in\x01",
            "already, shall we?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -8000, 0, 1130, 90)
    SetScenarioFlags(0x144, 6)
    EventEnd(0x5)
    Return()

    # Function_12_F38 end

    def Function_13_1133(): pass

    label("Function_13_1133")

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
            "#11PGood morning, and\x01",
            "welcome to Lake Beach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou are the people from\x01",
            "the Special Support\x01",
            "Section, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PYes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PDid you hear about us\x01",
            "from Mariabell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes, your reservation is\x01",
            "until noon today.\x02",
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
            "#11PWe have the following swimsuits\x01",
            "prepared, so please choose the\x01",
            "ones you would like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PWow, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PHmm, which should I go\x01",
            "with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F#6P...Hmm.\x02",
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
            "#00316F#11PBut Lloyd...\x02\x03",
            "#00315FIsn't this is our biggest\x01",
            "reward since joining the\x01",
            "Special Support Section!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PYou're exaggerating.\x02\x03",
            "#00002FBut it's true that I'm looking\x01",
            "forward to seeing how everyone\x01",
            "looks in their swimsuits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PI know right? Right?㈱\x02\x03",
            "#00301FI mean, Ilya and Cecil\x01",
            "in swimsuits!?\x02\x03",
            "#00307FAnd add a hottie like\x01",
            "Rixia on top of that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PC-Calm down.\x02\x03",
            "#00006F...Hmm, but there really\x01",
            "are a lot of attractive\x01",
            "women around us.\x02\x03",
            "#00002FCecil and Rixia of\x01",
            "course, but even Elie is\x01",
            "pretty stacked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PIlya's like a model, and\x01",
            "even Noｱl and Fran have\x01",
            "their good points.\x02\x03",
            "#00302FWell as for PeTiote and\x01",
            "Sullboy, we can expect\x01",
            "great things in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PThat's rude, Randy.\x02\x03",
            "#00005FAh... by the way, can\x01",
            "KeA swim?\x02\x03",
            "#00001FI didn't ask her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PHmm. If she has, it was a\x01",
            "long time ago, so she\x01",
            "probably doesn't remember.\x02\x03",
            "#00300FFor now, maybe someone\x01",
            "should watch her so she\x01",
            "doesn't drown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, you're right.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2434, 255, 80, 0)
    Sleep(800)

    ChrTalk(
        0x105,
        (
            "#1PHehe. You guys really\x01",
            "are doting parents.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_19BF():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19BF)
    Sleep(50)

    def lambda_19CF():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_19CF)
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
        "#00305FY-You changed already?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x105,
        (
            "Yeah. I'll be waiting\x01",
            "outside.\x02",
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
    OP_93(0x105, 0xB4, 0x1F4)
    Sound(2424, 255, 100, 0)
    Sleep(500)
    MoveCamera(325, 18, 0, 4000)

    def lambda_1B21():

        label("loc_1B21")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_1B21")

    QueueWorkItem2(0x101, 2, lambda_1B21)

    def lambda_1B33():

        label("loc_1B33")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_1B33")

    QueueWorkItem2(0x104, 2, lambda_1B33)

    def lambda_1B45():
        OP_95(0xFE, 104270, 0, 97380, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B45)
    WaitChrThread(0x105, 1)

    def lambda_1B63():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B63)
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
        "#00301F#5P─Suspicious.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#6PSuspicious... Who, Wazy?\x02\x03",
            "#00012FWell, I think he's\x01",
            "basically always\x01",
            "suspicious.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00306F#11PNo, that's not it.\x02\x03",
            "#00303FIt was his great execution,\x01",
            "changing quickly while we\x01",
            "were chatting like this.\x02\x03",
            "And that two-piece swimsuit\x01",
            "of his, usable by both\x01",
            "women and men...\x02\x03",
            "#00301FIsn't it suspicious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PI have no idea how any\x01",
            "of that is suspicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PC'mon, ya blockhead.\x02\x03",
            "#00300FWell, whatever. Let's\x01",
            "hurry and change\x01",
            "ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PRight, we shouldn't make\x01",
            "him wait.\x02",
        )
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
            "#12904F#6PNo, I was just thinking\x01",
            "men's swimsuits aren't\x01",
            "that interesting.\x02\x03",
            "#12902FWell, both of you are\x01",
            "well-built, so I guess\x01",
            "I'm not disappointed?\x02",
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
        "#12513F#5PNow look here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12801F#11PThat was uncalled for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12909F#6PHehe. Then, shall we\x01",
            "head for the beach?\x02",
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

    # Function_13_1133 end

    def Function_14_2317(): pass

    label("Function_14_2317")


    def lambda_231C():
        OP_9B(0x1, 0xFE, 0xA, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_231C)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_2317 end

    def Function_15_233C(): pass

    label("Function_15_233C")


    def lambda_2341():
        OP_9B(0x1, 0xFE, 0xFFF6, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2341)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_233C end

    def Function_16_2361(): pass

    label("Function_16_2361")

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
            "#12809F#11PAhhh. I'm tired, but man that\x01",
            "was a lot of fun.\x02\x03",
            "#12801FHmm. Maybe I'm being greedy but\x01",
            "I wish Rixia or Cecil would\x01",
            "have played volleyball too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12505F#6PHuh, why?...\x02",
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
        "#12513F#6PR-Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12802F#11PHmm? I wonder what\x01",
            "you're imagining.\x02\x03",
            "#12806FI mean, damn. You got to\x01",
            "put sunscreen on milady,\x01",
            "Cecil and Rixia, too!\x02\x03",
            "#12801FC'mon, tell me. How was\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512F#6PW-Well...\x02\x03",
            "All I can really say is\x01",
            "it was amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12807F#11PWhat!?\x02\x03",
            "#12810FYou asshole, keeping all\x01",
            "the beauties to\x01",
            "yourself!\x02",
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
        (
            "#12511F#6PWaugh! I give up, I give\x01",
            "up!\x02",
        )
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

    def lambda_2745():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2745)
    OP_9B(0x1, 0x104, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    WaitChrThread(0x101, 2)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12803F#11P─So Lloyd...\x02\x03",
            "#12802FWhose swimsuit struck\x01",
            "you the most?\x02",
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
            "#12511F#6PWhaaat!?\x02\x03",
            "#12508F(Hmm... If I had to\x01",
            "choose...)\x02",
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
            "#1KWhose swimsuit was best?\x07\x00\x02",
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
        (0, "loc_28F8"),
        (1, "loc_2A55"),
        (2, "loc_2B8C"),
        (3, "loc_2CD2"),
        (4, "loc_2E35"),
        (5, "loc_2F8E"),
        (6, "loc_30CA"),
        (7, "loc_3224"),
        (8, "loc_33A4"),
        (9, "loc_3584"),
        (10, "loc_36D5"),
        (SWITCH_DEFAULT, "loc_3833"),
    )


    label("loc_28F8")

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
            "#3C(Hmm, I always thought she had a\x01",
            "nice figure, but...)\x02\x03",
            "(This isn't good... I hope I'm not\x01",
            "too conscious of it when we're\x01",
            "working together.)\x02",
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
    Jump("loc_3833")

    label("loc_2A55")

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
            "#3C(It was a modest swimsuit, but it\x01",
            "was cute....)\x02\x03",
            "(The black dress looked pretty on\x01",
            "her light skin...)\x02",
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
    Jump("loc_3833")

    label("loc_2B8C")

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
            "#3C(Noｱl was sporty, just like I\x01",
            "thought.)\x02\x03",
            "(And yet, how to put it... She had\x01",
            "a charm that she normally\x01",
            "suppresses...)\x02",
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
    Jump("loc_3833")

    label("loc_2CD2")

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
            "#3C(Hmm, if we're talking about a\x01",
            "lovely figure in a swimsuit, that\x01",
            "would have to be Fran's.)\x02\x03",
            "(Pink with polka dots... It matched\x01",
            "her personality.)\x02",
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
    Jump("loc_3833")

    label("loc_2E35")

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
            "#3C(KeA's swimsuit had to be best.)\x02\x03",
            "(I wonder if Elie and Tio picked it\x01",
            "out for her.)\x02\x03",
            "(Simple and easy to move in, but\x01",
            "still stylish...)\x02",
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
    Jump("loc_3833")

    label("loc_2F8E")

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
            "#3C(Cecil... That was a bit of foul\x01",
            "play...)\x02\x03",
            "(I wasn't conscious of sister\x01",
            "Cecil's figure until now, but...)\x02",
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
    Jump("loc_3833")

    label("loc_30CA")

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
            "#3C(Miss Ilya... She looked like a\x01",
            "star.)\x02\x03",
            "(She sparkles brilliantly no matter\x01",
            "the situation... I can understand\x01",
            "why everyone admires her.)\x02",
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
    Jump("loc_3833")

    label("loc_3224")

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
            "#3C(Hmm. At her height, a girl with\x01",
            "her figure is against the rules...)\x02\x03",
            "(With the amount of skin she was\x01",
            "showing, it was like she was\x01",
            "wearing a scantily-clad stage\x02\x03",
            "costume...)\x02",
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
    Jump("loc_3833")

    label("loc_33A4")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_34AD")

    AnonymousTalk(
        0x101,
        (
            "#3C(Haha. She acts like a boy, but\x01",
            "she's really a girl.)\x02\x03",
            "(That was a huge mistake the first\x01",
            "time we met, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_353C")

    label("loc_34AD")


    AnonymousTalk(
        0x101,
        (
            "#3C(Haha. She acts like a boy,\x01",
            "but she's really a girl.)\x02\x03",
            "(When I was introduced to her\x01",
            "the first time, she seemed\x01",
            "the opposite, though.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_353C")

    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_3833")

    label("loc_3584")

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
            "#3C(Still, Randy... He's really well\x01",
            "built.)\x02\x03",
            "(Looking more closely, he has many\x01",
            "old scars... Could they be from his\x01",
            "jaeger days?)\x02",
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
    Jump("loc_3833")

    label("loc_36D5")

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
            "#3C(Wazy, huh... Now that Randy said\x01",
            "that, his swimsuit was rather\x01",
            "concerning.)\x02\x03",
            "(A unisex two-piece... I think it\x01",
            "was a simple style, though.)\x02",
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
    Jump("loc_3833")

    label("loc_3833")

    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#1PNow now, what might you\x01",
            "boys be chatting about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12511F#6P!!\x02",
    )

    CloseMessageWindow()

    def lambda_3885():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3885)
    Sleep(50)

    def lambda_3895():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3895)
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
            "#12805F#5PWhoa. You already\x01",
            "changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12PWell, you guys are young so I\x01",
            "guess your wild imaginations\x01",
            "can't be helped.\x02\x03",
            "#10302FBut wouldn't it be better to\x01",
            "be a little more serious and\x01",
            "talk to them directly?\x02\x03",
            "#10309FIt would be great if you made\x01",
            "them think you were\x01",
            "interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12511F#5PN-No! That's not what we\x01",
            "were saying!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12801F#5PI do agree but... That's\x01",
            "awfully condescending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PYeah, that's why I'm so\x01",
            "popular.\x02",
        )
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
            "#10304F#12PHehe, I'm heading back\x01",
            "to our hotel room.\x02\x03",
            "#10300FI wanna rest a bit\x01",
            "before we go to the\x01",
            "theme park.\x02\x03",
            "#10302FAdieu.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xB4, 0x1F4)
    MoveCamera(325, 18, 0, 4000)

    def lambda_3B85():

        label("loc_3B85")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_3B85")

    QueueWorkItem2(0x101, 2, lambda_3B85)

    def lambda_3B97():

        label("loc_3B97")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_3B97")

    QueueWorkItem2(0x104, 2, lambda_3B97)

    def lambda_3BA9():
        OP_95(0xFE, 104270, 0, 97380, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3BA9)
    WaitChrThread(0x105, 1)

    def lambda_3BC7():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3BC7)
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
            "#12807F#11POh, I can't take it\x01",
            "anymore!\x02\x03",
            "#12806FHe got changed so fast,\x01",
            "and what's with his\x01",
            "arrogance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12506F#5PWell it's probably the\x01",
            "people he deals with.\x02\x03",
            "#12500FEven now he works as a\x01",
            "host at night if he\x01",
            "feels like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12801F#11PWhy I am so jealous...?\x01",
            "I mean, why is he so\x01",
            "rude!?\x02\x03",
            "#12803FOne of these days I'm\x01",
            "going to tail and check\x01",
            "up on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12512F#5P(I'm unconvinced...)\x02",
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
            "Later, after Lloyd and the\x01",
            "others returned to the hotel and\x01",
            "rested...\x02\x03",
            "They decided to gather at the\x01",
            "theme park entrance after\x01",
            "everyone enjoyed their shopping.\x07\x00\x02",
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

    # Function_16_2361 end

    def Function_17_3F47(): pass

    label("Function_17_3F47")

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

    def lambda_401C():
        OP_97(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_401C)
    Sleep(500)

    def lambda_4039():
        OP_97(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_4039)
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
            "#11P#01105FLloyd, we're not going\x01",
            "to the theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FWell, we are, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        "#6P#00005FIt's oddly quiet.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#6P#00003FThe receptionist isn't\x01",
            "here either... Where\x01",
            "could they have gone?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6090, 1600, 50, 4000)
    OP_6F(0x1)
    Sleep(100)

    NpcTalk(
        0xE,
        "Woman's Voice",
        (
            "#4P#N#2SWhat is the meaning of\x01",
            "this!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "Woman's Voice",
        (
            "#4P#N#2S...I-I'm terribly\x01",
            "sorry...\x02",
        )
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
        "#11P#01105FI heard voices?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, there's some kind\x01",
            "of an argument...\x02",
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

    # Function_17_3F47 end

    def Function_18_42B6(): pass

    label("Function_18_42B6")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB0")
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
            "To have to go through\x01",
            "something like this when we've\x01",
            "finally come to the beach...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What the hell is the\x01",
            "beach manager doing!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm really sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PI wasn't paying enough\x01",
            "attention either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "N-Now, now. They\x01",
            "apologized, so isn't it\x01",
            "fine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You didn't get hurt\x01",
            "either, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No! That won't satisfy\x01",
            "me!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        (
            "Umm, is something the\x01",
            "matter?\x02",
        )
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

    def lambda_45CE():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45CE)
    Sleep(200)

    def lambda_45EB():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_45EB)
    Sleep(500)
    WaitChrThread(0x153, 1)

    ChrTalk(
        0x153,
        "#5P#01100FYou're fighting?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PI heard Miss Mariabell\x01",
            "invited you guys to the\x01",
            "beach...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, sorry! I left the\x01",
            "reception desk\x01",
            "unattended...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FNo, that's not a\x01",
            "problem... Has something\x01",
            "happened here?\x02",
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
            "When I was swimming just\x01",
            "now, someone tore my\x01",
            "swimsuit!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00005FY-Your swimsuit...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, there have been two or\x01",
            "three cases of torn women's\x01",
            "swimsuits since the beach opened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems it didn't happen\x01",
            "this morning during your\x01",
            "reservation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PWe heard the rumors\x01",
            "ourselves, but to think it\x01",
            "actually happened to us...\x02",
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
            "A girl had her swimsuit\x01",
            "torn and was embarrassed\x01",
            "in public, you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "At least complain some!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        "#6PE-Even if you say so...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "Anyway... Catch the\x01",
            "thief!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Otherwise, I'll sue!\x02",
    )

    CloseMessageWindow()

    def lambda_498B():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_498B)
    Sleep(100)

    def lambda_499B():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_499B)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHonestly, that seems\x01",
            "difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PThere haven't been any\x01",
            "eyewitness reports of\x01",
            "the criminal as yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#5P#01111F(Hmmm...? This seems\x01",
            "like a tough problem.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        (
            "#11P#01100F(Lloyd, aren't you going\x01",
            "to help them?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C23")

    label("loc_4AB0")

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
            "Catch the culprit who\x01",
            "tore my swimsuit at\x01",
            "once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Otherwise, I'll sue!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHonestly, that seems\x01",
            "difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PThere haven't been any\x01",
            "eyewitness reports of\x01",
            "the criminal as yet.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        (
            "#11P#01100F(Lloyd, aren't you going\x01",
            "to help them?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C23")

    Call(0, 19)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 7230, 0, 790, 270)
    EventEnd(0x5)
    Return()

    # Function_18_42B6 end

    def Function_19_4C49(): pass

    label("Function_19_4C49")


    ChrTalk(
        0x101,
        (
            "#5P#00003F(What should I do? We\x01",
            "were heading to the\x01",
            "theme park, but...)\x02",
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
            "[Help Catch the Criminal]\x01",      # 0
            "[Cancel]\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D0A")
    Call(0, 20)
    Jump("loc_4DAD")

    label("loc_4D0A")


    ChrTalk(
        0x101,
        (
            "#5P#00003F(We have an appointment at\x01",
            "the theme park... This isn't\x01",
            "our problem to solve.)\x02\x03",
            "#00000F(Let's leave this to the\x01",
            "Michelam Operations\x01",
            "Department.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15B, 5)

    label("loc_4DAD")

    Return()

    # Function_19_4C49 end

    def Function_20_4DAE(): pass

    label("Function_20_4DAE")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00000F...Everyone, could you\x01",
            "tell me about the\x01",
            "incident in detail?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4E77():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4E77)
    Sleep(100)

    def lambda_4E87():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4E87)
    Sleep(100)

    def lambda_4E97():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4E97)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5P#00004FAs a policeman, I can't\x01",
            "overlook such a heinous\x01",
            "crime.\x02\x03",
            "#00000FI may be able to identify\x01",
            "the criminal's profile.\x01",
            "Will you allow me to help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My... By all means,\x01",
            "please do!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#12PHaha. He says he'll find\x01",
            "the criminal. Isn't that\x01",
            "great?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmph, at least do your\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12PThen, talking in the corridor\x01",
            "isn't good. Let's move to the\x01",
            "locker room for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FAlright, let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#11P#01109FGo for it, Lloyd!\x02",
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
            "Quest [The Torn Swimsuit\x01",
            "Case]\x07\x00",
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
            "#6P#00001FCould you tell me the\x01",
            "situation when it\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...I was playing in the\x01",
            "water with my boyfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "We were tossing a beach\x01",
            "ball, practicing\x01",
            "swimming and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "A while later, I went to\x01",
            "buy drinks at the stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And, when I hadn't laid\x01",
            "eyes on her for some\x01",
            "time, I heard a scream...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When I got back, her\x01",
            "swimsuit was torn and she\x01",
            "was hiding in the lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "People nearby gathered\x01",
            "and... Oh, it was the\x01",
            "worst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "This lifeguard here\x01",
            "brought me a towel right\x01",
            "away, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FI see...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00001FYou were on duty at the\x01",
            "time. Did you see\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I was watching the whole\x01",
            "lake, but didn't see\x01",
            "anything that stood out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I didn't even notice her\x01",
            "swimsuit was torn until I\x01",
            "heard the scream and ran over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I tried asking the nearby guests\x01",
            "who gathered due to the commotion,\x01",
            "but no one had seen the criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Even I, the victim,\x01",
            "didn't see the criminal.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "After my boyfriend went to buy\x01",
            "drinks, I happened to look around,\x01",
            "and there was no one nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The moment my suit was\x01",
            "torn, I panicked and hid\x01",
            "in the water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FI see... You had no\x01",
            "choice.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00001FWere there any\x01",
            "eyewitnesses in any of\x01",
            "the similar incidents?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No. They all occurred on the\x01",
            "beach, just like this time, but\x01",
            "no one has seen the criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's just, the swimsuits are always\x01",
            "torn by something sharp, so I can't\x01",
            "think of them as accidents...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The modus operandi is the same each time,\x01",
            "so it's natural to think the same criminal\x01",
            "is responsible for all of them, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We reviewed our guest list\x01",
            "and there are no names common\x01",
            "to all of the incidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Just when you start thinking it\x01",
            "was an accident and forgetting\x01",
            "about it, it happens again.\x02",
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
        (
            "#12P#01111FLloyd, do you know who\x01",
            "did it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "Hey now, little lady.\x01",
            "You mustn't rush him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even if he is a policeman, there's\x01",
            "no way he could figure it out just\x01",
            "by listening to what we've heard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...No, I have an idea\x01",
            "about the criminal's\x01",
            "profile.\x02",
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
            "Even without\x01",
            "investigating the crime\x01",
            "scene?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FNormally I would but... I don't think much\x01",
            "evidence is there.\x02\x03",
            "#00001FOn top of the scene being a beach, some time\x01",
            "has passed since the crime occurred. It's\x01",
            "likely the waves have erased any evidence.\x02",
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
            "But, you know who the\x01",
            "criminal is, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes. By thinking about your\x01",
            "reports together, I can naturally\x01",
            "see a certain criminal profile.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#12P#01109FLloyd, you're so cool!\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    ChrTalk(
        0xE,
        (
            "Quit showing off and\x01",
            "answer me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The criminal who tore my\x01",
            "swimsuit... Who in the\x01",
            "world could it be?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00001F(There have been no witnesses,\x01",
            "and all incidents have\x01",
            "occurred at waterside...)\x02\x03",
            "(There's also the fact that\x01",
            "the swimsuits were torn by\x01",
            "something sharp.)\x02\x03",
            "#00003F(Thinking about these facts,\x01",
            "the likely criminal is...)\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B1")
    Sleep(500)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThe criminal in the torn\x01",
            "swimsuits incidents is?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "The victim herself\x01",          # 0
            "The victim's boyfriend\x01",      # 1
            "The lifeguard\x01",               # 2
            "Someone else entirely\x01",       # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F57")

    ChrTalk(
        0x101,
        (
            "#6P#00003FJudging from the situation, the\x01",
            "culprit isn't anyone here nor\x01",
            "one of the other tourists.\x02\x03",
            "#00001FMost likely, the culprit is\x01",
            "lurking on the beach... I think\x01",
            "it's some kind of "monster".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F52")
    OP_2C(0x7E, 0x1)

    label("loc_5F52")

    Jump("loc_60AC")

    label("loc_5F57")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#6P#00003F(No. Considering the situation,\x01",
            "they can't be the criminal.\x01",
            "...I'll try to rethink this.)\x02\x03",
            "#00001F(There have been no witnesses,\x01",
            "and all incidents have occurred\x01",
            "at waterside...)\x02\x03",
            "(There's also the fact that the\x01",
            "swimsuits were torn by\x01",
            "something sharp.)\x02\x03",
            "#00003F(Thinking about these facts,\x01",
            "the likely criminal is...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60AC")

    Jump("loc_5DA7")

    label("loc_60B1")

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
            "You're saying a monster\x01",
            "tore my girlfriend's\x01",
            "swimsuit!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I-Isn't that just too\x01",
            "absurd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Where's your proof!?\x01",
            "Your proof, I say!!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FI'll tell you in order.\x02\x03",
            "#00003FFirst, regarding the\x01",
            "torn swimsuit itself...\x02\x03",
            "#00001FIt was torn by something\x01",
            "sharp, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Y-Yes... All of the\x01",
            "incidents were the same\x01",
            "in that regard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FThen let me ask you this. Is\x01",
            "it possible to bring something\x01",
            "like that onto the beach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "N-No... That would be\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though I am called the\x01",
            "receptionist, I strictly\x01",
            "check for such things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes. For security reasons,\x01",
            "we staff carry a small\x01",
            "portable metal detector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's exactly why I have no\x01",
            "idea how someone got something\x01",
            "like that onto the beach...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Ah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000F...Yes. In other words, the criminal\x01",
            "didn't "bring in something sharp".\x02\x03",
            "#00003FMost likely, the body of the criminal\x01",
            "itself was "already equipped" with a\x01",
            "weapon that tears swimsuits...\x02\x03",
            "#00001FMost likely sharp claws or teeth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "S-So that's your\x01",
            "evidence the criminal is\x01",
            "a monster, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FNo. I can't decide it on\x01",
            "this alone.\x02\x03",
            "#00000FBut, combined with other\x01",
            "elements... It seems more\x01",
            "and more like the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Other elements?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FThis case shares many common\x01",
            "elements with other similar cases,\x01",
            "right?\x02\x03",
            "#00003FThere were no witnesses... The\x01",
            "crime occurred at waterside... The\x01",
            "modus operandi is exactly the same.\x02\x03",
            "#00001FThinking about those elements, it's\x01",
            "likely the same criminal is\x01",
            "responsible for all cases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. Although no name appears\x01",
            "consistently on the guest\x01",
            "list during an incident...\x02",
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
            "#12P#00003FYes. In other words, the\x01",
            "criminal isn't among your\x01",
            "regular guests.\x02\x03",
            "#00000FAnd because of your lifeguard,\x01",
            "the criminal couldn't have\x01",
            "come via the lake either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, if there was a guy who\x01",
            "tried to slip in, I think I\x01",
            "would have noticed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FThat considered, there's only one route\x01",
            "the criminal could have used to get to\x01",
            "the crime scene.\x02\x03",
            "The waters of Elm Lake... It's possible\x01",
            "if there's an aquatic monster whose\x01",
            "habitat is nearby.\x02\x03",
            "#00003FAnd, in the case of a small aquatic\x01",
            "monster, they could approach visitors on\x01",
            "the beach without the lifeguard noticing.\x02\x03",
            "#00001FPut another way... The crime couldn't\x01",
            "have occurred any other way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "S-So the incident could\x01",
            "only have been caused by\x01",
            "a monster. Is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It does seem to line\x01",
            "up...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "W-Wait a moment. Aren't\x01",
            "you forgetting something\x01",
            "important?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Why does a monster have\x01",
            "any need to tear women's\x01",
            "swimsuits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "T-There is that... What\x01",
            "do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Could it have been the\x01",
            "doing of some pervert\x01",
            "somewhere?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FO-Obviously someone like\x01",
            "that would have a motive,\x01",
            "but...\x02\x03",
            "#00001FThe fact that this incident\x01",
            "could only have been caused\x01",
            "by a monster hasn't changed.\x02\x03",
            "#00003FAll that leaves us with is\x01",
            ""a monster with such a\x01",
            "trait", right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But... What should we\x01",
            "do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Appearances of this monster\x01",
            "will impact confidence in the\x01",
            "Michelam Operations Department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope we can take this\x01",
            "chance to exterminate it\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "But, it's elusive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If we wait until it\x01",
            "appears, we won't be able\x01",
            "to run the beach at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm. I'm the victim here,\x01",
            "and I won't want to come\x01",
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
            "#12P#01100FThen... What if KeA was\x01",
            "bait?\x02",
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

    def lambda_6F44():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F44)
    Sleep(100)

    def lambda_6F54():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6F54)
    Sleep(100)

    def lambda_6F64():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6F64)
    Sleep(100)

    def lambda_6F74():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6F74)
    Sleep(100)

    def lambda_6F84():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6F84)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00011FK-KeA!? What are you\x01",
            "saying!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01105FI mean, that monster\x01",
            "wants to tear girls'\x01",
            "swimsuits, right?\x02\x03",
            "#01103FIf KeA plays by the\x01",
            "shore, it might come out\x01",
            "again.\x02\x03",
            "#01109FWhen that happens,\x01",
            "KeA'll be fine if you\x01",
            "protect me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FN-Now look here... There's\x01",
            "no way I can put you in\x01",
            "that kind of danger, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "T-That's right little\x01",
            "lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "So far it's just been some\x01",
            "torn swimsuits, but who can\x01",
            "say what'll happen next time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01108FHmm, but... Bell will be\x01",
            "troubled with the monster\x01",
            "still here, right?\x02\x03",
            "#01106FAs a thank-you for\x01",
            "inviting us, I want to\x01",
            "exterminate it somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FY-You have a point,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00003F...All right.\x02\x03",
            "#00001FI don't know if KeA's\x01",
            "plan will work, but\x01",
            "we'll do what we can.\x02\x03",
            "#00003FBut you won't be the\x01",
            "bait, KeA. It'll be one\x01",
            "of our friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01101FYeah!\x02",
    )

    CloseMessageWindow()

    def lambda_7303():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7303)
    Sleep(100)

    def lambda_7313():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7313)
    Sleep(100)

    def lambda_7323():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7323)
    Sleep(100)

    def lambda_7333():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7333)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "No way... Will they be\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes. The Support Section's members\x01",
            "are used to fighting monsters... I\x01",
            "think it'll be all right.\x02\x03",
            "#00003FProblem is, who will be the\x01",
            "bait...\x02\x03",
            "#00000FIt seems like I could ask Elie,\x01",
            "Tio or Noｱl for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01105FLloyd, who will you\x01",
            "call?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00003FLet me see...\x02",
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
            "#1KWho will you ask to be\x01",
            "the bait?\x07\x00\x02",
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
        (0, "loc_752F"),
        (1, "loc_7561"),
        (2, "loc_7592"),
        (SWITCH_DEFAULT, "loc_75C4"),
    )


    label("loc_752F")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x15B, 6)

    ChrTalk(
        0x101,
        "#6P#00000F...I'll ask Elie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_75C4")

    label("loc_7561")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x15B, 7)

    ChrTalk(
        0x101,
        "#6P#00000F...I'll ask Tio.\x02",
    )

    CloseMessageWindow()
    Jump("loc_75C4")

    label("loc_7592")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C4, 5)

    ChrTalk(
        0x101,
        "#6P#00000F...I'll ask Noｱl.\x02",
    )

    CloseMessageWindow()
    Jump("loc_75C4")

    label("loc_75C4")


    ChrTalk(
        0x153,
        (
            "#12P#01109FYeah, in that case,\x01",
            "everything's gonna be\x01",
            "all right!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00003FAnd so... I'd like to begin\x01",
            "the monster extermination\x01",
            "on the beach right away.\x02\x03",
            "#00000FCan I ask the staff to\x01",
            "clear the area?\x02",
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
            "Let's call this inspection\x01",
            "time and have the guests\x01",
            "leave for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Careful you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Beat up that swimsuit-\x01",
            "tearing monster for us!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FAlright, please leave it\x01",
            "to us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01109FAll right, let's gooo!!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_77D7")
    AddParty(0x1, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x1)
    Jump("loc_77F9")

    label("loc_77D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_77EF")
    AddParty(0x2, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x2)
    Jump("loc_77F9")

    label("loc_77EF")

    AddParty(0x8, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x3)

    label("loc_77F9")

    SetScenarioFlags(0x22, 3)
    NewScene("t1310", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_4DAE end

    def Function_21_7806(): pass

    label("Function_21_7806")

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
        "Good work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to all of you, the Michelam\x01",
            "Operations Department got through this\x01",
            "incident without losing confidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha. We're just glad we\x01",
            "could help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thank you very much. I\x01",
            "don't know how we can\x01",
            "ever thank you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, I'll report these\x01",
            "development-related monster\x01",
            "incidents to Lady Mariabell.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_7AB0")

    ChrTalk(
        0x102,
        (
            "#00100FYes, I think that's a\x01",
            "good idea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B03")

    label("loc_7AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_7ADE")

    ChrTalk(
        0x103,
        "#00200FThat would be best.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B03")

    label("loc_7ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_7B03")

    ChrTalk(
        0x109,
        "#10100FYes, please do.\x02",
    )

    CloseMessageWindow()

    label("loc_7B03")


    ChrTalk(
        0x101,
        (
            "#00000FHaha. I think Mariabell\x01",
            "will think of some\x01",
            "countermeasures.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        "#12PHaha. Nice work㈱\x02",
    )

    CloseMessageWindow()

    def lambda_7B75():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B75)
    Sleep(100)

    def lambda_7B85():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7B85)
    Sleep(100)

    def lambda_7B95():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_7B95)
    Sleep(100)

    def lambda_7BA5():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7BA5)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#12PYou were able to exterminate the\x01",
            "monster criminal in this torn\x01",
            "swimsuit case, weren't you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#12PAlllright, if that's\x01",
            "settled, let's have more\x01",
            "fun on the beach!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#6PWhat, you're going\x01",
            "again!? I thought you\x01",
            "learned your lesson...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PIsn't it obvious!? We\x01",
            "came all the way here.\x01",
            "We have to have fun.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#12PHaha. Then, we'll excuse\x01",
            "ourselves.\x02",
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
            "#12PI have to get back to\x01",
            "the lifeguard stand.\x01",
            "Thanks everyone.\x02",
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
            "#00000FIt's about time for us\x01",
            "to be going as well.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x153,
        "#6P#01100FYeah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_7EA4")

    ChrTalk(
        0x102,
        (
            "#00104FI want to look in the\x01",
            "boutique a while longer.\x01",
            "I'll see you there.\x02\x03",
            "#00100FHaha. Later, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F87")

    label("loc_7EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_7F1A")

    ChrTalk(
        0x103,
        (
            "#00204FI'll go to the theme\x01",
            "park ahead of you.\x02\x03",
            "#00202FZeit and Sully are\x01",
            "waiting for me. See you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F87")

    label("loc_7F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_7F87")

    ChrTalk(
        0x109,
        (
            "#10100FI'll go browse the\x01",
            "jewelry store with Fran\x01",
            "a while longer.\x02\x03",
            "#10109FThen, see you later!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F87")


    def lambda_7F8C():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F8C)
    Sleep(200)

    def lambda_7F9C():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7F9C)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FYeah, see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01109FSee you later!\x02",
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
            "Quest [The Torn Swimsuit\x01",
            "Case]\x07\x00",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_806A")
    RemoveParty(0x1, 0xFF)
    Jump("loc_8087")

    label("loc_806A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_807B")
    RemoveParty(0x2, 0xFF)
    Jump("loc_8087")

    label("loc_807B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_8087")
    RemoveParty(0x8, 0xFF)

    label("loc_8087")

    EventEnd(0x5)
    SetScenarioFlags(0x22, 1)
    NewScene("t1020", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_21_7806 end

    def Function_22_8096(): pass

    label("Function_22_8096")

    OP_95(0xE, 4990, 0, 50, 2000, 0x0)
    OP_95(0xE, 6570, 0, 1030, 2000, 0x0)
    OP_95(0xE, 10000, 0, 1020, 2000, 0x0)
    Return()

    # Function_22_8096 end

    def Function_23_80D3(): pass

    label("Function_23_80D3")

    OP_95(0xD, 4990, 0, 50, 2000, 0x0)
    OP_95(0xD, 6570, 0, 1030, 2000, 0x0)
    OP_95(0xD, 10000, 0, 1020, 2000, 0x0)
    Return()

    # Function_23_80D3 end

    def Function_24_8110(): pass

    label("Function_24_8110")

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

    # Function_24_8110 end

    SaveToFile()

Try(main)
