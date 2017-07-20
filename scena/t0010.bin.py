from ScenarioHelper import *

def main():
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
        "Milia",                 # 1
        "Donald",               # 2
        "Angers",               # 3
        "Mayor of Torta",             # 4
        "Ena's lady",               # 5
        "Derrick",               # 6
        "Elkin",               # 7
        "Harold",               # 8
        "Pete",                 # 9
        "Mayor of Torta",             # 10
        "Gabal",                 # 11
        "Almu",                 # 12
        "Airy",               # 13
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
        "Function_5_165E",         # 05, 5
        "Function_6_2378",         # 06, 6
        "Function_7_2480",         # 07, 7
        "Function_8_2F6F",         # 08, 8
        "Function_9_41DD",         # 09, 9
        "Function_10_4529",        # 0A, 10
        "Function_11_47CA",        # 0B, 11
        "Function_12_550F",        # 0C, 12
        "Function_13_58F2",        # 0D, 13
        "Function_14_5B16",        # 0E, 14
        "Function_15_5C11",        # 0F, 15
        "Function_16_60F2",        # 10, 16
        "Function_17_623D",        # 11, 17
        "Function_18_62DD",        # 12, 18
        "Function_19_6D6F",        # 13, 19
        "Function_20_729F",        # 14, 20
        "Function_21_73E5",        # 15, 21
        "Function_22_7E8B",        # 16, 22
        "Function_23_819B",        # 17, 23
        "Function_24_8F2D",        # 18, 24
        "Function_25_9BFB",        # 19, 25
        "Function_26_A31F",        # 1A, 26
        "Function_27_B6A5",        # 1B, 27
        "Function_28_B6F0",        # 1C, 28
        "Function_29_B73B",        # 1D, 29
        "Function_30_B786",        # 1E, 30
        "Function_31_B7D1",        # 1F, 31
        "Function_32_B81C",        # 20, 32
        "Function_33_B867",        # 21, 33
        "Function_34_B8C6",        # 22, 34
        "Function_35_B8F5",        # 23, 35
        "Function_36_B90C",        # 24, 36
        "Function_37_B923",        # 25, 37
        "Function_38_C016",        # 26, 38
        "Function_39_C061",        # 27, 39
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_811")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_778")

    ChrTalk(
        0xFE,
        (
            "In Crossbell City\x01",
            "The president appears to have been detained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got to move freely\x01",
            "The guards of the guilds,\x01",
            "He came to the village immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation,\x01",
            "Together with the power of the crossbell\x01",
            "I have to go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_80C")

    label("loc_778")


    ChrTalk(
        0xFE,
        (
            "I got to move freely\x01",
            "The guards of the guilds,\x01",
            "He came to the village immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation,\x01",
            "Together with the power of the crossbell\x01",
            "I have to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80C")

    Jump("loc_165A")

    label("loc_811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_992")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EE")

    ChrTalk(
        0xFE,
        (
            "Recently, Derrick concurrently confirms the safety\x01",
            "I often visit the village's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation,\x01",
            "Even if I only see the face of my acquaintance\x01",
            "It is quite secure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Serious and solid\x01",
            "It seems Derrick.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_98D")

    label("loc_8EE")


    ChrTalk(
        0xFE,
        (
            "Recently, Derrick concurrently confirms the safety\x01",
            "I often visit the village's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I only see the face of my acquaintance\x01",
            "It is quite secure.\x01",
            "Hehe, it seems like Derrick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98D")

    Jump("loc_165A")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A91")

    ChrTalk(
        0xFE,
        (
            "Elder brother Elkin\x01",
            "Every day \"I can not drive\"\x01",
            "It is only a sigh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even just a cramped situation\x01",
            "I feel depressed,\x01",
            "Gutchiguchi …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Under such circumstances\x01",
            "Every day you can eat fresh meals,\x01",
            "It's kind of thankful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B2F")

    label("loc_A91")


    ChrTalk(
        0xFE,
        (
            "Elder brother Elkin\x01",
            "Every day \"I can not drive\"\x01",
            "It is only a sigh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Under such circumstances\x01",
            "Every day you can eat fresh meals,\x01",
            "It's kind of thankful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2F")

    Jump("loc_165A")

    label("loc_B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BCB")

    ChrTalk(
        0xFE,
        (
            "Recently, around the old battlefield\x01",
            "I turned on like an armor\x01",
            "You see a devil monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A demon somewhere rich kept\x01",
            "I wonder if he ran away … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_165A")

    label("loc_BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C74")

    ChrTalk(
        0xFE,
        (
            "For our farmers,\x01",
            "Rain raises crops\x01",
            "Grace from heaven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to the goddess\x01",
            "We can eat Gohan too.\x01",
            "I must thank you properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CDB")

    label("loc_C74")


    ChrTalk(
        0xFE,
        (
            "For our farmers,\x01",
            "Rain raises crops\x01",
            "It is the blessing of the heavens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the goddess\x01",
            "I must thank you properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDB")

    Jump("loc_165A")

    label("loc_CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F4D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCB")

    ChrTalk(
        0xFE,
        (
            "The reform of the village that Derrick is advancing … …\x01",
            "I do not get much pins, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We introduced introducer to field,\x01",
            "It seems that everything will be easier … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I like farming because I like work.\x01",
            "It may be complicated to get work on machines.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E4A")

    label("loc_DCB")


    ChrTalk(
        0xFE,
        (
            "Reforming the village,\x01",
            "What makes it more convenient\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I like farming because I like work.\x01",
            "It may be complicated to be too convenient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4A")

    Jump("loc_F48")

    label("loc_E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF0")

    ChrTalk(
        0xFE,
        (
            "To that person Minnesu,\x01",
            "All the villagers were deceived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the world,\x01",
            "I do not mind trying to trick people\x01",
            "There are people to think …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I learned a lot.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F48")

    label("loc_EF0")


    ChrTalk(
        0xFE,
        (
            "In the world,\x01",
            "I do not mind trying to trick people\x01",
            "There are people to think …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I learned a lot.\x02",
    )

    CloseMessageWindow()

    label("loc_F48")

    Jump("loc_165A")

    label("loc_F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_116F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104D")

    ChrTalk(
        0xFE,
        (
            "If it is Elkin, now to the city\x01",
            "I'm going to ship the crop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, it is flying up somehow.\x01",
            "While often driving away while going home\x01",
            "Come home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, such things\x01",
            "You can get it cheaply,\x01",
            "I know I'm happy though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10B1")

    label("loc_104D")


    ChrTalk(
        0xFE,
        (
            "If it is Elkin, now to the city\x01",
            "I'm off to shipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After a while\x01",
            "I wonder if they will come back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B1")

    Jump("loc_116A")

    label("loc_10B6")


    ChrTalk(
        0xFE,
        (
            "Elkin's fellow, Mr. Minnesh.\x01",
            "After having the power tractor cheaply handed over\x01",
            "It has been floating all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand the feeling … ….\x01",
            "Do not meet accidents\x01",
            "I have to say it well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116A")

    Jump("loc_165A")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B7")

    ChrTalk(
        0xFE,
        (
            "The village mayor of this village, from villagers altogether\x01",
            "A suitable person is chosen by majority decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The next village mayor, the village manager's son Derrick\x01",
            "Everyone in the village acknowledges that it is suitable … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because Derrick is serious,\x01",
            "Everything is hard to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thinking about the future of the village\x01",
            "It's a nice thing ….\x01",
            "I'd like you to rely on us for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1333")

    label("loc_12B7")


    ChrTalk(
        0xFE,
        (
            "Because Derrick is serious,\x01",
            "Everything is hard to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I am suffering alone as it is,\x01",
            "I hope not to be rude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1333")

    Jump("loc_165A")

    label("loc_1338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_14FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146D")

    ChrTalk(
        0xFE,
        (
            "The accent of Elkin,\x01",
            "Please say \"Armoric accent\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the village with Uncle Donald\x01",
            "I only speak about Elkin,\x01",
            "It is an accent that has been transmitted from long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"This is Almorico villager\"\x01",
            "Since I feel it, I have to fix it\x01",
            "I think it's good, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A man is something I do not care\x01",
            "You have trouble.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14F6")

    label("loc_146D")


    ChrTalk(
        0xFE,
        (
            "Elkin 's Armoric accent,\x01",
            "It has been transmitted since a long time ago\x01",
            "In a sense it is a valuable accent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not dislike it,\x01",
            "I do not think I should fix it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F6")

    Jump("loc_165A")

    label("loc_14FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_165A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DE")

    ChrTalk(
        0xFE,
        (
            "Recently it is really peaceful.\x01",
            "Because there is also a moderate rainy day\x01",
            "Crops grow well … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the weather is nice like today\x01",
            "The sunny day is comfortable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, on a power track\x01",
            "I wonder if I should take a nap even with a straw.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_165A")

    label("loc_15DE")


    ChrTalk(
        0xFE,
        (
            "If the weather is nice like today\x01",
            "The sunny day is comfortable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, on a power track\x01",
            "I wonder if I should take a nap even with a straw.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165A")

    TalkEnd(0xFE)
    Return()

    # Function_4_693 end

    def Function_5_165E(): pass

    label("Function_5_165E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167C")
    Call(0, 6)
    Jump("loc_16FA")

    label("loc_167C")


    ChrTalk(
        0xFE,
        "Ha, it is what Angers says.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To maintain village food, too,\x01",
            "Ora and farmers firmly\x01",
            "I do not have to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FA")

    Jump("loc_2374")

    label("loc_16FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_189E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180A")

    ChrTalk(
        0xFE,
        (
            "After the Declaration of Independence, in Crosbell City\x01",
            "The truck from the village\x01",
            "I can not go …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell City, too,\x01",
            "People who are looking forward to fresh vegetables\x01",
            "It should be absolutely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To such people\x01",
            "I can not deliver crops,\x01",
            "You must bear as a producer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1899")

    label("loc_180A")


    ChrTalk(
        0xFE,
        (
            "Crossbell City, too,\x01",
            "People who are looking forward to fresh vegetables\x01",
            "It should be absolutely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The invalid declaration of this time, to resume dealings\x01",
            "I hope it connects.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1899")

    Jump("loc_2374")

    label("loc_189E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1A28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199C")

    ChrTalk(
        0xFE,
        (
            "A monster is a phantom beast\x01",
            "It will devastate the fields in the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Along with movement restrictions\x01",
            "The harvest is also pretty depressed,\x01",
            "Honesty It is an abandoned business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, still only in the village\x01",
            "I managed to cover it with self-sufficiency.\x01",
            "I must thank the goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A23")

    label("loc_199C")


    ChrTalk(
        0xFE,
        (
            "If only inside the village somehow\x01",
            "I am financially self-sufficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, this situation\x01",
            "How long will it continue …?\x01",
            "To be honest, I do not even know Ora.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A23")

    Jump("loc_2374")

    label("loc_1A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADE")

    ChrTalk(
        0xFE,
        (
            "I wonder if the city will be attacked\x01",
            "I was shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Moreover, the attackers\x01",
            "It seems that he has not been caught yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to Armorika village,\x01",
            "Worried and uneasy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B34")

    label("loc_1ADE")


    ChrTalk(
        0xFE,
        (
            "Since the street attacks,\x01",
            "I'm worried somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, also in the field work\x01",
            "My body is empty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B34")

    Jump("loc_2374")

    label("loc_1B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE5")

    ChrTalk(
        0xFE,
        (
            "Today, Kamille and the others\x01",
            "It is a Sunday school class at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ora is concerned only with agriculture\x01",
            "It is from teaching hey.\x01",
            "I want you to study properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C2B")

    label("loc_1BE5")


    ChrTalk(
        0xFE,
        "Well, agriculture is closed today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's go home at home for a long time.\x02",
    )

    CloseMessageWindow()

    label("loc_1C2B")

    Jump("loc_2374")

    label("loc_1C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E54")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE7")

    ChrTalk(
        0xFE,
        (
            "Mr. Minnes,\x01",
            "Also in private estates on the way of the old road\x01",
            "I heard that you are going to build something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is an agricultural tool station\x01",
            "I was doing it … ….\x01",
            "Well, I have to move it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4F")

    label("loc_1CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBF")

    ChrTalk(
        0xFE,
        (
            "That minnes is a man,\x01",
            "It was a bad guy for Hong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ola also, with that smile and attitude\x01",
            "It was totally deceived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… However, the parties'\x01",
            "Derrick surely should be shocked.\x01",
            "You should not have thought of it … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E4F")

    label("loc_1DBF")


    ChrTalk(
        0xFE,
        (
            "I think the village best\x01",
            "To deceive Derrick,\x01",
            "He was bad for Hong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That Minneshi man,\x01",
            "If you see it this time\x01",
            "I do it very well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4F")

    Jump("loc_2374")

    label("loc_1E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1ED8")

    ChrTalk(
        0xFE,
        (
            "Recently foreigners who often come to the village,\x01",
            "It is quite cheerful person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always smile,\x01",
            "I do not care what you say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2374")

    label("loc_1ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_205A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC0")

    ChrTalk(
        0xFE,
        (
            "From Elkin-kun\x01",
            "About conductivity track\x01",
            "Just being consulted … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Probably, it should be a lifetime soon.\x01",
            "Even if I repair it, it will be broken soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Elkin-kun\x01",
            "Especially because I cherished it,\x01",
            "I do not have to be in a hekko.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2055")

    label("loc_1FC0")


    ChrTalk(
        0xFE,
        (
            "The village's power track is\x01",
            "Probably, it is already a lifetime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since there is no room for Mira in the village,\x01",
            "It is hard to consult with the mayor …\x01",
            "I have to replace it as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2055")

    Jump("loc_2374")

    label("loc_205A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2202")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214F")

    ChrTalk(
        0xFE,
        (
            "In the world, agricultural conductors\x01",
            "There are many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Conductive power tillers to cultivate fields,\x01",
            "Conduct tractor for harvest … …\x01",
            "It will be indispensable for agriculture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in Almorika village\x01",
            "Everyone is boring old style though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21FD")

    label("loc_214F")


    ChrTalk(
        0xFE,
        (
            "Conductive force tractor to power-driven rpm ……\x01",
            "In this era, the conductors are\x01",
            "It is essential for agriculture as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Greedy, more convenient\x01",
            "I want the latest model, but …\x01",
            "Well, that's a luxury.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21FD")

    Jump("loc_2374")

    label("loc_2202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2374")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E5")

    ChrTalk(
        0xFE,
        (
            "Oh, in the village field\x01",
            "I made various vegetables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The vegetables made of Armorica\x01",
            "Taking plenty of the light of the heavenly lights,\x01",
            "That's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After shipping to Crossbell City,\x01",
            "I am glad if you eat deliciously.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2374")

    label("loc_22E5")


    ChrTalk(
        0xFE,
        (
            "Almorica vegetables,\x01",
            "Taking plenty of the light of the heavenly lights,\x01",
            "That's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently imports also increased,\x01",
            "You can not lose it in tasty absolutely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2374")

    TalkEnd(0xFE)
    Return()

    # Function_5_165E end

    def Function_6_2378(): pass

    label("Function_6_2378")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Ha ha\x01",
            "No way No way\x01",
            "What does it appear on the crossbell …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even for agricultural work due to uneasiness\x01",
            "My hands are gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ha, what is pitiable\x01",
            "I'm telling you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because it is such a time,\x01",
            "For Camille or a pulley\x01",
            "I have to work desperately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_6_2378 end

    def Function_7_2480(): pass

    label("Function_7_2480")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249E")
    Call(0, 6)
    Jump("loc_252C")

    label("loc_249E")


    ChrTalk(
        0xFE,
        (
            "This person, a bit\x01",
            "Because there is a weak point\x01",
            "Sometimes I have to hit my butt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Humans, because it's such a time\x01",
            "I am desperate to work\x01",
            "It is important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252C")

    Jump("loc_2F6B")

    label("loc_2531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_268B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25DD")

    ChrTalk(
        0xFE,
        (
            "Collin today as well\x01",
            "With our father\x01",
            "You seem to be playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am indebted to Mr. Harold,\x01",
            "I wonder if I will treat you today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2686")

    label("loc_25DD")


    ChrTalk(
        0xFE,
        (
            "I am indebted to Mr. Harold,\x01",
            "I wonder if I will treat you today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello every day, cooking Sophia\x01",
            "For Collin who is eating\x01",
            "It may be unsatisfactory though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2686")

    Jump("loc_2F6B")

    label("loc_268B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_27DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2768")

    ChrTalk(
        0xFE,
        (
            "Harold's wife\x01",
            "He is a really good cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything, at home in the city\x01",
            "Cooking class something\x01",
            "I heard that it is open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this is not the case,\x01",
            "I also want to go through.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27D6")

    label("loc_2768")


    ChrTalk(
        0xFE,
        (
            "Harold's wife\x01",
            "He is a really good cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Children are too old,\x01",
            "I am making friends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D6")

    Jump("loc_2F6B")

    label("loc_27DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_294D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C3")

    ChrTalk(
        0xFE,
        (
            "The damage of the attack incident,\x01",
            "It seems that it was really enormous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Oh no, it's frustrating.\x01",
            "With only such topics,\x01",
            "I can not feel depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In such a case,\x01",
            "Send usual routine\x01",
            "I have to get well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2948")

    label("loc_28C3")


    ChrTalk(
        0xFE,
        (
            "When listening to the story of the damage caused by the raid incident,\x01",
            "I feel sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In such a case,\x01",
            "I will send my usual daily life\x01",
            "I think it is the most important thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2948")

    Jump("loc_2F6B")

    label("loc_294D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A27")

    ChrTalk(
        0xFE,
        (
            "Through yesterday's incident,\x01",
            "The village headman and Derrick\x01",
            "You seem to have reconciled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both of us talked about the village\x01",
            "It is a human being who thinks first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This village, which has become tired lately,\x01",
            "From now on\x01",
            "It will get better.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A97")

    label("loc_2A27")


    ChrTalk(
        0xFE,
        (
            "The village chief and Derrick know about the village\x01",
            "It is a human being who thinks first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This village will definitely come\x01",
            "It will get better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A97")

    Jump("loc_2F6B")

    label("loc_2A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2BA8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2A")

    ChrTalk(
        0xFE,
        (
            "Even so,\x01",
            "The reform of the village Mong\x01",
            "That's not going to be such a sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is Mr. Minnes's\x01",
            "Is it a cumbersome skill?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA3")

    label("loc_2B2A")


    ChrTalk(
        0xFE,
        (
            "That kind of minnes is\x01",
            "To release a monster\x01",
            "I did not expect it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, to the children\x01",
            "I'm glad I did not have any injuries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA3")

    Jump("loc_2F6B")

    label("loc_2BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE4")

    ChrTalk(
        0xFE,
        "Well, I wonder what I will make today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C5A")

    label("loc_2BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF6")
    Call(0, 22)
    Jump("loc_2C5A")

    label("loc_2BF6")


    ChrTalk(
        0xFE,
        (
            "Well, that person\x01",
            "It was pretty good person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am friendly to children,\x01",
            "I think that it is not a bad person, but.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C5A")

    Jump("loc_2F6B")

    label("loc_2C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D54")

    ChrTalk(
        0xFE,
        (
            "In the field, sometimes bad shape\x01",
            "I can have vegetables and fruits ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because that is not for sale,\x01",
            "The villagers share it and eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how bad it is,\x01",
            "Because the taste is unchanging and it is delicious.\x01",
            "Thanks to that, households are saved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DFC")

    label("loc_2D54")


    ChrTalk(
        0xFE,
        (
            "Bad vegetables and fruits\x01",
            "Because you do not buy it at the store,\x01",
            "I divide it among villagers and eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so tasty\x01",
            "I do not buy it because its shape is bad,\x01",
            "I do not mind the city people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFC")

    Jump("loc_2F6B")

    label("loc_2E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E0F")
    Jump("loc_2F6B")

    label("loc_2E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EEE")

    ChrTalk(
        0xFE,
        (
            "Recently, Mr. Aretha\x01",
            "Please officially move here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My son is with my cocks\x01",
            "It really helps me playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am borrowing a room at the hotel now.\x01",
            "It looks like it's going well\x01",
            "I'm going to say hello.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F6B")

    label("loc_2EEE")


    ChrTalk(
        0xFE,
        (
            "Stefan,\x01",
            "Well with the chinens of my place\x01",
            "Please play with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Originally it is a village with few children,\x01",
            "It was nice to have good friends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F6B")

    TalkEnd(0xFE)
    Return()

    # Function_7_2480 end

    def Function_8_2F6F(): pass

    label("Function_8_2F6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F9C")
    Call(0, 25)
    Return()

    label("loc_2F9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FC1")
    Call(0, 19)
    Return()

    label("loc_2FC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FDF")
    Call(0, 13)
    Jump("loc_3182")

    label("loc_2FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E0")

    ChrTalk(
        0xFE,
        (
            "Mr. Harold\x01",
            "I am back in town earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Future village correspondence\x01",
            "You were discussing with Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Harold for a while now\x01",
            "I wanted you to remain … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that we can go around the world and do what we can\x01",
            "I told you I wanted to.\x01",
            "… … There is no way to do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3182")

    label("loc_30E0")


    ChrTalk(
        0xFE,
        (
            "…… There is also future response of the village,\x01",
            "Harold for a while now\x01",
            "I wanted you to remain … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, the Mock fighter also\x01",
            "It is something that comes,\x01",
            "I must do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3182")

    Jump("loc_41D9")

    label("loc_3187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_330E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3277")

    ChrTalk(
        0xFE,
        (
            "Independent invalid declaration was issued,\x01",
            "Derrick moves in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation …\x01",
            "Even if I served as a village chief for a long time\x01",
            "I do not know what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, what each person can do\x01",
            "I am going to do it firmly\x01",
            "It is important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3309")

    label("loc_3277")


    ChrTalk(
        0xFE,
        (
            "In this situation …\x01",
            "Even if I served as a village chief for a long time\x01",
            "I do not know what will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, what each person can do\x01",
            "I am going to do it firmly\x01",
            "It is important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3309")

    Jump("loc_41D9")

    label("loc_330E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_3461")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DF")

    ChrTalk(
        0xFE,
        (
            "Hmm, no way, to the battlefield\x01",
            "It is said that such people were … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like a tough guy,\x01",
            "I am planning to hand out the village\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As Almorica village,\x01",
            "Let's assume that we are going to stay still for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_345C")

    label("loc_33DF")


    ChrTalk(
        0xFE,
        (
            "Those lurking in the battlefield,\x01",
            "I am planning to hand out the village\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As Almorica village,\x01",
            "Let's assume that we are going to stay still for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_345C")

    Jump("loc_41D9")

    label("loc_3461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_360B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3594")

    ChrTalk(
        0xFE,
        (
            "Honest with President Dieter,\x01",
            "I feel something I can not attach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, influence of this village etc.\x01",
            "Compared to the population of Crossbell City\x01",
            "Something like nothing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……Anyways,\x01",
            "Harold's family also\x01",
            "It is to cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cooperating with the whole village to make this difficult\x01",
            "There is nothing else I will survive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3606")

    label("loc_3594")


    ChrTalk(
        0xFE,
        (
            "Harold's family also\x01",
            "It is to cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cooperating with the whole village to make this difficult\x01",
            "There is nothing else I will survive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3606")

    Jump("loc_41D9")

    label("loc_360B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_391A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F3")

    ChrTalk(
        0xFE,
        (
            "Hehuu, it's a tough time.\x01",
            "Thanks to my heart 's warming up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, as for Genba,\x01",
            "Please leave it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until he calmed down and returned to the city,\x01",
            "I will take care of it properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_376B")

    label("loc_36F3")


    ChrTalk(
        0xFE,
        (
            "The thing about Gabal,\x01",
            "Please leave it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until he calmed down and returned to the city,\x01",
            "I will take care of it properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376B")

    Jump("loc_3915")

    label("loc_3770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3878")

    ChrTalk(
        0xFE,
        (
            "The recent attack of the streets of the city ……\x01",
            "To the inhabitants of Almorika village,\x01",
            "Anxiety seems to spread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Empire's conspiracy theory also flows,\x01",
            "Beyond sure evidence\x01",
            "It is not easy to be swallowed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Anyway now,\x01",
            "Do not forget to watch out around the village\x01",
            "I ought to have it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3915")

    label("loc_3878")


    ChrTalk(
        0xFE,
        (
            "Derrick, young people in the village\x01",
            "It is alarming around me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the inhabitants of the village no more,\x01",
            "Even for not letting you feel uneasy …\x01",
            "Do not let go of vigilance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3915")

    Jump("loc_41D9")

    label("loc_391A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3935")
    Call(0, 10)
    Jump("loc_39C2")

    label("loc_3935")


    ChrTalk(
        0xFE,
        (
            "Hmm, the characteristics of the village\x01",
            "To have everyone know\x01",
            "It will not be bad anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are interested in it,\x01",
            "The migration to the village may increase, too … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C2")

    Jump("loc_41D9")

    label("loc_39C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E2")
    Jump("loc_3B5D")

    label("loc_39E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F1")
    Jump("loc_3B5D")

    label("loc_39F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A03")
    Jump("loc_3B5D")

    label("loc_3A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD3")

    ChrTalk(
        0xFE,
        "Protect this village called Armorica …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though my purpose was the same, both my son and I\x01",
            "The field of view was too narrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To make it aware this time incident\x01",
            "It was a trial given by the goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B5D")

    label("loc_3AD3")


    ChrTalk(
        0xFE,
        (
            "Protect this village called Armorica …\x01",
            "Both I and my son have the same feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, even words of young people\x01",
            "But I have to listen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B5D")

    Jump("loc_41D9")

    label("loc_3B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7D")
    Jump("loc_3DE0")

    label("loc_3B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8C")
    Jump("loc_3DE0")

    label("loc_3B8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C4F")

    ChrTalk(
        0xFE,
        (
            "Foreigners talking to Derrick …\x01",
            "It smells quite oddly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there is something wrong,\x01",
            "We must deal with it as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You guys, please collect the information.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CCD")

    label("loc_3C4F")


    ChrTalk(
        0xFE,
        (
            "Foreigners talking to Derrick …\x01",
            "If there is something wrong,\x01",
            "We must deal with it as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You guys, please collect the information.\x02",
    )

    CloseMessageWindow()

    label("loc_3CCD")

    Jump("loc_3DE0")

    label("loc_3CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D84")

    ChrTalk(
        0xFE,
        (
            "You guys really had a hard time.\x01",
            "Thanks and good-bye to you\x01",
            "I was able to know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a village head,\x01",
            "Somehow talk to Derrick\x01",
            "Let's persuade it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3DE0")

    label("loc_3D84")


    ChrTalk(
        0xFE,
        (
            "As a village head, as a parent ……\x01",
            "Before doing what Derrick had done earlier,\x01",
            "I have to persuade somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE0")

    Jump("loc_41D9")

    label("loc_3DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3FA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E00")
    Call(0, 9)
    Jump("loc_3F9B")

    label("loc_3E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0F")

    ChrTalk(
        0xFE,
        (
            "It depends on the young people leaving\x01",
            "Accompanied by shortage of workers, activation of trade\x01",
            "Declining food self-sufficiency rate in autonomous state … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although the village has many problems … …\x01",
            "Derek's reform plans are tomorrow\x01",
            "It can not be adopted either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is also the mission of the mayor to protect the tradition of the village.\x01",
            "I would like you to know that … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F9B")

    label("loc_3F0F")


    ChrTalk(
        0xFE,
        (
            "To protect the village tradition is also the mission of the mayor.\x01",
            "Changing is not only good things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Derrick will also be the next village head,\x01",
            "I would like you to know that … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9B")

    Jump("loc_41D9")

    label("loc_3FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_413B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FBB")
    Call(0, 9)
    Jump("loc_4136")

    label("loc_3FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B5")

    ChrTalk(
        0xFE,
        (
            "Becoming blind to reform\x01",
            "As for neglecting the tradition of the village,\x01",
            "It will cause disaster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Derrick thinks for the village\x01",
            "The reasons for reform plans are\x01",
            "I know enough … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The village should have the ideal\x01",
            "In order not to lose sight,\x01",
            "I have to think more carefully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4136")

    label("loc_40B5")


    ChrTalk(
        0xFE,
        (
            "…… Condition of the village, Watashi\x01",
            "I do not think that it is OK as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, the village should have the appearance\x01",
            "In order not to lose sight,\x01",
            "I have to think more carefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4136")

    Jump("loc_41D9")

    label("loc_413B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_41D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4156")
    Call(0, 9)
    Jump("loc_41D9")

    label("loc_4156")


    ChrTalk(
        0xFE,
        (
            "…… This trouble, in the first place\x01",
            "It is a problem that I will solve on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If something happens\x01",
            "Maybe I will ask …\x01",
            "Do not worry now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41D9")

    TalkEnd(0xFE)
    Return()

    # Function_8_2F6F end

    def Function_9_41DD(): pass

    label("Function_9_41DD")


    ChrTalk(
        0xB,
        "Oh, you guys at the Special Affairs Support Division ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FTurta, mayor of the mayor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, activities\x01",
            "I heard that it resumed,\x01",
            "It seems to be a breath, which is the most.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "…… Fuu ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105Fthat……\x01",
            "You seem to be tired somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No, …. Recently, only a little\x01",
            "I am suffering from personal problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, your hands\x01",
            "It is not enough to bother me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FIf such a problem exists\x01",
            "You might as well say …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, what you save\x01",
            "It is poison to your body, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, if we are the Special Support Section\x01",
            "It may be power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hahaha, really.\x01",
            "It's not a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If it really does not work\x01",
            "I might ask you guys,\x01",
            "Do not worry now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so……\x01",
            "I understand.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44C8")

    ChrTalk(
        0x103,
        (
            "#00200FIf something happen\x01",
            "Please contact me anytime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44FC")

    label("loc_44C8")


    ChrTalk(
        0x102,
        (
            "#00100FIf something happen\x01",
            "Please contact us anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44FC")


    ChrTalk(
        0xB,
        (
            "Oh, that time\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 1)
    Return()

    # Function_9_41DD end

    def Function_10_4529(): pass

    label("Function_10_4529")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "Derrick, you gave it out\x01",
            "\"Beekeeping experience event\"\x01",
            "Probably ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although it may be appealing indeed,\x01",
            "Is it alright to put amateurs in the fields?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Of course it is … …\x01",
            "Honey is a specialty in the village,\x01",
            "I do not think it's bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Measures against bees, too,\x01",
            "I guess we can tell it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm, there is room for thought … …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_471C")

    ChrTalk(
        0x101,
        (
            "#00002F(Apparently, the mayor and Derrick are\x01",
            "It seems that I could completely reconcile it. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F(\"It rains and solidifies the earth.\"\x01",
            "Huhu, let 's go bad if you do not get in the way. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BE")

    label("loc_471C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_47BE")

    ChrTalk(
        0x101,
        (
            "#00005F(That, the village head and Derrick san … ….\x01",
            "It seems that I reconciled myself before long. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F(Through the matter of Minnes\x01",
            "It might be something. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BE")

    SetScenarioFlags(0x16F, 6)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_10_4529 end

    def Function_11_47CA(): pass

    label("Function_11_47CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_490B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487D")

    ChrTalk(
        0xFE,
        (
            "Looking at that pale shining big tree,\x01",
            "It makes me feel uneasy …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But my husband and Derrick\x01",
            "I am doing my best.\x01",
            "I have to support you as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4906")

    label("loc_487D")


    ChrTalk(
        0xFE,
        (
            "Not limited to husbands and derricks,\x01",
            "A lot of people are now under this situation\x01",
            "I guess I'm doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not do much,\x01",
            "I have to support you as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4906")

    Jump("loc_550B")

    label("loc_490B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_49C6")

    ChrTalk(
        0xFE,
        (
            "The fact that an invalid declaration of an independent country has been made,\x01",
            "Presence of Dieter President\x01",
            "That justification has been shaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People in Crosbell City,\x01",
            "Sounds confusing, is not it …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_550B")

    label("loc_49C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AD0")

    ChrTalk(
        0xFE,
        (
            "That Arios\x01",
            "I will not become defense minister … …\x01",
            "I still can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this village, to all the hypocriteists\x01",
            "Thank you very much for your help,\x01",
            "I have not heard from you since I started independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am worried … … Everyone,\x01",
            "I wonder what I am doing now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B6F")

    label("loc_4AD0")


    ChrTalk(
        0xFE,
        (
            "In this village, to all the hypocriteists\x01",
            "Thank you very much for your help,\x01",
            "I have not heard from you since I started independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am worried … … Everyone,\x01",
            "I wonder what I am doing now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B6F")

    Jump("loc_550B")

    label("loc_4B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4C0D")

    ChrTalk(
        0xFE,
        (
            "Derricks take the initiative\x01",
            "They are looking around the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also unknown compound\x01",
            "It is said that it has been witnessed,\x01",
            "I want you to be careful …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_550B")

    label("loc_4C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D42")

    ChrTalk(
        0xFE,
        (
            "From yesterday evening, my husband and Derrick\x01",
            "About the new reform plan of the village\x01",
            "We are talking a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just do not change,\x01",
            "By conveying the traditional charm of the village\x01",
            "It seems like trying to regain liveliness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those two hold hands,\x01",
            "Surely Almorica village will be better.\x01",
            "Huhu, I must support it firmly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4DE3")

    label("loc_4D42")


    ChrTalk(
        0xFE,
        (
            "Well, with my husband and Derrick\x01",
            "Shall I make some even in warm cocoa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those two hold hands,\x01",
            "Surely Almorica village will be better.\x01",
            "Huhu, I must support it firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DE3")

    Jump("loc_550B")

    label("loc_4DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F8E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED3")

    ChrTalk(
        0xFE,
        (
            "My husband said Derrick\x01",
            "Harold's place\x01",
            "I'm going to consult him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are already alone\x01",
            "I can not do anything ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh My Goddess,\x01",
            "Please please Almorika village,\x01",
            "Please observe derrick ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F1B")

    label("loc_4ED3")


    ChrTalk(
        0xFE,
        (
            "Oh My Goddess,\x01",
            "Please please Almorika village,\x01",
            "Please observe derrick ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F1B")

    Jump("loc_4F89")

    label("loc_4F20")


    ChrTalk(
        0xFE,
        (
            "My husband and Derrick,\x01",
            "It seems I was able to reconcile.\x01",
            "I was relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone……\x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F89")

    Jump("loc_550B")

    label("loc_4F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_50CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5036")

    ChrTalk(
        0xFE,
        (
            "Recently, Derrick is almost\x01",
            "I have stopped showing my face to my house ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I'm worried.\x01",
            "No way, to be funny\x01",
            "You got involved … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50C5")

    label("loc_5036")


    ChrTalk(
        0xFE,
        (
            "Derrick and Mr. Minnes\x01",
            "I was talking about reform … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, two other relationships\x01",
            "Up to where I can not get back\x01",
            "I wonder if it has come.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C5")

    Jump("loc_550B")

    label("loc_50CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5206")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_519C")

    ChrTalk(
        0xFE,
        (
            "Yesterday's husband and Derrick's argument were\x01",
            "It was the most fierce I have ever had.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both of them became hot,\x01",
            "Me too, at last.#2RIsasa#I can not get it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haa …… How do you two\x01",
            "I wonder if it can be reconciled.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5201")

    label("loc_519C")


    ChrTalk(
        0xFE,
        (
            "Ha\x01",
            "How can Derrick and her husband\x01",
            "I wonder if it can be reconciled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To me,\x01",
            "What should I do ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5201")

    Jump("loc_550B")

    label("loc_5206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52EC")

    ChrTalk(
        0xFE,
        (
            "Husband and Derrick's argument,\x01",
            "It is becoming fierce day by day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Always I managed to take the place\x01",
            "Although it is contained, it also gradually\x01",
            "I am getting out of hand … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm worried.\x01",
            "If it does not become worse further\x01",
            "It's fine, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5361")

    label("loc_52EC")


    ChrTalk(
        0xFE,
        (
            "Husband and Derrick's argument,\x01",
            "It is becoming fierce day by day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm worried.\x01",
            "If it does not become worse further\x01",
            "It's fine, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5361")

    Jump("loc_550B")

    label("loc_5366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_550B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5475")

    ChrTalk(
        0xFE,
        (
            "Recently, husband and Derrick\x01",
            "On the future of Almorika village\x01",
            "I'm arguing everyday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is good in itself,\x01",
            "Because I will not yield one step either way\x01",
            "Always got a quarrel … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way parent-child relationship\x01",
            "It just gets worse.\x01",
            "Hah, my head hurts …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_550B")

    label("loc_5475")


    ChrTalk(
        0xFE,
        (
            "For the village, my husband and son\x01",
            "Discussion itself is\x01",
            "I think it's a good thing ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both of us are stubborn,\x01",
            "There is no indication that the settlement will arrive at all.\x01",
            "Hah, my head hurts …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550B")

    TalkEnd(0xFE)
    Return()

    # Function_11_47CA end

    def Function_12_550F(): pass

    label("Function_12_550F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_56C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552D")
    Call(0, 13)
    Jump("loc_56BF")

    label("loc_552D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5623")

    ChrTalk(
        0xFE,
        (
            "To the emergence of that huge tree,\x01",
            "The villagers also got quite anxious\x01",
            "It seems to be feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although the president was detained,\x01",
            "The problem of \"eidolon\" of blue flowers and highways\x01",
            "It has not been settled yet …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continuing to the villagers,\x01",
            "I will call for attention\x01",
            "It seems necessary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_56BF")

    label("loc_5623")


    ChrTalk(
        0xFE,
        (
            "Although the president was detained,\x01",
            "The problem of \"eidolon\" of blue flowers and highways\x01",
            "It has not been settled yet …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continuing to the villagers,\x01",
            "I will call for attention\x01",
            "It seems necessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56BF")

    Jump("loc_58EE")

    label("loc_56C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_56D2")
    Jump("loc_58EE")

    label("loc_56D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_56E0")
    Jump("loc_58EE")

    label("loc_56E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_56EE")
    Jump("loc_58EE")

    label("loc_56EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5709")
    Call(0, 10)
    Jump("loc_5773")

    label("loc_5709")


    ChrTalk(
        0xFE,
        (
            "…… Hmm, what my father says\x01",
            "It is reasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, I will make this plan a little more\x01",
            "I should look for it if you dig into it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5773")

    Jump("loc_58EE")

    label("loc_5778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_58EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5793")
    Jump("loc_58EE")

    label("loc_5793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_587A")

    ChrTalk(
        0xFE,
        (
            "I have a village problem alone\x01",
            "I tried to solve it.\x01",
            "It was a mistake in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this case, my own\x01",
            "I knew the shallowness of thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on with my father ……\x01",
            "No, together with all the residents\x01",
            "I have to think about the village.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_58EE")

    label("loc_587A")


    ChrTalk(
        0xFE,
        (
            "In this case, my own\x01",
            "I knew the shallowness of thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on all the residents\x01",
            "I have to think about the village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58EE")

    TalkEnd(0xFE)
    Return()

    # Function_12_550F end

    def Function_13_58F2(): pass

    label("Function_13_58F2")

    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "To the extent that such things happen,\x01",
            "Everyone did not expect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Developed as a trade city,\x01",
            "Forcibly take the form of independence\x01",
            "Influence the whole continent ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Then, ignoring the tradition,\x01",
            "I have been evolving too rapidly\x01",
            "Perhaps the shaking back came now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… However, please accept it\x01",
            "Is not it different to accept?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If this is the trial given by the goddess,\x01",
            "Whether we can overcome it ……\x01",
            "I think that it is tried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "…… Well, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Whew, too lazily\x01",
            "A stiff way of thinking\x01",
            "Maybe it should be revised.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 4)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_13_58F2 end

    def Function_14_5B16(): pass

    label("Function_14_5B16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5B27")
    Jump("loc_5C0D")

    label("loc_5B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5BCC")

    ChrTalk(
        0xFE,
        (
            "I bought a new type of power car bought from Mr. Minnes\x01",
            "I'm asked by the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will finish in a few days\x01",
            "I was talking … ….\x01",
            "Haha, I wish I could come back soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C0D")

    label("loc_5BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5BDA")
    Jump("loc_5C0D")

    label("loc_5BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5BE8")
    Jump("loc_5C0D")

    label("loc_5BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5BF6")
    Jump("loc_5C0D")

    label("loc_5BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5C04")
    Jump("loc_5C0D")

    label("loc_5C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5C0D")

    label("loc_5C0D")

    TalkEnd(0xFE)
    Return()

    # Function_14_5B16 end

    def Function_15_5C11(): pass

    label("Function_15_5C11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C36")
    Call(0, 19)
    Return()

    label("loc_5C36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5C47")
    Jump("loc_60EE")

    label("loc_5C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5DA5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C62")
    Jump("loc_5DA0")

    label("loc_5C62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C74")
    Jump("loc_5DA0")

    label("loc_5C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2A")

    ChrTalk(
        0xF,
        (
            "#03603FThis time really\x01",
            "Thank you very much.\x02\x03",
            "#03600FThanks to Derrick with you\x01",
            "The mayor was also able to settle.\x02\x03",
            "#03609FHuhuh, for all of you\x01",
            "It was a correct answer after consultation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5DA0")

    label("loc_5D2A")


    ChrTalk(
        0xF,
        (
            "#03603FThanks to Derrick with you\x01",
            "The mayor was also able to settle.\x02\x03",
            "#03609FHuhuh, for all of you\x01",
            "It was a correct answer after consultation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DA0")

    Jump("loc_60EE")

    label("loc_5DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_60EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EBE")

    ChrTalk(
        0xF,
        (
            "#03603FWith Derrick, in dealings with the village\x01",
            "I face many times over and over,\x01",
            "He is a polite and serious young man.\x02\x03",
            "#03608FSuch being caught up in something\x01",
            "If so, I can not leave it alone.\x02\x03",
            "#03601FEveryone, certainly valuable information\x01",
            "Please get it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5F4E")

    label("loc_5EBE")


    ChrTalk(
        0xF,
        (
            "#03608FDerrick is caught up in something\x01",
            "If so, I can not leave it alone.\x02\x03",
            "#03601FEveryone, certainly valuable information\x01",
            "Please get it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F4E")

    Jump("loc_60EE")

    label("loc_5F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6064")

    ChrTalk(
        0xF,
        (
            "#03608FThe real intention of a man named Minneshi\x01",
            "I do not know at the moment … …\x02\x03",
            "#03603FRegarding this matter, I and the village mayor\x01",
            "I think that I will proceed with caution.\x02\x03",
            "#03600FEveryone, get on a consultation\x01",
            "Thank you very much.\x02\x03",
            "If there is something again\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_60EE")

    label("loc_6064")


    ChrTalk(
        0xF,
        (
            "#03603FRegarding this matter, I and the village mayor\x01",
            "I think that I will proceed with caution.\x02\x03",
            "#03600FEveryone, if there is something again\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60EE")

    TalkEnd(0xFE)
    Return()

    # Function_15_5C11 end

    def Function_16_60F2(): pass

    label("Function_16_60F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61CD")

    ChrTalk(
        0xFE,
        (
            "Mr. Ian said that the draft constitution\x01",
            "Inevitable in relation to the creation\x01",
            "I could not come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it seems that it resolved successfully,\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From my side to the teacher\x01",
            "I will tell you the end.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6239")

    label("loc_61CD")


    ChrTalk(
        0xFE,
        (
            "It seems I solved it safely,\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From my side to the teacher\x01",
            "I will tell you the end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6239")

    TalkEnd(0xFE)
    Return()

    # Function_16_60F2 end

    def Function_17_623D(): pass

    label("Function_17_623D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62BD")

    ChrTalk(
        0xFE,
        (
            "…… That small alum,\x01",
            "He said that he was becoming so respectable … …\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    ChrTalk(
        0xFE,
        "………… Gusut … … … …\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x12, 0x10)
    SetScenarioFlags(0x1, 1)
    Jump("loc_62D9")

    label("loc_62BD")


    ChrTalk(
        0xFE,
        "………… Gusut … … … …\x02",
    )

    CloseMessageWindow()

    label("loc_62D9")

    TalkEnd(0xFE)
    Return()

    # Function_17_623D end

    def Function_18_62DD(): pass

    label("Function_18_62DD")

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
            "#11P─ ─ I see.\x01",
            "Was there such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PFirst, with that wolf\x01",
            "When I call on you\x01",
            "I thought I'd get out my back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PS-sorry\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#5P#3CHmm, apparently my\x01",
            "It seems that there was lack of consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PNo, no, to the legendary god warrior\x01",
            "That's why you are looking at me\x01",
            "It is an honor's arrival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PIn the village is a \"defense army\" and\x01",
            "It almost never comes … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAs long as you like staying\x01",
            "Let's be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PThank you so much\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#6PThat really helps\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PBut even at the hospital\x01",
            "There were a lot of critical people … …\x02\x03",
            "#10401FHere too, President Dieter\x01",
            "It seems that reputation is not very good, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PWell … Originally this village\x01",
            "You are a thin person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PEven if it is said that it is \"an independent country\"\x01",
            "It comes with pins at all … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PBecause of the example \"Phantom Beast\" appeared\x01",
            "Crop harvest is also depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PEven so, sometimes the defense forces and others\x01",
            "It corresponds to the extent that it comes to patrolling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#6PThey're too much\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3CA town village is surrounded by people in the city#4RMurmur#To\x01",
            "It is not something we do not care about … …\x02\x03",
            "#01201FHowever,\x01",
            "It seems that you are going too far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PWell …… I am also honest,\x01",
            "I feel something I can not attach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PHowever, influence of this village etc.\x01",
            "Compared to the population of Crossbell City\x01",
            "Something like nothing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PTo be honest, what happened\x01",
            "I thought I was thinking about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10408F#12PHmm. I see\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5PAbout \"phantom beast\"\x01",
            "Please also take care.\x02\x03",
            "#00001FBesides that, recently in\x01",
            "Is there anything in trouble?\x02\x03",
            "The village's security and atmosphere\x01",
            "I wonder if it is getting worse ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PNo, fortunately\x01",
            "It has not reached so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PNow cooperate with the whole village\x01",
            "In order to survive this difficulty\x01",
            "I am doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PHarold's family also\x01",
            "I am cooperating with you.\x02",
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
        "#00005F#5PHarold?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 0)), scpexpr(EXPR_END)), "loc_6B6D")

    ChrTalk(
        0x103,
        (
            "#00208F#6Pby the way……\x01",
            "When going out to see family\x01",
            "Like I was saying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B9E")

    label("loc_6B6D")


    ChrTalk(
        0x103,
        (
            "#00205F#6PHere at home\x01",
            "Are you coming?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B9E")


    ChrTalk(
        0xB,
        (
            "#11PWell, just when the strange happened,\x01",
            "I came to visit my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PImmediately thereafter\x01",
            "Because restricted movement of the highway was issued\x01",
            "It is staying as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#5PIs that right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PIf it is Harold's family\x01",
            "I am staying on the second floor of the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PIt would be good to go see him if you like\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYes, understood\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400F#12PLet's go pay him a visit\x02",
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

    # Function_18_62DD end

    def Function_19_6D6F(): pass

    label("Function_19_6D6F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7204")

    ChrTalk(
        0xB,
        (
            "Fuu …\x01",
            "Derrick's guy,\x01",
            "What on earth are you doing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FMakes you worry, right……\x01",
            "Perhaps he is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMayor Torta, Hello.\x01",
            "It is a person of the Special Affairs Support Division ……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FIs that … Harold?\x02",
    )

    CloseMessageWindow()

    def lambda_6F14():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F14)
    Sleep(50)

    def lambda_6F24():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F24)
    Sleep(50)

    def lambda_6F34():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6F34)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "Oh, you guys ……\x01",
            "I was waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FYou came to see the request.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, yeah ….\x02\x03",
            "#00005FBut, Mr. Harold\x01",
            "Why here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, in fact …\x01",
            "About this case\x01",
            "He has something to do with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FAfter discussing with the village chief,\x01",
            "I decided to consult with everyone.\x02\x03",
            "#03601FAnything, circumstances are circumstances.\x01",
            "This is for the pros of the investigation\x01",
            "I thought it would be better to order.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00101FIt seems very serious\x01",
            "It looks like circumstances.\x02\x03",
            "#00103FTo the son of the mayor\x01",
            "It looks like a related story, but ….\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7166():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7166)
    Sleep(50)

    def lambda_7176():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7176)
    Sleep(50)

    def lambda_7186():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7186)
    Sleep(300)

    ChrTalk(
        0xB,
        "Well, it's a little crowded.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you can accept it\x01",
            "I will tell you in detail … …\x01",
            "Is time okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7270")

    label("loc_7204")

    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        "Oh, have you got time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you accept the request\x01",
            "I will tell you in detail … …\x01",
            "Are you OK?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7270")

    Call(0, 20)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -41050, 0, -1950, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_19_6D6F end

    def Function_20_729F(): pass

    label("Function_20_729F")

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
            "【undertake】\x01",              # 0
            "【Not ready】\x01",      # 1
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
        (0, "loc_7315"),
        (1, "loc_731D"),
        (SWITCH_DEFAULT, "loc_73E4"),
    )


    label("loc_7315")

    Call(0, 21)
    Jump("loc_73E4")

    label("loc_731D")


    ChrTalk(
        0x101,
        (
            "#00006FI'm sorry……\x01",
            "I am a little busy now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "No … No …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Then, when time comes\x01",
            "Please come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By all means to you guys\x01",
            "I'd like you to lend me the power.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x173, 7)
    Jump("loc_73E4")

    label("loc_73E4")

    Return()

    # Function_20_729F end

    def Function_21_73E5(): pass

    label("Function_21_73E5")


    ChrTalk(
        0x101,
        (
            "#00000FYes, it's okay.\x01",
            "Please let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Oh, I will wear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, recently, my son\x01",
            "The state of derrick is strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Do something unthinkable behind the scenes\x01",
            "It seems like I am planning to do so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FIs it unfathomable?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I do not know the details … …\x01",
            "Anyway I can not read my thoughts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In the meantime, for example, Mr. Harold\x01",
            "\"I want to withhold future transactions\"\x01",
            "It seems to have offered that.\x02",
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
            "#00005FTransaction … ….\x01",
            "Why did you suddenly do such a thing?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FSure, Ms. Harold\x01",
            "Friendly with Almorika village\x01",
            "It should have been a relationship …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03608FYeah, I have a long time ago\x01",
            "I was allowed to do\x01",
            "I intended to do it … …\x02\x03",
            "#03601FSo, something for myself\x01",
            "I thought there was a non-existence\x01",
            "I asked the village mayor the reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FIf you ask,\x01",
            "Hold it to the village mayor at all\x01",
            "It was a story I did not remember ……\x02\x03",
            "#10300FIn other words, is that something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well done …\x01",
            "It is hard for Harold.\x01",
            "I have worked rude.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "He loses a good business partner\x01",
            "A considerable pain for the village … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I do not understand it My son\x01",
            "It should not be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIt is certainly incomprehensible …\x02\x03",
            "#00101FTo my son\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, I think so too\x01",
            "With Mr. Harold\x01",
            "I studied it variously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Then …\x01",
            "A certain unknown person\x01",
            "It is emerging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Recently, Ayatsu\x01",
            "With a suspicious alien\x01",
            "You seem to be meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FForeigner ……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FToo much detail\x01",
            "I do not know but …\x02\x03",
            "#03601FHowever, with Derrick\x01",
            "Discussing something inside\x01",
            "It seems to be doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FWell … well,\x01",
            "It certainly smells strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "So, to you\x01",
            "About that foreigner\x01",
            "I would like you to investigate in detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If there is something wrong,\x01",
            "I have to deal with it urgently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FExcuse me……\x01",
            "Take the time to deal with us this time\x01",
            "You do not even need to ask?\x02\x03",
            "#00200FDirectly told by my son\x01",
            "It should be the most reasonable … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FHey, Tio Suki ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "… … no, shy\x01",
            "It is as your daughter is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To tell the truth, the old son and the son\x01",
            "About the way the village is located\x01",
            "Do not repeat the collision …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I also heard the situation about this,\x01",
            "You answered nothing after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "It is a miserable story as a father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FSuch a thing ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Anyway, I understood the story.\x01",
            "I will respond to the investigation immediately.\x02\x03",
            "#00000FTo the people of the village for the beginning\x01",
            "I would like to hear it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Oh, I will ask you a favor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, Derrick is now\x01",
            "Together with young man Elkin\x01",
            "I am going to the delivery of crops to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Listening to the principal is\x01",
            "You should postpone it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FEveryone, certainly valuable information\x01",
            "Please get it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00000FWell, please leave it to me.\x02",
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
            "Quest 【Survey of suspicious person】\x07\x00",
            "I started!\x02",
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

    # Function_21_73E5 end

    def Function_22_7E8B(): pass

    label("Function_22_7E8B")

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
            "#00003FUm, I asked a little.\x01",
            "I'd like to ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Recently I am visiting the village\x01",
            "I asked about foreigners.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        "Oh, is that person?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh yeah … … If we are to say strongly,\x01",
            "It's a pretty good person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FWell done … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, once our children\x01",
            "I got through the playing beat\x01",
            "I have defiled his clothes … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Not only do not mind,\x01",
            "Kindly also sweets\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, I feel sorry\x01",
            "With an impressed person\x01",
            "I got a sigh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see……\x01",
            "Thanks for your cooperation.\x02",
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

    # Function_22_7E8B end

    def Function_23_819B(): pass

    label("Function_23_819B")

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
            "No way ….\x01",
            "The man named Mineness,\x01",
            "It was said that he was a quincy company … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And …\x01",
            "\"Almorica · Honey company\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03605FFactory in private estate ……\x01",
            "A large-scale plan to that extent\x01",
            "What is it that he was ahead …?\x02\x03",
            "#03608FThat Derrick,\x01",
            "Such a thing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005Fthat……\x01",
            "By the way, Mr. Derrick?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAh … well.\x01",
            "I can not see her … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWhen you get in at the hotel,\x01",
            "You said you were going back to the village?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well … actually, recently,\x01",
            "Do not stay too much at home\x01",
            "It has become.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Recently in \"Tonelico Tei\"\x01",
            "It seems that he is renting a room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Man also called Minnes\x01",
            "It seems that he was visiting the inn,\x01",
            "It may have moved because of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks to plans to build a factory in private property,\x01",
            "I could not notice as much as hair.\x01",
            "… … It is a miserable story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F…… I do not know what that is.\x02\x03",
            "#10300FUnexpectedly, being brought up by merchants\x01",
            "You might have moved.\x02\x03",
            "#10304FTo make it difficult for the village head to receive information.\x02",
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
        "Well, what does that mean …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell, from here\x01",
            "The leader will explain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWell … oh well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03605FMr. Lloyd,\x01",
            "Even if you are interested\x01",
            "Is it there?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F── To the last, our\x01",
            "It's like kan … ….\x02\x03",
            "#00001FTo the man named Minnes,\x01",
            "There are doubtful points.\x02",
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
        "What about you …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FThe plan he said,\x01",
            "Everyone who participated\x01",
            "I was able to earn profits.\x02\x03",
            "#00003FAlmorika village has acquired a new industry,\x01",
            "Quincy Company has a prospect in the future\x01",
            "You will get a subsidiary.\x02\x03",
            "#00008FTo be convincingly seemingly\x01",
            "His story is visible ……\x02\x03",
            "#00001FHow talk is too good.\x01",
            "… … Do not you think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03605F……!\x01",
            "Well, as I said, …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FBesides, Mr. Minnes\x01",
            "New type power track\x01",
            "I give it cheaply.\x02\x03",
            "#00200FThis is so-\x01",
            "Both \"upfront investment\"\x01",
            "I think you can see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FAs for the new model of the powertrain,\x01",
            "It is still expensive\x01",
            "There is no mistake … …\x02\x03",
            "#10101FTo be truly transferred to 50,000 mirrors,\x01",
            "I feel that it is too inconspicuous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FIn other words, in other words …\x02\x03",
            "#00301FAlways be able to collect the price\x01",
            "There is a \"prospect\"\x01",
            "It is going to be decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03601Fthat is……\x01",
            "It certainly is strange.\x02\x03",
            "#03603FIf you are a big company like Quincy\x01",
            "Cost-intensive projects\x01",
            "We can not move forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Fufu, huh, is that so ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Somehow it smells quiet\x01",
            "It came to me ……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001FTo Mr. Minnes, something different … …\x01",
            "Or surely profitable Ate\x01",
            "It may be there.\x02\x03",
            "#00003FI do not have any evidence … …\x01",
            "Just to be sure, those who kept in mind\x01",
            "I think it's good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well …\x01",
            "Let's be careful with care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……Now,\x01",
            "It was a hard time,\x01",
            "Municipal office workers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks quite\x01",
            "I was able to organize the situation.\x01",
            "I will reward you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, that's fine, but ….\x02\x03",
            "#00005FIs that okay?\x01",
            "If anything, continue the investigation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "No … … It's fine for a while now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As for the private property of the village,\x01",
            "Plan to build a selfish plant\x01",
            "There is no way to admit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As a village head,\x01",
            "Somehow talk to Derrick\x01",
            "Let's persuade it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F…… That might be nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThen, we\x01",
            "Excuse me.\x02\x03",
            "#00000FIf there is something again\x01",
            "Please call me at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, that time\x01",
            "Let's say hello well.\x02",
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
            "Quest 【Survey of suspicious person】\x07\x00",
            "Achieved!\x02",
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

    # Function_23_819B end

    def Function_24_8F2D(): pass

    label("Function_24_8F2D")

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
        "You guys did a good job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks, that person\x01",
            "From a fraudster's devil hand\x01",
            "The village was saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FEventually the murderer missed out\x01",
            "I should have ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FBut even in the police headquarters\x01",
            "I could report it … ….\x02\x03",
            "#00100FIt is a matter of time to get caught\x01",
            "I wonder if.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#03605FDerrick, you?\x02",
    )

    CloseMessageWindow()

    def lambda_919D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_919D)
    Sleep(50)

    def lambda_91AD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_91AD)
    Sleep(50)

    ChrTalk(
        0xD,
        (
            "…… To everyone,\x01",
            "It really bothered me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I am a fraud\x01",
            "Just as I got stuck,\x01",
            "To the situation so far ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108FSuch a thing, because of you ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Disagreeable……\x01",
            "Everything is my responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "With reform, reform and jockey,\x01",
            "Sticking to my father … …\x01",
            "Results These are different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To me I am the next village head\x01",
            "I do not have any qualifications.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        "…… There is not such a thing.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        "father……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm just conservative thought\x01",
            "Stick and talk about your story\x01",
            "I did not even listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The village is no good at this rate\x01",
            "Knowing that it will become,\x01",
            "I did not do anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Regarding this case\x01",
            "My responsibility will be great, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#03608FMayor of the village ……\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Through this case\x01",
            "I thought so often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To protect the village\x01",
            "To the thought of one individual\x01",
            "You should not stick to it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Derrick ……\x01",
            "From now on,\x01",
            "I want you to lend your wisdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Meet each other,\x01",
            "Discuss with all the villagers ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This village named Armorica\x01",
            "Let's protect it, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "… Ah, that's right.\x01",
            "I'm sorry, my dad … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Besides, more than ever\x01",
            "Thinking about the village\x01",
            "I will decide to live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWhatching\x01",
            "It seems I was able to reconcile.\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHaha, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, if it's like this\x01",
            "It was also a scam\x01",
            "Was not it bad?\x02",
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

    def lambda_973F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_973F)
    Sleep(50)

    def lambda_974F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_974F)
    Sleep(50)

    def lambda_975F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_975F)
    Sleep(50)

    def lambda_976F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_976F)
    Sleep(50)

    def lambda_977F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_977F)
    Sleep(50)

    def lambda_978F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_978F)
    Sleep(50)

    def lambda_979F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_979F)
    Sleep(50)

    def lambda_97AF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_97AF)
    Sleep(50)

    def lambda_97BF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_97BF)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10106FWow, Wazi ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHmm, things say good …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, no,\x01",
            "Because it is truly unscrupulous.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        "And anyway … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To you really\x01",
            "I am indebted to you.\x01",
            "I want you to repeat and thank you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_98B5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98B5)
    Sleep(50)

    def lambda_98C5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_98C5)
    Sleep(50)

    def lambda_98D5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_98D5)
    Sleep(50)

    def lambda_98E5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_98E5)
    Sleep(50)

    def lambda_98F5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_98F5)
    Sleep(50)

    def lambda_9905():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9905)
    Sleep(50)

    def lambda_9915():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9915)
    Sleep(50)

    def lambda_9925():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9925)
    Sleep(50)

    def lambda_9935():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9935)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "To Mr. Ian,\x01",
            "I have to say thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "From my side to the teacher\x01",
            "I will tell you the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03604FI, even a little to solve the case\x01",
            "It was good to serve you.\x02\x03",
            "#03600FFrom now on\x01",
            "Thank you, Mr. Mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Haha, this is true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAs a precaution, to that fraudster\x01",
            "Please be careful enough.\x02\x03",
            "#00000FIf there is something again,\x01",
            "Please contact the support department at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, I beg you to do my best.\x01",
            "Thank you so much.\x02",
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
            "Quest 【Investigation of suspicious merchant】\x07\x00",
            "Achieved!\x02",
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

    # Function_24_8F2D end

    def Function_25_9BFB(): pass

    label("Function_25_9BFB")

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
        "#00000FMayor Torta, Hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, those of the Special Affairs Support Division.\x01",
            "What on earth are you for today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FActually, to the village headman\x01",
            "What you want to ask\x01",
            "I have …\x02\x03",
            "#00003FTo the barn at the beekeeping place,\x01",
            "Have someone lived in?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Hmm, certainly now there\x01",
            "I am letting people stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Did you talk about three or four days ago?\x01",
            "\"Please hurt for a while\"\x01",
            "Suddenly asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Certainly … name ……\x01",
            "It is called Guébal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAfter all …!\x02\x03",
            "#00106FBut why to a barn?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Once, why should I take an accommodation\x01",
            "Did you say that …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "\"A place that is not noticeable is as good as possible\"\x01",
            "I heard what they say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I do not say anything after listening to the circumstances,\x01",
            "I'm caught up in so much importance\x01",
            "I thought that it was because … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No way, it's okay\x01",
            "He seemed to be a searcher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, something of a case\x01",
            "Are you the culprit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FNo, that's why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FTo Mr. Lloyd, to the mayor\x01",
            "Those who talk\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FOh, I see. …\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd requested by Alm and Airy\x01",
            "I explained the circumstances of searching for Gebal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "Hmm, I see.\x01",
            "You were a former lawmaker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oita before to escape allegations of tax evasion\x01",
            "Congressman who was hospitalized with sick disease ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It is said in the Crossbell Times\x01",
            "It feels like I saw the face I saw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, this time\x01",
            "It looks like it is not directly related.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMayor Torta is in the barn\x01",
            "Would you let me talk with Mr. Gebal?\x02\x03",
            "#00008FHe asked Almus\x01",
            "I do not want to see you, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "… … Well, OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I had a feud with my son,\x01",
            "After all it is not enough dialogue\x01",
            "It was the cause of anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The same#2RIron#To others\x01",
            "There is not a tricky step.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FMayor of the village ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hehuu, follow me.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_9BFB end

    def Function_26_A31F(): pass

    label("Function_26_A31F")

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
            "#00000FMr. Gebal … … is not it?\x02\x03",
            "#00006FFinally, I finally found it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#4PHun …\x01",
            "It is hard work and enthusiasm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PMy son and couple\x01",
            "She seems to be looking for me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PWhatever I am told\x01",
            "I will not see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWhy, why so stubborn …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4P…… Of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PMy son … …. Alum,\x01",
            "To have a grudge against me\x01",
            "It is no different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FI am grudging … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301Fif you can,\x01",
            "Can you tell me more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4P…… From the apprentices' apprenticeship era,\x01",
            "I have handled various corruption.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PWork only for status and honor, Mira,\x01",
            "I did not try to look after my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PAs such, my wife feels dissatisfied,\x01",
            "By concentrating on young Alm's childcare\x01",
            "I tried to confuse it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PAnd I took the picture more and more,\x01",
            "One day … as a child,\x01",
            "I have done something I should not do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PIn the gaps where my wife went out, on his own mansion\x01",
            "It invited mistress of those days.\x02",
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
        "#10106FWell, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FI feel like I'm doing it … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PAfter a while it became a place where my wife knew,\x01",
            "The wife who finally got the idea\x01",
            "I took Alm to return home to Ribeire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PI do not know anything after that … …\x01",
            "By divorce, both my wife and Alum\x01",
            "It must have caused a lot of painful feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PBut I wonder\x01",
            "I felt a sense of resistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PDivorce report was officially accepted\x01",
            "The next day, on the widened mansion\x01",
            "I was inviting another mistress … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FWell, hmm … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FIt is true, even if it is grudged\x01",
            "It is a kind of unlikely action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F…… Randy,\x01",
            "Or rather to straight out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PHun, as the redhead there,\x01",
            "I can not help being a grudge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PAlso, after all,\x01",
            "It is a man who was former chairman of Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PHowever, boring tax evasion etc.\x01",
            "Because I committed it to the former chairman\x01",
            "It is cut off to the tail easily ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PI had been arrested all the time\x01",
            "It was comfortably, ironically\x01",
            "I just finished with a loss of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4PThe body that lost this everything\x01",
            "There is no such thing as exposing it to my son ……\x01",
            "I can not bear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Gabal … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FWas that something like that …?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00001F……that.\x01",
            "Is it all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4P……What is it?\x01",
            "No matter what you say now ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Certainly you are,\x01",
            "To my son and his wife\x01",
            "It may have been a terrible thing.\x02\x03",
            "As an evil politician,\x01",
            "There are also things that are dark behind various\x01",
            "It may have come.\x02\x03",
            "#00000FBut, as for the words of the previous days,\x01",
            "I heard Gaebal's confession.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F… That's right.\x02\x03",
            "#00100FI can fully see the reflection heart,\x01",
            "Even in terms of society you already\x01",
            "I am sanctioned.\x02\x03",
            "#00108FI do not see you from feeling guilty is\x01",
            "It might not pass too much …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4PWell, but …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003Fin addition……\x02\x03",
            "#00002FI will never have that alm\x01",
            "I do not think that I am harassing you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4P……Huh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWe search for Gaebal's search\x01",
            "With Mr. Alm who was asking,\x01",
            "Mrs. Airy, his wife … …\x02\x03",
            "#00002FThey are building a warm family,\x01",
            "I seemed very happy.\x02\x03",
            "In the meantime, Mr. Alm who asked me\x01",
            "One desire to speak … one …\x02\x03",
            "#00004F\"Show me your child I was born,\x01",
            "Having a happy family built\x01",
            "I just wanted to report \".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4P……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha, that's right.\x02\x03",
            "#10106FAbout to be ate\x01",
            "I love to love you … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FWell, even with a small amount of \"resentment\"\x01",
            "If I have a dark feeling\x01",
            "I can not have such expression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHuh, how about you?\x02\x03",
            "#10304FWhen it comes to my poker face\x01",
            "I guess that it will be a bad thing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00211F… … Wasan,\x01",
            "Please do not mix.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, anyway.\x01",
            "Mr. Gebal, your son is\x01",
            "It means that I could grow brightly.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00004F…… That's all I can say from us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHow is it …?\x01",
            "After all, to Alums\x01",
            "Would you please meet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4P…………………………\x02",
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
            "#4P…… If it says that … …\x01",
            "You do not have to see me.\x02",
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
        "#00005FIs it true?\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x12,
        "#4PHun, what are you going to do when you say a lie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4P…… Look, my mind does not change\x01",
            "Why do not you call it quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FI understand.\x01",
            "Well then I will call you soon!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 35)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 36)
    Sleep(300)
    OP_68(76460, 1500, -1540, 2000)
    BeginChrThread(0x101, 3, 0, 34)

    def lambda_B52D():

        label("loc_B52D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B52D")

    QueueWorkItem2(0x102, 1, lambda_B52D)
    Sleep(50)

    def lambda_B542():

        label("loc_B542")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B542")

    QueueWorkItem2(0x103, 1, lambda_B542)
    Sleep(50)

    def lambda_B557():

        label("loc_B557")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B557")

    QueueWorkItem2(0x104, 1, lambda_B557)
    Sleep(50)

    def lambda_B56C():

        label("loc_B56C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B56C")

    QueueWorkItem2(0x109, 1, lambda_B56C)
    Sleep(50)

    def lambda_B581():

        label("loc_B581")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B581")

    QueueWorkItem2(0x105, 1, lambda_B581)
    Sleep(50)

    def lambda_B596():

        label("loc_B596")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B596")

    QueueWorkItem2(0xB, 1, lambda_B596)
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
            "Thus Lloyd\x01",
            "Hurry up and contact the \"Ryuujiro\".\x02\x03",
            "Alm and Airy\x01",
            "I called it to Almorika village.\x02\x03",
            "And for the gheba, let me get ready for the mind\x01",
            "They all had to wait for them outside the barn.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_A31F end

    def Function_27_B6A5(): pass

    label("Function_27_B6A5")


    def lambda_B6AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B6AA)

    def lambda_B6BB():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B6BB)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 75280, 0, 270, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_27_B6A5 end

    def Function_28_B6F0(): pass

    label("Function_28_B6F0")


    def lambda_B6F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B6F5)

    def lambda_B706():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B706)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 76460, 0, 280, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_28_B6F0 end

    def Function_29_B73B(): pass

    label("Function_29_B73B")


    def lambda_B740():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B740)

    def lambda_B751():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B751)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 75260, 0, -920, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_29_B73B end

    def Function_30_B786(): pass

    label("Function_30_B786")


    def lambda_B78B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B78B)

    def lambda_B79C():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B79C)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 76470, 0, -920, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_30_B786 end

    def Function_31_B7D1(): pass

    label("Function_31_B7D1")


    def lambda_B7D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B7D6)

    def lambda_B7E7():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B7E7)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 75210, 0, -2040, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_31_B7D1 end

    def Function_32_B81C(): pass

    label("Function_32_B81C")


    def lambda_B821():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B821)

    def lambda_B832():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B832)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 76180, 0, -2040, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_32_B81C end

    def Function_33_B867(): pass

    label("Function_33_B867")


    def lambda_B86C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_B86C)

    def lambda_B87D():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B87D)
    WaitChrThread(0xB, 1)
    OP_95(0xB, 77380, 0, -2650, 2000, 0x0)
    OP_95(0xB, 77640, 0, -310, 2000, 0x0)
    OP_93(0xB, 0x13B, 0x1F4)
    Return()

    # Function_33_B867 end

    def Function_34_B8C6(): pass

    label("Function_34_B8C6")


    def lambda_B8CB():
        OP_95(0xFE, 75070, 0, -5420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B8CB)
    Sleep(1000)

    def lambda_B8E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B8E8)
    Return()

    # Function_34_B8C6 end

    def Function_35_B8F5(): pass

    label("Function_35_B8F5")

    OP_93(0x103, 0x5A, 0x0)
    OP_9B(0x1, 0x103, 0xB4, 0x1F4, 0x7D0, 0x0)
    Return()

    # Function_35_B8F5 end

    def Function_36_B90C(): pass

    label("Function_36_B90C")

    OP_93(0x109, 0x5A, 0x0)
    OP_9B(0x1, 0x109, 0xB4, 0x2EE, 0x7D0, 0x0)
    Return()

    # Function_36_B90C end

    def Function_37_B923(): pass

    label("Function_37_B923")

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
        "Ah……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Did you mean …… Dad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Haha, it's been a long time.\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x12,
        "Um …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Hime, it's been a while, Alm.\x01",
            "About 15 years ago ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "And there …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Hello, Nice to meet you, my father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It is Alm 's wife, Airy.\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Well, yes ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "My son is so pretty\x01",
            "To be with your daughter is that,\x01",
            "My nose is also expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Well, my father-in-law … …\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x12,
        "Ah…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "…, that is … …\x01",
            "What is holding that arm … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Huh, our children.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "…… Almin,\x01",
            "Greeting to my grandpa?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x14,
        "baby",
        "Bubba.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Oh, okay, good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "…………, は は …………\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        (
            "Well, that … … Alm.\x01",
            "To you and mother,\x01",
            "Variety and painful thoughts ……\x02",
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
        "Er … What kind of thing?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "From such a thing, look at your father.\x01",
            "If this eyes of Armin went through … …\x01",
            "It's as beautiful as a blue rock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Airy …\x01",
            "Beautiful like a blue sky\x01",
            "It looks exactly like your eyes.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "Oh, if it says that, Alum …\x01",
            "Ear shape of Armin\x01",
            "It's filled with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Uhufu …\x01",
            "Watching and Capri\x01",
            "I want to eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oh Airy ……\x01",
            "I will not let this child with you forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Almu …\x01",
            "Let's be happy forever.\x02",
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
        "………… Guru …………\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BF3A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BF3A)
    Sleep(50)

    def lambda_BF4A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BF4A)
    Sleep(300)

    ChrTalk(
        0x13,
        "That, Dad … … What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Alm, maybe\x01",
            "Your physical condition is not good …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "…… Gusut … …\x01",
            "……… okay …… Even if it's okay ……\x02",
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

    # Function_37_B923 end

    def Function_38_C016(): pass

    label("Function_38_C016")


    def lambda_C01B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C01B)

    def lambda_C02C():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C02C)
    WaitChrThread(0x13, 1)
    OP_95(0x13, 74920, 0, 210, 2000, 0x0)
    OP_93(0x13, 0x0, 0x1F4)
    Return()

    # Function_38_C016 end

    def Function_39_C061(): pass

    label("Function_39_C061")


    def lambda_C066():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_C066)

    def lambda_C077():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C077)
    WaitChrThread(0x14, 1)
    OP_95(0x14, 76120, 0, 210, 2000, 0x0)
    OP_93(0x14, 0x0, 0x1F4)
    Return()

    # Function_39_C061 end

    SaveToFile()

Try(main)
