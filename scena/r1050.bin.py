from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Commander Sonya",        # 1
        "Inspector Donovan",      # 2
        "Grace",                  # 3
        "2nd Lt. Mireille",       # 4
        "Detective Raymond",      # 5
        "Reins",                  # 6
        "Policeman",              # 7
        "Policeman",              # 8
        "Policeman",              # 9
        "CGF Member",             # 10
        "CGF Member",             # 11
        "CGF Member",             # 12
        "CGF Member",             # 13
        "Conductor",              # 14
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
        "Function_5_E0C",          # 05, 5
        "Function_6_EFD",          # 06, 6
        "Function_7_11EE",         # 07, 7
        "Function_8_15C4",         # 08, 8
        "Function_9_1832",         # 09, 9
        "Function_10_1A55",        # 0A, 10
        "Function_11_1C02",        # 0B, 11
        "Function_12_1EEF",        # 0C, 12
        "Function_13_1F8A",        # 0D, 13
        "Function_14_202D",        # 0E, 14
        "Function_15_20D9",        # 0F, 15
        "Function_16_218F",        # 10, 16
        "Function_17_2265",        # 11, 17
        "Function_18_2323",        # 12, 18
        "Function_19_239F",        # 13, 19
        "Function_20_27C2",        # 14, 20
        "Function_21_2B4E",        # 15, 21
        "Function_22_2B5C",        # 16, 22
        "Function_23_2B6A",        # 17, 23
        "Function_24_2B78",        # 18, 24
        "Function_25_3606",        # 19, 25
        "Function_26_4A5B",        # 1A, 26
        "Function_27_4D19",        # 1B, 27
        "Function_28_7134",        # 1C, 28
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4E")
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
        "*sigh*, what a bad time I had.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I still have it good \x01",
            "to be unscathed compared to\x01",
            "those who were carried away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who would've thought a train\x01",
            "could derail like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYou look to be the\x01",
            "train conductor.\x02\x03",
            "#00000FIf you don't mind, could you tell us what \x01",
            "happened at the time of the accident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, if you want me to tell you,\x01",
            "I'll tell you everything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't give a decent talk to the officer\x01",
            "there when I was asked before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, it happened\x01",
            "all of a sudden, you see.\x01",
            "I was a little confused...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FUhhm, it's such an accident,\x01",
            "it can't be helped if you can't\x01",
            "remember it clearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FI think he was shocked\x01",
            "by the accident too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FIn this occasion, we don't mind\x01",
            "even a small thing.\x02\x03",
            "#00001FWasn't there anything\x01",
            "you found suspicious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Suspicious...\x01",
            "Uhhhm...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Ah, now that I think about it...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305F#6PDid something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just before the derailment accident, I\x01",
            "was having a call with the driver and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Suddenly he yelled.\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xFE,
        ""Waaah, what's that!?"...he said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The accident happened right after that.\x01",
            "The first carriage derailed and then the\x01",
            "following ones too, one after the other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And that...\x01",
            "Bring us to where we are now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200F"Waaah, what's that!?"...\x01",
            "A yell like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FA line just like he caught sight of\x01",
            "an unbelievable thing or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI wonder what the\x01",
            "driver saw...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 6)
    OP_29(0xA8, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D22")
    Call(0, 26)
    Return()

    label("loc_D22")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -50180, 0, -17560, 257)
    EventEnd(0x5)
    Jump("loc_E0B")

    label("loc_D4E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Just before the derailment accident,\x01",
            "when I was having a call with the \x01",
            "driver, he suddenly yelled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Waah, what's that!?"...he said.\x01",
            "The accident happened right after that.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_E0B")

    Return()

    # Function_4_65A end

    def Function_5_E0C(): pass

    label("Function_5_E0C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2A")
    Call(0, 11)
    Jump("loc_EF9")

    label("loc_E2A")


    ChrTalk(
        0xFE,
        (
            "#02003FUntil the heavy machineries\x01",
            "arrive, we CGF will cooperate\x01",
            "with the on-site inspection too.\x02\x03",
            "#02000FI've given detailed instructions\x01",
            "to the members too, so be free \x01",
            "to conduct your investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF9")

    TalkEnd(0xFE)
    Return()

    # Function_5_E0C end

    def Function_6_EFD(): pass

    label("Function_6_EFD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1144")

    ChrTalk(
        0xFE,
        (
            "Oh boy, looking at it again,\x01",
            "it was a hell of an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad that in this there\x01",
            "was not even one dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAlmost all passengers were\x01",
            "transferred to the Republic or\x01",
            "carried to the hospital, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIf possible, I would've liked\x01",
            "to hear things from them too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it can't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, right. Did you inquire with the\x01",
            "conductor who's resting over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When we talked to him just before,\x01",
            "we couldn't get important information,\x01",
            "but maybe now he remembered something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't forget to speak with him.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 2)
    Jump("loc_11EA")

    label("loc_1144")


    ChrTalk(
        0xFE,
        (
            "Did you inquire with the\x01",
            "conductor who's resting over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't forget to inquire with all the\x01",
            "persons from whom you can hear\x01",
            "things about the accident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EA")

    TalkEnd(0xFE)
    Return()

    # Function_6_EFD end

    def Function_7_11EE(): pass

    label("Function_7_11EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14DE")

    ChrTalk(
        0xFE,
        (
            "#02102FSo, Lloyd. Did you figure\x01",
            "out something new?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, I can't say anything yet.\x02\x03",
            "#00001FMiss Grace, is there\x01",
            "anything you noticed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02106FUhhm, let's see. Sometimes in\x01",
            "train accidents it happens, but...\x02\x03",
            "#02101FI think that this time, really,\x01",
            "both timing and place were\x01",
            "too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F...You're right.\x01",
            "In addition, we're at a time when \x01",
            "a state of emergency due to the \x01",
            "independence proposal is going on...\x02\x03",
            "#00103FIt's also possible that it was\x01",
            "planned on purpose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02106FWell, I'm talking without proofs,\x01",
            "so I don't intend to push my\x01",
            "ideas on you.\x02\x03",
            "#02109FAt any rate, do your best with\x01",
            "the investigation! And if you find\x01",
            "something, let me use it as data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHa ha, understood.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x17B, 1)
    Jump("loc_15C0")

    label("loc_14DE")


    ChrTalk(
        0xFE,
        (
            "#02103FSometimes in train accidents it happens, but...\x01",
            "This time, the timing and place were the worst.\x02\x03",
            "#02109FWell, in any case, do your best\x01",
            "with the investigation! And if you find\x01",
            "something, let me use it as data, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C0")

    TalkEnd(0xFE)
    Return()

    # Function_7_11EE end

    def Function_8_15C4(): pass

    label("Function_8_15C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C2")

    ChrTalk(
        0x104,
        (
            "#00300FMireille, how are your\x01",
            "repair works goin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#07901FWell, they're proceeding side by\x01",
            "side with your investigation, but...\x02\x03",
            "#07906FAs expected, we're in a fix\x01",
            "unless we move the train itself\x01",
            "using some heavy machinery.\x02\x03",
            "#07900FFor the time being, we're removing the\x01",
            "broken pieces scattered around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FAs I thought, we should help too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#07904FNo, there's no need.\x01",
            "You should focus on\x01",
            "the investigation.\x02\x03",
            "#07902FWe too will inform you if\x01",
            "we find out something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 4)
    Jump("loc_182E")

    label("loc_17C2")


    ChrTalk(
        0xFE,
        (
            "#07904FYou should focus on\x01",
            "the investigation.\x02\x03",
            "#07902FWe too will inform you if\x01",
            "we find out something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182E")

    TalkEnd(0xFE)
    Return()

    # Function_8_15C4 end

    def Function_9_1832(): pass

    label("Function_9_1832")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BB")

    ChrTalk(
        0xFE,
        (
            "Well, we checked what we could inside\x01",
            "the derailed railroad cars too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that there were no\x01",
            "important clues inside there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FWasn't there anything\x01",
            "suspicious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, there were only the\x01",
            "passengers' luggages.\x01",
            "There was nothing especially suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no doubt the\x01",
            "accident happened\x01",
            "due to an external cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FHmm...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 3)
    Jump("loc_1A51")

    label("loc_19BB")


    ChrTalk(
        0xFE,
        (
            "It seems there were no\x01",
            "important clues inside the \x01",
            "derailed railroad cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no doubt the\x01",
            "accident happened\x01",
            "due to an external cause.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A51")

    TalkEnd(0xFE)
    Return()

    # Function_9_1832 end

    def Function_10_1A55(): pass

    label("Function_10_1A55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B58")

    ChrTalk(
        0xFE,
        (
            "*sigh*, when it comes down to such an\x01",
            "accident scene, it's a shock even just looking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, in order to get the truth,\x01",
            "I must take a lot of good pictures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It often happens that\x01",
            "one picture becomes\x01",
            "some kind of evidence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BFE")

    label("loc_1B58")


    ChrTalk(
        0xFE,
        (
            "Collecting data on accident\x01",
            "scenes is shocking, but...\x01",
            "I must take a lot of good pictures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It often happens that\x01",
            "one picture becomes\x01",
            "some kind of evidence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFE")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A55 end

    def Function_11_1C02(): pass

    label("Function_11_1C02")

    OP_4B(0x8, 0x0)
    OP_4B(0x11, 0x0)
    OP_4B(0x12, 0x0)

    ChrTalk(
        0x8,
        (
            "#02000FYou, how much time seem it's \x01",
            "going to take until the heavy \x01",
            "machineries arrive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, they're scheduled to\x01",
            "arrive in not even 30 minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Still, with the investigation\x01",
            "taking time, will it be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If we can't restore one side of the \x01",
            "railroad tracks by evening, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02005FThen...?\x01",
            "There's no need to worry about that.\x02\x03",
            "#02001FWe absolutely\x01",
            "have to do it\x01",
            "at all costs.\x02\x03",
            "#02003F...You too understand\x01",
            "that, am I not right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P#1KY-Yes ma'am!!\x02",
    )


    ChrTalk(
        0x12,
        "#6P#1KY-Yes ma'am!!\x02",
    )

    OP_57(0x1)
    OP_5A()

    ChrTalk(
        0x104,
        "#00306F(Spartan as always...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F(Typical of Commander Sonya.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(She gave us a chance\x01",
            "at great pain...)\x02\x03",
            "#00001F(We must ascertain the accident\x01",
            "cause no matter what.)\x02",
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

    # Function_11_1C02 end

    def Function_12_1EEF(): pass

    label("Function_12_1EEF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Uhhm, getting too close\x01",
            "seems to be dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now it's retaining its balance, but what\x01",
            "if it were to fall for a reason or another?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1EEF end

    def Function_13_1F8A(): pass

    label("Function_13_1F8A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*siiigh*, glass and other stuff\x01",
            "is scattered all around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's dangerous if even one pebble\x01",
            "is on the railway tracks so I must\x01",
            "pick them all up.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1F8A end

    def Function_14_202D(): pass

    label("Function_14_202D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "To think it ended up derailing on\x01",
            "both sides of the tracks like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure the passengers who were travelling\x01",
            "or returning home must've been afraid.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_202D end

    def Function_15_20D9(): pass

    label("Function_15_20D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_218B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F7")
    Call(0, 11)
    Jump("loc_218B")

    label("loc_20F7")


    ChrTalk(
        0xFE,
        (
            "The heavy machineries are scheduled\x01",
            "to arrive in not even 30 minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until then, we have to advance the\x01",
            "repair works even just a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218B")

    TalkEnd(0xFE)
    Return()

    # Function_15_20D9 end

    def Function_16_218F(): pass

    label("Function_16_218F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_2261")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21AD")
    Call(0, 11)
    Jump("loc_2261")

    label("loc_21AD")


    ChrTalk(
        0xFE,
        (
            "The investigation is needed, but the\x01",
            "scheduled can't be delayed, eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, nothing we can do about it.\x01",
            "It's going to be dreadfully tough,\x01",
            "but we can only do our best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2261")

    TalkEnd(0xFE)
    Return()

    # Function_16_218F end

    def Function_17_2265(): pass

    label("Function_17_2265")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "When we were contacted,\x01",
            "I didn't imagine that it was\x01",
            "this much of an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems a considerable number of materials\x01",
            "too will be needed to repair the railroad tracks.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2265 end

    def Function_18_2323(): pass

    label("Function_18_2323")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The railroad tracks ended up\x01",
            "being greatly torn to pieces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess the derailment has\x01",
            "begun around here...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2323 end

    def Function_19_239F(): pass

    label("Function_19_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2725")
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
        "#12P#00100FThis car is the locomotive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FIt is the most important car\x01",
            "to have an orbal train run.\x02\x03",
            "#00200FInside there should be an orbal\x01",
            "engine for train made by the\x01",
            "Reinford Corp. and the driver's cab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10305FHm, even so, isn't there\x01",
            "something a little off, somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FYeah, I feel it's got way less\x01",
            "damage than you'd think it should.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FI-Indeed...\x01",
            "It seems a little unnatural\x01",
            "since it's the first carriage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah...\x01",
            "If it collided against something from\x01",
            "the front, it shouldn't be this clean.\x02\x03",
            "#00008FAnd so, it seems that the derailment\x01",
            "cause lies elsewhere...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 3)
    OP_29(0xA8, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26F9")
    Call(0, 26)
    Return()

    label("loc_26F9")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -6920, 0, -2370, 315)
    EventEnd(0x5)
    Jump("loc_27C1")

    label("loc_2725")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00003FIf it collided against something from\x01",
            "the front, it shouldn't be this clean.\x02\x03",
            "#00008FAnd so, the derailment\x01",
            "cause should lie elsewhere...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_27C1")

    Return()

    # Function_19_239F end

    def Function_20_27C2(): pass

    label("Function_20_27C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD0")
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
        "#6P#00005FWhat's...that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FIt's possible it was a fallen rock...\x01",
            "Could it be that it collided here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FJudging by the spherical dent,\x01",
            "it seems likely, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FUhhm...then, what's with the\x01",
            "scratches-like marks right in\x01",
            "the center of the dented part?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FAlso, thinking twice about it,\x01",
            "it seems they're positioned\x01",
            "quite high, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FUhhm...a simple fallen rock\x01",
            "shouldn't leave such marks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FWhat in the world collided with it...?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 4)
    OP_29(0xA8, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AA4")
    Call(0, 26)
    Return()

    label("loc_2AA4")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -13530, 0, -2950, 45)
    EventEnd(0x5)
    Jump("loc_2B4D")

    label("loc_2AD0")

    TalkBegin(0xFF)

    ChrTalk(
        0x102,
        (
            "#00108FUhhm...a simple fallen rock\x01",
            "shouldn't leave such marks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FWhat in the world collided with it...?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_2B4D")

    Return()

    # Function_20_27C2 end

    def Function_21_2B4E(): pass

    label("Function_21_2B4E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_21_2B4E end

    def Function_22_2B5C(): pass

    label("Function_22_2B5C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_22_2B5C end

    def Function_23_2B6A(): pass

    label("Function_23_2B6A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_23_2B6A end

    def Function_24_2B78(): pass

    label("Function_24_2B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351B")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C17")
    SetChrPos(0x101, -35490, 0, 7260, 0)
    SetChrPos(0x102, -38000, 0, 7070, 300)
    SetChrPos(0x103, -36900, 0, 7230, 330)
    SetChrPos(0x104, -34470, 0, 6820, 60)
    SetChrPos(0x109, -34930, 0, 5800, 60)
    SetChrPos(0x105, -36170, 0, 6550, 0)
    Jump("loc_2D06")

    label("loc_2C17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C91")
    SetChrPos(0x101, -55340, 0, 8020, 30)
    SetChrPos(0x102, -57740, 0, 8050, 330)
    SetChrPos(0x103, -56530, 0, 8270, 0)
    SetChrPos(0x104, -54080, 0, 7400, 60)
    SetChrPos(0x109, -56190, 0, 6600, 30)
    SetChrPos(0x105, -57360, 0, 7060, 300)
    Jump("loc_2D06")

    label("loc_2C91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D06")
    SetChrPos(0x101, -62900, 0, 8740, 0)
    SetChrPos(0x102, -65170, 0, 7220, 300)
    SetChrPos(0x103, -64310, 0, 8130, 330)
    SetChrPos(0x104, -61540, 0, 8920, 30)
    SetChrPos(0x109, -61980, 0, 7950, 60)
    SetChrPos(0x105, -63300, 0, 7610, 0)

    label("loc_2D06")

    OP_68(-12460, 600, 9000, 0)
    MoveCamera(23, 46, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28500, 0)
    OP_68(-65230, 600, 11100, 11000)
    MoveCamera(23, 35, 0, 4000)
    Sleep(11500)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D88")
    OP_68(-35670, 600, 9060, 0)
    MoveCamera(14, 37, 0, 0)
    Jump("loc_2DE3")

    label("loc_2D88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB8")
    OP_68(-54950, 600, 10680, 0)
    MoveCamera(21, 22, 0, 0)
    Jump("loc_2DE3")

    label("loc_2DB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE3")
    OP_68(-63520, 600, 10610, 0)
    MoveCamera(353, 23, 0, 0)

    label("loc_2DE3")

    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00005FThe scars on this wall of rock...\x01",
            "They're quite big.\x02\x03",
            "#00001FIt's like the whole surface was hollowed out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FThere're hollowed out marks on the ground too.\x01",
            "Maybe it means it derailed to the left side...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FBy the way, I wonder what is this azure-like\x01",
            "color stucked to the wall of rock...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIt appears some kind of painting\x01",
            "material is sticking to it...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD3")
    OP_68(-30920, 800, 4590, 3000)
    MoveCamera(76, 34, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(22500, 3000)
    Jump("loc_3052")

    label("loc_2FD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3015")
    OP_68(-30920, 800, 4590, 4000)
    MoveCamera(76, 34, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(22500, 3000)
    Jump("loc_3052")

    label("loc_3015")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3052")
    OP_68(-30920, 800, 4590, 5000)
    MoveCamera(76, 34, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(22500, 5000)

    label("loc_3052")


    def lambda_3057():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3057)
    Sleep(50)

    def lambda_3067():
        OP_93(0xFE, 0x64, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3067)
    Sleep(50)

    def lambda_3077():
        OP_93(0xFE, 0x6E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3077)
    Sleep(50)

    def lambda_3087():
        OP_93(0xFE, 0x69, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3087)
    Sleep(50)

    def lambda_3097():
        OP_93(0xFE, 0x64, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3097)
    Sleep(50)

    def lambda_30A7():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30A7)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3245")

    ChrTalk(
        0x109,
        (
            "#N#10100F#12PLooking at the train...\x01",
            "It seems the azure color paint\x01",
            "used on the railroad cars.\x02\x03",
            "#10103FThe train touched the wall of rock and\x01",
            "ran like that for a little while...\x01",
            "That seems proof of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FYeah, but...\x01",
            "Did it drag along so much\x01",
            "to cause these marks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#N#6P#00003FIt seems we need to rethink\x01",
            "about under which situation\x01",
            "these marks were caused.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D0")

    label("loc_3245")

    SetMessageWindowPos(220, 140, -1, -1)

    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10100FLooking at the train...\x01",
            "It seems the azure color paint\x01",
            "used on the railroad cars.\x02\x03",
            "#10103FThe train touched the wall of rock and\x01",
            "ran like that for a little while...\x01",
            "That seems proof of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00301FYeah, but...\x01",
            "Did it drag along so much\x01",
            "to cause these marks?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003FIt seems we need to rethink\x01",
            "about under which situation\x01",
            "these marks were caused.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_33D0")

    OP_5A()
    SetScenarioFlags(0x17A, 5)
    OP_29(0xA8, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3496")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3424")
    OP_68(-35670, 600, 9060, 0)
    MoveCamera(14, 37, 0, 0)
    Jump("loc_347F")

    label("loc_3424")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3454")
    OP_68(-54950, 600, 10680, 0)
    MoveCamera(21, 22, 0, 0)
    Jump("loc_347F")

    label("loc_3454")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347F")
    OP_68(-63520, 600, 10610, 0)
    MoveCamera(353, 23, 0, 0)

    label("loc_347F")

    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Call(0, 26)
    Return()

    label("loc_3496")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34CF")
    SetChrPos(0x0, -35980, 0, 7690, 339)
    Jump("loc_3514")

    label("loc_34CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34F4")
    SetChrPos(0x0, -56210, 0, 8260, 24)
    Jump("loc_3514")

    label("loc_34F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3514")
    SetChrPos(0x0, -65200, 0, 8340, 294)

    label("loc_3514")

    EventEnd(0x5)
    Jump("loc_3605")

    label("loc_351B")

    TalkBegin(0xFF)

    ChrTalk(
        0x109,
        (
            "#10100FThe paint stuck to the wall of rock marks...\x01",
            "Judging from the situation, I think we\x01",
            "can conclude that it's from the train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt seems we need to rethink\x01",
            "about under which situation\x01",
            "these marks were caused.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_3605")

    Return()

    # Function_24_2B78 end

    def Function_25_3606(): pass

    label("Function_25_3606")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_376A")
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

    label("loc_376A")

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
        "#00013F#12P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#6PM-My...\x02",
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
            "#02103F#6PWeeell, what a terrible\x01",
            "accident has happened!\x02\x03",
            "#02101FAnd exactly, the derailment accident cause is...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PAs you can see, it's currently under investigation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAll we can think of is that the first carriage has\x01",
            "derailed due to a fallen rock on the tracks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02003F#11PI'm sorry, but I beg the mass\x01",
            "media to retire from here.\x02\x03",
            "#02000FWe need to begin the\x01",
            "repair works immediately.\x02",
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
        "#02105F#6PEEH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PCommander, that's...\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#02006F#12PAs police, I understand you would like\x01",
            "to prioritize the on-site inspection.\x02\x03",
            "#02001FHowever, the transcontinental railway is an\x01",
            "important traffic route for the Zemuria continent...\x02\x03",
            "It has been already requested to be repaired\x01",
            "ASAP from the railway corporation, both the \x01",
            "Empire and Republic and Mayor Dieter too.\x02\x03",
            "As CGF, we must comply\x01",
            "to those requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PWell, I understand the logic, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02101F#6PBut if you don't understand the cause,\x01",
            "don't you fear it could happen again?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#02003F#11PIn regard to that, we can only\x01",
            "do it in parallel to the repairs.\x02\x03",
            "#02001FAt any rate, by evening at latest, we\x01",
            "must open a side of the railway tracks.\x02\x03",
            "Before the arranged machineries arrive, we──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PPlease wait!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3ED2():
        OP_93(0x8, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3ED2)
    Sleep(50)

    def lambda_3EE2():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3EE2)
    Sleep(50)

    def lambda_3EF2():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3EF2)
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

    def lambda_3F5E():
        OP_9B(0x0, 0x101, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F5E)
    Sleep(0)

    def lambda_3F76():
        OP_9B(0x0, 0x109, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F76)
    Sleep(0)

    def lambda_3F8E():
        OP_9B(0x0, 0x102, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F8E)
    Sleep(0)

    def lambda_3FA6():
        OP_9B(0x0, 0x103, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3FA6)
    Sleep(0)

    def lambda_3FBE():
        OP_9B(0x0, 0x104, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3FBE)
    Sleep(0)

    def lambda_3FD6():
        OP_9B(0x0, 0x105, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3FD6)
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
        "#02005F#11PYou all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#02105F#5POh, Lloyd and company?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5POoh, so you've come, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PExcuse me, Commander...\x02\x03",
            "#10113FYou're doing repair works without\x01",
            "even an on-site inspection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11PYou too, being a CGF member, know the\x01",
            "importance of this railway, right?\x02\x03",
            "#02001FI wouldn't want to say this, but...\x02\x03",
            "If we're late with the repairs, \x01",
            "we could be liable to be interfering\x01",
            "with the Empire and Republic.\x02",
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
        "#10111F#12PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#6P...You made your due considerations.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P*sigh*, if we got told that, we too\x01",
            "couldn't take the strong hand with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02106F#5PHmm, however, we have a mission\x01",
            "to inquiry about the truth...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#6P──Commander Sonya.\x02\x03",
            "#00001FCould you give us 30 minutes, no, just\x01",
            "until the heavy machineries arrive?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#02005F#11PTo you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYes. This accident happened in\x01",
            "the current Crossbell condition...\x02\x03",
            "#00001FTo me, I can't think this is\x01",
            "just a simple coincidence.\x02\x03",
            "I want to see if it wasn't\x01",
            "really "inevitable".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02001F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PThere could also be damage\x01",
            "from those "Cryptids"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PWell, isn't it alright to leave this to\x01",
            "us even just for conscience' sake?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#02006F#11P...Right, it seems I, of all people,\x01",
            "have been a little bit impatient.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#02002F#12P──Inspector Donovan.\x01",
            "Let's prioritize the on-site inspection first.\x02\x03",
            "On the other hand, when the repair works\x01",
            "begin, we will have you focus on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PYes, we too don't have any objections.\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x2D, 0x1F4)

    ChrTalk(
        0xA,
        (
            "#02109F#6PExcuse meeee... If possible,\x01",
            "I'd like to collect data too...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#02003F#11PFeel free to, until the\x01",
            "repair works begin.\x02\x03",
            "#02000FHowever... Do not interfere\x01",
            "with the on-site inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#02110F#6PYes, that's a given!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PInspector, can you let us join\x01",
            "the on-site inspection too?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_482F():
        OP_93(0x8, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_482F)
    Sleep(50)

    def lambda_483F():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_483F)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0xA, 0)

    ChrTalk(
        0x9,
        "#5PYeah, let's split the job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5POh, right, the conductor who was\x01",
            "on the train is resting over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThe driver has been take to the hospital, but I \x01",
            "guess you can ask the guy about the accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#12PThen, let's begin the investigation.\x02",
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

    # Function_25_3606 end

    def Function_26_4A5B(): pass

    label("Function_26_4A5B")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F...All right, now we have gathered\x01",
            "the needed intel, more or less.\x02",
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

    def lambda_4B48():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4B48)
    Sleep(50)

    def lambda_4B58():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4B58)
    Sleep(50)

    def lambda_4B68():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4B68)
    Sleep(50)

    def lambda_4B78():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4B78)
    Sleep(50)

    def lambda_4B88():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4B88)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#10105FHuh, already!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F...As expected from Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FSomehow I'm disappointed,\x01",
            "since I don't have the slightest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FI think I have noticed\x01",
            "a few things too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FWhat do we do? Should we try\x01",
            "examining the information now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... Let's call the Commander,\x01",
            "the Inspector and the others too.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Call(0, 27)
    Return()

    # Function_26_4A5B end

    def Function_27_4D19(): pass

    label("Function_27_4D19")

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
            "#02001F#11PWell then...\x01",
            "Did you confirm something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYes, first of all, about the possibility\x01",
            "of a rock to have fallen on the tracks...\x02\x03",
            "#00001FI think I can say that I can\x01",
            "strongly deny that possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PH-How come?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PIn other words, you have proof\x01",
            "to substantiate that, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, about that──\x02",
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
            "#1KYou can deny a fallen rock because...?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "The driver's yell the conductor heard\x01",                     # 0
            "The lack of scratches on the locomotive cusp\x01",              # 1
            "The greatly dented mark on the locomotive right side\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_51D5"),
        (1, "loc_5340"),
        (2, "loc_53DE"),
        (SWITCH_DEFAULT, "loc_5555"),
    )


    label("loc_51D5")


    ChrTalk(
        0x105,
        (
            "#10306F#6P──Well, that itself is not enough proof\x01",
            "to say it wasn't a fallen rock, right?\x02\x03",
            "#10301FIt's also possible he gave out a\x01",
            "scream since a rock fell suddenly in\x01",
            "the direction they were proceeding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PI see...right.\x02\x03",
            "#00013F...Then, as expected, it's the lack of\x01",
            "scratches on the locomotive cusp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#6PYeah, I think so too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5555")

    label("loc_5340")

    OP_2C(0xA8, 0x2)

    ChrTalk(
        0x101,
        (
            "#00003F#6PWe found many suspicious\x01",
            "evidences, however...\x02\x03",
            "#00013FThe decisive factor is the lack of scratches\x01",
            "on the locomotive cusp, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5555")

    label("loc_53DE")

    OP_2C(0xA8, 0x1)

    ChrTalk(
        0x105,
        (
            "#10306F#6P──Well, it's true that maybe that's\x01",
            "an important clue, but it's not\x01",
            "proof enough, you know?\x02\x03",
            "#10300FIt's also possible it collided with a rock that came\x01",
            "rolling down from the right side of the cliff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PI see...right.\x02\x03",
            "#00013F...Then, as expected, it's the lack of\x01",
            "scratches on the locomotive cusp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#6PYeah, I think so too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5555")

    label("loc_5555")


    ChrTalk(
        0x8,
        "#02005F#11PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07901F#11PIndeed, on the locomotive cusp there\x01",
            "are no scratches at all, but...\x02",
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
            "#00003FNormally, a derailment due to a fallen rock\x01",
            "happens in case the first carriage collides\x01",
            "with a rock that fell on the railroad tracks.\x02\x03",
            "As a result, the giant mass running\x01",
            "at high speed looses balance, leaves\x01",
            "the railroad tracks and derails...\x02\x03",
            "#00001FIn addition, it's difficult to think\x01",
            "it derailed in such a flashy way.\x02",
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
        "#02101F#12POoh, I see...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAnd yet, on the locomotive cusp we can't\x01",
            "find something like scratches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAnd that means the first and\x01",
            "most likely cause vanishes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11P...I understand.\x01",
            "It really is a fact we can't overlook.\x02\x03",
            "#02001FThen, is there another possibility you\x01",
            "could think of about the derailment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PYes...\x01",
            "At the very beginning, I thought that\x01",
            "some kind of explosive had been used.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5928():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5928)
    Sleep(50)

    def lambda_5938():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5938)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x102,
        "#00101F#5PW-What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#6PA terrorist act by some \x01",
            "kind of armed group...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6P──Well, I thought of that\x01",
            "possibility at first too.\x02\x03",
            "#00301FBut accordin' to what we've\x01",
            "surveyed, it seems there were\x01",
            "no explosives traces at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07906F#11PRight, at present, we haven't\x01",
            "found anything too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PSo, if I have to think\x01",
            "about something else...\x02\x03",
            "#00013FIt could be that the train was rammed from\x01",
            "the locomotive right side by "something".\x02",
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
        "#5PW-What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PR-Rammed...\x01",
            "That's so absurd...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02105F#12PIn blistering car races\x01",
            "that happens too, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00203F#12PI see...\x02\x03",
            "#00201FThe greatly dented part on\x01",
            "the locomotive right side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PYeah, I think that maybe\x01",
            "that's what happened.\x02",
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
            "#00003FThat "something" got down right beside\x01",
            "the locomotive of the running train.\x02\x03",
            "#00001FThe driver's scream that he let out\x01",
            "probably happened at that moment.\x02",
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
            "#00008FWhile running parallel to it, that "something"\x01",
            "rammed the locomotive from the right side...\x02\x03",
            "The locomotive derailed to the left\x01",
            "side due to the new added vector.\x02",
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
            "#00013FThen, that "something" kept pushing the\x01",
            "locomotive to the wall of rock on the left...\x02\x03",
            "And in the end, it finally made it stop\x01",
            "leaving long marks on the wall of rock.\x02\x03",
            "#00003FThen, the carriages that were following,\x01",
            "derailed scattering in that way.\x02",
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
            "#00000F#6P...For the time being,\x01",
            "this is my hypothesis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHUUUH...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#07902F#11P...Wonderfully done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PDear me, didn't you surpass your\x01",
            "older brother for reasoning ability?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02104F#12PIndeed...\x01",
            "Mr. Guy was the type to investigate\x01",
            "with a lot more instinct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PHey now, ain't him popular?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5P*giggle*...\x01",
            "Isn't it great, somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6POh boy, I too wasn't able to put\x01",
            "everything together to that extent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02004F#11PUh uh, impressive.\x02\x03",
            "#02001F──Then, Lloyd.\x02\x03",
            "The "something" that did all that,\x01",
            "was it a monster as I suspect?\x02\x03",
            "Or else, one of those recently appeared "Cryptids"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PLet's see...\x02",
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
            "#1KThe "something" that caused the accident is?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "A "Cryptid", very likely\x01",      # 0
            "I can't declare it yet\x01",        # 1
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
        (0, "loc_650A"),
        (1, "loc_66FE"),
        (SWITCH_DEFAULT, "loc_68AA"),
    )


    label("loc_650A")


    ChrTalk(
        0x101,
        (
            "#00006F#6PYes, it has strength to\x01",
            "be able to make derail\x01",
            "a running train.\x02\x03",
            "#00001FI think the most natural thing is\x01",
            "to think it was a large-scale Cryptid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#12PHowever, Mr. Lloyd.\x02\x03",
            "#00200FDespite a Cryptid appeared, I don't sense\x01",
            "the presence of the higher elements...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PI see, I didn't consider that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11P...Hm, it also doesn't seem that\x01",
            "those "Azure Flowers" that were\x01",
            "reported yesterday are blooming...\x02\x03",
            "#02008FThen, what kind of being could it be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68AA")

    label("loc_66FE")

    OP_2C(0xA8, 0x1)

    ChrTalk(
        0x101,
        (
            "#00006F#6PIndeed, it has strength\x01",
            "to be able to make\x01",
            "derail a running train.\x02\x03",
            "#00008FI think it's natural to think\x01",
            "about a large-scale Cryptid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PHowever, despite a Cryptid appeared, I don't \x01",
            "sense the presence of the higher elements...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#6PThose "Azure Flowers" too don't\x01",
            "seem to be blooming nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11PYou're indeed right...\x02\x03",
            "#02008FThen, what kind of being could it be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68AA")

    label("loc_68AA")

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
            "#00006F#6P(If I have to think about something else,\x01",
            "it could be a "Society" archaism, but...)\x02\x03",
            "#00008F(Are they people to make a move so directly?)\x02",
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
        "#07905F#11PW-What was that...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PA m-monster's howl...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PA-And also it seemed\x01",
            "too eerie...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PActivating the sensors...!\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(300)
    OP_68(600, 900, 3450, 1500)

    def lambda_6BCE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6BCE)

    def lambda_6BDB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6BDB)

    def lambda_6BE8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6BE8)

    def lambda_6BF5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6BF5)

    def lambda_6C02():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6C02)

    def lambda_6C0F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6C0F)

    def lambda_6C1C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6C1C)

    def lambda_6C29():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_6C29)

    def lambda_6C36():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_6C36)

    def lambda_6C43():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_6C43)

    def lambda_6C50():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_6C50)

    def lambda_6C5D():
        OP_95(0xFE, 2500, 0, 2050, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C5D)
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
            "#02101F#6PW-Where is it!?\x02\x03",
            "Reins, get a picture of\x01",
            "it in a way or another!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PPlease, don't say such an absurdity!\x02",
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
            "#00207F#12P──Distance, 10 selge!\x01",
            "Going far away to the west...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#5PKh...\x02\x03",
            "#00007FEveryone, let's chase it down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#5PYeah, gotcha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PRoger that!\x02",
    )

    CloseMessageWindow()

    def lambda_6E55():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_6E55)
    Sleep(50)

    def lambda_6E65():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6E65)
    Sleep(50)

    def lambda_6E75():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_6E75)
    Sleep(50)

    def lambda_6E85():
        OP_93(0xB, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_6E85)
    Sleep(50)

    def lambda_6E95():
        OP_93(0xC, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6E95)
    Sleep(50)

    def lambda_6EA5():
        OP_93(0xD, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6EA5)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)

    ChrTalk(
        0x9,
        "#5PHey now, don't do anything stupid!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#07907F#11PThe CGF will back you up too!\x02",
    )

    CloseMessageWindow()

    def lambda_6F23():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6F23)
    Sleep(50)

    def lambda_6F33():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6F33)
    Sleep(50)

    def lambda_6F43():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6F43)
    Sleep(50)

    def lambda_6F53():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6F53)
    Sleep(50)

    def lambda_6F63():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6F63)
    Sleep(50)

    def lambda_6F73():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6F73)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00013F#6PNo, please, focus on\x01",
            "the repair works!\x02\x03",
            "We'll try to chase it first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#07906F#11PKh...you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02003F#11P...The heavy machineries should be here soon.\x01",
            "It seems we can only accept your kind offer.\x02\x03",
            "#02001FWe'll come running if something happens,\x01",
            "so contact us in case!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#6PRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308F#6P............\x02",
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

    # Function_27_4D19 end

    def Function_28_7134(): pass

    label("Function_28_7134")

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

    label("loc_71D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F0")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("loc_71D3")

    label("loc_71F0")

    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Fade(250)
    Sound(812, 0, 100, 0)
    StopSound(852, 500, 100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_28_7134 end

    SaveToFile()

Try(main)
