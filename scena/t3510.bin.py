from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t3510.bin",                # FileName
        "t3510",                    # MapName
        "t3510",                    # Location
        0x005C,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x01',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 92, 0, 2, 0, 3],
    )

    BuildStringList((
        "t3510",                  # 0
        "Receptionist Malcana",         # 1
        "Reception Thomas",           # 2
        "Ricardo",               # 3
        "tourist",                 # 4
        "tourist",                 # 5
        "tourist",                 # 6
        "Citizen",                   # 7
        "Citizen",                   # 8
        "boy",                 # 9
        "Carrier Aaron",           # 10
        "Billy",                 # 11
        "Female officer",               # 12
        "Airborne",                 # 13
        "Policeman",                   # 14
        "Policeman",                   # 15
        "Grace",               # 16
        "Raines",               # 17
        "Reporter Noticia",         # 18
        "A reporter",                   # 19
        "A reporter",                   # 20
        "A reporter",                   # 21
        "A reporter",                   # 22
    ))

    AddCharChip((
        "chr/ch10500.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "chr/ch28200.itc",                   # 03
        "chr/ch28100.itc",                   # 04
        "chr/ch22000.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch21800.itc",                   # 07
        "chr/ch20200.itc",                   # 08
        "chr/ch20302.itc",                   # 09
        "chr/ch34202.itc",                   # 0A
    ))

    DeclNpc(4294957076, 150,     2849,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294958946, 150,     6730,    135,  261,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6679,    0,       5530,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294955996, 5000,    4760,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294956567, 5000,    5769,    225,  389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294966257, 5000,    13960,   315,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294961617, 0,       4294964757, 225,  389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294956977, 5199,    8109,    45,   389,  0x0, 0,   9,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(4294958427, 5199,    10039,   225,  389,  0x0, 0,   10,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 18,  0.25999999046325684,   7.989999771118164,     0.0,                   36.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -0.04333333298563957,  -3.994999885559082,    -0.0,                  1.0])

    DeclActor(4294958606, 0,       2530,    1000,    4294957076, 1600,    2850,    0x007E, 0,  7,  0x0000)
    DeclActor(4294960086, 0,       5680,    1000,    4294958946, 1600,    6730,    0x007E, 0,  9,  0x0000)
    DeclActor(4294959706, 0,       4294964856, 1200,    4294959706, 1500,    4294964856, 0x007C, 0,  17, 0x0000)

    ChipFrameInfo(1136, 0)                                       # 0

    ScpFunction((
        "Function_0_470",          # 00, 0
        "Function_1_520",          # 01, 1
        "Function_2_56D",          # 02, 2
        "Function_3_6EA",          # 03, 3
        "Function_4_75D",          # 04, 4
        "Function_5_A2C",          # 05, 5
        "Function_6_AEF",          # 06, 6
        "Function_7_107F",         # 07, 7
        "Function_8_1083",         # 08, 8
        "Function_9_1586",         # 09, 9
        "Function_10_158A",        # 0A, 10
        "Function_11_1A84",        # 0B, 11
        "Function_12_1B01",        # 0C, 12
        "Function_13_1B97",        # 0D, 13
        "Function_14_1C33",        # 0E, 14
        "Function_15_1CD8",        # 0F, 15
        "Function_16_1D4D",        # 10, 16
        "Function_17_1DBA",        # 11, 17
        "Function_18_1E99",        # 12, 18
        "Function_19_1FE0",        # 13, 19
        "Function_20_21C6",        # 14, 20
        "Function_21_227F",        # 15, 21
        "Function_22_2BF8",        # 16, 22
        "Function_23_2E2E",        # 17, 23
        "Function_24_2F82",        # 18, 24
        "Function_25_30A0",        # 19, 25
        "Function_26_3A93",        # 1A, 26
        "Function_27_3F9F",        # 1B, 27
        "Function_28_47F6",        # 1C, 28
        "Function_29_4992",        # 1D, 29
        "Function_30_4ACE",        # 1E, 30
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

    SetMapObjFlags(0x0, 0x2000000)
    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_546")
    ClearMapObjFlags(0x5, 0x2000000)
    Jump("loc_555")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_555")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C")
    ClearMapObjFlags(0x0, 0x2000000)

    label("loc_56C")

    Return()

    # Function_1_520 end

    def Function_2_56D(): pass

    label("Function_2_56D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_594")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 6600, 0, -3500, 180)

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrPos(0x8, 0, 0, -5500, 90)
    SetChrPos(0x9, 1500, 0, -5500, 270)
    SetChrPos(0xA, 340, 0, 6490, 180)
    Jump("loc_6A7")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_6A7")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5F1")
    Jump("loc_6A7")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_66E")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0x9)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_669")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 5480, 0, 5530, 90)
    TurnDirection(0xA, 0x12, 0)

    label("loc_669")

    Jump("loc_6A7")

    label("loc_66E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67C")
    Jump("loc_6A7")

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_69E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x10)
    Jump("loc_6A7")

    label("loc_69E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A7")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6BE")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 4)
    Event(0, 19)
    Jump("loc_6E9")

    label("loc_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_6D5")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 4)
    Event(0, 21)
    Jump("loc_6E9")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_6E9")
    ClearScenarioFlags(0x22, 2)
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_6E9")

    Return()

    # Function_2_56D end

    def Function_3_6EA(): pass

    label("Function_3_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6FE")
    OP_24(0x86)
    ClearScenarioFlags(0x0, 4)
    Jump("loc_71A")

    label("loc_6FE")

    SoundDistance(0x86, 0x16D0, 0x0, 0x259E, 0x1388, 0x30D40, 0x64, 0x0)

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_72B")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)

    label("loc_72B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_745")
    ModifyEventFlags(0, 0, 0x80)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_745")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75C")
    ClearMapObjFlags(0x0, 0x4)

    label("loc_75C")

    Return()

    # Function_3_6EA end

    def Function_4_75D(): pass

    label("Function_4_75D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_795")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_791")
    Call(0, 22)
    Return()

    label("loc_791")

    Call(0, 23)
    Return()

    label("loc_795")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E0")

    ChrTalk(
        0xFE,
        (
            "Where the package arrived incorrectly\x01",
            "Go around in order, check the baggage correctly\x01",
            "Please exchange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First of all, Mainz, then Ursula Hospital,\x01",
            "Finally it would be nice to go to a private house in a residential area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The address of the private house in the residential area is\x01",
            "I write it in the slip, so when I go to the end\x01",
            "Please check it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is troublesome and bad, but I asked for your best regards.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_955")

    label("loc_8E0")


    ChrTalk(
        0xFE,
        (
            "First of all, Mainz, then Ursula Hospital,\x01",
            "Finally it would be nice to go to a private house in a residential area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is troublesome and bad, but I asked for your best regards.\x02",
    )

    CloseMessageWindow()

    label("loc_955")

    Jump("loc_A28")

    label("loc_95A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E0")

    ChrTalk(
        0xFE,
        "Thanks for your help, I was saved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it's your head …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to report it to the president.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A28")

    label("loc_9E0")


    ChrTalk(
        0xFE,
        "Thanks for your help, I was saved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope to see you again.\x02",
    )

    CloseMessageWindow()

    label("loc_A28")

    TalkEnd(0xFE)
    Return()

    # Function_4_75D end

    def Function_5_A2C(): pass

    label("Function_5_A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_A6B")
    Call(0, 28)
    Jump("loc_A6E")

    label("loc_A6B")

    Call(0, 27)

    label("loc_A6E")

    Return()

    label("loc_A6F")

    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "When the crossbell is like this\x01",
            "To deceive medical supplies … …\x01",
            "I can not forgive you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys,\x01",
            "Somehow catch the culprit!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_5_A2C end

    def Function_6_AEF(): pass

    label("Function_6_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_B2E")
    Call(0, 28)
    Jump("loc_B31")

    label("loc_B2E")

    Call(0, 27)

    label("loc_B31")

    Return()

    label("loc_B32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BBC")

    ChrTalk(
        0xA,
        (
            "さっきここにPolicemanたちが来てな。\x01",
            "She seems to be investigating traces of hunting soldiers at the depot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It's bad, but please do not enter further.\x02",
    )

    CloseMessageWindow()
    Jump("loc_107B")

    label("loc_BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BCA")
    Jump("loc_107B")

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BD8")
    Jump("loc_107B")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F52")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD6")

    ChrTalk(
        0xFE,
        (
            "You, medical supplies\x01",
            "You regained well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From Ursula Hospital earlier\x01",
            "I heard that the package arrived,\x01",
            "I was relieved at last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In future it seems that this is not the case,\x01",
            "Take care more carefully\x01",
            "I should not do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D78")

    label("loc_CD6")


    ChrTalk(
        0xFE,
        (
            "From Ursula Hospital earlier\x01",
            "I heard that the package arrived,\x01",
            "I was relieved at last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In future it seems that this is not the case,\x01",
            "Take care more carefully\x01",
            "I should not do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D78")

    Jump("loc_F4D")

    label("loc_D7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5A")

    ChrTalk(
        0xFE,
        (
            "…… Eventually, medical supplies\x01",
            "You have been running away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, it's not your fault.\x01",
            "All I was carelessly cheated is all bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Take care more carefully in the future\x01",
            "Do not check it … um …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_ECE")

    label("loc_E5A")


    ChrTalk(
        0xFE,
        (
            "…… Eventually, medical supplies\x01",
            "You have been running away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Take care more carefully in the future\x01",
            "Do not check it … um …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECE")

    Jump("loc_F4D")

    label("loc_ED3")


    ChrTalk(
        0xFE,
        (
            "No way to be deceived by forged documents …\x01",
            "Damn, it is my responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ursula hospital also\x01",
            "I have to contact you later … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4D")

    Jump("loc_107B")

    label("loc_F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_107B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1009")

    ChrTalk(
        0xFE,
        (
            "Kapua express flight guys, too,\x01",
            "At the airport it became familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a privately operated transport company,\x01",
            "He seems to have made a considerable achievement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, the economy is a good story.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_107B")

    label("loc_1009")


    ChrTalk(
        0xFE,
        (
            "Kapua express flights,\x01",
            "As a privately operated transport company,\x01",
            "He seems to have made a considerable achievement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, the economy is a good story.\x02",
    )

    CloseMessageWindow()

    label("loc_107B")

    TalkEnd(0xFE)
    Return()

    # Function_6_AEF end

    def Function_7_107F(): pass

    label("Function_7_107F")

    Call(0, 8)
    Return()

    # Function_7_107F end

    def Function_8_1083(): pass

    label("Function_8_1083")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1174")

    ChrTalk(
        0x8,
        (
            "The god who wandered around hunters and towns left,\x01",
            "I tried returning to work for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can not operate any airmail,\x01",
            "What shall I do now …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is nothing that we regain everyday life\x01",
            "Is it possible to do …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11F8")

    label("loc_1174")


    ChrTalk(
        0x8,
        (
            "I can not operate any airmail,\x01",
            "What shall I do now …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is nothing that we regain everyday life\x01",
            "Is it possible to do …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F8")

    Jump("loc_1582")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_13AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1309")

    ChrTalk(
        0x8,
        (
            "For Libert and Remiferia,\x01",
            "To restore this time crossbar city\x01",
            "We receive great support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Donations and goods also gathered,\x01",
            "Reconstruction work is also relatively early\x01",
            "He said he showed calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a citizen of Crossbell,\x01",
            "By all means I would like to thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13A8")

    label("loc_1309")


    ChrTalk(
        0x8,
        (
            "For Libert and Remiferia,\x01",
            "To restore this time crossbar city\x01",
            "We receive great support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a citizen of Crossbell,\x01",
            "By all means I would like to thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A8")

    Jump("loc_1582")

    label("loc_13AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CE")

    ChrTalk(
        0x8,
        (
            "Since independence advocacy has been done,\x01",
            "I feel uneasy about the situation of Crossbell\x01",
            "It seems that customers are coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Indeed, the trip that was scheduled\x01",
            "Those who are canceled\x01",
            "You can see it in a small number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it may be unreasonable,\x01",
            "From the inhabitants of the crossbell\x01",
            "I am a little sad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1582")

    label("loc_14CE")


    ChrTalk(
        0x8,
        (
            "Since independence advocacy has been done,\x01",
            "I feel uneasy about the situation of Crossbell\x01",
            "It seems that customers are coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it may be unreasonable,\x01",
            "From the inhabitants of the crossbell\x01",
            "I am a little sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1582")

    TalkEnd(0x8)
    Return()

    # Function_8_1083 end

    def Function_9_1586(): pass

    label("Function_9_1586")

    Call(0, 10)
    Return()

    # Function_9_1586 end

    def Function_10_158A(): pass

    label("Function_10_158A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_170C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B8")

    ChrTalk(
        0x9,
        (
            "Since the declaration of independence was made,\x01",
            "This airport is to the invasion of the two major countries\x01",
            "It was an interception point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Previously, the hunters who attacked the city\x01",
            "As a president's private unit\x01",
            "I heard he was packing up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… I can say something.\x01",
            "I believed in the President's word and agreed independently\x01",
            "What was our heart …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1707")

    label("loc_16B8")


    ChrTalk(
        0x9,
        (
            "I believed in the President's word and agreed independently\x01",
            "What was our heart …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1707")

    Jump("loc_1A80")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1827")

    ChrTalk(
        0x9,
        (
            "That crossbell raid incident,\x01",
            "Mercifully as an empire's conspiracy\x01",
            "It seems whispered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There is no confirmation … …\x01",
            "There is no smoke without fire,\x01",
            "Because I say it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Looking at the way of the empire so far,\x01",
            "The possibility of being true is high …\x01",
            "I can not but think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18CB")

    label("loc_1827")


    ChrTalk(
        0x9,
        (
            "That crossbell raid incident,\x01",
            "Mercifully as an empire's conspiracy\x01",
            "It seems whispered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There is no confirmation,\x01",
            "The possibility of being true is high …\x01",
            "I can not but think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CB")

    Jump("loc_1A80")

    label("loc_18D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1A80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D5")

    ChrTalk(
        0x9,
        (
            "This is reception desk for arrival and departure,\x01",
            "We keep baggage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it was delivery of luggage to a foreign country,\x01",
            "To the people of \"Kapua Express\" just coming\x01",
            "Why do not you try asking us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When packages arrive faster than normal air transport\x01",
            "It seems quite popular.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A80")

    label("loc_19D5")


    ChrTalk(
        0x9,
        (
            "If it was delivery of luggage to a foreign country,\x01",
            "To the people of \"Kapua Express\" just coming\x01",
            "Why do not you try asking us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When packages arrive faster than normal air transport\x01",
            "It seems quite popular.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A80")

    TalkEnd(0x9)
    Return()

    # Function_10_158A end

    def Function_11_1A84(): pass

    label("Function_11_1A84")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh ~, Hey Hey!\x01",
            "You can see the airship flying away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honey, please look into you too!\x01",
            "It's definitely excited!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1A84 end

    def Function_12_1B01(): pass

    label("Function_12_1B01")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "はあ、boyって\x01",
            "No matter how many you are children, hey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, such a big one\x01",
            "It's amazing skill to fly in the sky.\x01",
            "I will admire the point obediently.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1B01 end

    def Function_13_1B97(): pass

    label("Function_13_1B97")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, that green flying boat\x01",
            "It looks like a passenger ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently it is made by Linefault\x01",
            "It seems to be an old-fashioned high speed boat … …\x01",
            "I wonder what kind of aristocratic belongings.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1B97 end

    def Function_14_1C33(): pass

    label("Function_14_1C33")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The restoration of the city ended as usual,\x01",
            "For a while family members\x01",
            "I think I will go abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have my parents home\x01",
            "Per Remiferia\x01",
            "Surely it will be safe, yeah.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1C33 end

    def Function_15_1CD8(): pass

    label("Function_15_1CD8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Haha, it is supposed to be coming home suddenly\x01",
            "I was surprised … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband has something to say.\x01",
            "Recently somehow noises ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1CD8 end

    def Function_16_1D4D(): pass

    label("Function_16_1D4D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm going to take an airship from now.\x01",
            "Well, I'm looking forward to it ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of photos from the sky\x01",
            "I have to take a picture.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1D4D end

    def Function_17_1DBA(): pass

    label("Function_17_1DBA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1E30")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Welcome to Crossbell Independent Country!\x01",
            "Stay and stay\x01",
            "To \"Hotel Millennium\"!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E80")

    label("loc_1E30")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Welcome to Crossbell Autonomous Region!\x01",
            "Stay and stay\x01",
            "To \"Hotel Millennium\"!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E80")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_1DBA end

    def Function_18_1E99(): pass

    label("Function_18_1E99")

    EventBegin(0x1)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F26")

    ChrTalk(
        0xA,
        (
            "さっきここにPolicemanたちが来てな。\x01",
            "She seems to be investigating traces of hunting soldiers at the depot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It's bad, but please do not enter further.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F91")

    label("loc_1F26")

    TurnDirection(0xA, 0x0, 500)

    ChrTalk(
        0xA,
        (
            "Oops ……\x01",
            "It is the gate of the boarding gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I have to bring tickets\x01",
            "Please be careful not to enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F91")

    Sleep(50)
    SetChrPos(0x0, 960, 0, 5140, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FD2")
    TurnDirection(0xA, 0x12, 0)
    Jump("loc_1FD9")

    label("loc_1FD2")

    OP_93(0xA, 0xB4, 0x0)

    label("loc_1FD9")

    OP_4C(0xA, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_18_1E99 end

    def Function_19_1FE0(): pass

    label("Function_19_1FE0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("apl/ch50314.itc", 0x1F)
    LoadChrToIndex("chr/ch47900.itc", 0x20)
    LoadChrToIndex("chr/ch27400.itc", 0x21)
    LoadChrToIndex("chr/ch27800.itc", 0x22)
    LoadChrToIndex("chr/ch27900.itc", 0x23)
    LoadChrToIndex("chr/ch27600.itc", 0x24)
    LoadEffect(0x0, "event/eva02_00.eff")
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x22)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x17, -1450, 5000, 13350, 0)
    SetChrPos(0x18, -900, 5000, 13950, 0)
    SetChrPos(0x19, 3000, 5000, 13450, 0)
    SetChrPos(0x1A, 1150, 5000, 13950, 0)
    SetChrPos(0x1B, -3150, 5000, 13350, 45)
    SetChrPos(0x1C, 1550, 5000, 12500, 0)
    SetChrPos(0x1D, 4700, 5000, 13000, 0)
    BeginChrThread(0x18, 3, 0, 20)
    OP_68(1000, 8000, 13250, 0)
    MoveCamera(315, 15, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(37800, 0)
    OP_68(1000, 6000, 13250, 5000)
    SetCameraDistance(35800, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1FE0 end

    def Function_20_21C6(): pass

    label("Function_20_21C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_227E")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21F4")
    Sleep(500)
    Jump("loc_223C")

    label("loc_21F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_220B")
    Sleep(1000)
    Jump("loc_223C")

    label("loc_220B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2222")
    Sleep(1500)
    Jump("loc_223C")

    label("loc_2222")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2239")
    Sleep(2000)
    Jump("loc_223C")

    label("loc_2239")

    Sleep(2500)

    label("loc_223C")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 80, 0)
    Jump("Function_20_21C6")

    label("loc_227E")

    Return()

    # Function_20_21C6 end

    def Function_21_227F(): pass

    label("Function_21_227F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11200.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("apl/ch51212.itc", 0x24)
    LoadChrToIndex("chr/ch30000.itc", 0x25)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07100.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x2)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x101, 3000, 5000, 11400, 0)
    SetChrPos(0x102, 2700, 5100, 13000, 90)
    SetChrPos(0x104, 4500, 5000, 10600, 0)
    SetChrPos(0x109, 4800, 5100, 12300, 270)
    SetChrPos(0x105, 3300, 5000, 10100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -8300, 5000, 6700, 90)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -4300, 0, -6800, 45)
    BeginChrThread(0x15, 0, 0, 0)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -3700, 0, 6600, 180)
    BeginChrThread(0x16, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    OP_78(0x5, 0x14)
    OP_49()
    SetChrPos(0x14, -7700, 0, 29900, 270)
    OP_D5(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_11(0xE4, 0xA9, 0x9D, 0x32, 0xBE, 0x0)
    OP_68(0, 2000, 0, 0)
    MoveCamera(330, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, 7500, 0, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(4300, 6500, 12000, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(20500, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#6P#10102FHigh-speed cruiser of Liber,\x01",
            "\"Arseille\" … ….\x02\x03",
            "#10109FHa\x01",
            "After all it is an amazing ship, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PI made the name of ZCF wake up.\x01",
            "The world's fastest airship … …\x02\x03",
            "#00100FI still keep updating my self-record\x01",
            "It seems that others are not drawn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FThen, Princess Libert\x01",
            "It's a flagship ride.\x02\x03",
            "#00302FWas it Princess Claudia?\x01",
            "I feel like a way of doing things.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00004F#5PExactly not \"princess\"\x01",
            "Though it is \"Wang Qiu\".\x02\x03",
            "#00000FIn other words,\x01",
            "I will be the next Queen's Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FWell ~, I see.\x02\x03",
            "#00301F… … No way I called it\x01",
            "Are you sure you do not have anything wrong?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00106FWell, yes.\x01",
            "I do not know exactly.\x02\x03",
            "#00108FIf you ask Bell\x01",
            "About your highness schedule\x01",
            "I think I understand ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x105, 0x13, 500)

    def lambda_27D0():

        label("loc_27D0")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_27D0")

    QueueWorkItem2(0x105, 2, lambda_27D0)

    ChrTalk(
        0x105,
        (
            "#11P#10302FGiggle\x01",
            "Does not it seem necessary?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#5P#00005FHuh.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    ClearChrFlags(0x13, 0x80)

    NpcTalk(
        0x13,
        "Dignified voice",
        (
            "── We kept you waiting.\x01",
            "Are you the members of the Special Affairs Division?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_28C1():

        label("loc_28C1")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_28C1")

    QueueWorkItem2(0x101, 2, lambda_28C1)
    Sleep(50)

    def lambda_28D6():

        label("loc_28D6")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_28D6")

    QueueWorkItem2(0x104, 2, lambda_28D6)
    Sleep(100)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)
    Fade(500)
    OP_68(-7500, 6100, 7000, 0)
    MoveCamera(336, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    OP_68(1800, 6100, 11300, 5500)
    MoveCamera(321, 19, 0, 5500)

    def lambda_2941():
        OP_95(0xFE, -4300, 5000, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2941)
    WaitChrThread(0x13, 1)

    def lambda_295F():
        OP_95(0xFE, 1000, 5000, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_295F)
    WaitChrThread(0x13, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011FAh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FIt is! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FAnd after all …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FO Oh, the moment ago\x01",
            "The lady was making a noise …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07105F#5P……?\x02\x03",
            "#07104FOh, this is rude.\x01",
            "Were you at the unveiling ceremony?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(20000, 300)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x13,
        (
            "─ ─ It was delayed.\x01",
            "Riber King Army, Royal Guard,\x01",
            "It is Uria · Schwarzzu.\x02\x03",
            "By the life of His Holiness Claudia\x01",
            "From here on you to \"Arseille\"\x01",
            "I will show you.\x02\x03",
            "Come along, please.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(20500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    SetScenarioFlags(0x22, 1)
    NewScene("t3520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_227F end

    def Function_22_2BF8(): pass

    label("Function_22_2BF8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6860, 1250, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FSorry, you are\x01",
            "Are you the Kapua express mail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Oh, but that's right ……\x01",
            "Are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FCrossbell Police,\x01",
            "It is a person of the affairs support department.\x02\x03",
            "Confirm the request\x01",
            "I asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oh, you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, thank you.\x01",
            "I was totally in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It's a cumbersome task,\x01",
            "Will you take over?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_2BF8 end

    def Function_23_2E2E(): pass

    label("Function_23_2E2E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6860, 1250, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "Oh, maybe\x01",
            "Have you got your hands free?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It's a cumbersome task,\x01",
            "Will you take over?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_2E2E end

    def Function_24_2F82(): pass

    label("Function_24_2F82")

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
            "【undertake】\x01",      # 0
            "【quit】\x01",          # 1
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
        (0, "loc_2FEC"),
        (1, "loc_2FF4"),
        (SWITCH_DEFAULT, "loc_309F"),
    )


    label("loc_2FEC")

    Call(0, 25)
    Jump("loc_309F")

    label("loc_2FF4")


    ChrTalk(
        0x101,
        (
            "#00006FSorry, now it's kinda\x01",
            "My hands are not open ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Oh, is that so?\x01",
            "Sorry ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Then, if your hands are empty\x01",
            "Please talk to me again!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x175, 4)
    Jump("loc_309F")

    label("loc_309F")

    Return()

    # Function_24_2F82 end

    def Function_25_30A0(): pass

    label("Function_25_30A0")


    ChrTalk(
        0x101,
        "#00000FWell, please leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FRequest is certain, misled package\x01",
            "What a story it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "We flying around the continent\x01",
            "Luggage in various places\x01",
            "I'm delivering it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "This time, to the package delivered here\x01",
            "There is a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The addressee is going upside down,\x01",
            "Some baggage in the wrong place\x01",
            "She seems to have arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWell … that is tough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FTo make a mistake in slips\x01",
            "I do not think so, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Wow, the president of our company\x01",
            "He is a cheap person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Several times until now\x01",
            "There was such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "When it is terrible, instead of slips\x01",
            "A letter from my acquaintance\x01",
            "Or you can not affix it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha ……\x01",
            "Inadvertently\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, I am a respectable person.\x01",
            "We who did not go\x01",
            "It picked up … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "…… Kohon, sorry.\x01",
            "The talk deviated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "In short, it was incorrectly delivered\x01",
            "I'd like to ask for re-delivery of my luggage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "After delivery to autonomous state, always\x01",
            "I leave it to the local shipping company\x01",
            "There is no land intuition at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FI see,\x01",
            "I understood the circumstances.\x02\x03",
            "#10302FThe location of misplaced baggage is\x01",
            "Are you able to figure out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, where I confirmed\x01",
            "According to …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "To Mainz's \"Red Brick Tea\"\x01",
            "Luggage addressed to Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "At Ursula Hospital\x01",
            "It is addressed to a private house in a residential area in the city\x01",
            "The package seems to have arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "You go around that address to you,\x01",
            "While collecting erroneously arranged packages\x01",
            "I'd like you to deliver the original package.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "… and so on,\x01",
            "Please accept this.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '易碎品的小包裹'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('易碎品的小包裹', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '发往住宅街的送货单'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('发往住宅街的送货单', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000FThis is \"Red Brick Tea\"\x01",
            "It was supposed to have arrived\x01",
            "Is it a baggage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThis voucher is for the package that arrived at the hospital\x01",
            "It should be originally attached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oh, that sort of thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "First of all, that parcel\x01",
            "With \"Red Brick Tea\"\x01",
            "Please deliver it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It is addressed to Ursula Hospital\x01",
            "Because the baggage should have arrived\x01",
            "Receive it, um … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "…… Somehow say by yourself\x01",
            "I do not understand it.\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003FAnd anyway … …\x01",
            "Do that in order\x01",
            "I hope I can exchange it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Well, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Although it is troublesome and bad,\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, sorry.\x02\x03",
            "#00000F… Well then, immediately\x01",
            "To Mainz's \"Red Brick Tea\"\x01",
            "Do you want to go there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWhew, quite\x01",
            "The bones are going to break.\x02",
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
            "Quest 【Redelivery of misdelivered package】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x175, 5)
    OP_29(0x85, 0x1, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_25_30A0 end

    def Function_26_3A93(): pass

    label("Function_26_3A93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(6860, 2500, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    OP_68(6860, 1250, -5300, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x11,
        (
            "Oh, properly a correct addressee\x01",
            "It looks like he delivered the package.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, I was saved.\x01",
            "Thank you very much, support department Saint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYou are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "by the way……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "That older sister,\x01",
            "Does not it look kind of pale?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#1SGrumbling ……\x01",
            "To talk with ghosts ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10309FHuh, I heard it was a shock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FI understand the feeling ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FWell, it will fit in there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FEr, um … ….\x01",
            "Because it is such a thing,\x01",
            "please do not worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "Really?\x01",
            "Oh well ok but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well then, here I am\x01",
            "Excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If there is something again\x01",
            "Please do not ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, anytime.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FWe look forward.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3EDF")
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F… Well then, then\x01",
            "On the West Crossbell Highway\x01",
            "Let's hurry to the derailment site.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EDF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Redelivery of misdelivered package】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x85, 0x1, 0x5)
    OP_29(0x85, 0x1, 0x6)
    OP_29(0x85, 0x4, 0x10)
    SubItemNumber('发往住宅街的送货单', 1)
    OP_4C(0x11, 0xFF)
    ClearMapFlags(0x10000000)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3F87")
    EventEnd(0x5)
    NewScene("c0000", 103, 0, 0)
    IdleLoop()
    Jump("loc_3F9E")

    label("loc_3F87")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    EventEnd(0x5)

    label("loc_3F9E")

    Return()

    # Function_26_3A93 end

    def Function_27_3F9F(): pass

    label("Function_27_3F9F")

    EventBegin(0x0)
    Fade(500)
    OP_68(5810, 1250, 4500, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, 5480, 0, 4000, 0)
    SetChrPos(0x102, 6680, 0, 4000, 0)
    SetChrPos(0x104, 5480, 0, 2800, 0)
    SetChrPos(0x103, 6580, 0, 2800, 0)
    SetChrPos(0x105, 5480, 0, 1600, 0)
    SetChrPos(0x109, 6680, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()

    ChrTalk(
        0x12,
        "Ha, what am I supposed to do ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If I keep more firmly\x01",
            "To such a thing …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005Fthat……\x01",
            "What did you do?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_410C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_410C)
    Sleep(10)

    def lambda_411C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_411C)
    WaitChrThread(0xA, 2)
    Sleep(500)

    ChrTalk(
        0x12,
        (
            "Oh, you are the Special Affairs Division … …\x01",
            "Actually, I am in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Today, at Ursula hospital\x01",
            "Medical supplies from Remiferia\x01",
            "I was planning to deliver … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Apparently, where and where\x01",
            "It seems he cheated him and took it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FI cheated medical supplies …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh … … just a while ago,\x01",
            "Even transport company human beings\x01",
            "I visited here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "\"Since Rhyss' transportation can not come,\x01",
            "He took over the transportation of goods by proxy \"\x01",
            "Please say a plausible reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To those who are so lying\x01",
            "I could not see it, and it was a reply\x01",
            "I handed over the baggage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "But I also like that power of attorney\x01",
            "I do not remember giving out to others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "So while I was talking a lot,\x01",
            "I realized that I was deceived by my baggage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FHmm … in short,\x01",
            "Was the proxy letter fake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301FHowever, in this emergency\x01",
            "I do not want to cheat medical supplies\x01",
            "Equivalently it is bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FVictims of that raid incident also\x01",
            "Even though I have been hospitalized a lot … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FSuch medical supplies,\x01",
            "If you squeeze it behind, to Mira as it is\x01",
            "I guess it will be.\x02\x03",
            "#00301FCunning of Mira\x01",
            "Fire place thief would be tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FIt is terrible …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "But I was in embarrassed … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Even now at Ursula Hospital\x01",
            "I'm waiting for the arrival of goods\x01",
            "Even if said\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, it's all my responsibility ……\x01",
            "At least for limes transportation\x01",
            "If you check it … ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xA, 500)

    ChrTalk(
        0x12,
        (
            "No … you're not bad.\x01",
            "Whatever you think is bad\x01",
            "He is a fraudster of luggage.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x101, 500)

    ChrTalk(
        0x12,
        (
            "そうだ……You guys,\x01",
            "The culprit who cheated medical supplies\x01",
            "Can not you find them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I am admitted to Ursula hospital\x01",
            "For patients as well,\x01",
            "I want you to catch it.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 29)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x12, 0xA, 0)
    TurnDirection(0xA, 0x12, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6080, 0, 4000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_3F9F end

    def Function_28_47F6(): pass

    label("Function_28_47F6")

    EventBegin(0x0)
    Fade(500)
    OP_68(5810, 1250, 4500, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, 5480, 0, 4000, 0)
    SetChrPos(0x102, 6680, 0, 4000, 0)
    SetChrPos(0x104, 5480, 0, 2800, 0)
    SetChrPos(0x103, 6580, 0, 2800, 0)
    SetChrPos(0x105, 5480, 0, 1600, 0)
    SetChrPos(0x109, 6680, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x12, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "The culprit who cheated medical supplies ……\x01",
            "Can not you find them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I am admitted to Ursula hospital\x01",
            "For patients as well,\x01",
            "I want you to catch it.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 29)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x12, 0xA, 0)
    TurnDirection(0xA, 0x12, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6080, 0, 4000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_47F6 end

    def Function_29_4992(): pass

    label("Function_29_4992")

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
            "undertake\x01",      # 0
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
        (0, "loc_49F4"),
        (1, "loc_49FC"),
        (SWITCH_DEFAULT, "loc_4ACD"),
    )


    label("loc_49F4")

    Call(0, 30)
    Jump("loc_4ACD")

    label("loc_49FC")


    ChrTalk(
        0x101,
        (
            "#00003FExcuse me……\x01",
            "I have something I can not remove now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That's right.\x01",
            "Then it can not be helped …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If you have time\x01",
            "Please call me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Only you are reliant.\x01",
            "Please do not hesitate to ask me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19B, 6)
    Jump("loc_4ACD")

    label("loc_4ACD")

    Return()

    # Function_29_4992 end

    def Function_30_4ACE(): pass

    label("Function_30_4ACE")


    ChrTalk(
        0x101,
        (
            "#00003F… … still time since the incidents\x01",
            "I do not seem to have gone through … ….\x01",
            "You can make it in time if you hurry.\x02\x03",
            "#00000FPlease leave it to us once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh … I will wear it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FBut the opponent has already worked\x01",
            "It seems I have finished ……\x01",
            "You seemed to be really in a hurry.\x02\x03",
            "#00101FSomething like showing the destination of the criminal\x01",
            "Did not there be any clues?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "That's right.\x01",
            "Because I have not seen it\x01",
            "I can not say it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "by the way……\x01",
            "That man was made by Rheinfault\x01",
            "It seems that he was on a black carrying car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Empire who looks good also has a good appearance\x01",
            "It was a feeling, and maybe ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FDirectly to the Empire\x01",
            "The possibility of trying to be high\x01",
            "It might be expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103Fperhaps,\x01",
            "This time around the Belgard gate\x01",
            "Maybe it is around arrival.\x02\x03",
            "#10101FJust to be sure, the path of the transport vehicle\x01",
            "Those who listened and chased\x01",
            "I think that is good, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, it's also a long way to go\x01",
            "I do not seem to be able to do it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyways……\x01",
            "Let's chase after somehow.\x02\x03",
            "#00001FBillyさんたちはここで\x01",
            "Please wait for contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Oh, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I beg you to do my best, you!\x02",
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
            "Quest 【Search for medical supplies】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x93, 0x4, 0x2)
    OP_29(0x93, 0x1, 0x0)
    Return()

    # Function_30_4ACE end

    SaveToFile()

Try(main)
