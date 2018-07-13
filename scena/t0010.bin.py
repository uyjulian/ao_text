from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0010.bin",                # FileName
        "t0010",                    # MapName
        "t0010",                    # Location
        0x0037,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x19,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 55, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0010",                  # 0
        "Miria",                  # 1
        "Donald",                 # 2
        "Ange",                   # 3
        "Village Chief Tolta",    # 4
        "Mrs. Ena",               # 5
        "Derrick",                # 6
        "Elkin",                  # 7
        "Harold",                 # 8
        "Pete",                   # 9
        "Village Chief Tolta",    # 10
        "Geval",                  # 11
        "Alm",                    # 12
        "Aerie",                  # 13
    ))

    AddCharChip((
        "chr/ch24002.itc",                   # 00
        "chr/ch45400.itc",                   # 01
        "chr/ch09302.itc",                   # 02
        "chr/ch24300.itc",                   # 03
        "chr/ch32300.itc",                   # 04
        "chr/ch23702.itc",                   # 05
        "chr/ch24202.itc",                   # 06
        "chr/ch24100.itc",                   # 07
        "chr/ch24400.itc",                   # 08
        "chr/ch22200.itc",                   # 09
        "chr/ch24302.itc",                   # 0A
        "chr/ch24000.itc",                   # 0B
        "chr/ch47700.itc",                   # 0C
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

    DeclNpc(519,     180,     4294965446, 180,  261,  0x0, 0,   5,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(38409,   180,     540,     180,  261,  0x0, 0,   6,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(33700,   0,       4294964677, 204,  261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294928817, 180,     4294965517, 90,   325,  0x0, 0,   0,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(4294885676, 0,       3410,    0,    261,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294929247, 0,       4294967156, 180,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294966157, 0,       2380,    90,   389,  0x0, 0,   8,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(4294933096, 180,     4294965767, 270,  389,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294932896, 0,       4294966996, 270,  389,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(76569,   0,       4294965116, 0,    389,  0x0, 0,   11,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(75800,   0,       2000,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(792, 0)                                        # 0

    ScpFunction((
        "Function_0_318",          # 00, 0
        "Function_1_3D0",          # 01, 1
        "Function_2_3FB",          # 02, 2
        "Function_3_65A",          # 03, 3
        "Function_4_693",          # 04, 4
        "Function_5_1940",         # 05, 5
        "Function_6_2867",         # 06, 6
        "Function_7_299C",         # 07, 7
        "Function_8_3554",         # 08, 8
        "Function_9_4B86",         # 09, 9
        "Function_10_4F80",        # 0A, 10
        "Function_11_527B",        # 0B, 11
        "Function_12_61A8",        # 0C, 12
        "Function_13_6667",        # 0D, 13
        "Function_14_68AC",        # 0E, 14
        "Function_15_69BA",        # 0F, 15
        "Function_16_6F0D",        # 10, 16
        "Function_17_7045",        # 11, 17
        "Function_18_70CE",        # 12, 18
        "Function_19_7C73",        # 13, 19
        "Function_20_8236",        # 14, 20
        "Function_21_8383",        # 15, 21
        "Function_22_8EB1",        # 16, 22
        "Function_23_91BB",        # 17, 23
        "Function_24_A009",        # 18, 24
        "Function_25_AE3B",        # 19, 25
        "Function_26_B61A",        # 1A, 26
        "Function_27_C9BD",        # 1B, 27
        "Function_28_CA08",        # 1C, 28
        "Function_29_CA53",        # 1D, 29
        "Function_30_CA9E",        # 1E, 30
        "Function_31_CAE9",        # 1F, 31
        "Function_32_CB34",        # 20, 32
        "Function_33_CB7F",        # 21, 33
        "Function_34_CBDE",        # 22, 34
        "Function_35_CC0D",        # 23, 35
        "Function_36_CC24",        # 24, 36
        "Function_37_CC3B",        # 25, 37
        "Function_38_D2C7",        # 26, 38
        "Function_39_D312",        # 27, 39
    ))


    def Function_0_318(): pass

    label("Function_0_318")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_358"),
        (1, "loc_364"),
        (2, "loc_370"),
        (3, "loc_37C"),
        (4, "loc_388"),
        (5, "loc_394"),
        (6, "loc_3A0"),
        (SWITCH_DEFAULT, "loc_3AC"),
    )


    label("loc_358")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_364")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_370")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_37C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_388")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_394")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3CF")

    Return()

    # Function_0_318 end

    def Function_1_3D0(): pass

    label("Function_1_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FA")
    OP_94(0xFE, 0xFFFFF326, 0xB68, 0x100E, 0xFFFFFEDE, 0x7D0)
    Sleep(250)
    Jump("Function_1_3D0")

    label("loc_3FA")

    Return()

    # Function_1_3D0 end

    def Function_2_3FB(): pass

    label("Function_2_3FB")

    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0x8, 0x5)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CB")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -47480, 0, -1230, 90)
    SetChrChipByIndex(0xB, 0xB)
    ClearChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x40)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, -46490, 0, -1230, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490")
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_490")

    SetChrChipByIndex(0xA, 0xA)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 38320, 180, -2250, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C6")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_4C6")

    Jump("loc_5FA")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4D9")
    Jump("loc_5FA")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_4E7")
    Jump("loc_5FA")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_5FA")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_51E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_519")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_519")

    Jump("loc_5FA")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_540")
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_5FA")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_584")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_57A")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x2)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_57F")

    label("loc_57A")

    SetChrFlags(0xB, 0x80)

    label("loc_57F")

    Jump("loc_5FA")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5AF")
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x2)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)

    label("loc_5AF")

    Jump("loc_5FA")

    label("loc_5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C2")
    Jump("loc_5FA")

    label("loc_5C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrFlags(0xA, 0x80)
    Jump("loc_5FA")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_5FA")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5F1")
    Jump("loc_5FA")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5FA")

    label("loc_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_60E")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_659")

    label("loc_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_622")
    ClearScenarioFlags(0x22, 1)
    Event(0, 23)
    Jump("loc_659")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_636")
    ClearScenarioFlags(0x22, 2)
    Event(0, 24)
    Jump("loc_659")

    label("loc_636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_64A")
    ClearScenarioFlags(0x22, 3)
    Event(0, 26)
    Jump("loc_659")

    label("loc_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_659")
    ClearScenarioFlags(0x22, 4)
    Event(0, 37)

    label("loc_659")

    Return()

    # Function_2_3FB end

    def Function_3_65A(): pass

    label("Function_3_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_66C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_692")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_692")

    Return()

    # Function_3_65A end

    def Function_4_693(): pass

    label("Function_4_693")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78C")

    ChrTalk(
        0xFE,
        (
            "I heard the President was\x01",
            "arrested in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that we can move\x01",
            "freely, the Bracers will\x01",
            "be here right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The situation being what it is,\x01",
            "we have to combine the whole\x01",
            "strength of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_82C")

    label("loc_78C")


    ChrTalk(
        0xFE,
        (
            "Now that we can move\x01",
            "freely, the Bracers will\x01",
            "be here right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The situation being what it is,\x01",
            "we have to combine the whole\x01",
            "strength of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82C")

    Jump("loc_193C")

    label("loc_831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93F")

    ChrTalk(
        0xFE,
        (
            "Recently, Derrick has been checking\x01",
            "to see if the villagers are safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In a situation like this, even just\x01",
            "seeing the faces of your friends\x01",
            "can make you feel relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected from Derrick,\x01",
            "he's serious and has an even head.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9F2")

    label("loc_93F")


    ChrTalk(
        0xFE,
        (
            "Recently, Derrick has been checking\x01",
            "to see if the villagers are safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just seeing the faces of your\x01",
            "friends can make you feel relieved.\x01",
            "Uh uh, that's very like Derrick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F2")

    Jump("loc_193C")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_BCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1C")

    ChrTalk(
        0xFE,
        (
            "Everyday my brother Elkin\x01",
            "does nothing but sigh saying\x01",
            "that he can't drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because it's an uneasy situation\x01",
            "and he feels depressed, he\x01",
            "complains and complains...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just be thankful we can eat\x01",
            "fresh food daily, even in\x01",
            "a situation like this, jeez.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BC5")

    label("loc_B1C")


    ChrTalk(
        0xFE,
        (
            "Everyday my brother Elkin\x01",
            "does nothing but sigh saying\x01",
            "that he can't drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just be thankful we can eat\x01",
            "fresh food daily, even in\x01",
            "a situation like this, jeez.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC5")

    Jump("loc_193C")

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CA0")

    ChrTalk(
        0xFE,
        (
            "I've being seen strange monsters\x01",
            "wearing something like an armor \x01",
            "around the Ancient Battlefield lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if they're runaway monsters a rich \x01",
            "person somewhere was keeping as pets...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_193C")

    label("loc_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D58")

    ChrTalk(
        0xFE,
        (
            "To us farmers, rain is\x01",
            "like a blessing on our\x01",
            "crops from heaven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's thanks to the Goddess\x01",
            "that we can eat. I must pay\x01",
            "my proper respects to her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DD3")

    label("loc_D58")


    ChrTalk(
        0xFE,
        (
            "To us farmers, rain is\x01",
            "like a blessing on our\x01",
            "crops from heaven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to pay my proper\x01",
            "respect to the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD3")

    Jump("loc_193C")

    label("loc_DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFA")

    ChrTalk(
        0xFE,
        (
            "The reform Derrick is advancing in\x01",
            "the village... I don't really get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By introducing orbal tools in the fields,\x01",
            "various things will get easier, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I like field work. I have mixed feelings\x01",
            "about having my work taken by machines.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F8D")

    label("loc_EFA")


    ChrTalk(
        0xFE,
        (
            "It's nice that things\x01",
            "will get easier due to\x01",
            "village reform, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I like field work. I have mixed\x01",
            "feelings about it becoming too easy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8D")

    Jump("loc_10B9")

    label("loc_F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1047")

    ChrTalk(
        0xFE,
        (
            "That Minneth deceived\x01",
            "all of the villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think a person in this\x01",
            "world exists who could deceive\x01",
            "others without remorse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I learned something.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10B9")

    label("loc_1047")


    ChrTalk(
        0xFE,
        (
            "To think a person in this\x01",
            "world exists who could deceive\x01",
            "others without remorse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I learned something.\x02",
    )

    CloseMessageWindow()

    label("loc_10B9")

    Jump("loc_193C")

    label("loc_10BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_132E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1253")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D6")

    ChrTalk(
        0xFE,
        (
            "If you're looking for Elkin, he's\x01",
            "delivering our produce to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's been in high spirits\x01",
            "lately. He often takes side\x01",
            "trips on his way back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, he got something\x01",
            "like that for cheap, so I\x01",
            "understand why he's happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_124E")

    label("loc_11D6")


    ChrTalk(
        0xFE,
        (
            "If you're looking for Elkin, he's\x01",
            "delivering our produce to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think he'll\x01",
            "be back for awhile.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124E")

    Jump("loc_1329")

    label("loc_1253")


    ChrTalk(
        0xFE,
        (
            "That Elkin. He's been in a good\x01",
            "mood ever since that Minneth sold\x01",
            "him that orbal truck for cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand how he's feeling but...\x01",
            "I've got to tell him often to take\x01",
            "care not to get into an accident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1329")

    Jump("loc_193C")

    label("loc_132E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_153B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C8")

    ChrTalk(
        0xFE,
        (
            "For generations, we've selected the best person\x01",
            "among the villagers to be the chief by majority rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The villagers all acknowledge the chief's son, Derrick,\x01",
            "as being the right man to be the next Village Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Derrick is serious. he thinks\x01",
            "hard about everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thinking about the village's future\x01",
            "is a good thing... But I want him\x01",
            "to rely on us a little more.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1536")

    label("loc_14C8")


    ChrTalk(
        0xFE,
        (
            "Derrick is serious. he thinks\x01",
            "hard about everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing good will come\x01",
            "of worrying by himself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1536")

    Jump("loc_193C")

    label("loc_153B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_177C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CA")

    ChrTalk(
        0xFE,
        (
            "Elkin's accent is what they\x01",
            "call "Armorica's accent."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the village, only the old Donald and\x01",
            "Elkin speak that way. It's an accent\x01",
            "that's been handed down over generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It feels like "This is what it means to be\x01",
            "a villager from Armorica", so I don't think \x01",
            "he has to force himself to correct it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Men... They worry about\x01",
            "the silliest things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1777")

    label("loc_16CA")


    ChrTalk(
        0xFE,
        (
            "Elkin's Armorica's accent has been\x01",
            "passed down for generations.\x01",
            "In a way, it's a valuable thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't hate it. I don't think he\x01",
            "has to force himself to fix it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1777")

    Jump("loc_193C")

    label("loc_177C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_193C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189C")

    ChrTalk(
        0xFE,
        (
            "It's been really peaceful lately.\x01",
            "There's been rainy days too,\x01",
            "so the crops are growing well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the weather's like it is today,\x01",
            "I feel like basking in the sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I could spread out straw on the orbal\x01",
            "truck and then take an afternoon nap.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_193C")

    label("loc_189C")


    ChrTalk(
        0xFE,
        (
            "When the weather's like it is today,\x01",
            "I feel like basking in the sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I could spread out straw on the orbal\x01",
            "truck and then take an afternoon nap.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_193C")

    TalkEnd(0xFE)
    Return()

    # Function_4_693 end

    def Function_5_1940(): pass

    label("Function_5_1940")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195E")
    Call(0, 6)
    Jump("loc_19CC")

    label("loc_195E")


    ChrTalk(
        0xFE,
        "*sigh*, it's as Ange says, isn't it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Us farmers have to\x01",
            "work to preserve the\x01",
            "village's food supply.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CC")

    Jump("loc_2863")

    label("loc_19D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B06")

    ChrTalk(
        0xFE,
        (
            "Ever since the declaration of\x01",
            "independence, our truck hasn't been\x01",
            "able to go to Crossbell City, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure there are people in Crossbell\x01",
            "City who are eagerly awaiting the\x01",
            "arrival of fresh veggies, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To us producers, not\x01",
            "being able to deliver\x01",
            "them is painful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BCE")

    label("loc_1B06")


    ChrTalk(
        0xFE,
        (
            "I'm sure there are people in Crossbell\x01",
            "City who are eagerly awaiting the\x01",
            "arrival of fresh veggies, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope this declaration of invalidity is\x01",
            "connected to the resumption of our business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCE")

    Jump("loc_2863")

    label("loc_1BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D13")

    ChrTalk(
        0xFE,
        (
            "A "Cryptid" monster laid waste\x01",
            "to our fields along the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That together with the movement restrictions,\x01",
            "and our harvest's looking quite poor...\x01",
            "Honestly, our business is doomed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even so, the village is\x01",
            "somehow self-sufficient. We must\x01",
            "thank to the Goddess for that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D8B")

    label("loc_1D13")


    ChrTalk(
        0xFE,
        (
            "We can at least\x01",
            "feed our village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's just, how long will\x01",
            "this situation go on? \x01",
            "...I honestly have no idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8B")

    Jump("loc_2863")

    label("loc_1D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1ED0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E59")

    ChrTalk(
        0xFE,
        (
            "I'm surprised the\x01",
            "city was attacked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And what's more, it seems the\x01",
            "attackers haven't been captured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but be worried\x01",
            "that they'll come to Armorica.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ECB")

    label("loc_1E59")


    ChrTalk(
        0xFE,
        (
            "I've been anxious ever since\x01",
            "the attack on the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I can't give field\x01",
            "work everything I have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECB")

    Jump("loc_2863")

    label("loc_1ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1FFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F99")

    ChrTalk(
        0xFE,
        (
            "Camille and the others have a Sunday\x01",
            "School lesson at the bar-inn today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, I can only teach them\x01",
            "stuff about farming, you know.\x01",
            "I want them to study hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FF9")

    label("loc_1F99")


    ChrTalk(
        0xFE,
        "Now then, I think I'll take a day off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's been awhile since I took it easy at home.\x02",
    )

    CloseMessageWindow()

    label("loc_1FF9")

    Jump("loc_2863")

    label("loc_1FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2262")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C5")

    ChrTalk(
        0xFE,
        (
            "Mr. Minneth is planning on building\x01",
            "something at our private property \x01",
            "on the old road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That place is our farm tools\x01",
            "storehouse... I guess we'll\x01",
            "have to move it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225D")

    label("loc_20C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A9")

    ChrTalk(
        0xFE,
        (
            "So that Minneth turned\x01",
            "out to be a bad guy, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too was completely deceived\x01",
            "by his smile and attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But it must have been a real\x01",
            "shock to Derrick. I hope he's\x01",
            "not too hard on himself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_225D")

    label("loc_21A9")


    ChrTalk(
        0xFE,
        (
            "He must have been a really bad guy\x01",
            "if he tricked Derrick, who is always\x01",
            "the first to care about our village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The next time I see\x01",
            "that Minneth, I'm gonna\x01",
            "let him have it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225D")

    Jump("loc_2863")

    label("loc_2262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2309")

    ChrTalk(
        0xFE,
        (
            "The foreigner who's been coming to the\x01",
            "village recently is quite the cheerful fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He always smiles, and it makes\x01",
            "me feel at ease, somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2863")

    label("loc_2309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_24E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2402")

    ChrTalk(
        0xFE,
        (
            "Elkin consulted\x01",
            "me about the\x01",
            "truck, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's probably near the end of it's lifespan.\x01",
            "Even if maintained, it'll probably break soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's really precious to\x01",
            "Elkin. I hope he's not\x01",
            "too depressed over this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24E4")

    label("loc_2402")


    ChrTalk(
        0xFE,
        (
            "The village's orbal truck is probably\x01",
            "near the end of it's lifespan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The village doesn't have the mira for a new one,\x01",
            "so it'll be hard to break this to the chief. It won't\x01",
            "be good if we don't get a replacement soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E4")

    Jump("loc_2863")

    label("loc_24E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_26B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25DF")

    ChrTalk(
        0xFE,
        (
            "There are orbal tools for\x01",
            "farming in this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Orbal plows for tilling and orbal\x01",
            "tractors for harvesting... To a\x01",
            "farmer, these are indispensable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, those in Armorica are\x01",
            "worn-out and old fashioned.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26B2")

    label("loc_25DF")


    ChrTalk(
        0xFE,
        (
            "Orbal plows and tractors... In\x01",
            "this era, these orbal tools are\x01",
            "indispensable for farming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I could hape for more, I'd want\x01",
            "the more useful latest models, but...\x01",
            "Well, in the end, they'd be a luxury.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B2")

    Jump("loc_2863")

    label("loc_26B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2863")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C2")

    ChrTalk(
        0xFE,
        (
            "We produce various vegetables\x01",
            "in the fields of this village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The vegetables grown in\x01",
            "Armorica bathe in the light\x01",
            "of the sun, and grow by it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm happy they can be enjoyed in Crossbell\x01",
            "City too, since we ship them even there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2863")

    label("loc_27C2")


    ChrTalk(
        0xFE,
        (
            "The vegetables of Armorica\x01",
            "bathe in the light of the\x01",
            "sun, and grow by it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Imports have risen lately, but our\x01",
            "vegetables won't lose to their tastiness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2863")

    TalkEnd(0xFE)
    Return()

    # Function_5_1940 end

    def Function_6_2867(): pass

    label("Function_6_2867")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Ahhhh... I can't believe\x01",
            "something like that has\x01",
            "appeared in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm so anxious, I can't\x01",
            "start my farmwork...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh*, what kind of pathetic\x01",
            "thing are you saying now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Precisely because of times\x01",
            "like these, we have to work\x01",
            "hard for Camille and Pooley.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_6_2867 end

    def Function_7_299C(): pass

    label("Function_7_299C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29BA")
    Call(0, 6)
    Jump("loc_2A4D")

    label("loc_29BA")


    ChrTalk(
        0xFE,
        (
            "This man is rather timid,\x01",
            "so I have to encourage\x01",
            "him from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in times like\x01",
            "these that hard work is\x01",
            "especially important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4D")

    Jump("loc_3550")

    label("loc_2A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AFA")

    ChrTalk(
        0xFE,
        (
            "It looks like Colin is\x01",
            "playing with our little\x01",
            "ones again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Harold is always helping us,\x01",
            "so I think I'll treat him today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BA7")

    label("loc_2AFA")


    ChrTalk(
        0xFE,
        (
            "Mr. Harold is always helping us,\x01",
            "so I think I'll treat him today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha, I wonder if Colin, who eats\x01",
            "Mrs. Sophia's cooking every day,\x01",
            "will be unsatisfied with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA7")

    Jump("loc_3550")

    label("loc_2BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2D0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8E")

    ChrTalk(
        0xFE,
        (
            "Mr. Harold's wife is really\x01",
            "good at cooking, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand she holds\x01",
            "cooking classes in her\x01",
            "home in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the situation was different,\x01",
            "I would like to try going there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D09")

    label("loc_2C8E")


    ChrTalk(
        0xFE,
        (
            "Mr. Harold's wife is really\x01",
            "good at cooking, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our kids are close in age too,\x01",
            "and easily became friends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D09")

    Jump("loc_3550")

    label("loc_2D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E0B")

    ChrTalk(
        0xFE,
        (
            "I heard the damage from\x01",
            "the attack was great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Oh, no, enough.\x01",
            "If all I talk about is that,\x01",
            "it'll ruin my mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially because it's a time\x01",
            "like this, we have to cheerfully\x01",
            "live out ordinary days as usual.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EC3")

    label("loc_2E0B")


    ChrTalk(
        0xFE,
        (
            "Whenever I hear about the raid\x01",
            "attack, it always ruins my mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially because it's a time like\x01",
            "this, the most important thing is to\x01",
            "live out our ordinary days as usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC3")

    Jump("loc_3550")

    label("loc_2EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3059")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD0")

    ChrTalk(
        0xFE,
        (
            "It seems the Village Chief and\x01",
            "Derrick made up through\x01",
            "yesterday's incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those two put the needs of\x01",
            "the village above all else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although the village has declined\x01",
            "recently, I'm sure things will be\x01",
            "better going forward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3054")

    label("loc_2FD0")


    ChrTalk(
        0xFE,
        (
            "The Village Chief and Derrick put the \x01",
            "needs of the village above all else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure things will be\x01",
            "better going forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3054")

    Jump("loc_3550")

    label("loc_3059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_316A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30ED")

    ChrTalk(
        0xFE,
        (
            "But even so, to think\x01",
            "the village reform could\x01",
            "happen this quickly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It must be due to Mr.\x01",
            "Minneth's ability.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3165")

    label("loc_30ED")


    ChrTalk(
        0xFE,
        (
            "I never expected that\x01",
            "Mr. Minneth would\x01",
            "release monsters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, thank goodness our\x01",
            "children weren't hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3165")

    Jump("loc_3550")

    label("loc_316A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A5")

    ChrTalk(
        0xFE,
        "Now then, what to make today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3223")

    label("loc_31A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B7")
    Call(0, 22)
    Jump("loc_3223")

    label("loc_31B7")


    ChrTalk(
        0xFE,
        (
            "Wow, that guy's a\x01",
            "person of character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's nice to our kids too...\x01",
            "I don't think he's a bad guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3223")

    Jump("loc_3550")

    label("loc_3228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330F")

    ChrTalk(
        0xFE,
        (
            "In the fields, we sometimes get\x01",
            "oddly-shaped fruits or vegetables...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't sell those, so we\x01",
            "share them within the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter the shape,\x01",
            "they're delicious all\x01",
            "the same, you see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33E0")

    label("loc_330F")


    ChrTalk(
        0xFE,
        (
            "Oddly-shaped fruits and vegetables\x01",
            "can't be sold in a store, so we\x01",
            "share them amongst the villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't understand city dwellers,\x01",
            "who wouldn't buy something this\x01",
            "delicious because of its shape.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E0")

    Jump("loc_3550")

    label("loc_33E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33F3")
    Jump("loc_3550")

    label("loc_33F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C9")

    ChrTalk(
        0xFE,
        (
            "Mrs. Aretha officially\x01",
            "moved here recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her son plays with our\x01",
            "kids. It's a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're now renting a room\x01",
            "at the inn. I think I'll go\x01",
            "say hi every now and then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3550")

    label("loc_34C9")


    ChrTalk(
        0xFE,
        (
            "Stefan often\x01",
            "plays with\x01",
            "our kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't have many children in this village.\x01",
            "Thank goodness they could make a good friend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3550")

    TalkEnd(0xFE)
    Return()

    # Function_7_299C end

    def Function_8_3554(): pass

    label("Function_8_3554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3581")
    Call(0, 25)
    Return()

    label("loc_3581")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35A6")
    Call(0, 19)
    Return()

    label("loc_35A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_37A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C4")
    Call(0, 13)
    Jump("loc_37A0")

    label("loc_35C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F7")

    ChrTalk(
        0xFE,
        (
            "Harold returned to\x01",
            "the city earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I discussed with Derrick how the village\x01",
            "is going to deal with this going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish Harold had remained\x01",
            "for awhile longer, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he wanted to visit various\x01",
            "places, doing what he can. \x01",
            "...I suppose it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37A0")

    label("loc_36F7")


    ChrTalk(
        0xFE,
        (
            "...We'll be able to deal with\x01",
            "this, but I wish Harold had\x01",
            "remained for awhile longer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, a Bracer has\x01",
            "also come.... We've got\x01",
            "to do our best, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A0")

    Jump("loc_4B82")

    label("loc_37A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_396D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C5")

    ChrTalk(
        0xFE,
        (
            "After the independence declaration of invalidity,\x01",
            "Derrick is working hard about many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This situation... I've served\x01",
            "a long time as Village Chief, \x01",
            "yet I don't know what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, it's\x01",
            "important for each of\x01",
            "us to do what we can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3968")

    label("loc_38C5")


    ChrTalk(
        0xFE,
        (
            "This situation... I've served\x01",
            "a long time as Village Chief, \x01",
            "yet I don't know what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, it's\x01",
            "important for each of\x01",
            "us to do what we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3968")

    Jump("loc_4B82")

    label("loc_396D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_3B17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A79")

    ChrTalk(
        0xFE,
        (
            "Hmm, I can't believe those people\x01",
            "were at the Ancient Battlefield...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though they are people we mustn't let\x01",
            "down our guard to, they show no sign\x01",
            "of aggression towards the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll keep our eye on\x01",
            "them for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B12")

    label("loc_3A79")


    ChrTalk(
        0xFE,
        (
            "The people concealed in the\x01",
            "Ancient Battlefield show no sign\x01",
            "of aggression towards the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll keep our eye on\x01",
            "them for the time being.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B12")

    Jump("loc_4B82")

    label("loc_3B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3D21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C90")

    ChrTalk(
        0xFE,
        (
            "To be perfectly honest, I feel President\x01",
            "Dieter isn't one to be followed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, compared to the influence\x01",
            "on the population of Crossbell City,\x01",
            "it's like there's none in this village...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Anyway, Harold's\x01",
            "family too is\x01",
            "helping us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no choice other than for us villagers to\x01",
            "cooperate and get through these difficulties.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D1C")

    label("loc_3C90")


    ChrTalk(
        0xFE,
        (
            "Harold's family is\x01",
            "helping us too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no choice other than for us villagers to\x01",
            "cooperate and get through these difficulties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D1C")

    Jump("loc_4B82")

    label("loc_3D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_40B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3E94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1D")

    ChrTalk(
        0xFE,
        (
            "Uh uh. It's a difficult time in many ways,\x01",
            "but... Thanks to that, my heart is warmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, please leave\x01",
            "Mr. Geval to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll look after him properly until he\x01",
            "calms down and returns to the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E8F")

    label("loc_3E1D")


    ChrTalk(
        0xFE,
        (
            "Please leave\x01",
            "Mr. Geval to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll look after him properly until he\x01",
            "calms down and returns to the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E8F")

    Jump("loc_40AE")

    label("loc_3E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE0")

    ChrTalk(
        0xFE,
        (
            "The attack on the city a few days\x01",
            "ago... Anxiety is spreading amongst\x01",
            "the citizens of Armorica Village, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The theory that it was an Imperial\x01",
            "conspiracy is spreading, but without\x01",
            "definitive proof, I hesitate to swallow it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Anyway, right now, we\x01",
            "have to guard the village\x01",
            "and surrounding areas.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40AE")

    label("loc_3FE0")


    ChrTalk(
        0xFE,
        (
            "I asked our village's young men, Derrick\x01",
            "included, to guard the surrounding areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to make the village citizens\x01",
            "any more anxious than they already are,\x01",
            "but... We have to be vigilant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40AE")

    Jump("loc_4B82")

    label("loc_40B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CE")
    Call(0, 10)
    Jump("loc_4164")

    label("loc_40CE")


    ChrTalk(
        0xFE,
        (
            "Hmm. Making the village\x01",
            "features known to everyone\x01",
            "is not bad at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they're interested, migration\x01",
            "in the village could increase too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4164")

    Jump("loc_4B82")

    label("loc_4169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4343")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4184")
    Jump("loc_433E")

    label("loc_4184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4193")
    Jump("loc_433E")

    label("loc_4193")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A5")
    Jump("loc_433E")

    label("loc_41A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4294")

    ChrTalk(
        0xFE,
        "To protect this village called Armorica...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our objectives were the same, but my\x01",
            "son's and my views were both too narrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This case must have been a trial given to\x01",
            "us by the Goddess to make us realize that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_433E")

    label("loc_4294")


    ChrTalk(
        0xFE,
        (
            "To protect this village called Armorica...\x01",
            "It's a feeling my son and I both share.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, I'll have to properly listen\x01",
            "to the words of the young men too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_433E")

    Jump("loc_4B82")

    label("loc_4343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4654")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435E")
    Jump("loc_464F")

    label("loc_435E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_436D")
    Jump("loc_464F")

    label("loc_436D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_453C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_447C")

    ChrTalk(
        0xFE,
        (
            "Derrick's secret discussions with that foreigner...\x01",
            "It's suspicious, no matter how you look at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If some sort of evil scheme is being planned,\x01",
            "it must be dealt with immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please everyone, collect information for me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4537")

    label("loc_447C")


    ChrTalk(
        0xFE,
        (
            "Derrick's secret discussions with the\x01",
            "foreigner... If they're cooking up some sort of\x01",
            "evil plan, it must be dealt with immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please everyone, collect information for me.\x02",
    )

    CloseMessageWindow()

    label("loc_4537")

    Jump("loc_464F")

    label("loc_453C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45ED")

    ChrTalk(
        0xFE,
        (
            "Truly, good work everyone.\x01",
            "Thanks to you, I have a\x01",
            "rough idea of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Later, I'll speak with\x01",
            "Derrick as the chief and\x01",
            "try to persuade him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_464F")

    label("loc_45ED")


    ChrTalk(
        0xFE,
        (
            "As the Village Chief and his parent...\x01",
            "I've got to persuade Derrick\x01",
            "before he moves forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_464F")

    Jump("loc_4B82")

    label("loc_4654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_48AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_466F")
    Call(0, 9)
    Jump("loc_48A7")

    label("loc_466F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47FA")

    ChrTalk(
        0xFE,
        (
            "Lack of manpower because the young ones go away, \x01",
            "decline of the autonomous state internal food self-\x01",
            "sufficiency following the increase of foreign trades...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The village has a mountain of\x01",
            "problems... I can't accept Derrick's\x01",
            "reform proposals just like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The chief has a duty to protect the village's traditions\x01",
            "as well. I want him to understand that, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48A7")

    label("loc_47FA")


    ChrTalk(
        0xFE,
        (
            "The chief has a duty to protect the village's\x01",
            "traditions as well. Change isn't only a good thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the next Village Chief, I want\x01",
            "him to understand that, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48A7")

    Jump("loc_4B82")

    label("loc_48AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4AB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C7")
    Call(0, 9)
    Jump("loc_4AB1")

    label("loc_48C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49FD")

    ChrTalk(
        0xFE,
        (
            "To blindly accept reform and\x01",
            "ignore the village's traditions\x01",
            "is to invite disaster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know Derrick only wants the\x01",
            "best for the village when he thinks\x01",
            "about village reforms, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't lose sight of how the\x01",
            "village should be. I'll have to\x01",
            "consider his proposals carefully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AB1")

    label("loc_49FD")


    ChrTalk(
        0xFE,
        (
            "...Even I don't think the current\x01",
            "situation in the village is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, we can't lose sight of how the\x01",
            "village should be. I'll have to\x01",
            "consider his proposals carefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AB1")

    Jump("loc_4B82")

    label("loc_4AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AD1")
    Call(0, 9)
    Jump("loc_4B82")

    label("loc_4AD1")


    ChrTalk(
        0xFE,
        (
            "...These troubles are something I should\x01",
            "be solving myself in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If something happens,\x01",
            "I'll probably count on you, but...\x01",
            "For now, don't worry about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B82")

    TalkEnd(0xFE)
    Return()

    # Function_8_3554 end

    def Function_9_4B86(): pass

    label("Function_9_4B86")


    ChrTalk(
        0xB,
        "Oh, you're the Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FVillage Chief Tolta, it's been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ha ha. I'd heard you'd resumed\x01",
            "activities, but most importantly\x01",
            "you're all in good health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FUmm... You look\x01",
            "tired somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well... Recently, I've been worried\x01",
            "about a little personal problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, it's not on the level of something\x01",
            "you should trouble yourselves with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FDon't say that. If you're worried\x01",
            "about something, why not tell us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah. It's bad for your health keepin'\x01",
            "that stuff bottled up inside, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHa ha. The Special Support\x01",
            "Section may be able to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ha ha. It's really\x01",
            "no big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I'm really unable to do anything\x01",
            "I'll send you guys a request, so\x01",
            "there's no need to worry for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... \x01",
            "Understood.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F15")

    ChrTalk(
        0x103,
        (
            "#00200FPlease contact us if\x01",
            "you ever need anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F57")

    label("loc_4F15")


    ChrTalk(
        0x102,
        (
            "#00100FPlease contact us if you\x01",
            "ever need anything, alright?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F57")


    ChrTalk(
        0xB,
        (
            "Sure. \x01",
            "I'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 1)
    Return()

    # Function_9_4B86 end

    def Function_10_4F80(): pass

    label("Function_10_4F80")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "Derrick, about your idea, the\x01",
            ""Bee-Keeping Experience Event"...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It has appeal for sure, but is it really\x01",
            "all right to let amateurs into our fields?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I know that, but... \x01",
            "Honey is our village's specialty. \x01",
            "I don't think it's too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I was thinking we could show\x01",
            "them how to cope with bees...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm. I could consider it...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_51B3")

    ChrTalk(
        0x101,
        (
            "#00002F(It looks like the Village Chief and \x01",
            "Mr. Derrick could reconcile...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F("What doesn't kill you makes you\x01",
            "stronger", they say, right?\x01",
            "*giggle*, let's not interrupt them.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_526F")

    label("loc_51B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_526F")

    ChrTalk(
        0x101,
        (
            "#00005F(Huh? The Village Chief and Mr. Derrick... \x01",
            "It looks like they made up just like that.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F(It may have been through the\x01",
            "Minneth case that this happened.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_526F")

    SetScenarioFlags(0x16F, 6)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_10_4F80 end

    def Function_11_527B(): pass

    label("Function_11_527B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_53E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5349")

    ChrTalk(
        0xFE,
        (
            "When I look at that glowing, pale azure tree,\x01",
            "I get this feeling of extreme anxiety...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, my husband and Derrick\x01",
            "are doing their best. \x01",
            "I too have to support them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53DB")

    label("loc_5349")


    ChrTalk(
        0xFE,
        (
            "And it's not just them. \x01",
            "In the situation, a lot of\x01",
            "people are doing their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't do big things, but\x01",
            "I too have to support them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53DB")

    Jump("loc_61A4")

    label("loc_53E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_54A9")

    ChrTalk(
        0xFE,
        (
            "The independence declaration of invalidity\x01",
            "means that the lawfulness of President\x01",
            "Dieter's government is shaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure the people of Crossbell\x01",
            "City are in chaos right now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61A4")

    label("loc_54A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_567F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CA")

    ChrTalk(
        0xFE,
        (
            "To think that Mr. Arios became\x01",
            "Secretary of Defense...\x01",
            "I still can't believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Bracers have helped this village\x01",
            "greatly, but since independence we haven't\x01",
            "been able to get in contact with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried... I wonder\x01",
            "how they're doing now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_567A")

    label("loc_55CA")


    ChrTalk(
        0xFE,
        (
            "The Bracers have helped this village\x01",
            "greatly, but since independence we haven't\x01",
            "been able to get in contact with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried... I wonder\x01",
            "how they're doing now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_567A")

    Jump("loc_61A4")

    label("loc_567F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5747")

    ChrTalk(
        0xFE,
        (
            "Derrick and the others took the initiative and are\x01",
            "performing patrols of the village's surrounding areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he saw some\x01",
            "unknown monsters too. \x01",
            "I hope he'll be careful...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61A4")

    label("loc_5747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58A5")

    ChrTalk(
        0xFE,
        (
            "Since yesterday evening, my\x01",
            "husband and Derrick have been\x01",
            "discussing various new reforms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it is not a change. Is seems they'll\x01",
            "try to recover the village's energy by\x01",
            "conveying its traditional charms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those two cooperate, I'm sure it\x01",
            "will be good for Armorica. Uh uh, \x01",
            "I have to support them properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_594C")

    label("loc_58A5")


    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll make\x01",
            "some hot cocoa for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those two cooperate, I'm sure it\x01",
            "will be good for Armorica. Uh uh, \x01",
            "I have to support them properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_594C")

    Jump("loc_61A4")

    label("loc_5951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5AE4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A30")

    ChrTalk(
        0xFE,
        (
            "My husband went to\x01",
            "Mr. Harold's place to\x01",
            "discuss about Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't do anything\x01",
            "anymore with just us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goddess, please watch\x01",
            "over Derrick and\x01",
            "Armorica Village...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A70")

    label("loc_5A30")


    ChrTalk(
        0xFE,
        (
            "Goddess, please watch\x01",
            "over Derrick and\x01",
            "Armorica Village...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A70")

    Jump("loc_5ADF")

    label("loc_5A75")


    ChrTalk(
        0xFE,
        (
            "My husband and Derrick\x01",
            "finally reconciled.\x01",
            "I too feel relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone... \x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ADF")

    Jump("loc_61A4")

    label("loc_5AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5C46")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B96")

    ChrTalk(
        0xFE,
        (
            "Lately, Derrick has hardly ever\x01",
            "showed his face at home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm worried. \x01",
            "I wonder if he's gotten involved\x01",
            "in something ridiculous...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C41")

    label("loc_5B96")


    ChrTalk(
        0xFE,
        (
            "To think he's talking about village\x01",
            "reform with that Minneth...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, maybe we've come to a point\x01",
            "where the relationship between\x01",
            "those two can't be recovered.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C41")

    Jump("loc_61A4")

    label("loc_5C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5DCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D47")

    ChrTalk(
        0xFE,
        (
            "The other day's argument between my husband\x01",
            "and Derrick was the worst one I've seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things got hot between them, \x01",
            "and in the end, I couldn't remonstrate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... How can I get those\x01",
            "two to reconcile, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5DC6")

    label("loc_5D47")


    ChrTalk(
        0xFE,
        (
            "*sigh*... How can I get\x01",
            "Derrick and my husband\x01",
            "to reconcile, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't even know what\x01",
            "I should do anymore...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DC6")

    Jump("loc_61A4")

    label("loc_5DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EE0")

    ChrTalk(
        0xFE,
        (
            "The arguments between my my husband and\x01",
            "Derrick grow more intense by the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always manage to end them somehow, \x01",
            "but things are gradually getting out of control...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm worried. \x01",
            "I hope things don't get\x01",
            "any worse than this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5F7B")

    label("loc_5EE0")


    ChrTalk(
        0xFE,
        (
            "The arguments between my my husband and\x01",
            "Derrick grow more intense by the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm worried. \x01",
            "I hope things don't get\x01",
            "any worse than this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F7B")

    Jump("loc_61A4")

    label("loc_5F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_61A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D7")

    ChrTalk(
        0xFE,
        (
            "Lately, there have been violent\x01",
            "arguments about Armorica's future\x01",
            "between Derrick and my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In and of itself, that would be fine,\x01",
            "but neither is willing to back down,\x01",
            "so it always ends up in a quarrel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, our relationship\x01",
            "with our son will only get worse. \x01",
            "*sigh*, my head hurts...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_61A4")

    label("loc_60D7")


    ChrTalk(
        0xFE,
        (
            "I think my husband and son having\x01",
            "arguments for the sake of the\x01",
            "village itself is fine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those two are stubborn and there's\x01",
            "no sign of them reaching an agreement. \x01",
            "*sigh*, my head hurts...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61A4")

    TalkEnd(0xFE)
    Return()

    # Function_11_527B end

    def Function_12_61A8(): pass

    label("Function_12_61A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_63D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61C6")
    Call(0, 13)
    Jump("loc_63D3")

    label("loc_61C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6305")

    ChrTalk(
        0xFE,
        (
            "With the appearance of that huge tree, \x01",
            "it seem the villagers are feeling quite anxious.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although the President was arrested, the\x01",
            "problems of the Azure Flowers and the "Cryptids"\x01",
            "on the highway still aren't solved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems I need to\x01",
            "continue to remind the\x01",
            "villagers to be cautious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_63D3")

    label("loc_6305")


    ChrTalk(
        0xFE,
        (
            "Although the President was arrested, the\x01",
            "problems of the Azure Flowers and the "Cryptids"\x01",
            "on the highway still aren't solved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems I need to\x01",
            "continue to remind the\x01",
            "villagers to be cautious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63D3")

    Jump("loc_6663")

    label("loc_63D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_63E6")
    Jump("loc_6663")

    label("loc_63E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_63F4")
    Jump("loc_6663")

    label("loc_63F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6402")
    Jump("loc_6663")

    label("loc_6402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_641D")
    Call(0, 10)
    Jump("loc_6493")

    label("loc_641D")


    ChrTalk(
        0xFE,
        (
            "...Hm, even what my father\x01",
            "says is quite right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like a good idea to\x01",
            "investigate this plan further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6493")

    Jump("loc_6663")

    label("loc_6498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6663")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64B3")
    Jump("loc_6663")

    label("loc_64B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65CB")

    ChrTalk(
        0xFE,
        (
            "It was a mistake from the start\x01",
            "to attempt to solve the problems\x01",
            "of this village by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This case made me realize my\x01",
            "own judgment is inadequate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going forward, I'll need to think\x01",
            "of this village with my father...\x01",
            "No, with all of the citizens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6663")

    label("loc_65CB")


    ChrTalk(
        0xFE,
        (
            "This case made me realize my\x01",
            "own judgment is inadequate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going forward, I'll need to think of this\x01",
            "village together with all of the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6663")

    TalkEnd(0xFE)
    Return()

    # Function_12_61A8 end

    def Function_13_6667(): pass

    label("Function_13_6667")

    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "No one expected something like\x01",
            "this to happen, did they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As a trade city, forcibly taking\x01",
            "independence will have an influence\x01",
            "throughout the whole continent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And neglecting tradition...\x01",
            "Maybe the rebound of continued too\x01",
            "sudden evolution has now come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...But, is it wrong to be content\x01",
            "with that and accept it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If this is a trial given to us by the\x01",
            "Goddess, can we get through it?\x01",
            "...That's what I want to find out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Hmm, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Goodness. I wonder\x01",
            "if I too should change my\x01",
            "stubborn way of thinking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 4)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_13_6667 end

    def Function_14_68AC(): pass

    label("Function_14_68AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_68BD")
    Jump("loc_69B6")

    label("loc_68BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6975")

    ChrTalk(
        0xFE,
        (
            "The police are investigating the new\x01",
            "orbal truck I bought from Mr. Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They said it wouldn't take\x01",
            "too long, but... *sigh*, I\x01",
            "wonder if it'll be back soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69B6")

    label("loc_6975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6983")
    Jump("loc_69B6")

    label("loc_6983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6991")
    Jump("loc_69B6")

    label("loc_6991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_699F")
    Jump("loc_69B6")

    label("loc_699F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_69AD")
    Jump("loc_69B6")

    label("loc_69AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_69B6")

    label("loc_69B6")

    TalkEnd(0xFE)
    Return()

    # Function_14_68AC end

    def Function_15_69BA(): pass

    label("Function_15_69BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69DF")
    Call(0, 19)
    Return()

    label("loc_69DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_69F0")
    Jump("loc_6F09")

    label("loc_69F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6B89")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A0B")
    Jump("loc_6B84")

    label("loc_6A0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A1D")
    Jump("loc_6B84")

    label("loc_6A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AEF")

    ChrTalk(
        0xF,
        (
            "#03603FThank you very much\x01",
            "for your help.\x02\x03",
            "#03600FThanks to you, Derrick and the\x01",
            "Village Chief were able to reconcile.\x02\x03",
            "#03609FUh uh. I knew it. Consulting\x01",
            "with you was the right choice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6B84")

    label("loc_6AEF")


    ChrTalk(
        0xF,
        (
            "#03603FThanks to you, Derrick and the\x01",
            "Village Chief were able to reconcile.\x02\x03",
            "#03609FUh uh. I knew it. Consulting\x01",
            "with you was the right choice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B84")

    Jump("loc_6F09")

    label("loc_6B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6F09")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CBC")

    ChrTalk(
        0xF,
        (
            "#03603FDerrick and I have met many times\x01",
            "through village business. He is a\x01",
            "polite and diligent young man.\x02\x03",
            "#03608FIf someone like him has gotten involved\x01",
            "in something, I can't let it pass.\x02\x03",
            "#03601FEveryone, please see if you can\x01",
            "find any profitable information.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6D53")

    label("loc_6CBC")


    ChrTalk(
        0xF,
        (
            "#03608FIf Derrick has gotten involved in\x01",
            "something, I can't let it pass.\x02\x03",
            "#03601FEveryone, please see if you can\x01",
            "find any profitable information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D53")

    Jump("loc_6F09")

    label("loc_6D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E77")

    ChrTalk(
        0xF,
        (
            "#03608FI don't know that man, Minneth's true\x01",
            "objective at this time, but...\x02\x03",
            "#03603FBoth I and the Village Chief want to\x01",
            "advance this case carefully.\x02\x03",
            "#03600FEveryone, thank you very\x01",
            "much forinvestigating for us.\x02\x03",
            "I'll be counting on you\x01",
            "if anything else happens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6F09")

    label("loc_6E77")


    ChrTalk(
        0xF,
        (
            "#03603FBoth I and the Village Chief want to\x01",
            "advance this case carefully.\x02\x03",
            "#03600FEveryone, I'll be counting on\x01",
            "you if anything else happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F09")

    TalkEnd(0xFE)
    Return()

    # Function_15_69BA end

    def Function_16_6F0D(): pass

    label("Function_16_6F0D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FD9")

    ChrTalk(
        0xFE,
        (
            "Lawyer Ian is busy\x01",
            "drafting the constitution\x01",
            "and couldn't make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it seems it was successfully\x01",
            "resolved. That's a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will convey the facts\x01",
            "to Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7041")

    label("loc_6FD9")


    ChrTalk(
        0xFE,
        (
            "It seems it was successfully\x01",
            "resolved. That's great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will convey the facts\x01",
            "to Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7041")

    TalkEnd(0xFE)
    Return()

    # Function_16_6F0D end

    def Function_17_7045(): pass

    label("Function_17_7045")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70B9")

    ChrTalk(
        0xFE,
        (
            "...To think Alm who was that\x01",
            "small became such a fine man...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    ChrTalk(
        0xFE,
        "...*sob*...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x12, 0x10)
    SetScenarioFlags(0x1, 1)
    Jump("loc_70CA")

    label("loc_70B9")


    ChrTalk(
        0xFE,
        "...*sob*...\x02",
    )

    CloseMessageWindow()

    label("loc_70CA")

    TalkEnd(0xFE)
    Return()

    # Function_17_7045 end

    def Function_18_70CE(): pass

    label("Function_18_70CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    LoadChrToIndex("chr/ch03102.itc", 0x20)
    LoadChrToIndex("chr/ch02702.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x107, 0x21)
    SetChrSubChip(0x107, 0x0)
    BeginChrThread(0x107, 3, 0, 0)
    SetMapObjFrame(0xFF, "kage03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ha03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika00", 0x0, 0x1)
    SetChrPos(0x101, -38500, 200, -1500, 90)
    SetChrPos(0x103, -38500, 200, -2800, 90)
    SetChrPos(0x105, -34300, 200, -1700, 270)
    SetChrPos(0x107, -38700, 0, 600, 90)
    SetChrPos(0xB, -36300, 200, 100, 180)
    OP_68(-36290, 2500, -2150, 0)
    MoveCamera(327, 15, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Sleep(1000)
    OP_68(-36290, 1500, -2150, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xB,
        (
            "#11P──I see. So that's\x01",
            "what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAt first, I feared for my\x01",
            "life when you showed up\x01",
            "with that noble wolf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PS-Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#5P#3CHmm. It seems I've been\x01",
            "inconsiderate to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PNo, no. It is the greatest of\x01",
            "honors to be able to see a\x01",
            "legendary Divine Wolf like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PThe "State Guard" hardly ever\x01",
            "comes to the village, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PPlease stay as\x01",
            "long as you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5P...Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#6PThat really helps.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PHowever, there're a lot of people in\x01",
            "critical condition at the hospital too...\x02\x03",
            "#10401FEven here President Dieter's reputation\x01",
            "doesn't seem all that great, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PHm... It's probably because his\x01",
            "connection to this village is weak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PI never thought he'd go through with\x01",
            "an "independence declaration"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11POur harvests are down because of the\x01",
            "appearance of those "Cryptids", too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PEven so, the State Guard stops\x01",
            "by on patrol every so often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#6P...How careless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CIt's normal for those in the city to\x01",
            "ignore those living in villages...\x02\x03",
            "#01201FHowever, it seems to\x01",
            "have gone too far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PHm... Honestly, I too feel\x01",
            "we mustn't follow them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAlthough, compared to the influence\x01",
            "on the population of Crossbell City,\x01",
            "it's like there's none in this village...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PHonestly, I'm at a\x01",
            "loss as to what to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10408F#12PHmm, I see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5PWe'll watch out for\x01",
            "those "Cryptids" too.\x02\x03",
            "#00001FAside from that, is there anything\x01",
            "else that's been troubling you lately?\x02\x03",
            "Maintenance of order, destabilization... \x01",
            "Anything like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PNo, thankfully it\x01",
            "hasn't come to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PFor now, the whole village is\x01",
            "cooperating to weather this\x01",
            "disaster as best as we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PHarold's family is\x01",
            "helping us, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5PMr. Harold's...!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 0)), scpexpr(EXPR_END)), "loc_7A17")

    ChrTalk(
        0x103,
        (
            "#00208F#6PThat's right... I remember he\x01",
            "said he was going to vacation\x01",
            "here with his family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A48")

    label("loc_7A17")


    ChrTalk(
        0x103,
        (
            "#00205F#6PHas he come here\x01",
            "with his family?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A48")


    ChrTalk(
        0xB,
        (
            "#11PHm, he had just arrived with his family\x01",
            "when that phenomenon occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAfter that, the highway movement\x01",
            "restrictions went into effect immediately,\x01",
            "and they've been staying here since then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#5PIs that right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PIncidentally, they're staying\x01",
            "on the 2nd floor of the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PYou could pay them a visit, if you like.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PAlright, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400F#12PShall we go visit them, then?\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    EndChrThread(0x107, 0x3)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, -40400, 0, -1800, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A1, 3)
    OP_29(0xAF, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_70CE end

    def Function_19_7C73(): pass

    label("Function_19_7C73")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-37080, 1500, -1060, 0)
    MoveCamera(329, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -38110, 0, 380, 180)
    SetChrPos(0x102, -37060, 0, 1370, 180)
    SetChrPos(0x103, -39710, 0, -190, 135)
    SetChrPos(0x104, -35620, 0, 1220, 180)
    SetChrPos(0x109, -38610, 0, 2220, 180)
    SetChrPos(0x105, -39730, 0, 1380, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8189")

    ChrTalk(
        0xB,
        (
            "*sigh*... That fool of\x01",
            "Derrick, what in the\x01",
            "world is he doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FI'm worried... \x01",
            "It's quite possible that he's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FGood day, Village Chief Tolta. \x01",
            "We're the Special Support Section...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FHuh? ...Mr. Harold?\x02",
    )

    CloseMessageWindow()

    def lambda_7E3F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E3F)
    Sleep(50)

    def lambda_7E4F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E4F)
    Sleep(50)

    def lambda_7E5F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E5F)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "Oh, it's you... \x01",
            "I've been waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FYou saw the request, didn't you.\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FS-Sure...\x02\x03",
            "#00005FBut, why are you\x01",
            "here Mr. Harold?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As a matter of fact,\x01",
            "he too has a connection\x01",
            "to this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FI was speaking with Village Chief Tolta\x01",
            "and we decided to consult with all of you.\x02\x03",
            "#03601FAfter all, the circumstances being what they are.\x01",
            "We thought it was a good idea to enlist the\x01",
            "help of investigation professionals.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00101FThe situation seems\x01",
            "very serious.\x02\x03",
            "#00103FIt seems something\x01",
            "concerning your son...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80E7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80E7)
    Sleep(50)

    def lambda_80F7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_80F7)
    Sleep(50)

    def lambda_8107():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8107)
    Sleep(300)

    ChrTalk(
        0xB,
        "Hm, it's a bit complicated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you'll accept, I'd be happy\x01",
            "to give you the details.\x01",
            "Is now a good time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8207")

    label("loc_8189")

    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        "Oh, have you made time for this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you're taking up the\x01",
            "request, I'll tell you the\x01",
            "details... Is it all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8207")

    Call(0, 20)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -41050, 0, -1950, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_19_7C73 end

    def Function_20_8236(): pass

    label("Function_20_8236")

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
            "[Accept]\x01",            # 0
            "[Not Prepared]\x01",      # 1
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
        (0, "loc_829E"),
        (1, "loc_82A6"),
        (SWITCH_DEFAULT, "loc_8382"),
    )


    label("loc_829E")

    Call(0, 21)
    Jump("loc_8382")

    label("loc_82A6")


    ChrTalk(
        0x101,
        (
            "#00006FWe're terribly sorry, but...\x01",
            "We're a little busy right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm, is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Then, if you have time,\x01",
            "please come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If possible, I would like\x01",
            "help from all of you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x173, 7)
    Jump("loc_8382")

    label("loc_8382")

    Return()

    # Function_20_8236 end

    def Function_21_8383(): pass

    label("Function_21_8383")


    ChrTalk(
        0x101,
        (
            "#00000FYes, it is.\x01",
            "Please, tell us what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Ah, I'm in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "──My son Derrick has been\x01",
            "acting strange lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems like he's planning\x01",
            "something bad in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FBad...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't know the details, but...\x01",
            "I can guess what he's thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Lately he told Harold that\x01",
            "he didn't want to make any\x01",
            "more future transactions.\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FHe doesn't...\x01",
            "Why that all of a sudden?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FI'm positive you're on\x01",
            "good terms with Armorica\x01",
            "Village, Mr. Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03608FYes, I've treated the\x01",
            "people here with\x01",
            "kindness for a long time.\x02\x03",
            "#03601FAnd so, thinking I had made some\x01",
            "mistake, I came here to ast the\x01",
            "Village Chief the reason why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FSeems like the Village Chief\x01",
            "has no idea either,\x01",
            "from the sound of it.\x02\x03",
            "#10300FIsn't that right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Correct... A grave\x01",
            "rudeness has been\x01",
            "done to Harold.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Losing a good customer such as himself\x01",
            "would be a huge blow for the village...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm sure my son too\x01",
            "is aware of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThat's strange...\x02\x03",
            "#00101FI wonder if anything\x01",
            "happened to him...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, I think so too. That's\x01",
            "why I was discussing the\x01",
            "matter with Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And... A certain\x01",
            "suspicious character\x01",
            "came to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems he's been\x01",
            "meeting with a suspicious\x01",
            "foreigner recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FA foreigner...you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FWe don't know\x01",
            "many details, but...\x02\x03",
            "#03601FIt's just, it seems he's\x01",
            "been discussing something\x01",
            "with Mr. Derrick in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm... Secret talks, you say.\x01",
            "That does sound suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And so, I'd like you guys\x01",
            "to investigate that\x01",
            "foreigner in detail for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And, if he's planning some evil scheme,\x01",
            "to put a stop to it immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FExcuse me for asking, but...\x01",
            "Is such an incident really\x01",
            "worth issuing a request for?\x02\x03",
            "#00200FIt would be logical to speak\x01",
            "with your son directly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FWhoa there, peTiote...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Well, it's embarrassing, \x01",
            "but the young lady is right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You see, for a long time now, my\x01",
            "son and I have repeatedly clashed\x01",
            "over how to run this village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I asked him about this matter, in\x01",
            "the end, nothing would be answered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "As his father, it pains me to say this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...I understand. We'll begin \x01",
            "our investigation right away.\x02\x03",
            "#00000FI was thinking of starting with\x01",
            "interviews of the villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yes, please go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, Derrick is with\x01",
            "Elkin right now delivering\x01",
            "produce in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It might be best to save your\x01",
            "interview with him for last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FEveryone, please get some\x01",
            "profitable information for us.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00000FYes, please leave it to us.\x02",
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
            "Quest [Suspect Investigation]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x82, 0x1, 0x0)
    SetScenarioFlags(0x174, 0)
    SetChrSubChip(0xB, 0x0)
    Return()

    # Function_21_8383 end

    def Function_22_8EB1(): pass

    label("Function_22_8EB1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(35510, 1500, -2430, 0)
    MoveCamera(288, 34, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 34950, 0, -2440, 225)
    SetChrPos(0x102, 34150, 0, -1180, 180)
    SetChrPos(0x103, 35670, 0, -3780, 270)
    SetChrPos(0x104, 35390, 0, -1060, 225)
    SetChrPos(0x109, 34780, 0, 40, 180)
    SetChrPos(0x105, 35960, 0, -2370, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0xA, 0x2D, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FExcuse me, I'd like to ask\x01",
            "you a little something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked about the foreigner who has\x01",
            "been visiting the village recently.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        "Oh, him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm... If pushed, I'd say\x01",
            "he's quite a man of character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FOf character... ?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah. One time our kids were\x01",
            "playing and he passed by and\x01",
            "got his clothes dirty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He paid it no mind\x01",
            "and gave them\x01",
            "sweets instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Man, I breathed a sigh\x01",
            "being thankful to him\x01",
            "or in admiration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... Thank you\x01",
            "for your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x174, 3)
    OP_29(0x82, 0x1, 0x3)
    SetChrPos(0x0, 34950, 0, -2440, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_8EB1 end

    def Function_23_91BB(): pass

    label("Function_23_91BB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-37080, 2500, -1060, 0)
    MoveCamera(329, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -38110, 0, 380, 180)
    SetChrPos(0x102, -37060, 0, 1370, 180)
    SetChrPos(0x103, -39710, 0, -190, 135)
    SetChrPos(0x104, -35620, 0, 1220, 180)
    SetChrPos(0x109, -38610, 0, 2220, 180)
    SetChrPos(0x105, -39730, 0, 1380, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x1)
    OP_68(-37080, 1500, -1060, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0xB,
        (
            "I can't believe it...\x01",
            "That Minneth is\x01",
            "Quincy Company staff?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And there's the bit about the\x01",
            ""Armorica Honey Company" too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03605FA factory on your private\x01",
            "property... It seems quite the\x01",
            "large-scale plan is unfolding...\x02\x03",
            "#03608FTo think Derrick could do\x01",
            "something like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm... By the way,\x01",
            "where is Mr. Derrick now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FOh...that's right. \x01",
            "We didn't see him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWe ran into him at the hotel. He said\x01",
            "he was headed back to the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm... Derrick isn't home\x01",
            "all that often these days,\x01",
            "to tell you the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems he's been renting a\x01",
            "room at "Ash Tree" Inn lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Minneth has been visiting\x01",
            "the inn too, it seems. \x01",
            "Maybe he moved for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because of that, I couldn't notice such a thing like\x01",
            "a plan to build a factory on our private property.\x01",
            "...What a pathetic story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F...I wonder about that.\x02\x03",
            "#10300FUnexpectedly, he could've moved due to\x01",
            "a suggestion by that trader so that...\x02\x03",
            "#10304F...Information would be hard\x01",
            "to reach you, Village Chief.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        "W-What do you mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell, I'll let our\x01",
            "leader explain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FHey... Well, fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03605FMr. Lloyd, are you\x01",
            "concerned about\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F──This is just my\x01",
            "speculation but...\x02\x03",
            "#00001FThere're some suspicious\x01",
            "points about Minneth.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        "What...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FThe plan he told us\x01",
            "about benefits all\x01",
            "parties involved.\x02\x03",
            "#00003FArmorica Village would gain a new industry and \x01",
            "Quincy Company would gain a subsidiary to\x01",
            "further their business in the future.\x02\x03",
            "#00008FHis argument seems persuasive\x01",
            "on the surface, but...\x02\x03",
            "#00001FEverything is a little too perfect.\x01",
            "...Don't you think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03605F...!\x01",
            "N-Now that you mention it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FOn top of that,\x01",
            "Mr. Minneth sold a new\x01",
            "orbal truck for cheap.\x02\x03",
            "#00200FI think we can\x01",
            "think of that as a\x01",
            ""prior investment."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FI don't think anyone would\x01",
            "dispute that new orbal\x01",
            "cars are expensive...\x02\x03",
            "#10101FIt's unprecedented to part with\x01",
            "one for a mere 50,000 mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FConversely...\x02\x03",
            "#00301FIt means he's\x01",
            ""certain" to make\x01",
            "that mira back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03601FThat's...\x01",
            "Strange indeed.\x02\x03",
            "#03603FFor a company as large as Quincy,\x01",
            "it shouldn't advance a project\x01",
            "neglecting such a cost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "H-Hm, that might be true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, it's\x01",
            "rather suspicious...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001FMr. Minneth has some other\x01",
            "objective... Possibly one\x01",
            "guaranteed to make him a profit.\x02\x03",
            "#00003FThere's no evidence\x01",
            "though... You should\x01",
            "keep that in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes... I'll be\x01",
            "very careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...That was some\x01",
            "great work, Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks to you, I feel I could \x01",
            "understand the situation well.\x01",
            "Allow me to thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, you don't have to...\x02\x03",
            "#00005FAre you sure you're ok? If not,\x01",
            "we'll continue investigating...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "No... You've done enough for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "From the start, I could never go\x01",
            "along with a plan to build a factory\x01",
            "on our village's private property.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Later, I'll speak with\x01",
            "Derrick as the chief and\x01",
            "try to persuade him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F...That could be for the best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThen, we'll\x01",
            "excuse ourselves.\x02\x03",
            "#00000FPlease contact us again anytime\x01",
            "if something happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Sure, in that case, I'll be\x01",
            "counting on you again.\x02",
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
            "Quest [Suspect Investigation]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x82, 0x1, 0x7)
    OP_29(0x82, 0x1, 0x8)
    OP_29(0x82, 0x4, 0x10)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0x0, -41050, 0, -1950, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_91BB end

    def Function_24_A009(): pass

    label("Function_24_A009")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    OP_68(-46010, 3100, -2510, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xB, -47740, 0, -120, 180)
    SetChrPos(0xF, -48950, 0, -2510, 45)
    SetChrPos(0xD, -46260, 0, 50, 180)
    SetChrPos(0x10, -49140, 0, -3150, 45)
    SetChrPos(0x101, -47540, 0, -1830, 0)
    SetChrPos(0x102, -46230, 0, -1750, 315)
    SetChrPos(0x103, -44810, 0, -1320, 315)
    SetChrPos(0x104, -45630, 0, -3150, 315)
    SetChrPos(0x109, -46960, 0, -3110, 0)
    SetChrPos(0x105, -44330, 0, -2660, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-46010, 1900, -2510, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0xB,
        "Well done, ladies and gentlemen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You all saved this\x01",
            "village from the evil\x01",
            "clutches of that crook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThough in the end,\x01",
            "the criminal fled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FBut we reported the\x01",
            "matter to police HQ...\x02\x03",
            "#00100FIt's only a matter of\x01",
            "time before he's caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#03605FDerrick?\x02",
    )

    CloseMessageWindow()

    def lambda_A295():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A295)
    Sleep(50)

    def lambda_A2A5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A2A5)
    Sleep(50)

    ChrTalk(
        0xD,
        (
            "...I really caused big\x01",
            "trouble to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I got caught up in his\x01",
            "fraud and it led to\x01",
            "such a situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108FDon't say that. It's not your fa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No... \x01",
            "It's completely my fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I was so desperate to improve the village\x01",
            "that I didn't listen to my father... \x01",
            "And you already know the result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm unqualified to be\x01",
            "the next Village Chief.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        "...That's not true.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        "Father...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've been so rigid in my\x01",
            "conservative ways that I didn't\x01",
            "even listen to your proposals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Though I am aware the village\x01",
            "will eventually fail at this rate, \x01",
            "I've done nothing about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I bear a large share of the\x01",
            "responsibility for this incident, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#03608FVillage Chief...\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Through this incident, \x01",
            "I've finally realized that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To protect this village,\x01",
            "we mustn't rely on a single\x01",
            "person's stubborn thoughts.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Derrick... \x01",
            "From now on, I'd like you to\x01",
            "lend me your wisdom too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Each of us will contribute our ideas,\x01",
            "and we'll discuss them with the villagers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is how it must be if we\x01",
            "are to protect this village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Yeah, you're right.\x01",
            "I'm sorry, father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'll think more\x01",
            "about the village\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*... It seems\x01",
            "you were able to\x01",
            "reconcile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHa ha, looks that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell if this is the outcome, \x01",
            "then I guess falling for a fraud\x01",
            "wasn't too bad after all?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_A910():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A910)
    Sleep(50)

    def lambda_A920():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A920)
    Sleep(50)

    def lambda_A930():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A930)
    Sleep(50)

    def lambda_A940():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A940)
    Sleep(50)

    def lambda_A950():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A950)
    Sleep(50)

    def lambda_A960():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A960)
    Sleep(50)

    def lambda_A970():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A970)
    Sleep(50)

    def lambda_A980():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A980)
    Sleep(50)

    def lambda_A990():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A990)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10106FW-Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHm, it is not what you say, but how you say it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FN-No no, that was\x01",
            "definitely out of line.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        "A-Anyway...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "All of you have helped us greatly\x01",
            "I would like to thank all of you\x01",
            "once again.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AA99():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA99)
    Sleep(50)

    def lambda_AAA9():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AAA9)
    Sleep(50)

    def lambda_AAB9():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AAB9)
    Sleep(50)

    def lambda_AAC9():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AAC9)
    Sleep(50)

    def lambda_AAD9():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AAD9)
    Sleep(50)

    def lambda_AAE9():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AAE9)
    Sleep(50)

    def lambda_AAF9():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_AAF9)
    Sleep(50)

    def lambda_AB09():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_AB09)
    Sleep(50)

    def lambda_AB19():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_AB19)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "I must thank Lawyer Ian\x01",
            "once again as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I will convey your message\x01",
            "to Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03604FI too am glad to have been even a little\x01",
            "useful in resolving this incident.\x02\x03",
            "#03600FI look forward to continuing to work\x01",
            "with you in the future, Village Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Ha ha, same here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FJust in case, please be on\x01",
            "the lookout for that crook.\x02\x03",
            "#00000FAnd if you ever need our help again,\x01",
            "don't hesitate to contact us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, I'll be counting on you then.\x01",
            "Thank you so much for all your help.\x02",
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
            "Quest [Suspicious Trader Investigation]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x87, 0x1, 0xA)
    OP_29(0x87, 0x1, 0xB)
    OP_29(0x87, 0x4, 0x10)
    SetChrPos(0xB, -38480, 180, -1780, 90)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xF, -34200, 180, -1530, 270)
    SetChrChipByIndex(0xF, 0x2)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrPos(0xD, -38050, 0, -140, 180)
    SetChrPos(0x10, -34400, 0, -300, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrPos(0x0, -46650, 0, -1460, 135)
    OP_69(0xFF, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_24_A009 end

    def Function_25_AE3B(): pass

    label("Function_25_AE3B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xB, 0x0, 0x0)
    OP_68(-37850, 1500, -940, 0)
    MoveCamera(327, 34, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26120, 0)
    SetChrPos(0x101, -38350, 0, -70, 180)
    SetChrPos(0x102, -39580, 0, -40, 135)
    SetChrPos(0x103, -37610, 0, 1040, 180)
    SetChrPos(0x104, -39030, 0, 1050, 180)
    SetChrPos(0x109, -38350, 0, 1950, 180)
    SetChrPos(0x105, -40330, 0, 1370, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FGood day, Village Chief Tolta.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, the Special Support Section.\x01",
            "How can I help you today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe would like to ask\x01",
            "you something...\x01\x02\x03",
            "#00003FAre you letting someone\x01",
            "stay in your bee yard shed?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Hm, actually I am letting\x01",
            "someone stay there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It was about three or four days\x01",
            "ago. "Please let me stay here\x01",
            "for awhile", he asked suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think his name is...\x01",
            "Mr. Geval.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FI knew it...!\x02\x03",
            "#00106FBut, why a shed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I did ask him where he'd\x01",
            "like to stay, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            ""A place that's as inconspicuous\x01",
            "as possible" was his reply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I didn't ask his circumstances,\x01",
            "but I think he's involved in\x01",
            "something that's quite serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To think he's someone\x01",
            "you're looking for...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Is he a person of interest related\x01",
            "to some incident or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FNo, that is not the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FMr. Lloyd, I think it's\x01",
            "best if we tell the Village\x01",
            "Chief everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah, I think you're right...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that they were searching\x01",
            "for Geval due to Alm and Aerie's request.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "Hmm, I see... So he's\x01",
            "a former congressman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And the congressman who faked being\x01",
            "ill to evade taxes awhile back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now that you mention it, I think I remember\x01",
            "seeing his face in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FThis request isn't directly\x01",
            "related to that incident, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FVillage Chief Tolta, will you let us speak\x01",
            "with Mr. Geval who is in the shed?\x02\x03",
            "#00008FIt seems he doesn't want to see\x01",
            "Mr. Alm and Mrs. Aerie, but even so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Hm, very well then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was on bad terms with my son as\x01",
            "well. In the end, the problem turned\x01",
            "out to be that we didn't talk enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't want anyone else to fall\x01",
            "into the same rut that I did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FVillage Chief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Uh uh, follow me, please.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_AE3B end

    def Function_26_B61A(): pass

    label("Function_26_B61A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(76390, 1500, 1360, 0)
    MoveCamera(315, 32, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0xC)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 75800, 0, 2000, 0)
    SetChrChipByIndex(0xB, 0xB)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x101, 75070, 0, -5420, 0)
    SetChrPos(0x102, 75070, 0, -5420, 0)
    SetChrPos(0x103, 75070, 0, -5420, 0)
    SetChrPos(0x104, 75070, 0, -5420, 0)
    SetChrPos(0x109, 75070, 0, -5420, 0)
    SetChrPos(0x105, 75070, 0, -5420, 0)
    SetChrPos(0xB, 75070, 0, -5420, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(76600, 1500, -270, 3000)
    BeginChrThread(0x101, 3, 0, 27)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 28)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 29)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 30)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 32)
    Sleep(500)
    BeginChrThread(0xB, 3, 0, 33)
    WaitChrThread(0xB, 3)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FYou are Mr. Geval...correct?\x02\x03",
            "#00006F*phew*, we finally found you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#4PHmph... How nice\x01",
            "you're hardworking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PSo my son and his wife are\x01",
            "looking for me, are they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PNo matter what you say,\x01",
            "I'll never meet with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FW-Why are you being so obstinate...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4P...It should be obvious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PMy son... Alm hates\x01",
            "me. There can't be\x01",
            "any doubt about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FHe hates you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301FIf possible, can you\x01",
            "give us the details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4P...When I was a new congressman, I got\x01",
            "involved with various corrupt dealings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PI worked only for status, honor and\x01",
            "mira, and turned my back on my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PThough my wife was dissatisfied,\x01",
            "she focused on raising Alm and\x01",
            "distracted herself with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PThen, as I got more and more carried\x01",
            "away, one day... I did something\x01",
            "one with a child should never do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PWhen my wife was out, I invited\x01",
            "my mistress to my own mansion.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10106FN-No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FYou really deserved it then, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PMy wife found out about it before\x01",
            "long. Finally, my dear wife took\x01",
            "Alm and returned to Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PI'm not sure what happened to them after\x01",
            "that, but... I'm sure both Alm and my wife\x01",
            "have painful memories due to the divorce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PBut of all things, I felt\x01",
            "refreshed after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PThe day after my divorce was\x01",
            "finalized, I invited another\x01",
            "lover to my vast estate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FH-Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI guess it can't be helped\x01",
            "if he hates you, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F...Mr. Randy, \x01",
            "you are too direct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PHmph, it's like that redhead said.\x01",
            "It can't be helped if I'm hated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PAnd... In the end, I was a follower\x01",
            "of former Chairman Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PHowever, because of a trivial\x01",
            "tax evasion charge, I was easily\x01",
            "cast away by the former Chairman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PLife'd probably be easier for me\x01",
            "if I was jailed, but as luck would\x01",
            "have it, I only lost my seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PExposing my son to my shame\x01",
            "at having lost everything... \x01",
            "I don't think I could bear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Mr. Geval...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FSo that's how it is...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00001F...Umm, can I say\x01",
            "one thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4P...What? Even if you\x01",
            "say something now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...It may be true that you've\x01",
            "done some horrible things\x01",
            "to your son and wife.\x02\x03",
            "It may be true that you've\x01",
            "done some underhanded things\x01",
            "as a corrupt politician.\x02\x03",
            "#00000FBut, based on what I just heard, it\x01",
            "sounds like you regret your actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...Right.\x02\x03",
            "#00100FYou've reflected plenty on your mistakes.\x01",
            "I'm sure everyone would see that you've\x01",
            "already been punished enough.\x02\x03",
            "#00108FSaying you won't meet them out of guilt...\x01",
            "That doesn't make much sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4PB-But, I...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAlso...\x02\x03",
            "#00002FIn my judgment, Mr. Alm\x01",
            "doesn't hate you after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4P...Huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FMr. Alm and his wife,\x01",
            "Mrs. Aerie, who gave us\x01",
            "the request to look for you...\x02\x03",
            "#00002FThey have built a loving\x01",
            "family and looked very happy.\x02\x03",
            "He requested just one\x01",
            "thing of us. It was...\x02\x03",
            "#00004F"I want to show father our\x01",
            "child and tell him about\x01",
            "the happy family we've built."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha, that's right.\x02\x03",
            "#10106FIt seems like they love\x01",
            "each other very much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FIf they hated you even a\x01",
            "little, his face wouldn't\x01",
            "have been like that at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHu hu, who knows?\x02\x03",
            "#10304FIf he had my poker face, I think\x01",
            "he'd manage to conceal it, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00211F...Mr. Wazy, please\x01",
            "don't stir things up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell anyway, Mr. Geval.\x01",
            "Your son has grown up\x01",
            "into a fine man.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00004F...That's all we can say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWhat do you want to do?\x01",
            "Wouldn't you like \x01",
            "to see them...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4P............\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0x0, 0x1F4)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    Sleep(2000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        (
            "#4P...If you'd say that much... \x01",
            "I might see them.\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FR-Really?\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x12,
        "#4PHmph, why would I lie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4P...Now how about calling them\x01",
            "over before I change my mind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FR-Right. Then, I'll\x01",
            "do so right away!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 35)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 36)
    Sleep(300)
    OP_68(76460, 1500, -1540, 2000)
    BeginChrThread(0x101, 3, 0, 34)

    def lambda_C854():

        label("loc_C854")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C854")

    QueueWorkItem2(0x102, 1, lambda_C854)
    Sleep(50)

    def lambda_C869():

        label("loc_C869")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C869")

    QueueWorkItem2(0x103, 1, lambda_C869)
    Sleep(50)

    def lambda_C87E():

        label("loc_C87E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C87E")

    QueueWorkItem2(0x104, 1, lambda_C87E)
    Sleep(50)

    def lambda_C893():

        label("loc_C893")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C893")

    QueueWorkItem2(0x109, 1, lambda_C893)
    Sleep(50)

    def lambda_C8A8():

        label("loc_C8A8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C8A8")

    QueueWorkItem2(0x105, 1, lambda_C8A8)
    Sleep(50)

    def lambda_C8BD():

        label("loc_C8BD")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C8BD")

    QueueWorkItem2(0xB, 1, lambda_C8BD)
    WaitChrThread(0x101, 3)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0xB, 0x1)
    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd hurriedly contacted\x01",
            ""The Old Dragon Inn"...\x02\x03",
            "And called Alm and Aerie\x01",
            "to Armorica Village.\x02\x03",
            "Everyone waited outside the shed to let\x01",
            "Geval mentally prepare to meet them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_B61A end

    def Function_27_C9BD(): pass

    label("Function_27_C9BD")


    def lambda_C9C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C9C2)

    def lambda_C9D3():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C9D3)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 75280, 0, 270, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_27_C9BD end

    def Function_28_CA08(): pass

    label("Function_28_CA08")


    def lambda_CA0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CA0D)

    def lambda_CA1E():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CA1E)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 76460, 0, 280, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_28_CA08 end

    def Function_29_CA53(): pass

    label("Function_29_CA53")


    def lambda_CA58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CA58)

    def lambda_CA69():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CA69)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 75260, 0, -920, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_29_CA53 end

    def Function_30_CA9E(): pass

    label("Function_30_CA9E")


    def lambda_CAA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CAA3)

    def lambda_CAB4():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CAB4)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 76470, 0, -920, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_30_CA9E end

    def Function_31_CAE9(): pass

    label("Function_31_CAE9")


    def lambda_CAEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CAEE)

    def lambda_CAFF():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CAFF)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 75210, 0, -2040, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_31_CAE9 end

    def Function_32_CB34(): pass

    label("Function_32_CB34")


    def lambda_CB39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_CB39)

    def lambda_CB4A():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CB4A)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 76180, 0, -2040, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_32_CB34 end

    def Function_33_CB7F(): pass

    label("Function_33_CB7F")


    def lambda_CB84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_CB84)

    def lambda_CB95():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_CB95)
    WaitChrThread(0xB, 1)
    OP_95(0xB, 77380, 0, -2650, 2000, 0x0)
    OP_95(0xB, 77640, 0, -310, 2000, 0x0)
    OP_93(0xB, 0x13B, 0x1F4)
    Return()

    # Function_33_CB7F end

    def Function_34_CBDE(): pass

    label("Function_34_CBDE")


    def lambda_CBE3():
        OP_95(0xFE, 75070, 0, -5420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CBE3)
    Sleep(1000)

    def lambda_CC00():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CC00)
    Return()

    # Function_34_CBDE end

    def Function_35_CC0D(): pass

    label("Function_35_CC0D")

    OP_93(0x103, 0x5A, 0x0)
    OP_9B(0x1, 0x103, 0xB4, 0x1F4, 0x7D0, 0x0)
    Return()

    # Function_35_CC0D end

    def Function_36_CC24(): pass

    label("Function_36_CC24")

    OP_93(0x109, 0x5A, 0x0)
    OP_9B(0x1, 0x109, 0xB4, 0x2EE, 0x7D0, 0x0)
    Return()

    # Function_36_CC24 end

    def Function_37_CC3B(): pass

    label("Function_37_CC3B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(76170, 1500, -1190, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27560, 0)
    LoadChrToIndex("chr/ch46300.itc", 0x1E)
    LoadChrToIndex("chr/ch46200.itc", 0x1F)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0xC)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 75790, 0, 2210, 0)
    SetChrChipByIndex(0x13, 0x1E)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 75070, 0, -5420, 0)
    SetChrChipByIndex(0x14, 0x1F)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 75070, 0, -5420, 0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x13, 3, 0, 38)
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 39)
    OP_68(76070, 1500, 900, 4000)
    SetCameraDistance(24880, 4000)
    OP_6F(0x79)

    ChrTalk(
        0x13,
        "Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Is it you...father?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Ahaha, it's been awhile.\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x12,
        "Y-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I-It's been awhile, Alm.\x01",
            "15 years, in fact...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "And she's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Nice to meet you, father-in-law.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I am Alm's wife, Aerie. \x01",
            "It is very nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "H-Hm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I'm glad my son\x01",
            "found a young lady\x01",
            "as nice as yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Oh, father-in-law...\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x12,
        "Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "...T-That one...\x01",
            "In your arms there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Uh uh, it's our child.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "...Almin, why don't you\x01",
            "say hi to your grandpa?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x14,
        "Baby",
        "*goo goo*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Oh, very nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...Ha, ha ha...\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        (
            "S-Say...Alm. I know I\x01",
            "gave you and your mother\x01",
            "a lot of bad memories.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0x0, 0x1F4)
    Sleep(300)
    OP_63(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13,
        "Huh... What's that now?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "More importantly father,\x01",
            "look at this. Almin's eyes\x01",
            "sparkle like pure Sapphirls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "They're just like\x01",
            "yours Aerie─beautiful\x01",
            "as the clear blue sky.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "Yes, but Alm, the\x01",
            "shape of his ears is\x01",
            "the same as yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Uhuhu... Every time\x01",
            "I see them I want\x01",
            "to eat them up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oh, Aerie... I won't let our\x01",
            "child go as long as I live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Alm... We'll be\x01",
            "happy forever.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x12)
    OP_93(0x12, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x12,
        "...*sob*...\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D206():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D206)
    Sleep(50)

    def lambda_D216():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D216)
    Sleep(300)

    ChrTalk(
        0x13,
        "Oh, father...what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Maybe he's not\x01",
            "feeling well, Alm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "...*sob*...\x01",
            "...I'm fine...I'm really fine...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0x12, 0xFF)
    SetScenarioFlags(0x22, 3)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_CC3B end

    def Function_38_D2C7(): pass

    label("Function_38_D2C7")


    def lambda_D2CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_D2CC)

    def lambda_D2DD():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D2DD)
    WaitChrThread(0x13, 1)
    OP_95(0x13, 74920, 0, 210, 2000, 0x0)
    OP_93(0x13, 0x0, 0x1F4)
    Return()

    # Function_38_D2C7 end

    def Function_39_D312(): pass

    label("Function_39_D312")


    def lambda_D317():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_D317)

    def lambda_D328():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D328)
    WaitChrThread(0x14, 1)
    OP_95(0x14, 76120, 0, 210, 2000, 0x0)
    OP_93(0x14, 0x0, 0x1F4)
    Return()

    # Function_39_D312 end

    SaveToFile()

Try(main)
