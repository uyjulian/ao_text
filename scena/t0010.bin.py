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
        "Function_5_187B",         # 05, 5
        "Function_6_275B",         # 06, 6
        "Function_7_289A",         # 07, 7
        "Function_8_33F8",         # 08, 8
        "Function_9_49AD",         # 09, 9
        "Function_10_4D91",        # 0A, 10
        "Function_11_505B",        # 0B, 11
        "Function_12_5F26",        # 0C, 12
        "Function_13_63D1",        # 0D, 13
        "Function_14_6612",        # 0E, 14
        "Function_15_671C",        # 0F, 15
        "Function_16_6C31",        # 10, 16
        "Function_17_6D6B",        # 11, 17
        "Function_18_6DE9",        # 12, 18
        "Function_19_793D",        # 13, 19
        "Function_20_7ED6",        # 14, 20
        "Function_21_801C",        # 15, 21
        "Function_22_8B67",        # 16, 22
        "Function_23_8E83",        # 17, 23
        "Function_24_9C2B",        # 18, 24
        "Function_25_AA41",        # 19, 25
        "Function_26_B1DB",        # 1A, 26
        "Function_27_C4FA",        # 1B, 27
        "Function_28_C545",        # 1C, 28
        "Function_29_C590",        # 1D, 29
        "Function_30_C5DB",        # 1E, 30
        "Function_31_C626",        # 1F, 31
        "Function_32_C671",        # 20, 32
        "Function_33_C6BC",        # 21, 33
        "Function_34_C71B",        # 22, 34
        "Function_35_C74A",        # 23, 35
        "Function_36_C761",        # 24, 36
        "Function_37_C778",        # 25, 37
        "Function_38_CDCA",        # 26, 38
        "Function_39_CE15",        # 27, 39
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
            "I heard the President\x01",
            "was arrested in\x01",
            "Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that we can move\x01",
            "freely, the bracers will\x01",
            "be here right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The situation being what it\x01",
            "is, we have to combine the\x01",
            "whole strength of Crossbell.\x02",
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
            "freely, the bracers will\x01",
            "be here right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The situation being what it\x01",
            "is, we have to combine the\x01",
            "whole strength of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82C")

    Jump("loc_1877")

    label("loc_831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92F")

    ChrTalk(
        0xFE,
        (
            "Recently, Derrick has\x01",
            "been checking to see that\x01",
            "the villagers are safe.\x02",
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
            "It seems Derrick is\x01",
            "taking this seriously.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9E3")

    label("loc_92F")


    ChrTalk(
        0xFE,
        (
            "Recently, Derrick has\x01",
            "been checking to see that\x01",
            "the villagers are safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just seeing the faces of your\x01",
            "friends can make you feel relieved.\x01",
            "Haha, that's very like Derrick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E3")

    Jump("loc_1877")

    label("loc_9E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEE")

    ChrTalk(
        0xFE,
        (
            "My brother Elkin says\x01",
            "daily "I can't drive"\x01",
            "and sighs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because it's an uneasy\x01",
            "situation and he feels depressed,\x01",
            "he complains and complains...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm thankful we can eat\x01",
            "fresh food daily, even in\x01",
            "a situation like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B78")

    label("loc_AEE")


    ChrTalk(
        0xFE,
        (
            "My brother Elkin says\x01",
            "daily "I can't drive"\x01",
            "and sighs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm thankful we can eat\x01",
            "fresh food daily, even in\x01",
            "a situation like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B78")

    Jump("loc_1877")

    label("loc_B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C2B")

    ChrTalk(
        0xFE,
        (
            "I've seen a strange armored\x01",
            "monster around the Ancient\x01",
            "Battlefield lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it's a monster\x01",
            "a rich person somewhere\x01",
            "was keeping as a pet...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1877")

    label("loc_C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE3")

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
    Jump("loc_D5E")

    label("loc_CE3")


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

    label("loc_D5E")

    Jump("loc_1877")

    label("loc_D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_103C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E77")

    ChrTalk(
        0xFE,
        (
            "The reform Derrick is\x01",
            "advancing in the village...\x01",
            "I don't really get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By introducing orbal tools in\x01",
            "the fields, various things\x01",
            "will get easier, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I like field work. I have\x01",
            "mixed feelings about\x01",
            "working by machine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F0B")

    label("loc_E77")


    ChrTalk(
        0xFE,
        (
            "It would be great if\x01",
            "things got easier due to\x01",
            "village reform, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I like field work. I have\x01",
            "mixed feelings about it\x01",
            "becoming too easy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0B")

    Jump("loc_1037")

    label("loc_F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC5")

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
    Jump("loc_1037")

    label("loc_FC5")


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

    label("loc_1037")

    Jump("loc_1877")

    label("loc_103C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_12A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1154")

    ChrTalk(
        0xFE,
        (
            "If you're looking for\x01",
            "Elkin, he's delivering\x01",
            "our produce to the city.\x02",
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
    Jump("loc_11CD")

    label("loc_1154")


    ChrTalk(
        0xFE,
        (
            "If you're looking for\x01",
            "Elkin, he's delivering\x01",
            "our produce to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think he'll be\x01",
            "back for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CD")

    Jump("loc_12A3")

    label("loc_11D2")


    ChrTalk(
        0xFE,
        (
            "That Elkin. He's been in a good\x01",
            "mood ever since Minneth sold\x01",
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

    label("loc_12A3")

    Jump("loc_1877")

    label("loc_12A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_149E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1428")

    ChrTalk(
        0xFE,
        (
            "For generations, we've selected\x01",
            "best person to be village chief\x01",
            "by majority rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The villagers all acknowledge the\x01",
            "chief's son Derrick as being the\x01",
            "right man to be the next chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Derrick is serious.\x01",
            "There's nothing more to\x01",
            "think about.\x02",
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
    Jump("loc_1499")

    label("loc_1428")


    ChrTalk(
        0xFE,
        (
            "Derrick is serious.\x01",
            "There's nothing more to\x01",
            "think about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing good will come\x01",
            "of worrying by myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1499")

    Jump("loc_1877")

    label("loc_149E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160F")

    ChrTalk(
        0xFE,
        (
            "Elkin's accent is what\x01",
            "they call "Armorica\x01",
            "Accent."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the village, only Old Man Donald and\x01",
            "Elkin speak that way. It's an accent\x01",
            "that's been handed down over generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like "This is what it means to\x01",
            "be a villager." I don't think he has\x01",
            "to force himself to correct it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Men worry about the\x01",
            "silliest things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16BA")

    label("loc_160F")


    ChrTalk(
        0xFE,
        (
            "Elkin's Armorica accent has been\x01",
            "passed down for generations. In\x01",
            "a way, it's a valuable thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't hate it. I don't\x01",
            "think he has to force\x01",
            "himself to fix it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BA")

    Jump("loc_1877")

    label("loc_16BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DA")

    ChrTalk(
        0xFE,
        (
            "It's been really peaceful lately.\x01",
            "There's been rainy days too, so\x01",
            "the crops are growing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the weather's like\x01",
            "it is today, I feel like\x01",
            "basking in the sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I'll distribute straw\x01",
            "on the orbal truck and then\x01",
            "take an afternoon nap.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1877")

    label("loc_17DA")


    ChrTalk(
        0xFE,
        (
            "When the weather's like\x01",
            "it is today, I feel like\x01",
            "basking in the sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I'll distribute straw\x01",
            "on the orbal truck and then\x01",
            "take an afternoon nap.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1877")

    TalkEnd(0xFE)
    Return()

    # Function_4_693 end

    def Function_5_187B(): pass

    label("Function_5_187B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_190C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1899")
    Call(0, 6)
    Jump("loc_1907")

    label("loc_1899")


    ChrTalk(
        0xFE,
        (
            "*sigh*, it's as Ange\x01",
            "says, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Us farmers have to work\x01",
            "to preserve the\x01",
            "village's food supply.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1907")

    Jump("loc_2757")

    label("loc_190C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A41")

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
    Jump("loc_1B06")

    label("loc_1A41")


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
            "I hope this invalidity\x01",
            "declaration is connected to the\x01",
            "resumption of our business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B06")

    Jump("loc_2757")

    label("loc_1B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1CBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C41")

    ChrTalk(
        0xFE,
        (
            "A Cryptid monster laid\x01",
            "waste to our fields\x01",
            "along the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Add the movement restrictions on top of\x01",
            "that and our harvest's looking quite\x01",
            "poor. Honestly, our business is doomed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, we can at least feed our\x01",
            "village. I've got to give\x01",
            "thanks to the Goddess for that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CB8")

    label("loc_1C41")


    ChrTalk(
        0xFE,
        (
            "We can at least feed our\x01",
            "village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's just, how long will\x01",
            "this situation go on? ...I\x01",
            "honestly have no idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB8")

    Jump("loc_2757")

    label("loc_1CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D86")

    ChrTalk(
        0xFE,
        (
            "I'm surprised the city\x01",
            "was attacked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And what's more, it\x01",
            "seems the attackers\x01",
            "haven't been captured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but be\x01",
            "worried that they'll\x01",
            "come to Armorica.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DF8")

    label("loc_1D86")


    ChrTalk(
        0xFE,
        (
            "I've been anxious ever\x01",
            "since the attack on the\x01",
            "city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I can't give\x01",
            "field work everything I\x01",
            "have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF8")

    Jump("loc_2757")

    label("loc_1DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB7")

    ChrTalk(
        0xFE,
        (
            "Camille and the others have\x01",
            "a Sunday School lesson at\x01",
            "the bar-inn today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're learning about\x01",
            "stuff other than farming.\x01",
            "I want them to study hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F18")

    label("loc_1EB7")


    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll\x01",
            "take a day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a while since\x01",
            "I took it easy at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F18")

    Jump("loc_2757")

    label("loc_1F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_216F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD9")

    ChrTalk(
        0xFE,
        (
            "Minneth is planning on building\x01",
            "something at our private\x01",
            "property on the old path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That place is our tool\x01",
            "storehouse... I guess\x01",
            "we'll have to move it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_216A")

    label("loc_1FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BD")

    ChrTalk(
        0xFE,
        (
            "So that Minneth turned\x01",
            "out to be a bad guy,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too was completely\x01",
            "deceived by his smile\x01",
            "and attitude.\x02",
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
    Jump("loc_216A")

    label("loc_20BD")


    ChrTalk(
        0xFE,
        (
            "He must have been a really bad guy\x01",
            "if he tricked Derrick, who was\x01",
            "only trying to help our village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The next time I see that\x01",
            "Minneth, I'm going to\x01",
            "let him have it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_216A")

    Jump("loc_2757")

    label("loc_216F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2216")

    ChrTalk(
        0xFE,
        (
            "The foreigner that's been\x01",
            "coming to the village recently\x01",
            "is quite the cheerful fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He always smiles, and I\x01",
            "makes me feel at ease,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2757")

    label("loc_2216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_23F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230F")

    ChrTalk(
        0xFE,
        (
            "Elkin consulted me about\x01",
            "the truck, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's probably near the end of it's\x01",
            "lifespan. Even if maintained,\x01",
            "it'll probably break soon.\x02",
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
    Jump("loc_23F1")

    label("loc_230F")


    ChrTalk(
        0xFE,
        (
            "The village's orbal truck\x01",
            "is probably near the end\x01",
            "of it's lifespan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The village doesn't have the mira for a new one,\x01",
            "so it'll be hard to break this to the chief. It\x01",
            "won't be good if we don't get a replacement soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F1")

    Jump("loc_2757")

    label("loc_23F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24EC")

    ChrTalk(
        0xFE,
        (
            "There are orbal tools\x01",
            "for farming in this\x01",
            "world.\x02",
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
            "Well, those in Armorica\x01",
            "are worn-out and old\x01",
            "fashioned.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25BC")

    label("loc_24EC")


    ChrTalk(
        0xFE,
        (
            "Orbal plows and tractors... In\x01",
            "the era, these orbal tools are\x01",
            "indispensable for farming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if it's greed, but I want\x01",
            "the more useful latest model, but...\x01",
            "Well, in the end, it's a luxury.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25BC")

    Jump("loc_2757")

    label("loc_25C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2757")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B6")

    ChrTalk(
        0xFE,
        (
            "We produce various\x01",
            "vegetables in the fields\x01",
            "of this village.\x02",
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
            "And we delight when they\x01",
            "are shipped from\x01",
            "Armorica and eaten.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2757")

    label("loc_26B6")


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
            "Imports have risen lately,\x01",
            "but our vegetables won't\x01",
            "lose to their tastiness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2757")

    TalkEnd(0xFE)
    Return()

    # Function_5_187B end

    def Function_6_275B(): pass

    label("Function_6_275B")

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
            "*sigh*, what kind of\x01",
            "miserable thing are you\x01",
            "saying now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's precisely because of times\x01",
            "like these that we have to work\x01",
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

    # Function_6_275B end

    def Function_7_289A(): pass

    label("Function_7_289A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B8")
    Call(0, 6)
    Jump("loc_294B")

    label("loc_28B8")


    ChrTalk(
        0xFE,
        (
            "That man is rather timid,\x01",
            "so I have to encourage\x01",
            "him from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in times like these\x01",
            "that hard work is\x01",
            "especially important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294B")

    Jump("loc_33F4")

    label("loc_2950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2A9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F4")

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
            "Harold is always helping\x01",
            "us, so I think I'll\x01",
            "treat him today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A96")

    label("loc_29F4")


    ChrTalk(
        0xFE,
        (
            "Harold is always helping\x01",
            "us, so I think I'll\x01",
            "treat him today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I wonder if Colin, who\x01",
            "eats Sophia's cooking every day,\x01",
            "will be displeased with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A96")

    Jump("loc_33F4")

    label("loc_2A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2BEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7B")

    ChrTalk(
        0xFE,
        (
            "Harold's wife is really\x01",
            "good at cooking, you\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand she opened\x01",
            "a cooking class in her\x01",
            "home in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the situation were\x01",
            "different, I would have\x01",
            "liked to try going.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BEA")

    label("loc_2B7B")


    ChrTalk(
        0xFE,
        (
            "Harold's wife is really\x01",
            "good at cooking, you\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They are close in age,\x01",
            "and easily became\x01",
            "friends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BEA")

    Jump("loc_33F4")

    label("loc_2BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEC")

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
            "...Enough of that. If all\x01",
            "I talk about is that,\x01",
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
    Jump("loc_2D9F")

    label("loc_2CEC")


    ChrTalk(
        0xFE,
        (
            "Whenever I hear about\x01",
            "the attack, it always\x01",
            "ruins my mood.\x02",
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

    label("loc_2D9F")

    Jump("loc_33F4")

    label("loc_2DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EA4")

    ChrTalk(
        0xFE,
        (
            "It seems the chief and\x01",
            "Derrick made up through\x01",
            "yesterday's incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those two put the needs\x01",
            "of the village above all\x01",
            "else.\x02",
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
    Jump("loc_2F1F")

    label("loc_2EA4")


    ChrTalk(
        0xFE,
        (
            "The chief and Derrick\x01",
            "put the needs of the\x01",
            "village above all else.\x02",
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

    label("loc_2F1F")

    Jump("loc_33F4")

    label("loc_2F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_301F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA6")

    ChrTalk(
        0xFE,
        (
            "But even so, to think\x01",
            "reform could happen this\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It must be due to\x01",
            "Minneth's ability.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301A")

    label("loc_2FA6")


    ChrTalk(
        0xFE,
        (
            "I never expected that\x01",
            "Minneth would release\x01",
            "monsters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, thank goodness\x01",
            "our children weren't\x01",
            "hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301A")

    Jump("loc_33F4")

    label("loc_301F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_305A")

    ChrTalk(
        0xFE,
        (
            "Now then, what to make\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30CC")

    label("loc_305A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306C")
    Call(0, 22)
    Jump("loc_30CC")

    label("loc_306C")


    ChrTalk(
        0xFE,
        (
            "Wow, that guy's quite\x01",
            "capable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was nice to our kids.\x01",
            "I don't think he's a bad\x01",
            "guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30CC")

    Jump("loc_33F4")

    label("loc_30D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_328E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B8")

    ChrTalk(
        0xFE,
        (
            "In the fields, we\x01",
            "sometimes get oddly-shaped\x01",
            "fruits or vegetables...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't sell those, so\x01",
            "we share them within the\x01",
            "village.\x02",
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
    Jump("loc_3289")

    label("loc_31B8")


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

    label("loc_3289")

    Jump("loc_33F4")

    label("loc_328E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_329C")
    Jump("loc_33F4")

    label("loc_329C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_33F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_336D")

    ChrTalk(
        0xFE,
        (
            "Aretha officially moved\x01",
            "here recently.\x02",
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
    Jump("loc_33F4")

    label("loc_336D")


    ChrTalk(
        0xFE,
        (
            "Stefan often plays with\x01",
            "our kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't have many children in\x01",
            "this village. Thank goodness\x01",
            "they could make a good friend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F4")

    TalkEnd(0xFE)
    Return()

    # Function_7_289A end

    def Function_8_33F8(): pass

    label("Function_8_33F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3425")
    Call(0, 25)
    Return()

    label("loc_3425")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_344A")
    Call(0, 19)
    Return()

    label("loc_344A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3645")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3468")
    Call(0, 13)
    Jump("loc_3640")

    label("loc_3468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3595")

    ChrTalk(
        0xFE,
        (
            "Harold returned to the\x01",
            "city earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I discussed with Derrick how\x01",
            "the village is going to deal\x01",
            "with this going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish Harold had stayed\x01",
            "a while longer, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he wanted to visit various\x01",
            "places, doing what he can. ...I\x01",
            "suppose it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3640")

    label("loc_3595")


    ChrTalk(
        0xFE,
        (
            "...We'll be able to deal with\x01",
            "this, but I wish Harold had\x01",
            "remained for a while longer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, the bracers\x01",
            "are coming, and we've\x01",
            "got to do our best, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3640")

    Jump("loc_49A9")

    label("loc_3645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_37F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3753")

    ChrTalk(
        0xFE,
        (
            "There was the independence\x01",
            "invalidity declaration, and\x01",
            "Derrick is working hard too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This situation... I've served\x01",
            "a long time as chief, yet I\x01",
            "don't know what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, it's important\x01",
            "for each of us to do\x01",
            "what we can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37ED")

    label("loc_3753")


    ChrTalk(
        0xFE,
        (
            "This situation... I've served\x01",
            "a long time as chief, yet I\x01",
            "don't know what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, it's important\x01",
            "for each of us to do\x01",
            "what we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37ED")

    Jump("loc_49A9")

    label("loc_37F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_399D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38FF")

    ChrTalk(
        0xFE,
        (
            "Hmm, I can't believe\x01",
            "those people were at the\x01",
            "Ancient Battlefield...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though they are opponents who don't let\x01",
            "down their guard, they show no sign of\x01",
            "aggression towards the village.\x02",
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
    Jump("loc_3998")

    label("loc_38FF")


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

    label("loc_3998")

    Jump("loc_49A9")

    label("loc_399D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3B99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AFF")

    ChrTalk(
        0xFE,
        (
            "To be perfectly honest, I\x01",
            "feel President Dieter\x01",
            "isn't one to be followed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, compared to the\x01",
            "influence of Crossbell City,\x01",
            "this village is like nothing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Anyway, Harold's\x01",
            "family is cooperating\x01",
            "with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no choice other than for\x01",
            "us villagers to cooperate and\x01",
            "get through these difficulties.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B94")

    label("loc_3AFF")


    ChrTalk(
        0xFE,
        (
            "Harold's family is\x01",
            "cooperating with us too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no choice other than for\x01",
            "us villagers to cooperate and\x01",
            "get through these difficulties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B94")

    Jump("loc_49A9")

    label("loc_3B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F22")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C90")

    ChrTalk(
        0xFE,
        (
            "Haha. It's a difficult time\x01",
            "in many ways, but... Thanks\x01",
            "to that, my heart is warmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, please leave\x01",
            "Geval to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll look after him properly\x01",
            "until he calms down and\x01",
            "returns to the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CFE")

    label("loc_3C90")


    ChrTalk(
        0xFE,
        (
            "Please leave Geval to\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll look after him properly\x01",
            "until he calms down and\x01",
            "returns to the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFE")

    Jump("loc_3F1D")

    label("loc_3D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E4F")

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
    Jump("loc_3F1D")

    label("loc_3E4F")


    ChrTalk(
        0xFE,
        (
            "I asked our village's young\x01",
            "men, Derrick included, to\x01",
            "guard the surrounding areas.\x02",
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

    label("loc_3F1D")

    Jump("loc_49A9")

    label("loc_3F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3D")
    Call(0, 10)
    Jump("loc_3FC8")

    label("loc_3F3D")


    ChrTalk(
        0xFE,
        (
            "Hmm. The villagers are\x01",
            "understanding so it\x01",
            "wasn't too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are interested,\x01",
            "migration to the village\x01",
            "may have increased...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC8")

    Jump("loc_49A9")

    label("loc_3FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4198")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE8")
    Jump("loc_4193")

    label("loc_3FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FF7")
    Jump("loc_4193")

    label("loc_3FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4009")
    Jump("loc_4193")

    label("loc_4009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40FC")

    ChrTalk(
        0xFE,
        (
            "To protect this village\x01",
            "called Armorica...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our objectives were the\x01",
            "same, but my son's views and\x01",
            "my own were both too narrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This case must have been a trial\x01",
            "given to us by the Goddess to\x01",
            "make us realize that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4193")

    label("loc_40FC")


    ChrTalk(
        0xFE,
        (
            "To protect this village called\x01",
            "Armorica... It's a feeling my\x01",
            "son and I both share.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, I must\x01",
            "listen to the words of\x01",
            "the young man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4193")

    Jump("loc_49A9")

    label("loc_4198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_449C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B3")
    Jump("loc_4497")

    label("loc_41B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C2")
    Jump("loc_4497")

    label("loc_41C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42CE")

    ChrTalk(
        0xFE,
        (
            "Derrick's secret discussions with\x01",
            "the foreigner... It suspicious,\x01",
            "no matter how you look at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they're cooking up some\x01",
            "sort of evil plan, it must\x01",
            "be dealt with immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please everyone, collect\x01",
            "information for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4389")

    label("loc_42CE")


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
        (
            "Please everyone, collect\x01",
            "information for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4389")

    Jump("loc_4497")

    label("loc_438E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443F")

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
    Jump("loc_4497")

    label("loc_443F")


    ChrTalk(
        0xFE,
        (
            "As the chief and a parent...\x01",
            "I've got to persuade Derrick\x01",
            "before he moves forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4497")

    Jump("loc_49A9")

    label("loc_449C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_46D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44B7")
    Call(0, 9)
    Jump("loc_46D2")

    label("loc_44B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_462D")

    ChrTalk(
        0xFE,
        (
            "Lack of manpower because the young ones go away,\x01",
            "decline of the state's food self-sufficiency\x01",
            "following the increase in foreign trade...\x02",
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
            "The chief has a duty to protect the\x01",
            "village's traditions as well. I\x01",
            "want him to understand that, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46D2")

    label("loc_462D")


    ChrTalk(
        0xFE,
        (
            "The chief has a duty to protect\x01",
            "the village's traditions as well.\x01",
            "Change isn't only a good thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the next chief, I\x01",
            "want him to understand\x01",
            "that, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46D2")

    Jump("loc_49A9")

    label("loc_46D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_48DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F2")
    Call(0, 9)
    Jump("loc_48D8")

    label("loc_46F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4824")

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
            "Because of his reform proposals,\x01",
            "I know Derrick only wants the\x01",
            "best for the village, but...\x02",
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
    Jump("loc_48D8")

    label("loc_4824")


    ChrTalk(
        0xFE,
        (
            "...Even I don't think\x01",
            "the current situation in\x01",
            "the village is good.\x02",
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

    label("loc_48D8")

    Jump("loc_49A9")

    label("loc_48DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_49A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F8")
    Call(0, 9)
    Jump("loc_49A9")

    label("loc_48F8")


    ChrTalk(
        0xFE,
        (
            "...These troubles are\x01",
            "something I should be solving\x01",
            "myself in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If something happens, I'll\x01",
            "probably count on you, but...\x01",
            "For now, don't worry about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A9")

    TalkEnd(0xFE)
    Return()

    # Function_8_33F8 end

    def Function_9_49AD(): pass

    label("Function_9_49AD")


    ChrTalk(
        0xB,
        (
            "Oh, you're the Special\x01",
            "Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FChief Tolta, it's been a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. I'd heard you'd resumed\x01",
            "activities, but most importantly\x01",
            "you're all in good health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FUmm... You look tired\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No... Recently, I've\x01",
            "been worried about a\x01",
            "little personal problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, it's not on the level\x01",
            "of something you should\x01",
            "trouble yourselves with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FDon't say that. If you're\x01",
            "worried about something,\x01",
            "why not tell us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah. It's bad for your\x01",
            "health keeping that stuff\x01",
            "bottled up inside, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe. The Special\x01",
            "Support Section may be\x01",
            "able to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. It's really no big\x01",
            "deal.\x02",
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
        "#00003FI see... Understood.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D2C")

    ChrTalk(
        0x103,
        (
            "#00200FPlease contact us if you\x01",
            "ever need anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D69")

    label("loc_4D2C")


    ChrTalk(
        0x102,
        (
            "#00100FPlease contact us if you\x01",
            "ever need anything, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D69")


    ChrTalk(
        0xB,
        (
            "Sure. I'll be counting\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 1)
    Return()

    # Function_9_49AD end

    def Function_10_4D91(): pass

    label("Function_10_4D91")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "Derrick, about your\x01",
            ""Beekeeping Experience\x01",
            "Event" idea...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It has appeal to be sure, but\x01",
            "is it really all right to let\x01",
            "amateurs into our fields?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I understand that, but... Honey\x01",
            "is our village's specialty. I\x01",
            "don't think it's too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I was thinking we could\x01",
            "show them how to deal\x01",
            "with bees...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm. I could consider\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4FB0")

    ChrTalk(
        0x101,
        (
            "#00002F(It looks like the Chief\x01",
            "and Derrick reconciled\x01",
            "completely.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F("What doesn't kill you makes\x01",
            "you stronger", they say, right?\x01",
            "Let's not interrupt them.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504F")

    label("loc_4FB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_504F")

    ChrTalk(
        0x101,
        (
            "#00005F(Huh? The Chief and\x01",
            "Derrick... It looks like they\x01",
            "made up just like that.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F(Maybe this happened\x01",
            "through the Minneth\x01",
            "case.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_504F")

    SetScenarioFlags(0x16F, 6)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_10_4D91 end

    def Function_11_505B(): pass

    label("Function_11_505B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5123")

    ChrTalk(
        0xFE,
        (
            "When I look at that glowing,\x01",
            "pale blue tree, I get this\x01",
            "feeling of extreme anxiety...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, my husband and Derrick\x01",
            "are doing their best. I\x01",
            "have to support them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_51B4")

    label("loc_5123")


    ChrTalk(
        0xFE,
        (
            "And it's not just them. In\x01",
            "the situation, a lot of\x01",
            "people are doing their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't do big things,\x01",
            "but I too have to\x01",
            "support them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B4")

    Jump("loc_5F22")

    label("loc_51B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_527F")

    ChrTalk(
        0xFE,
        (
            "The independence invalidity declaration\x01",
            "means that the lawfulness of President\x01",
            "Dieter's government is shaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure the people of\x01",
            "Crossbell City are in\x01",
            "chaos right now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F22")

    label("loc_527F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5451")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539C")

    ChrTalk(
        0xFE,
        (
            "To think that Arios became\x01",
            "Secretary of Defense... I\x01",
            "still can't believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bracers have helped this village\x01",
            "greatly, but we haven't been able to get in\x01",
            "contact with them since the independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried... I wonder\x01",
            "how they're doing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_544C")

    label("loc_539C")


    ChrTalk(
        0xFE,
        (
            "The bracers have helped this village\x01",
            "greatly, but we haven't been able to get in\x01",
            "contact with them since the independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried... I wonder\x01",
            "how they're doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_544C")

    Jump("loc_5F22")

    label("loc_5451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5501")

    ChrTalk(
        0xFE,
        (
            "Derrick took the initiative and\x01",
            "is performing patrols of the\x01",
            "village's surrounding areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he saw an\x01",
            "unknown monster. I hope\x01",
            "he'll be careful...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F22")

    label("loc_5501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5667")

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
            "conveying the village's traditional charms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those two cooperate, I'm sure it\x01",
            "will be good for Armorica. Haha, I\x01",
            "have to support them properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_570C")

    label("loc_5667")


    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll\x01",
            "make some hot cocoa for\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those two cooperate, I'm sure it\x01",
            "will be good for Armorica. Haha, I\x01",
            "have to support them properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_570C")

    Jump("loc_5F22")

    label("loc_5711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_587D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5824")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57DF")

    ChrTalk(
        0xFE,
        (
            "My husband went to\x01",
            "Harold's place to\x01",
            "discuss Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With just us, we can't\x01",
            "do anything...\x02",
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
    Jump("loc_581F")

    label("loc_57DF")


    ChrTalk(
        0xFE,
        (
            "Goddess, please watch\x01",
            "over Derrick and\x01",
            "Armorica Village...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_581F")

    Jump("loc_5878")

    label("loc_5824")


    ChrTalk(
        0xFE,
        (
            "My husband and Derrick\x01",
            "finally reconciled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone... Thank you so\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5878")

    Jump("loc_5F22")

    label("loc_587D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59D0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_592A")

    ChrTalk(
        0xFE,
        (
            "Lately, Derrick has\x01",
            "hardly ever showed his\x01",
            "face at home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, I'm worried. I wonder\x01",
            "if he's gotten involved in\x01",
            "something ridiculous...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59CB")

    label("loc_592A")


    ChrTalk(
        0xFE,
        (
            "To think he's talking\x01",
            "about village reform\x01",
            "with that Minneth...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, we've come to a place\x01",
            "where the relationship between\x01",
            "those two can't be recovered.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59CB")

    Jump("loc_5F22")

    label("loc_59D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ACD")

    ChrTalk(
        0xFE,
        (
            "The argument between my\x01",
            "husband and Derrick was\x01",
            "the worst one I've seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things got hot between them,\x01",
            "and in the end I couldn't\x01",
            "get them to back down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... How can I get\x01",
            "those two to reconcile,\x01",
            "I wonder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5B4C")

    label("loc_5ACD")


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
            "I don't even know what I\x01",
            "should do anymore...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B4C")

    Jump("loc_5F22")

    label("loc_5B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C63")

    ChrTalk(
        0xFE,
        (
            "The arguments between my my\x01",
            "husband and Derrick grow\x01",
            "more intense by the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always manage to end them\x01",
            "somehow, but things are gradually\x01",
            "getting out of control...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm worried. I\x01",
            "hope things don't get\x01",
            "any worse than this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5CFD")

    label("loc_5C63")


    ChrTalk(
        0xFE,
        (
            "The arguments between my my\x01",
            "husband and Derrick grow\x01",
            "more intense by the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm worried. I\x01",
            "hope things don't get\x01",
            "any worse than this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CFD")

    Jump("loc_5F22")

    label("loc_5D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5F22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E56")

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
            "At this rate, my relationship\x01",
            "with my son will only get\x01",
            "worse. *sigh*, my head hurts...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5F22")

    label("loc_5E56")


    ChrTalk(
        0xFE,
        (
            "I think my son and husband having\x01",
            "arguments for the sake of the\x01",
            "village itself is fine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those two are stubborn and there's\x01",
            "no sign of them reaching an\x01",
            "agreement. *sigh*, my head hurts...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F22")

    TalkEnd(0xFE)
    Return()

    # Function_11_505B end

    def Function_12_5F26(): pass

    label("Function_12_5F26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_614F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F44")
    Call(0, 13)
    Jump("loc_614A")

    label("loc_5F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_607F")

    ChrTalk(
        0xFE,
        (
            "With the appearance of that huge\x01",
            "tree, it seems the villagers are\x01",
            "feeling quite anxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although the President was arrested, the\x01",
            "problems of the blue flowers and the Cryptids\x01",
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
    Jump("loc_614A")

    label("loc_607F")


    ChrTalk(
        0xFE,
        (
            "Although the President was arrested, the\x01",
            "problems of the blue flowers and the Cryptids\x01",
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

    label("loc_614A")

    Jump("loc_63CD")

    label("loc_614F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_615D")
    Jump("loc_63CD")

    label("loc_615D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_616B")
    Jump("loc_63CD")

    label("loc_616B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6179")
    Jump("loc_63CD")

    label("loc_6179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6208")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6194")
    Call(0, 10)
    Jump("loc_6203")

    label("loc_6194")


    ChrTalk(
        0xFE,
        (
            "...Yes. What my father\x01",
            "says most of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like a good\x01",
            "idea to investigate this\x01",
            "plan further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6203")

    Jump("loc_63CD")

    label("loc_6208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_63CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6223")
    Jump("loc_63CD")

    label("loc_6223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6335")

    ChrTalk(
        0xFE,
        (
            "It was a mistake from the start\x01",
            "to attempt to solve the problems\x01",
            "of this village myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This case made me\x01",
            "realize my own judgment\x01",
            "is inadequate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going forward, I'll need to think\x01",
            "of this village with my dad...\x01",
            "no, with all of the citizens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_63CD")

    label("loc_6335")


    ChrTalk(
        0xFE,
        (
            "This case made me\x01",
            "realize my own judgment\x01",
            "is inadequate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going forward, I'll need to\x01",
            "think of this village together\x01",
            "with all of the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63CD")

    TalkEnd(0xFE)
    Return()

    # Function_12_5F26 end

    def Function_13_63D1(): pass

    label("Function_13_63D1")

    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "No one expected anything\x01",
            "like this to happen, did\x01",
            "they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As a trade city, forcibly taking\x01",
            "independence will have an influence\x01",
            "throughout the entire continent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And neglecting tradition... Perhaps\x01",
            "this is the price we are paying for\x01",
            "our continued rapid progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...But, you're not\x01",
            "content as things stand,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If this is a trial given to us by\x01",
            "the Goddess, can we get through it?\x01",
            "...That's what I want to find out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Hmm, so that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Goodness. I wonder if you\x01",
            "can't change your\x01",
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

    # Function_13_63D1 end

    def Function_14_6612(): pass

    label("Function_14_6612")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6623")
    Jump("loc_6718")

    label("loc_6623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_66D7")

    ChrTalk(
        0xFE,
        (
            "The police are investigating\x01",
            "the new orbal truck I bought\x01",
            "from Minneth.\x02",
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
    Jump("loc_6718")

    label("loc_66D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_66E5")
    Jump("loc_6718")

    label("loc_66E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_66F3")
    Jump("loc_6718")

    label("loc_66F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6701")
    Jump("loc_6718")

    label("loc_6701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_670F")
    Jump("loc_6718")

    label("loc_670F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6718")

    label("loc_6718")

    TalkEnd(0xFE)
    Return()

    # Function_14_6612 end

    def Function_15_671C(): pass

    label("Function_15_671C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6741")
    Call(0, 19)
    Return()

    label("loc_6741")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6752")
    Jump("loc_6C2D")

    label("loc_6752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_68D9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_676D")
    Jump("loc_68D4")

    label("loc_676D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_677F")
    Jump("loc_68D4")

    label("loc_677F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6848")

    ChrTalk(
        0xF,
        (
            "#03603FThank you very much for\x01",
            "your help.\x02\x03",
            "#03600FThanks to you, Derrick\x01",
            "and the chief were able\x01",
            "to reconcile.\x02\x03",
            "#03609FHaha. I knew it.\x01",
            "Consulting with you was\x01",
            "the right choice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_68D4")

    label("loc_6848")


    ChrTalk(
        0xF,
        (
            "#03603FThanks to you, Derrick\x01",
            "and the chief were able\x01",
            "to reconcile.\x02\x03",
            "#03609FHaha. I knew it.\x01",
            "Consulting with you was\x01",
            "the right choice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D4")

    Jump("loc_6C2D")

    label("loc_68D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6C2D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A09")

    ChrTalk(
        0xF,
        (
            "#03603FDerrick and I have met many times\x01",
            "through village business. He is a\x01",
            "polite and diligent young man.\x02\x03",
            "#03608FIf someone like that has gotten\x01",
            "involved is something, I can't\x01",
            "let it pass.\x02\x03",
            "#03601FEveryone, please see if you can\x01",
            "find any information on him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6A9C")

    label("loc_6A09")


    ChrTalk(
        0xF,
        (
            "#03608FIf Derrick has gotten\x01",
            "involved in something, I\x01",
            "can't let it pass.\x02\x03",
            "#03601FEveryone, please see if\x01",
            "you can find any\x01",
            "information on him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A9C")

    Jump("loc_6C2D")

    label("loc_6AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BA3")

    ChrTalk(
        0xF,
        (
            "#03608FI don't know Minneth's\x01",
            "true objective at this\x01",
            "time, but...\x02\x03",
            "#03603FBoth I and the mayor\x01",
            "want to advance this\x01",
            "case carefully.\x02\x03",
            "#03600FEveryone, thank you for\x01",
            "consulting with us.\x02\x03",
            "I'll be counting on you\x01",
            "if anything else\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6C2D")

    label("loc_6BA3")


    ChrTalk(
        0xF,
        (
            "#03603FBoth I and the mayor\x01",
            "want to advance this\x01",
            "case carefully.\x02\x03",
            "#03600FEveryone, I'll be\x01",
            "counting on you if\x01",
            "anything else happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C2D")

    TalkEnd(0xFE)
    Return()

    # Function_15_671C end

    def Function_16_6C31(): pass

    label("Function_16_6C31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CFE")

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
            "But it seems it was\x01",
            "successfully resolved.\x01",
            "That's a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll convey your message\x01",
            "to Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6D67")

    label("loc_6CFE")


    ChrTalk(
        0xFE,
        (
            "It seems it was\x01",
            "successfully resolved.\x01",
            "That's great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll convey your message\x01",
            "to Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D67")

    TalkEnd(0xFE)
    Return()

    # Function_16_6C31 end

    def Function_17_6D6B(): pass

    label("Function_17_6D6B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DD4")

    ChrTalk(
        0xFE,
        (
            "...To think that tiny\x01",
            "Alm became that fine\x01",
            "man...\x02",
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
    Jump("loc_6DE5")

    label("loc_6DD4")


    ChrTalk(
        0xFE,
        "...*sob*...\x02",
    )

    CloseMessageWindow()

    label("loc_6DE5")

    TalkEnd(0xFE)
    Return()

    # Function_17_6D6B end

    def Function_18_6DE9(): pass

    label("Function_18_6DE9")

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
            "#11P─I see. So that's what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAt first, I feared for\x01",
            "my life when you showed\x01",
            "up with that wolf.\x02",
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
            "legendary divine wolf like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PThe State Guard hardly\x01",
            "ever comes to the\x01",
            "village, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PPlease stay as long as\x01",
            "you like.\x02",
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
        "#00204F#6PThat'll be a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PHowever, there are a lot of\x01",
            "people in critical\x01",
            "condition at the hospital.\x02\x03",
            "#10401FEven now, President\x01",
            "Dieter's reputation doesn't\x01",
            "seem all that great, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PHmm... It's probably\x01",
            "because his connection\x01",
            "to this village is weak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PI never thought he'd go\x01",
            "through with the "Declaration\x01",
            "of Independence".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11POur harvests are down\x01",
            "because of the appearance\x01",
            "of that Cryptid, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PEven so, the State Guard\x01",
            "stops by on patrol every\x01",
            "now and then.\x02",
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
            "#01203F#5P#3CIt's normal for those in\x01",
            "the city to ignore those\x01",
            "living in villages...\x02\x03",
            "#01201FHowever, it seems to\x01",
            "have gone too far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PHmm... Honestly, I feel\x01",
            "we mustn't follow them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAlthough, compared to the\x01",
            "influence of Crossbell City,\x01",
            "this village is like nothing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PHonestly, I'm at a loss\x01",
            "as to what to do.\x02",
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
            "#00003F#5PWe'll watch out for that\x01",
            "Cryptid.\x02\x03",
            "#00001FAside from that, is there\x01",
            "anything else that's been\x01",
            "troubling you lately?\x02\x03",
            "Maintenance of order,\x01",
            "destabilization...\x01",
            "Anything like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PThankfully, it hasn't\x01",
            "come to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PFor now, the whole village is\x01",
            "cooperating to weather this\x01",
            "disaster as best we can.\x02",
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
        "#00005F#5PHarold!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 0)), scpexpr(EXPR_END)), "loc_76F4")

    ChrTalk(
        0x103,
        (
            "#00208F#6PThat's right... I remember he\x01",
            "said he was going to vacation\x01",
            "here with his family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7725")

    label("loc_76F4")


    ChrTalk(
        0x103,
        (
            "#00205F#6PHas he come here with\x01",
            "his family?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7725")


    ChrTalk(
        0xB,
        (
            "#11PYes. His family arrived\x01",
            "just when that\x01",
            "phenomenon occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAfter that, the highway movement\x01",
            "restrictions went into effect\x01",
            "immediately, and they were trapped here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PSo that's what\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PIncidentally, they're\x01",
            "staying on the 2nd floor\x01",
            "of the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PYou could pay them a\x01",
            "visit, if you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PAlright, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400F#12PShall we head over,\x01",
            "then?\x02",
        )
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

    # Function_18_6DE9 end

    def Function_19_793D(): pass

    label("Function_19_793D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E27")

    ChrTalk(
        0xB,
        (
            "*sigh*... That Derrick,\x01",
            "what in the world is he\x01",
            "doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FI'm worried... It's\x01",
            "quite possible that\x01",
            "he's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FGood day, Chief Tolta.\x01",
            "We're the Special\x01",
            "Support Section...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FHuh? Harold?\x02",
    )

    CloseMessageWindow()

    def lambda_7AF0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7AF0)
    Sleep(50)

    def lambda_7B00():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7B00)
    Sleep(50)

    def lambda_7B10():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7B10)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "Oh, it's you... I've\x01",
            "been waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FYou saw my request,\x01",
            "didn't you. Thank you\x01",
            "for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FS-Sure...\x02\x03",
            "#00005FBut, why is Harold here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As a matter of fact,\x01",
            "he's has a connection to\x01",
            "this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FI was speaking with Chief Tolta, and we\x01",
            "decided to consult with all of you.\x02\x03",
            "#03601FThe circumstances being what they are, anyway.\x01",
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
            "#00101FThe situation seems very\x01",
            "serious.\x02\x03",
            "#00103FIt seems to be something\x01",
            "concerning your son?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D84():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D84)
    Sleep(50)

    def lambda_7D94():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7D94)
    Sleep(50)

    def lambda_7DA4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7DA4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Hmm, it's a bit\x01",
            "complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you'll accept, I'd be\x01",
            "happy to give you the\x01",
            "details. Is now a good time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EA7")

    label("loc_7E27")

    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "Oh, have you made time\x01",
            "for this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you're taking up the\x01",
            "request, I'll tell you the\x01",
            "details... Is that all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EA7")

    Call(0, 20)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -41050, 0, -1950, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_19_793D end

    def Function_20_7ED6(): pass

    label("Function_20_7ED6")

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
            "[Accept]\x01",               # 0
            "[We're Not Ready]\x01",      # 1
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
        (0, "loc_7F41"),
        (1, "loc_7F49"),
        (SWITCH_DEFAULT, "loc_801B"),
    )


    label("loc_7F41")

    Call(0, 21)
    Jump("loc_801B")

    label("loc_7F49")


    ChrTalk(
        0x101,
        (
            "#00006FWe're terribly sorry,\x01",
            "but... We're a little\x01",
            "busy right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Then, please come again\x01",
            "if you have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If possible, I'd like\x01",
            "help from all of you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x173, 7)
    Jump("loc_801B")

    label("loc_801B")

    Return()

    # Function_20_7ED6 end

    def Function_21_801C(): pass

    label("Function_21_801C")


    ChrTalk(
        0x101,
        (
            "#00000FYes, no problem. Please\x01",
            "tell us what's going on.\x02",
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
            "My son Derrick has been\x01",
            "acting strange lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems like he's\x01",
            "planning something bad\x01",
            "in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FBad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't know the details,\x01",
            "but... I can guess what\x01",
            "he's thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The other day, he told Harold he\x01",
            "wanted to "pass on all future\x01",
            "transactions" or something.\x02",
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
            "#00005FStop trading? Why that\x01",
            "all of a sudden?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FIt's true you're on good\x01",
            "terms with Armorica,\x01",
            "Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03608FYes, I've treated the people\x01",
            "here with kindness for many\x01",
            "years.\x02\x03",
            "#03601FAnd so, thinking I had made\x01",
            "some mistake, I came here to\x01",
            "ask Chief Tolta the reason why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FIt seems like Chief Tolta\x01",
            "has no idea either, from\x01",
            "the sound of it.\x02\x03",
            "#10300FIsn't that right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes... A grave rudeness\x01",
            "has been done to Harold.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Losing a good customers\x01",
            "such as himself would be a\x01",
            "huge blow for the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I am sure my foolish son\x01",
            "isn't aware of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThat certainly is\x01",
            "strange...\x02\x03",
            "#00101FI wonder what happened\x01",
            "to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, I thought so too.\x01",
            "That's why I was discussing\x01",
            "the matter with Harold.\x02",
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
            "It's seems he's been\x01",
            "meeting with a suspicious\x01",
            "foreigner recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FA foreigner... you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FI don't know too many\x01",
            "details, but...\x02\x03",
            "#03601FIt's just, it seems he's\x01",
            "been discussing something\x01",
            "with Derrick in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm... Secret discussions,\x01",
            "you say. That does sound\x01",
            "suspicious.\x02",
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
            "And, if he is planning\x01",
            "some evil scheme, to put\x01",
            "a stop to it immediately.\x02",
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
            "with your son directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWhoa, calm down there\x01",
            "PeTiote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Well I hate to admit\x01",
            "it, but the young lady\x01",
            "over there is right.\x02",
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
            "If I asked him about this\x01",
            "matter, in the end,\x01",
            "nothing would be answered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As his father, it pains\x01",
            "me to say this.\x02",
        )
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
            "#00003FI understand. We'll\x01",
            "begin our investigation\x01",
            "right away.\x02\x03",
            "#00000FI was thinking of\x01",
            "starting with interviews\x01",
            "of the villagers.\x02",
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
            "It might be best to save\x01",
            "your interview with him\x01",
            "for last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FEveryone, please see if\x01",
            "you can find any\x01",
            "information on him.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FYes, please leave it to\x01",
            "us.\x02",
        )
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
            "Quest [Investigating a\x01",
            "Suspicious Character]\x07\x00\x01",
            "started!\x02",
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

    # Function_21_801C end

    def Function_22_8B67(): pass

    label("Function_22_8B67")

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
            "#00003FUmm, I'd like to ask you\x01",
            "a little something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked about the foreigner\x01",
            "who's been visiting the\x01",
            "village recently.\x07\x00\x02",
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
            "Hmm... He speaks\x01",
            "forcefully, but is quite\x01",
            "considerate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FConsiderate... you say?\x02",
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
            "He paid it no mind and\x01",
            "gave them sweets\x01",
            "instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Man, I'm not sure if I feel\x01",
            "guilty or if I admire him. It\x01",
            "just takes my breath away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... Thank you for\x01",
            "your cooperation.\x02",
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

    # Function_22_8B67 end

    def Function_23_8E83(): pass

    label("Function_23_8E83")

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
            "I don't believe it! That\x01",
            "Minneth is Quincy\x01",
            "Company staff?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And there's the bit\x01",
            "about the "Armorica\x01",
            "Honey Company" too.\x02",
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
            "#00005FUmm... By the way, where\x01",
            "is Derrick now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FOh, that's right. We\x01",
            "didn't see him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWe ran into him at the\x01",
            "hotel. He said he was\x01",
            "headed back to the village.\x02",
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
            "It's seems he's been\x01",
            "renting a room at Ash\x01",
            "Tree Inn lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Minneth has been visiting\x01",
            "the inn too, it seems. He\x01",
            "must be on the move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I had no idea about his plan to\x01",
            "build a factory on our private\x01",
            "property. How shameful of me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F...I wonder about that.\x02\x03",
            "#10300FUnexpectedly, he could have\x01",
            "acted on that trader's\x01",
            "suggestion, right?\x02\x03",
            "#10304FSo that it would be hard\x01",
            "for you to learn of it,\x01",
            "Chief.\x02",
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
        "W-What do you mean?\x02",
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
            "#03605FLloyd, are you concerned\x01",
            "about something?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FThis is just my\x01",
            "intuition but...\x02\x03",
            "#00001FThere are some\x01",
            "suspicious points about\x01",
            "Minneth.\x02",
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
        "What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FThe plan he told us about benefits\x01",
            "all parties involved.\x02\x03",
            "#00003FArmorica would gain jobs, and Quincy\x01",
            "Company would gain a subsidiary to\x01",
            "further their business.\x02\x03",
            "#00008FHis argument seems persuasive on the\x01",
            "surface, but...\x02\x03",
            "#00001FEverything is a little too perfect.\x01",
            "...Don't you think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03605F!! Now that you mention\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FOn top of that, he sold\x01",
            "a new orbal truck for\x01",
            "cheap.\x02\x03",
            "#00200FI think we can think of\x01",
            "that as an "advance\x01",
            "investment".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FI don't think anyone would\x01",
            "dispute that new orbal\x01",
            "cars are expensive...\x02\x03",
            "#10101FIt's unprecedented to part\x01",
            "with one for a mere 50,000\x01",
            "mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FConversely...\x02\x03",
            "#00301FIt means he's "certain"\x01",
            "to make that money back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03601FThat is strange.\x02\x03",
            "#03603FFor a company as large as\x01",
            "Quincy, such a cost is nothing\x01",
            "if it's for advancing a project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-Hmm, that might be\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, it's rather\x01",
            "suspicious.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001FMinneth has some other\x01",
            "objective... Possibly one\x01",
            "guaranteed to make him a profit.\x02\x03",
            "#00003FWe have no evidence though... We\x01",
            "should keep that in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes... We'll be very\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...That was some great\x01",
            "work, Special Support\x01",
            "Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks to you, I feel\x01",
            "the situation is under\x01",
            "control. I thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh, well that's fine,\x01",
            "but...\x02\x03",
            "#00005FAre you sure you're ok?\x01",
            "If not, we'll continue\x01",
            "investigating...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No... You've done enough\x01",
            "for now.\x02",
        )
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
        (
            "#00103F...I pray for your\x01",
            "success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThen, we'll excuse\x01",
            "ourselves.\x02\x03",
            "#00000FPlease contact us again\x01",
            "anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Sure. You can look\x01",
            "forward to it.\x02",
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
            "Quest [Investigating a\x01",
            "Suspicious Character]\x07\x00\x01",
            "completed!\x02",
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

    # Function_23_8E83 end

    def Function_24_9C2B(): pass

    label("Function_24_9C2B")

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
        (
            "Well done, ladies and\x01",
            "gentlemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You all saved this\x01",
            "village from the demon\x01",
            "hand of that crook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThough in the end, the\x01",
            "criminal fled...\x02",
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

    def lambda_9EB4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9EB4)
    Sleep(50)

    def lambda_9EC4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9EC4)
    Sleep(50)

    ChrTalk(
        0xD,
        (
            "I've really gone and\x01",
            "done it this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I got caught up in his\x01",
            "fraud and it led all of\x01",
            "us to this point...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FDon't say that. It's not\x01",
            "your fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No... It's completely my\x01",
            "fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I was so desperate to improve the village\x01",
            "that I didn't listen to my father... And\x01",
            "you already know the result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm unqualified to be\x01",
            "the next chief.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        "None of that matters.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        "Father?\x02",
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
            "will eventually fail at this\x01",
            "rate, I've done nothing about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I bear a large share of\x01",
            "the responsibility for\x01",
            "this incident, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#03608FChief...\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Through this incident,\x01",
            "I've finally realized\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To protect this village, we\x01",
            "mustn't rely on a single\x01",
            "person's stubborn thoughts.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Derrick... For now on,\x01",
            "I'd like you to lend me\x01",
            "your wisdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Each of us will contribute\x01",
            "our ideas, and we'll discuss\x01",
            "them with the villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is how it must be\x01",
            "if we're going to\x01",
            "protect this village.\x02",
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
            "I'll think more about\x01",
            "the village from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha... It seems you\x01",
            "were able to reconcile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHaha, looks that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell if this is the outcome,\x01",
            "then I guess falling for a\x01",
            "fraud isn't too bad after all?\x02",
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

    def lambda_A513():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A513)
    Sleep(50)

    def lambda_A523():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A523)
    Sleep(50)

    def lambda_A533():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A533)
    Sleep(50)

    def lambda_A543():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A543)
    Sleep(50)

    def lambda_A553():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A553)
    Sleep(50)

    def lambda_A563():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A563)
    Sleep(50)

    def lambda_A573():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A573)
    Sleep(50)

    def lambda_A583():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A583)
    Sleep(50)

    def lambda_A593():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A593)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10106FW-Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHmm, it's not what you\x01",
            "say, but how you say\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FN-No, that was\x01",
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
            "Once again, all of you have\x01",
            "helped us greatly. I would like\x01",
            "to thank all of you once again.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A6A6():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A6A6)
    Sleep(50)

    def lambda_A6B6():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6B6)
    Sleep(50)

    def lambda_A6C6():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A6C6)
    Sleep(50)

    def lambda_A6D6():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A6D6)
    Sleep(50)

    def lambda_A6E6():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A6E6)
    Sleep(50)

    def lambda_A6F6():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A6F6)
    Sleep(50)

    def lambda_A706():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A706)
    Sleep(50)

    def lambda_A716():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A716)
    Sleep(50)

    def lambda_A726():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A726)
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
            "I'll convey your message\x01",
            "to Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03604FI too am glad to have been\x01",
            "even a little useful in\x01",
            "resolving this incident.\x02\x03",
            "#03600FI look forward to\x01",
            "continuing to work with\x01",
            "you in the future, Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Haha, same here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FJust in case, please be\x01",
            "on the lookout for that\x01",
            "crook.\x02\x03",
            "#00000FAnd if you ever need our\x01",
            "help again, don't\x01",
            "hesitate to contact us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, I'll be counting on\x01",
            "you then. Thank you so\x01",
            "much for all your help.\x02",
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
            "Quest [Investigating the\x01",
            "Suspicious Trader]\x07\x00\x01",
            "completed!\x02",
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

    # Function_24_9C2B end

    def Function_25_AA41(): pass

    label("Function_25_AA41")

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
        "#00000FGood day, Chief Tolta.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, the Special Support\x01",
            "Section. How can I help\x01",
            "you today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe'd like to ask you\x01",
            "something, Chief.\x02\x03",
            "#00003FAre you letting someone\x01",
            "stay in your bee yard\x01",
            "shed?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Yes, actually I am\x01",
            "letting someone stay\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It was about three or four days\x01",
            "ago. "Please let me stay here\x01",
            "awhile", he asked suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Mr. Geval... I think his\x01",
            "name was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FI knew it!\x02\x03",
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
            "A place that's as\x01",
            "inconspicuous as\x01",
            "possible was his reply.\x02",
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
            "Could he be the one\x01",
            "you're searching for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Is he a person of\x01",
            "interest related to some\x01",
            "incident or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FNo, that's not the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FLloyd, I think it's best\x01",
            "if we tell Chief\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, I think you're\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that they\x01",
            "were searching for Geval due\x01",
            "to Alm and Aerie's request.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "Hmm, I see... So he's a\x01",
            "former congressman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He's the congressman who\x01",
            "faked being ill to evade\x01",
            "taxes a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now that you mention it, I\x01",
            "think I remember seeing his\x01",
            "face in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FThis request isn't\x01",
            "directly related to that\x01",
            "incident, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FChief Tolta, will you\x01",
            "let us speak with Geval\x01",
            "in the shed?\x02\x03",
            "#00008FIt seems he doesn't want\x01",
            "to see Alm and Aerie,\x01",
            "but even so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Hmm, very well then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was on bad terms with my son as\x01",
            "well. In the end, the problem turned\x01",
            "out to be that we don't talk enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't want anyone else\x01",
            "to fall into the same\x01",
            "rut that I did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FChief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Haha. Follow me, please.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_AA41 end

    def Function_26_B1DB(): pass

    label("Function_26_B1DB")

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
            "#00000FYou are Geval... right?\x02\x03",
            "#00006FPhew, we finally found\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#4PHmph... You guys are\x01",
            "relentless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PSo my son and his wife\x01",
            "are looking for me, are\x01",
            "they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PNo matter what you say,\x01",
            "I'll never meet with\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FW-Why are you being so\x01",
            "obstinate?\x02",
        )
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
            "#4PMy son... Alm hates me.\x01",
            "There can't be any doubt\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FHates?\x02",
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
            "#4PWhen I was a new congressman,\x01",
            "I got involved with various\x01",
            "corrupt dealings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PI worked only for status,\x01",
            "honor and mira, and turned\x01",
            "my back on my family.\x02",
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
            "#4PThen, I got more and more carried\x01",
            "away, and one day... I did something\x01",
            "one with a child should never do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PWhen my wife was out, I\x01",
            "invited my mistress to\x01",
            "my own mansion.\x02",
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
        (
            "#00306FYou really deserved it\x01",
            "then, huh...\x02",
        )
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
            "that, but... I'm sure both Alm and my widow\x01",
            "have painful memories of the divorce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PBut of all things, I\x01",
            "felt refreshed after\x01",
            "that.\x02",
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
            "#00306FI guess it can't be\x01",
            "helped if she hates you,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FRandy, you're too\x01",
            "direct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PHmph, it's like that\x01",
            "redhead said. It can't be\x01",
            "helped if people hate me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PAnd... In the end, I was\x01",
            "a follower of Chairman\x01",
            "Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PHowever, because of a trivial\x01",
            "tax evasion charge, I can't\x01",
            "so easily cut ties with him.\x02",
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
            "#4PExposing my son to my shame of\x01",
            "having lost everything... I\x01",
            "don't think I could bear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Geval...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FSo that's how it is, is\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#00001FUm, can I say one thing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PWhat!? What could you\x01",
            "possibly have to say\x01",
            "now!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt may be true that you've\x01",
            "done some horrible things to\x01",
            "your son and wife.\x02\x03",
            "It may be true that you've\x01",
            "done some underhanded things\x01",
            "as a corrupt politician.\x02\x03",
            "#00000FBut, based on what I just\x01",
            "heard, it sounds like you\x01",
            "regret your actions.\x02",
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
            "#00108FSaying you won't meet them out of\x01",
            "guilt... That doesn't make much sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4PB-But!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAlso...\x02\x03",
            "#00002FIn my judgment, Alm\x01",
            "doesn't hate you after\x01",
            "all.\x02",
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
            "#00004FWhen Alm and his wife Aerie\x01",
            "gave us the request...\x02\x03",
            "#00002FThey had built a loving\x01",
            "family and looked happy.\x02\x03",
            "He requested just one thing\x01",
            "of us. It was...\x02\x03",
            "#00004F"I want to show father our\x01",
            "child and tell him about the\x01",
            "happy family we've built."\x02",
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
            "each other very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FIf they hate you even a\x01",
            "little, their faces\x01",
            "didn't show it at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHehe, I wonder about that.\x02\x03",
            "#10304FIf they had my poker face,\x01",
            "I think they'd manage to\x01",
            "conceal it, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00211FWazy, stop being weird.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell anyway, Geval. Your\x01",
            "son has grown quite a\x01",
            "bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F...That's all we can\x01",
            "say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell? Wouldn't you like\x01",
            "to see Alm and Aerie?\x02",
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
            "#4P...If you'd say that\x01",
            "much... I might see\x01",
            "them.\x02",
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
            "#4P...Now, how about\x01",
            "calling them over before\x01",
            "I change my mind!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FR-Right. Then, I'll do\x01",
            "so right away!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 35)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 36)
    Sleep(300)
    OP_68(76460, 1500, -1540, 2000)
    BeginChrThread(0x101, 3, 0, 34)

    def lambda_C390():

        label("loc_C390")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C390")

    QueueWorkItem2(0x102, 1, lambda_C390)
    Sleep(50)

    def lambda_C3A5():

        label("loc_C3A5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C3A5")

    QueueWorkItem2(0x103, 1, lambda_C3A5)
    Sleep(50)

    def lambda_C3BA():

        label("loc_C3BA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C3BA")

    QueueWorkItem2(0x104, 1, lambda_C3BA)
    Sleep(50)

    def lambda_C3CF():

        label("loc_C3CF")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C3CF")

    QueueWorkItem2(0x109, 1, lambda_C3CF)
    Sleep(50)

    def lambda_C3E4():

        label("loc_C3E4")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C3E4")

    QueueWorkItem2(0x105, 1, lambda_C3E4)
    Sleep(50)

    def lambda_C3F9():

        label("loc_C3F9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_C3F9")

    QueueWorkItem2(0xB, 1, lambda_C3F9)
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
            "The Old Dragon...\x02\x03",
            "And summoned Alm and Aerie\x01",
            "to Armorica Village.\x02\x03",
            "Everyone waited outside the\x01",
            "shed to prepare them for\x01",
            "what they were about to see.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_B1DB end

    def Function_27_C4FA(): pass

    label("Function_27_C4FA")


    def lambda_C4FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C4FF)

    def lambda_C510():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C510)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 75280, 0, 270, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_27_C4FA end

    def Function_28_C545(): pass

    label("Function_28_C545")


    def lambda_C54A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C54A)

    def lambda_C55B():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C55B)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 76460, 0, 280, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_28_C545 end

    def Function_29_C590(): pass

    label("Function_29_C590")


    def lambda_C595():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C595)

    def lambda_C5A6():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C5A6)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 75260, 0, -920, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_29_C590 end

    def Function_30_C5DB(): pass

    label("Function_30_C5DB")


    def lambda_C5E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C5E0)

    def lambda_C5F1():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C5F1)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 76470, 0, -920, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_30_C5DB end

    def Function_31_C626(): pass

    label("Function_31_C626")


    def lambda_C62B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C62B)

    def lambda_C63C():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C63C)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 75210, 0, -2040, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_31_C626 end

    def Function_32_C671(): pass

    label("Function_32_C671")


    def lambda_C676():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C676)

    def lambda_C687():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C687)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 76180, 0, -2040, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_32_C671 end

    def Function_33_C6BC(): pass

    label("Function_33_C6BC")


    def lambda_C6C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_C6C1)

    def lambda_C6D2():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C6D2)
    WaitChrThread(0xB, 1)
    OP_95(0xB, 77380, 0, -2650, 2000, 0x0)
    OP_95(0xB, 77640, 0, -310, 2000, 0x0)
    OP_93(0xB, 0x13B, 0x1F4)
    Return()

    # Function_33_C6BC end

    def Function_34_C71B(): pass

    label("Function_34_C71B")


    def lambda_C720():
        OP_95(0xFE, 75070, 0, -5420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C720)
    Sleep(1000)

    def lambda_C73D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C73D)
    Return()

    # Function_34_C71B end

    def Function_35_C74A(): pass

    label("Function_35_C74A")

    OP_93(0x103, 0x5A, 0x0)
    OP_9B(0x1, 0x103, 0xB4, 0x1F4, 0x7D0, 0x0)
    Return()

    # Function_35_C74A end

    def Function_36_C761(): pass

    label("Function_36_C761")

    OP_93(0x109, 0x5A, 0x0)
    OP_9B(0x1, 0x109, 0xB4, 0x2EE, 0x7D0, 0x0)
    Return()

    # Function_36_C761 end

    def Function_37_C778(): pass

    label("Function_37_C778")

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
        "Are you... my dad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Ahaha, it's been a\x01",
            "while.\x02",
        )
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
            "I-It's been a while,\x01",
            "son. 15 years, in\x01",
            "fact...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "And she is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "How do you do, Geval.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I'm Alm's wife Aerie.\x01",
            "It's very nice to meet\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "S-Sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I'm glad my son found a\x01",
            "young lady as nice as\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Oh, Geval...\x02",
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
            "...T-That is... In your\x01",
            "arms there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Haha, it's our daughter.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "Almin, say hi to your\x01",
            "grandpa!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x14,
        "Baby",
        "Babubu.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Oh, very nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...Ha, haha...\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        (
            "S-Say, Alm. I know I\x01",
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
            "More importantly dad, look\x01",
            "at this. Almin's eyes\x01",
            "sparkle like pure sapphirl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "They're just like yours\x01",
            "Aerie─ beautiful as the\x01",
            "clear blue sky.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "Yes, but Alm, the shape\x01",
            "of her ears is the same\x01",
            "as yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Uhuhu... Every time I\x01",
            "see them I want to eat\x01",
            "them up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Yes Aerie... I'll never\x01",
            "let go of our child as\x01",
            "long as I live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Alm... We'll be together\x01",
            "forever.\x02",
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

    def lambda_CD1F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CD1F)
    Sleep(50)

    def lambda_CD2F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_CD2F)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "Huh? Father? What's\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Maybe he's not feeling\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "No... I'm fine... I'm\x01",
            "fine...\x02",
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

    # Function_37_C778 end

    def Function_38_CDCA(): pass

    label("Function_38_CDCA")


    def lambda_CDCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_CDCF)

    def lambda_CDE0():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CDE0)
    WaitChrThread(0x13, 1)
    OP_95(0x13, 74920, 0, 210, 2000, 0x0)
    OP_93(0x13, 0x0, 0x1F4)
    Return()

    # Function_38_CDCA end

    def Function_39_CE15(): pass

    label("Function_39_CE15")


    def lambda_CE1A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_CE1A)

    def lambda_CE2B():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_CE2B)
    WaitChrThread(0x14, 1)
    OP_95(0x14, 76120, 0, 210, 2000, 0x0)
    OP_93(0x14, 0x0, 0x1F4)
    Return()

    # Function_39_CE15 end

    SaveToFile()

Try(main)
