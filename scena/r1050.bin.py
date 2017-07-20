from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r1050.bin",                # FileName
        "r1050",                    # MapName
        "r1050",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x05,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 1, 0, 2],
    )

    BuildStringList((
        "r1050",                  # 0
        "Sonya Command",           # 1
        "Donovan",           # 2
        "Grace",               # 3
        "Lieutenant Mireille",           # 4
        "Raymond investigator",       # 5
        "Raines",               # 6
        "Policeman",                   # 7
        "Policeman",                   # 8
        "Policeman",                   # 9
        "A security guard",               # 10
        "A security guard",               # 11
        "A security guard",               # 12
        "A security guard",               # 13
        "conductor",                   # 14
    ))

    AddCharChip((
        "chr/ch05700.itc",                   # 00
        "chr/ch30300.itc",                   # 01
        "chr/ch06000.itc",                   # 02
        "chr/ch32600.itc",                   # 03
        "chr/ch30200.itc",                   # 04
        "chr/ch28100.itc",                   # 05
        "chr/ch30000.itc",                   # 06
        "chr/ch31200.itc",                   # 07
        "chr/ch31300.itc",                   # 08
        "chr/ch28302.itc",                   # 09
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   4,   255,  0)

    DeclActor(4294958516, 0,       4294966476, 3000,    4294958516, 3000,    4294966476, 0x007C, 0,  19, 0x0000)
    DeclActor(4294953166, 0,       4294966676, 2000,    4294953166, 3000,    4294966676, 0x007C, 0,  20, 0x0000)
    DeclActor(4294931196, 0,       9060,    3000,    4294931196, 2000,    9560,    0x007C, 0,  21, 0x0000)
    DeclActor(4294911776, 0,       9690,    3000,    4294911776, 2000,    10190,   0x007C, 0,  22, 0x0000)
    DeclActor(4294902057, 0,       9800,    3000,    4294902057, 2000,    10300,   0x007C, 0,  23, 0x0000)

    ChipFrameInfo(956, 0)                                        # 0

    ScpFunction((
        "Function_0_3BC",          # 00, 0
        "Function_1_46C",          # 01, 1
        "Function_2_4A3",          # 02, 2
        "Function_3_4EC",          # 03, 3
        "Function_4_65A",          # 04, 4
        "Function_5_DA1",          # 05, 5
        "Function_6_E51",          # 06, 6
        "Function_7_10BB",         # 07, 7
        "Function_8_13FA",         # 08, 8
        "Function_9_1638",         # 09, 9
        "Function_10_1822",        # 0A, 10
        "Function_11_19A7",        # 0B, 11
        "Function_12_1C5E",        # 0C, 12
        "Function_13_1CD9",        # 0D, 13
        "Function_14_1D69",        # 0E, 14
        "Function_15_1DF6",        # 0F, 15
        "Function_16_1E80",        # 10, 16
        "Function_17_1F27",        # 11, 17
        "Function_18_1FA5",        # 12, 18
        "Function_19_2008",        # 13, 19
        "Function_20_239F",        # 14, 20
        "Function_21_26DC",        # 15, 21
        "Function_22_26EA",        # 16, 22
        "Function_23_26F8",        # 17, 23
        "Function_24_2706",        # 18, 24
        "Function_25_30AC",        # 19, 25
        "Function_26_42FB",        # 1A, 26
        "Function_27_455F",        # 1B, 27
        "Function_28_65B1",        # 1C, 28
    ))


    def Function_0_3BC(): pass

    label("Function_0_3BC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3F4"),
        (1, "loc_400"),
        (2, "loc_40C"),
        (3, "loc_418"),
        (4, "loc_424"),
        (5, "loc_430"),
        (6, "loc_43C"),
        (SWITCH_DEFAULT, "loc_448"),
    )


    label("loc_3F4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_400")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_40C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_418")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_424")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_430")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_43C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_448")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_454")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_46B")

    Return()

    # Function_0_3BC end

    def Function_1_46C(): pass

    label("Function_1_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47D")
    Call(0, 3)

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_493")
    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4A2")
    ClearScenarioFlags(0x22, 0)
    Event(0, 27)

    label("loc_4A2")

    Return()

    # Function_1_46C end

    def Function_2_4A3(): pass

    label("Function_2_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_4B5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B5")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EB")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_4EB")

    Return()

    # Function_2_4A3 end

    def Function_3_4EC(): pass

    label("Function_3_4EC")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_541")
    SetChrFlags(0xA, 0x10)

    label("loc_541")

    SetChrChipByIndex(0x15, 0x9)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56B")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x12, 0x10)

    label("loc_56B")

    SetChrPos(0x8, 4770, 0, 5830, 180)
    SetChrPos(0x9, -23110, 0, -1910, 315)
    SetChrPos(0xA, 2240, 0, -2630, 288)
    SetChrPos(0xB, -58480, 0, -11340, 225)
    SetChrPos(0xC, -29410, 0, -6490, 346)
    SetChrPos(0xD, 1110, 0, -4130, 279)
    SetChrPos(0xE, -35240, 0, -6360, 315)
    SetChrPos(0xF, -44860, 0, -8410, 77)
    SetChrPos(0x10, -56970, 160, 900, 137)
    SetChrPos(0x11, 4230, 0, 3880, 359)
    SetChrPos(0x12, 5440, 0, 3940, 359)
    SetChrPos(0x13, -59570, 0, -12240, 45)
    SetChrPos(0x14, -67820, 170, 440, 180)
    SetChrPos(0x15, -52090, 0, -18010, 98)
    Return()

    # Function_3_4EC end

    def Function_4_65A(): pass

    label("Function_4_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D01")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -50420, 0, -17890, 270)
    SetChrPos(0x102, -50870, 0, -16710, 225)
    SetChrPos(0x104, -49670, 0, -18710, 270)
    SetChrPos(0x103, -49820, 0, -17210, 270)
    SetChrPos(0x109, -50030, 0, -15940, 225)
    SetChrPos(0x105, -49100, 0, -15920, 225)
    OP_68(-48700, 2210, -19060, 0)
    MoveCamera(302, 24, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(12640, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xFE,
        "Oh that was the worst\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Compared to people who were carried\x01",
            "I am still intact I still like the way\x01",
            "I wonder what ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way No way\x01",
            "The train is derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI was on the train.\x01",
            "It looks like a conductor.\x02\x03",
            "#00000FIf you do not mind, you should do something about the accident\x01",
            "Would you mind telling me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, if I could talk\x01",
            "I'd like to tell you anything ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To a criminal who is lying there earlier\x01",
            "I can not talk about it when asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, in the blink of an eye\x01",
            "Because it was an event.\x01",
            "I mean a bit confused ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FWell, this is the only accident\x01",
            "Even if you do not remember clearly\x01",
            "There may not be any choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FShock of accident also\x01",
            "I think there are … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FIn this case, even a small thing\x01",
            "does not matter.\x02\x03",
            "#00001FWhat I was concerned about\x01",
            "Was not there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Worried … ….\x01",
            "Well …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh now that you mention it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305F#6PWhat happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just before the derailment accident, to the driver\x01",
            "I was in business communication with communication … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He was shouting \"Oh, what's that?!\"\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xFE,
        "\"Wow, what! Is it? \"… ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The accident happened just after that.\x01",
            "The leading car derailed and the connected vehicle also\x01",
            "I followed it one after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And then …\x01",
            "That means it will lead to now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200F\"Wow, what! Is it? \"\x01",
            "A cry of … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FIt's as if you can not believe it#18R噵 噵 噵 噵 噵 噵 噵 噵 噵#\x01",
            "As if I saw it#18R噵 噵 噵 噵 噵 噵 噵 噵 噵#It's a line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FAs a driver,\x01",
            "I wonder what he saw … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 6)
    OP_29(0xA8, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD5")
    Call(0, 26)
    Return()

    label("loc_CD5")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -50180, 0, -17560, 257)
    EventEnd(0x5)
    Jump("loc_DA0")

    label("loc_D01")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Just before the derailment accident,\x01",
            "When I was contacting business by communication\x01",
            "The driver suddenly cried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Wow, what! Is it? \"… ….\x01",
            "The derailment accident happened just after that.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_DA0")

    Return()

    # Function_4_65A end

    def Function_5_DA1(): pass

    label("Function_5_DA1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBF")
    Call(0, 11)
    Jump("loc_E4D")

    label("loc_DBF")


    ChrTalk(
        0xFE,
        (
            "#02003FUntil heavy machinery arrives,\x01",
            "We also guards on site verification\x01",
            "I will cooperate with you.\x02\x03",
            "#02000FTo the members\x01",
            "Because I have said it,\x01",
            "Please do research freely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4D")

    TalkEnd(0xFE)
    Return()

    # Function_5_DA1 end

    def Function_6_E51(): pass

    label("Function_6_E51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1036")

    ChrTalk(
        0xFE,
        (
            "Well, even if I look at it again\x01",
            "It is a terrible big accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is often one dead person in this\x01",
            "It did not come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FMost passengers\x01",
            "Shipped or transferred to the Republic,\x01",
            "You seem to have been taken to a hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIf possible, even those people\x01",
            "I wanted to hear the story, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it can not be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, I'm taking a rest over there\x01",
            "Did you hear the story in the conductor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When we heard a story a while ago\x01",
            "We did not get much information,\x01",
            "Now maybe I remembered something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do not forget to listen to the story.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 2)
    Jump("loc_10B7")

    label("loc_1036")


    ChrTalk(
        0xFE,
        (
            "I am resting over there\x01",
            "Did you hear the story in the conductor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can hear things at the time of the accident soon\x01",
            "It is the only person, do not forget\x01",
            "Please listen to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B7")

    TalkEnd(0xFE)
    Return()

    # Function_6_E51 end

    def Function_7_10BB(): pass

    label("Function_7_10BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1353")

    ChrTalk(
        0xFE,
        (
            "#02102FHow about you, Lloyd.\x01",
            "Did you know something new?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, I can not say anything yet.\x02\x03",
            "#00001FWhat is Mr. Grace,\x01",
            "Have not noticed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02106FWell, well.\x01",
            "Sometimes the train accident itself … …\x02\x03",
            "#02101FAs I thought,\x01",
            "Both timing and location\x01",
            "I think it's too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F……I agree.\x01",
            "Even just as independent advocate\x01",
            "It is when the state of tension is continuing … …\x02\x03",
            "#00103FMaybe there is some intention\x01",
            "The possibility of working …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02106FWell, there is no evidence\x01",
            "Impose my thought\x01",
            "I do not mean to go.\x02\x03",
            "#02109FAnyway, the survey is\x01",
            "Good luck!\x01",
            "Let me interview you if you know something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FOkay, I understand.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x17B, 1)
    Jump("loc_13F6")

    label("loc_1353")


    ChrTalk(
        0xFE,
        (
            "#02103FSometimes the train accident itself … …\x01",
            "Timing and location are the worst this time.\x02\x03",
            "#02109FWell anyway, the survey is\x01",
            "Good luck!\x01",
            "Let me interview you if you know something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F6")

    TalkEnd(0xFE)
    Return()

    # Function_7_10BB end

    def Function_8_13FA(): pass

    label("Function_8_13FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CC")

    ChrTalk(
        0x104,
        (
            "#00300FMireille,\x01",
            "How about those who are restoring?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#07901FYeah, with your investigation\x01",
            "I am going in parallel, but ….\x02\x03",
            "#07906FAfter all, once using a heavy machine\x01",
            "I have to move the train itself\x01",
            "You can not get out of hand.\x02\x03",
            "#07900FTentatively, now it's scattered\x01",
            "I'm removing the debris.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FAfter all, we helped … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#07904FNo, it does not reach that.\x01",
            "For you to investigate\x01",
            "Please concentrate.\x02\x03",
            "#07902FEven our people,\x01",
            "I can tell you if I know something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 4)
    Jump("loc_1634")

    label("loc_15CC")


    ChrTalk(
        0xFE,
        (
            "#07904FFor you to investigate\x01",
            "Please concentrate.\x02\x03",
            "#07902FEven our people,\x01",
            "I can tell you if I know something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1634")

    TalkEnd(0xFE)
    Return()

    # Function_8_13FA end

    def Function_9_1638(): pass

    label("Function_9_1638")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179E")

    ChrTalk(
        0xFE,
        (
            "Once in the collapsed vehicle\x01",
            "I examined it as much as I could find it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are a lot of clues inside\x01",
            "It seemed not to be ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FSomething suspicious is\x01",
            "Did not you put it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, it was the passenger's\x01",
            "It was all my bags,\x01",
            "I wonder if anything was particularly suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By external factors\x01",
            "The accident happened\x01",
            "There must be no doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FHM……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 3)
    Jump("loc_181E")

    label("loc_179E")


    ChrTalk(
        0xFE,
        (
            "Inside the fallen car\x01",
            "A big clue\x01",
            "It seemed not to be ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By external factors\x01",
            "The accident happened\x01",
            "There must be no doubt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181E")

    TalkEnd(0xFE)
    Return()

    # Function_9_1638 end

    def Function_10_1822(): pass

    label("Function_10_1822")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190B")

    ChrTalk(
        0xFE,
        (
            "Hello, when it comes to the accident site so far,\x01",
            "Even just looking is a shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But to tell the truth\x01",
            "I have to take a lot of good pictures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is a picture?\x01",
            "Even becoming evidence,\x01",
            "It is enough to be possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19A3")

    label("loc_190B")


    ChrTalk(
        0xFE,
        (
            "Interview at the accident site\x01",
            "Shocking though ….\x01",
            "I have to take a lot of good pictures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is a picture?\x01",
            "Even becoming evidence,\x01",
            "It is enough to be possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A3")

    TalkEnd(0xFE)
    Return()

    # Function_10_1822 end

    def Function_11_19A7(): pass

    label("Function_11_19A7")

    OP_4B(0x8, 0x0)
    OP_4B(0x11, 0x0)
    OP_4B(0x12, 0x0)

    ChrTalk(
        0x8,
        (
            "#02000Fyou,\x01",
            "Until heavy machinery arrives\x01",
            "How much longer does it take?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, without waiting for 30 minutes\x01",
            "I am planning to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "However, taking time to investigate\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If you want one side track by evening\x01",
            "If recovery is not possible ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02005FIf you can not … ….?\x01",
            "I do not need such worries.\x02\x03",
            "#02001FWhatever you do,\x01",
            "If you do not do it\x01",
            "Because it will not be.\x02\x03",
            "#02003F… …. You too, it is\x01",
            "You know what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P#1KHa, Ha! It is!\x02",
    )


    ChrTalk(
        0x12,
        "#6P#1KHa, Ha! It is!\x02",
    )

    OP_57(0x1)
    OP_5A()

    ChrTalk(
        0x104,
        "#00306F(As usual Sparta ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F(It seems to be Sonya commander.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Let's have a chance\x01",
            "I got it given … …)\x02\x03",
            "#00001F(Whatever the cause of the accident\x01",
            "I have to keep track of it. )\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0x0)
    OP_4C(0x11, 0x0)
    OP_4C(0x12, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x17B, 0)
    Return()

    # Function_11_19A7 end

    def Function_12_1C5E(): pass

    label("Function_12_1C5E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, getting closer to you\x01",
            "It looks dangerous …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I keep a balance now,\x01",
            "What shall I do if I fall into time.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1C5E end

    def Function_13_1CD9(): pass

    label("Function_13_1CD9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, a glass or something\x01",
            "It scatters … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are a pebble on the track\x01",
            "It is not dangerous, by evening\x01",
            "I have to pick them all up.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1CD9 end

    def Function_14_1D69(): pass

    label("Function_14_1D69")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "As covering both these tracks\x01",
            "I do not want to derail … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Travelers and returnees who were on board also,\x01",
            "I guess I had a horrible feeling.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1D69 end

    def Function_15_1DF6(): pass

    label("Function_15_1DF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_1E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E14")
    Call(0, 11)
    Jump("loc_1E7C")

    label("loc_1E14")


    ChrTalk(
        0xFE,
        (
            "Without waiting for heavy machinery to be 30 minutes\x01",
            "I am planning to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By then, little by little\x01",
            "I have to work on it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7C")

    TalkEnd(0xFE)
    Return()

    # Function_15_1DF6 end

    def Function_16_1E80(): pass

    label("Function_16_1E80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_1F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9E")
    Call(0, 11)
    Jump("loc_1F23")

    label("loc_1E9E")


    ChrTalk(
        0xFE,
        (
            "Survey is necessary, but schedule\x01",
            "Can not delay, or …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it can not be helped.\x01",
            "It will be frighteningly difficult,\x01",
            "I have no choice but to try hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F23")

    TalkEnd(0xFE)
    Return()

    # Function_16_1E80 end

    def Function_17_1F27(): pass

    label("Function_17_1F27")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "When you receive contact,\x01",
            "What is the accident so far\x01",
            "I did not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Materials used for repairing the tracks are also\x01",
            "You seem to need a considerable amount.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1F27 end

    def Function_18_1FA5(): pass

    label("Function_18_1FA5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The track is large\x01",
            "I am out of 1000.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Derail from this area\x01",
            "I wonder if it started …\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1FA5 end

    def Function_19_2008(): pass

    label("Function_19_2008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_231E")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -5900, 0, -3220, 315)
    SetChrPos(0x103, -5230, 0, -1840, 315)
    SetChrPos(0x104, -5870, 0, -4650, 315)
    SetChrPos(0x105, -4270, 0, -990, 315)
    SetChrPos(0x109, -7140, 0, -4500, 315)
    SetChrPos(0x102, -4660, 0, -3090, 315)
    OP_68(-8420, 1510, -430, 0)
    MoveCamera(322, 8, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(17870, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x102,
        "#12P#00100FThis is the locomotive\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FIn driving train\x01",
            "It is the most important vehicle.\x02\x03",
            "#00200FInside is made by Rhinefault\x01",
            "Train oval engine and\x01",
            "There should be a driver's cab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10305FHmm, even so\x01",
            "Does not it make sense of discomfort somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FOh, than I imagined\x01",
            "I do not feel like scratching a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FWell, indeed …\x01",
            "Although it is the first car a bit\x01",
            "It is unnatural feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FAh……\x01",
            "If you hit something from the front\x01",
            "It should not be beautiful so far.\x02\x03",
            "#00008FIf so, the cause of derailment is\x01",
            "There seems to be other things ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 3)
    OP_29(0xA8, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22F2")
    Call(0, 26)
    Return()

    label("loc_22F2")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -6920, 0, -2370, 315)
    EventEnd(0x5)
    Jump("loc_239E")

    label("loc_231E")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00003FIf you hit something from the front\x01",
            "It should not be beautiful so far.\x02\x03",
            "#00008FIf so, the cause of derailment is\x01",
            "There should be other things … …\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_239E")

    Return()

    # Function_19_2008 end

    def Function_20_239F(): pass

    label("Function_20_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266A")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -14120, 0, -3340, 33)
    SetChrPos(0x102, -15310, 0, -3410, 33)
    SetChrPos(0x103, -13250, 0, -3620, 33)
    SetChrPos(0x104, -12440, 0, -4610, 33)
    SetChrPos(0x109, -13500, 0, -4730, 33)
    SetChrPos(0x105, -14610, 0, -4320, 33)
    OP_68(-13690, 2009, -2900, 0)
    MoveCamera(345, 9, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(16170, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00005FWhat is this\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FThere was a possibility of falling rocks,\x01",
            "Maybe a conflict here …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FAs far as spherical dents are concerned\x01",
            "It seems likely, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FWell …\x01",
            "It is in the middle of the recessed part\x01",
            "What is a wound like scratch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FBesides, when thinking carefully\x01",
            "It keeps a lot higher position\x01",
            "It looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FWell … … It's just a falling rock\x01",
            "I can not get such a bruise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FLet's keep going\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 4)
    OP_29(0xA8, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_263E")
    Call(0, 26)
    Return()

    label("loc_263E")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -13530, 0, -2950, 45)
    EventEnd(0x5)
    Jump("loc_26DB")

    label("loc_266A")

    TalkBegin(0xFF)

    ChrTalk(
        0x102,
        (
            "#00108FWell … … It's just a falling rock\x01",
            "I can not get such a bruise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FLet's keep going\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_26DB")

    Return()

    # Function_20_239F end

    def Function_21_26DC(): pass

    label("Function_21_26DC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_21_26DC end

    def Function_22_26EA(): pass

    label("Function_22_26EA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_22_26EA end

    def Function_23_26F8(): pass

    label("Function_23_26F8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_23_26F8 end

    def Function_24_2706(): pass

    label("Function_24_2706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF5")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A5")
    SetChrPos(0x101, -35490, 0, 7260, 0)
    SetChrPos(0x102, -38000, 0, 7070, 300)
    SetChrPos(0x103, -36900, 0, 7230, 330)
    SetChrPos(0x104, -34470, 0, 6820, 60)
    SetChrPos(0x109, -34930, 0, 5800, 60)
    SetChrPos(0x105, -36170, 0, 6550, 0)
    Jump("loc_2894")

    label("loc_27A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281F")
    SetChrPos(0x101, -55340, 0, 8020, 30)
    SetChrPos(0x102, -57740, 0, 8050, 330)
    SetChrPos(0x103, -56530, 0, 8270, 0)
    SetChrPos(0x104, -54080, 0, 7400, 60)
    SetChrPos(0x109, -56190, 0, 6600, 30)
    SetChrPos(0x105, -57360, 0, 7060, 300)
    Jump("loc_2894")

    label("loc_281F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2894")
    SetChrPos(0x101, -62900, 0, 8740, 0)
    SetChrPos(0x102, -65170, 0, 7220, 300)
    SetChrPos(0x103, -64310, 0, 8130, 330)
    SetChrPos(0x104, -61540, 0, 8920, 30)
    SetChrPos(0x109, -61980, 0, 7950, 60)
    SetChrPos(0x105, -63300, 0, 7610, 0)

    label("loc_2894")

    OP_68(-12460, 600, 9000, 0)
    MoveCamera(23, 46, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28500, 0)
    OP_68(-65230, 600, 11100, 11000)
    MoveCamera(23, 35, 0, 4000)
    Sleep(11500)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2916")
    OP_68(-35670, 600, 9060, 0)
    MoveCamera(14, 37, 0, 0)
    Jump("loc_2971")

    label("loc_2916")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2946")
    OP_68(-54950, 600, 10680, 0)
    MoveCamera(21, 22, 0, 0)
    Jump("loc_2971")

    label("loc_2946")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2971")
    OP_68(-63520, 600, 10610, 0)
    MoveCamera(353, 23, 0, 0)

    label("loc_2971")

    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00005FThe scars of this rock wall …\x01",
            "Do not hold it long enough.\x02\x03",
            "#00001FAnd one side is marked up\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FThere are marks that have also been scooped on the ground.\x01",
            "I wonder if I derailed to the left … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FBy the way, about the rock wall\x01",
            "What is this bluish color, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FApparently, some paint\x01",
            "It seems that it is attached … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0B")
    OP_68(-30920, 800, 4590, 3000)
    MoveCamera(76, 34, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(22500, 3000)
    Jump("loc_2B8A")

    label("loc_2B0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4D")
    OP_68(-30920, 800, 4590, 4000)
    MoveCamera(76, 34, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(22500, 3000)
    Jump("loc_2B8A")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B8A")
    OP_68(-30920, 800, 4590, 5000)
    MoveCamera(76, 34, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(22500, 5000)

    label("loc_2B8A")


    def lambda_2B8F():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2B8F)
    Sleep(50)

    def lambda_2B9F():
        OP_93(0xFE, 0x64, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B9F)
    Sleep(50)

    def lambda_2BAF():
        OP_93(0xFE, 0x6E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BAF)
    Sleep(50)

    def lambda_2BBF():
        OP_93(0xFE, 0x69, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2BBF)
    Sleep(50)

    def lambda_2BCF():
        OP_93(0xFE, 0x64, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BCF)
    Sleep(50)

    def lambda_2BDF():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BDF)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D4E")

    ChrTalk(
        0x109,
        (
            "#N#10100F#12PAs far as seeing the train ……\x01",
            "It is used for the car body\x01",
            "It looks like a blue paint.\x02\x03",
            "#10103FThe train and the rocky wall are in contact,\x01",
            "I ran as it was for a while …\x01",
            "It is likely to prove that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FOh, but … ….\x01",
            "Like a long dragged like this\x01",
            "Is it a scratch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#N#6P#00003FIn what situation\x01",
            "Whether such a scratch will occur, again\x01",
            "It seems necessary to think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EAA")

    label("loc_2D4E")

    SetMessageWindowPos(220, 140, -1, -1)

    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10100FAs far as seeing the train ……\x01",
            "It is used for the car body\x01",
            "It looks like a blue paint.\x02\x03",
            "#10103FThe train and the rocky wall are in contact,\x01",
            "I ran as it was for a while …\x01",
            "It is likely to prove that.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00301FOh, but … ….\x01",
            "Like a long dragged like this\x01",
            "Is it a scratch?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003FIn what situation\x01",
            "Whether such a scratch will occur, again\x01",
            "It seems necessary to think.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2EAA")

    OP_5A()
    SetScenarioFlags(0x17A, 5)
    OP_29(0xA8, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F70")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EFE")
    OP_68(-35670, 600, 9060, 0)
    MoveCamera(14, 37, 0, 0)
    Jump("loc_2F59")

    label("loc_2EFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2E")
    OP_68(-54950, 600, 10680, 0)
    MoveCamera(21, 22, 0, 0)
    Jump("loc_2F59")

    label("loc_2F2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F59")
    OP_68(-63520, 600, 10610, 0)
    MoveCamera(353, 23, 0, 0)

    label("loc_2F59")

    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Call(0, 26)
    Return()

    label("loc_2F70")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FA9")
    SetChrPos(0x0, -35980, 0, 7690, 339)
    Jump("loc_2FEE")

    label("loc_2FA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FCE")
    SetChrPos(0x0, -56210, 0, 8260, 24)
    Jump("loc_2FEE")

    label("loc_2FCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FEE")
    SetChrPos(0x0, -65200, 0, 8340, 294)

    label("loc_2FEE")

    EventEnd(0x5)
    Jump("loc_30AB")

    label("loc_2FF5")

    TalkBegin(0xFF)

    ChrTalk(
        0x109,
        (
            "#10100FPaints adhering to scars of the rock wall ……\x01",
            "Thinking from the situation and those of the train\x01",
            "I think you can declare it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn what situation\x01",
            "Whether such a scratch will occur, again\x01",
            "It seems necessary to think.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_30AB")

    Return()

    # Function_24_2706 end

    def Function_25_30AC(): pass

    label("Function_25_30AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, 10050, 0, -10800, 315)
    SetChrPos(0x102, 9850, 0, -11950, 315)
    SetChrPos(0x103, 11450, 0, -12190, 315)
    SetChrPos(0x104, 11600, 0, -10950, 315)
    SetChrPos(0x109, 10250, 0, -13300, 315)
    SetChrPos(0x105, 11600, 0, -13350, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3210")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Call(0, 3)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0x8, -800, 0, 6350, 180)
    SetChrPos(0x9, -2000, 0, 6350, 180)
    SetChrPos(0xA, -1400, 0, 4550, 0)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)

    label("loc_3210")

    OP_68(10700, 1300, -11950, 0)
    MoveCamera(315, 29, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19750, 0)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    SetCameraDistance(18750, 2500)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013F#12P…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#6PThis is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    ReplaceBGM("ed7205", "ed7151")
    Fade(1000)
    OP_68(-65000, 1500, -500, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(38750, 0)
    OP_68(-10000, 1500, -500, 15000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrPos(0x101, 6880, 0, -2350, 315)
    SetChrPos(0x104, 8500, 0, -4240, 315)
    SetChrPos(0x109, 7880, 0, -1770, 315)
    SetChrPos(0x102, 8189, 0, -3020, 315)
    SetChrPos(0x103, 7170, 0, -3840, 315)
    SetChrPos(0x105, 9130, 0, -2510, 315)
    OP_68(-1400, 1000, 5450, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19400, 0)
    SetCameraDistance(17900, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#02103F#6PNo, very serious accident\x01",
            "It has happened!\x02\x03",
            "#02101FWhat is the cause?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PAs you can see we're in the middle of an investigation\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PIf it can be considered, it falls to the track\x01",
            "It is tough that the leading car has derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02003F#11PI am sorry, but from here\x01",
            "Please take over on the mass communication.\x02\x03",
            "#02000FImmediate recovery work\x01",
            "I need to get started.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0x5A, 0x1F4)

    ChrTalk(
        0xA,
        "#02105F#6PHuh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PCommander, that is\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#02006F#12PAs a police, on-site verification\x01",
            "I understand your desire to give priority.\x02\x03",
            "#02001FBut this transit railroad\x01",
            "The aorta in the continental …\x02\x03",
            "Already the railroad corporation, the direction of the Imperial Republic,\x01",
            "Also from Mayor Dieter\x01",
            "Restoration of urgent urgent is requested.\x02\x03",
            "As we are the guards\x01",
            "We must respond to that request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PWell I know that already\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02101F#6PBut if you do not know the cause of the accident\x01",
            "There is a fear of recurrence … …?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#02003F#11PRegarding that,\x01",
            "It will only be parallel with recovery.\x02\x03",
            "#02001FAnyway at the latest, by evening\x01",
            "It is necessary to empty one side route.\x02\x03",
            "Until the next critical transport arrives\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PWait please!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_389B():
        OP_93(0x8, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_389B)
    Sleep(50)

    def lambda_38AB():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_38AB)
    Sleep(50)

    def lambda_38BB():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_38BB)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    Sleep(100)
    Fade(500)
    OP_68(3340, 1400, 1660, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20650, 0)
    OP_68(780, 1400, 3820, 3000)
    SetCameraDistance(20650, 3000)

    def lambda_3927():
        OP_9B(0x0, 0x101, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3927)
    Sleep(0)

    def lambda_393F():
        OP_9B(0x0, 0x109, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_393F)
    Sleep(0)

    def lambda_3957():
        OP_9B(0x0, 0x102, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3957)
    Sleep(0)

    def lambda_396F():
        OP_9B(0x0, 0x103, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_396F)
    Sleep(0)

    def lambda_3987():
        OP_9B(0x0, 0x104, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3987)
    Sleep(0)

    def lambda_399F():
        OP_9B(0x0, 0x105, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_399F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        "#02005F#11PYou guys…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#02105F#5POh it's Lloyd and his friends!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5POh you're here\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PUh, Commander…\x02\x03",
            "#10113FDo not do on-site verification\x01",
            "Are you going into restoration work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11PIf you belong to a guard as well\x01",
            "You will understand the importance of this route.\x02\x03",
            "#02001FAnd I don't want to have to say it but\x02\x03",
            "If recovery is delayed,\x01",
            "Just by that side of the Empire and Republic\x01",
            "It could lead to invitation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10111F#12PT-that is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#6PI can understand that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWell, as it is said\x01",
            "I can not get out too strongly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02106F#5PWell, but here\x01",
            "The mission is to pursue the truth … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#6PCommander Sonya\x02\x03",
            "#00001F30 minutes, until the heavy machine came\x01",
            "Will not we have the time?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#02005F#11PYou guys…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah, with the current crossbell\x01",
            "What this accident happened …\x02\x03",
            "#00001FVery much to myself,\x01",
            "I do not think it is mere coincidence.\x02\x03",
            "Is it really \"inevitability\"?\x01",
            "Should not you figure out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02001F#11P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PBy the example \"eidolon\"\x01",
            "There is also the possibility of damage … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PWell, even if you let me relax\x01",
            "Is not it something you want?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#02006F#11P… Well, what you have done with me\x01",
            "It seems that he was a little impatient.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#02002F#12P── Department of Donovan.\x01",
            "Let's give priority to on-site verification first.\x02\x03",
            "If the restoration work starts instead\x01",
            "I will focus on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PYes, no complaints here\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x2D, 0x1F4)

    ChrTalk(
        0xA,
        (
            "#02109F#6PUm, I hope.\x01",
            "We also interviewed … …\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#02003F#11PUntil restoration work begins\x01",
            "Please feel free.\x02\x03",
            "#02000FHowever, …\x01",
            "Do not disturb the site verification.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#02110F#6PYes, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PMr. Guard, our own\x01",
            "Even if you go into on-site verification?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_40FE():
        OP_93(0x8, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_40FE)
    Sleep(50)

    def lambda_410E():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_410E)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0xA, 0)

    ChrTalk(
        0x9,
        "#5PYes, let's split up\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5POh yeah, to the other side\x01",
            "The conductor that was on the train was absent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThe driver was brought to the hospital\x01",
            "You can hear the story at the time of the accident from him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6PRoger that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#12PWell then, begin the misison\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(21150, 1500)
    OP_6F(0x79)
    OP_0D()
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Call(0, 3)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    SetChrPos(0x0, -1000, 0, 1850, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x163, 1)
    OP_29(0xA8, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_25_30AC end

    def Function_26_42FB(): pass

    label("Function_26_42FB")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003FOkay, in general,\x01",
            "We gathered the necessary information.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_43D5():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_43D5)
    Sleep(50)

    def lambda_43E5():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_43E5)
    Sleep(50)

    def lambda_43F5():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_43F5)
    Sleep(50)

    def lambda_4405():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4405)
    Sleep(50)

    def lambda_4415():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4415)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#10105FHuh? Already\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FThat's our Lloyd\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI, ah, out of attitude\x01",
            "I did not understand the translation … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FSome of me also\x01",
            "I wonder if I have noticed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101Fwhat will you do?\x01",
            "Would you like to review the information immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh……\x01",
            "Let's call commanders and police.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Call(0, 27)
    Return()

    # Function_26_42FB end

    def Function_27_455F(): pass

    label("Function_27_455F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis257.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis258.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis259.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis260.itp")
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(852)
    SoundLoad(891)
    SetChrPos(0x101, 200, 0, 2550, 0)
    SetChrPos(0x102, -650, 0, 2100, 0)
    SetChrPos(0x103, 1500, 0, 2050, 0)
    SetChrPos(0x104, -800, 0, 1100, 0)
    SetChrPos(0x109, 850, 0, 1450, 0)
    SetChrPos(0x105, 1050, 0, 400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrPos(0x8, 0, 0, 4500, 180)
    SetChrPos(0x9, -1000, 0, 4750, 180)
    SetChrPos(0xA, 2250, 0, 4100, 225)
    SetChrPos(0xB, 800, 0, 4950, 180)
    SetChrPos(0xC, -900, 0, 5850, 180)
    SetChrPos(0xD, 600, 0, 6100, 180)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_68(90, 900, 3590, 0)
    MoveCamera(310, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21550, 0)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    SetCameraDistance(20650, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#02001F#11PWell ……\x01",
            "I wonder if there is anything found out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah, first, falling rocks etc.\x01",
            "It is a possibility that it fell to the railroad track … …\x02\x03",
            "#00001FIt can be denied first\x01",
            "I think that I can say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PWhy would that be\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThat is to support it\x01",
            "You have evidence?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, that is\x02",
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
            "#1KWhat is the basis for denying falling rocks?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Cry of the driver who the conductor heard\x01",          # 0
            "Lack of scratches at the tip of the locomotive\x01",            # 1
            "Large recessed trace on the right side of the locomotive\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_49AC"),
        (1, "loc_4ABE"),
        (2, "loc_4B3F"),
        (SWITCH_DEFAULT, "loc_4C7D"),
    )


    label("loc_49AC")


    ChrTalk(
        0x105,
        (
            "#10306F#6P─ ─ No, in itself\x01",
            "Is not it a falsification of falling rocks?\x02\x03",
            "#10301FSuddenly falling rock falls in the direction of travel\x01",
            "There is also a possibility of screaming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PWe found some dubious evidence but\x02\x03",
            "#00013F… and so on, after all\x01",
            "There is little scratches at the tip of the locomotive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#6POh, I think so too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C7D")

    label("loc_4ABE")

    OP_2C(0xA8, 0x2)

    ChrTalk(
        0x101,
        (
            "#00003F#6PVarious, dubious evidence\x01",
            "I have been found … ….\x02\x03",
            "#00013FWhat is decisive is that the\x01",
            "I think that it is less scratch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C7D")

    label("loc_4B3F")

    OP_2C(0xA8, 0x1)

    ChrTalk(
        0x105,
        (
            "#10306F#6P─ ─ No, indeed it is\x01",
            "It may be an important clue\x01",
            "Is not it a falsification of falling rocks?\x02\x03",
            "#10300FA falling rock falls from the cliff on the right side\x01",
            "There is also the possibility of bumping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PWe found some dubious evidence but\x02\x03",
            "#00013F… and so on, after all\x01",
            "There is little scratches at the tip of the locomotive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#6POh, I think so too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C7D")

    label("loc_4C7D")


    ChrTalk(
        0x8,
        "#02005F#11PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07901F#11PCertainly, at the tip of the locomotive\x01",
            "Especially there were no scratches … …\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    SetMessageWindowPos(300, 200, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003FUsually, when derailing with falling rocks,\x01",
            "The rock that fell on the railway is the top car\x01",
            "I think that it is a case of collision.\x02\x03",
            "As a result, I got on speed\x01",
            "Huge mass breaks the balance,\x01",
            "Get off the track and derail … …\x02\x03",
            "#00001FApart from that, so far\x01",
            "Derailing should be difficult to think.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    ChrTalk(
        0xA,
        "#02101F#12POh, I see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PNevertheless at the tip of the locomotive\x01",
            "I can not find a scratchy scar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThe most likely possibility\x01",
            "Is it because it disappears first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11P… … process.\x01",
            "It certainly can not be overlooked.\x02\x03",
            "#02001FThen, other thoughts\x01",
            "Is there a possibility of derailment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PYes……\x01",
            "At first, some explosives\x01",
            "I thought that it was used.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4F96():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4F96)
    Sleep(50)

    def lambda_4FA6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4FA6)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x102,
        "#00101F#5PTh-that is!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#6PSome armed group\x01",
            "They said they had terrorism work … …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6P─ ─ No, the possibilities are\x01",
            "I thought first of all.\x02\x03",
            "#00301FI tried overlooking the whole street\x01",
            "Apparently explosives\x01",
            "There was no evidence that it was used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07906F#11PWell, for now\x01",
            "I have not found it either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PIn that case\x01",
            "If it can be thought of elsewhere ……\x02\x03",
            "#00013FTo \"something\" from the right side of the locomotive\x01",
            "It probably was hurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        "#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHowever,\x01",
            "Such a muffler …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02105F#12PIf it is a car race dead heat\x01",
            "There seems to be such a thing ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00203F#12PI see…\x02\x03",
            "#00201FIt was on the right side of the locomotive\x01",
            "It is a dented part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5POh, maybe this kind of thing\x01",
            "I guess it happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 0, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003FThat \"something\" is the train\x01",
            "I got off to the side of the locomotive.\x02\x03",
            "#00001FThe screams the driver offered raised\x01",
            "Perhaps, it will be at that time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 200, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00008F\"Something\" is running as it is\x01",
            "Hit the body from the right side of the locomotive … …\x02\x03",
            "Vector from the side was added\x01",
            "The locomotive will derail on the left side.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(0, 200, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00013FAnd \"something\" locomotives\x01",
            "Continue to press on the rock wall on the left … …\x02\x03",
            "In a leave behind a long scar on the rock wall\x01",
            "I finally stopped.\x02\x03",
            "#00003FAnd the following passenger is like this\x01",
            "It was to derail in disjointed form.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x9)
    OP_64(0xC)
    OP_64(0x8)
    OP_64(0xB)
    OP_64(0xA)
    OP_64(0xD)

    ChrTalk(
        0x101,
        (
            "#00000F#6P…… for the time being\x01",
            "It is a hypothesis at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PRight….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#07902F#11PExcellent\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PNo, I got to reasoning,\x01",
            "You broke your brother, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02104F#12Psurely……\x01",
            "Gai is more intuitive\x01",
            "It was a type to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6POi oi that's some high praise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5PHehu ……\x01",
            "It is sort of proud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PWhew, I too\x01",
            "I wonder if I could not summarize it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02004F#11PHa, not bad\x02\x03",
            "#02001FSo then Lloyd\x02\x03",
            "What I said was \"something\"\x01",
            "Is it still a monster?\x02\x03",
            "Or maybe one of those Cryptids we've seen\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PRight…\x02",
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
            "#1KWhat is \"something\" that caused the accident?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Possibility of \"Phantom beast\" is high\x01",      # 0
            "I can not yet affirm\x01",          # 1
        )
    )

    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis261.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis262.itp")
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A76"),
        (1, "loc_5C05"),
        (SWITCH_DEFAULT, "loc_5D6E"),
    )


    label("loc_5A76")


    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah, traveling train\x01",
            "It is enough to be derailed\x01",
            "He is the owner of power.\x02\x03",
            "#00001FThink of it as a big eid beast\x01",
            "I think that it is the most natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#12PBut, Mr. Lloyd.\x02\x03",
            "#00200FTo the extent that a phantom beast appeared\x01",
            "I do not feel the sign of the superordinate attribute, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PI see, it was there ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11P…… Hmm, I was in a report yesterday.\x01",
            "\"Blue flower\" does not seem to bloom … …\x02\x03",
            "#02008FSo then what was it\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D6E")

    label("loc_5C05")

    OP_2C(0xA8, 0x1)

    ChrTalk(
        0x101,
        (
            "#00006F#6PCertainly, the train to travel\x01",
            "It is enough to be derailed\x01",
            "He is the owner of power.\x02\x03",
            "#00008FThink of it as a big eid beast\x01",
            "I think that it is nature … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PBut, despite the appearance of a phantom beast\x01",
            "I do not feel the sign of the superordinate attribute ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#6PThat \"blue flower\" also\x01",
            "It looks like they are not blooming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11PThat's right…\x02\x03",
            "#02008FSo then what was it\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D6E")

    label("loc_5D6E")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#6P(If you can think elsewhere\x01",
            "Although it would be a puppet weapon of \"association\" … …)\x02\x03",
            "#00008F(Could it really move like that?)\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    Sound(891, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(2000)
    CancelBlur(1000)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#07905F#11PWhat was that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PA monster's cry?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PThat's it.\x01",
            "It feels too creepy … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PI will activate my sensors\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(300)
    OP_68(600, 900, 3450, 1500)

    def lambda_6078():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6078)

    def lambda_6085():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6085)

    def lambda_6092():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6092)

    def lambda_609F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_609F)

    def lambda_60AC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_60AC)

    def lambda_60B9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_60B9)

    def lambda_60C6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_60C6)

    def lambda_60D3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_60D3)

    def lambda_60E0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_60E0)

    def lambda_60ED():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_60ED)

    def lambda_60FA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_60FA)

    def lambda_6107():
        OP_95(0xFE, 2500, 0, 2050, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6107)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x103, 3, 0, 28)
    Sleep(3000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(200)
    OP_93(0xA, 0x0, 0x1F4)
    Sleep(100)
    OP_93(0xA, 0x10E, 0x1F4)
    Sleep(200)
    TurnDirection(0xA, 0xD, 500)

    ChrTalk(
        0xA,
        (
            "#02101F#6PWhere, where is it?\x02\x03",
            "Rains,\x01",
            "Somehow put it in the camera!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PPlease do not be uncomfortable ~!\x02",
    )

    CloseMessageWindow()
    Sound(891, 0, 50, 0)
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x103, 3)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    ReplaceBGM("ed7205", "ed7203")
    ReplaceBGM("ed7250", "ed7203")
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#00207F#12P─ ─ Distance 10 Serge!\x01",
            "I will move further to the west … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#5PUgh..\x02\x03",
            "#00007FEveryone, we're going after it\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#5PYeah, after you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PRoger that\x02",
    )

    CloseMessageWindow()

    def lambda_62F4():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_62F4)
    Sleep(50)

    def lambda_6304():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6304)
    Sleep(50)

    def lambda_6314():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_6314)
    Sleep(50)

    def lambda_6324():
        OP_93(0xB, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_6324)
    Sleep(50)

    def lambda_6334():
        OP_93(0xC, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6334)
    Sleep(50)

    def lambda_6344():
        OP_93(0xD, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6344)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)

    ChrTalk(
        0x9,
        "#5POi oi don't overdo it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#07907F#11PThe guard force will support!\x02",
    )

    CloseMessageWindow()

    def lambda_63B1():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_63B1)
    Sleep(50)

    def lambda_63C1():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_63C1)
    Sleep(50)

    def lambda_63D1():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_63D1)
    Sleep(50)

    def lambda_63E1():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_63E1)
    Sleep(50)

    def lambda_63F1():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_63F1)
    Sleep(50)

    def lambda_6401():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6401)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00013F#6PNo, there\x01",
            "Please concentrate on restoration work!\x02\x03",
            "We will pursue first\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#07906F#11PUgh, I suppose\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02003F#11P…… Heavy equipment arrives soon.\x01",
            "It seems that I only have to give up with your words.\x02\x03",
            "#02001FIf something happens I can rush\x01",
            "Be sure to contact them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#6PRoger that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F#6P…\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(21650, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_24(0x354)
    SetScenarioFlags(0x22, 1)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_455F end

    def Function_28_65B1(): pass

    label("Function_28_65B1")

    Sound(2192, 255, 80, 0)
    Sleep(800)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sound(812, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(357, 0, 70, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xFE, 0x5, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    label("loc_6650")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_666D")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("loc_6650")

    label("loc_666D")

    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Fade(250)
    Sound(812, 0, 100, 0)
    StopSound(852, 500, 100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_28_65B1 end

    SaveToFile()

Try(main)
