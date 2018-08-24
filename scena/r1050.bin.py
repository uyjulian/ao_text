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
        "Function_5_D7A",          # 05, 5
        "Function_6_E66",          # 06, 6
        "Function_7_1122",         # 07, 7
        "Function_8_14CC",         # 08, 8
        "Function_9_1717",         # 09, 9
        "Function_10_190F",        # 0A, 10
        "Function_11_1AA8",        # 0B, 11
        "Function_12_1D73",        # 0C, 12
        "Function_13_1DF2",        # 0D, 13
        "Function_14_1E92",        # 0E, 14
        "Function_15_1F30",        # 0F, 15
        "Function_16_1FDC",        # 10, 16
        "Function_17_20AF",        # 11, 17
        "Function_18_2164",        # 12, 18
        "Function_19_21D5",        # 13, 19
        "Function_20_25EF",        # 14, 20
        "Function_21_299E",        # 15, 21
        "Function_22_29AC",        # 16, 22
        "Function_23_29BA",        # 17, 23
        "Function_24_29C8",        # 18, 24
        "Function_25_344A",        # 19, 25
        "Function_26_4822",        # 1A, 26
        "Function_27_4AD2",        # 1B, 27
        "Function_28_6E45",        # 1C, 28
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD1")
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
        "*sigh*, that was awful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I have it better\x01",
            "than those who were taken\x01",
            "to hospital, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe the\x01",
            "train derailed like\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYou're the conductor, right?\x02\x03",
            "#00000FIf you don't mind, could you\x01",
            "tell us what happened at the\x01",
            "time of the accident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, I'll tell you\x01",
            "everything I can...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had trouble telling\x01",
            "the officer over there\x01",
            "earlier.\x02",
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
            "#12P#10106FHmm. With an accident like\x01",
            "this one, it can't be helped\x01",
            "if some things are unclear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FI think he's shocked by\x01",
            "the accident as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FWe don't mind even if\x01",
            "it's something small.\x02\x03",
            "#00001FWasn't there anything\x01",
            "you found suspicious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Suspicious... Hmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Ah, come to think of it!\x02",
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
            "Just before the derailment,\x01",
            "I was on a call with the\x01",
            "driver and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Suddenly he screamed.\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xFE,
        (
            ""Waaah, what's that!?",\x01",
            "he said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The accident happened right after that.\x01",
            "The lead car derailed and the linked\x01",
            "cars followed, one after the next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And that... brings us to\x01",
            "where we are now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00200F"Waaah, what's that!?",\x01",
            "he screamed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FThat line suggests he saw\x01",
            "something he couldn't\x01",
            "believe, doesn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FJust what did the driver\x01",
            "see, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 6)
    OP_29(0xA8, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA5")
    Call(0, 26)
    Return()

    label("loc_CA5")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -50180, 0, -17560, 257)
    EventEnd(0x5)
    Jump("loc_D79")

    label("loc_CD1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Just before the derailment, I\x01",
            "was on a call with the driver\x01",
            "when he suddenly scream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Waah, what's that!?",\x01",
            "he said. The accident\x01",
            "happened right after.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_D79")

    Return()

    # Function_4_65A end

    def Function_5_D7A(): pass

    label("Function_5_D7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_E62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D98")
    Call(0, 11)
    Jump("loc_E62")

    label("loc_D98")


    ChrTalk(
        0xFE,
        (
            "#02003FUntil the heavy machinery arrives,\x01",
            "we CGF will cooperate with the\x01",
            "survey of the scene.\x02\x03",
            "#02000FI've explained things to the other\x01",
            "members, so please feel free to\x01",
            "conduct your investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E62")

    TalkEnd(0xFE)
    Return()

    # Function_5_D7A end

    def Function_6_E66(): pass

    label("Function_6_E66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1084")

    ChrTalk(
        0xFE,
        (
            "Oh man. Looking at it\x01",
            "again, this was one hell\x01",
            "of an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Luckily there wasn't\x01",
            "even a single person\x01",
            "killed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt seems almost all\x01",
            "passengers were taken to the\x01",
            "Republic or the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIf possible, I'd have\x01",
            "liked to hear from them\x01",
            "as well, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it can't be\x01",
            "helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, right. Did you\x01",
            "interview the conductor\x01",
            "resting over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We didn't get anything important\x01",
            "when we asked him before, but\x01",
            "maybe he's remembered something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't forget to speak\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 2)
    Jump("loc_111E")

    label("loc_1084")


    ChrTalk(
        0xFE,
        (
            "Did you interview the\x01",
            "conductor resting over\x01",
            "there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's the only one who was there\x01",
            "at the time of the accident.\x01",
            "Don't forget to interview him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111E")

    TalkEnd(0xFE)
    Return()

    # Function_6_E66 end

    def Function_7_1122(): pass

    label("Function_7_1122")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F2")

    ChrTalk(
        0xFE,
        (
            "#02102FSo, Lloyd. Did you\x01",
            "figure anything out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, I can't yet say.\x02\x03",
            "#00001FGrace, did you notice\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02106FHmm, let me think. Train\x01",
            "accidents happen every\x01",
            "now and then.\x02\x03",
            "#02101FBut this time, I think\x01",
            "both the time and place\x01",
            "were too awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F...You're right. And to make matters\x01",
            "worse, there's a state of emergency\x01",
            "due to the independence proposal...\x02\x03",
            "#00103FIt's possible that someone had a\x01",
            "reason to cause this accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02106FI don't have any proof, though. I'm\x01",
            "trying to force my ideas on you guys.\x02\x03",
            "#02109FAnyhow, do your best with the\x01",
            "investigation! And if you find something,\x01",
            "let me use it for my coverage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHaha, understood.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x17B, 1)
    Jump("loc_14C8")

    label("loc_13F2")


    ChrTalk(
        0xFE,
        (
            "#02103FTrain accidents happen, but... This time,\x01",
            "the timing and place were simply awful.\x02\x03",
            "#02109FWell anyhow, do your best with the\x01",
            "investigation! And if you find something,\x01",
            "let me use it for my coverage, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C8")

    TalkEnd(0xFE)
    Return()

    # Function_7_1122 end

    def Function_8_14CC(): pass

    label("Function_8_14CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B1")

    ChrTalk(
        0x104,
        (
            "#00300FMireille, how're the\x01",
            "repairs going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#07901FWell, they're proceeding side\x01",
            "by side with your\x01",
            "investigation, but...\x02\x03",
            "#07906FAs expected, we're in a bind\x01",
            "until we move the train\x01",
            "itself using heavy machinery.\x02\x03",
            "#07900FFor the time being, we're\x01",
            "clearing the broken pieces\x01",
            "scattered around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI knew it, we should\x01",
            "help too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#07904FNo, there's no need. You\x01",
            "should focus on the\x01",
            "investigation.\x02\x03",
            "#07902FWe'll inform you if we\x01",
            "learn anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 4)
    Jump("loc_1713")

    label("loc_16B1")


    ChrTalk(
        0xFE,
        (
            "#07904FYou should focus on the\x01",
            "investigation.\x02\x03",
            "#07902FWe'll inform you if we\x01",
            "learn anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1713")

    TalkEnd(0xFE)
    Return()

    # Function_8_14CC end

    def Function_9_1717(): pass

    label("Function_9_1717")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1888")

    ChrTalk(
        0xFE,
        (
            "Well, we checked what we\x01",
            "could inside the\x01",
            "derailed cars, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There were no important\x01",
            "clues inside there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FWas there anything\x01",
            "suspicious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No. All we found was the\x01",
            "passengers' luggage. There wasn't\x01",
            "anything particularly suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The accident happened\x01",
            "due to an external\x01",
            "cause, without a doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FHmm...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 3)
    Jump("loc_190B")

    label("loc_1888")


    ChrTalk(
        0xFE,
        (
            "There were no important\x01",
            "clues inside the\x01",
            "derailed cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The accident happened\x01",
            "due to an external\x01",
            "cause, without a doubt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190B")

    TalkEnd(0xFE)
    Return()

    # Function_9_1717 end

    def Function_10_190F(): pass

    label("Function_10_190F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0A")

    ChrTalk(
        0xFE,
        (
            "*sigh*, with an accident\x01",
            "scene like this, it's a shock\x01",
            "even just looking at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, in order to get\x01",
            "the truth, I must take a\x01",
            "lot of good pictures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It often happens that a\x01",
            "picture becomes some\x01",
            "kind of evidence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AA4")

    label("loc_1A0A")


    ChrTalk(
        0xFE,
        (
            "Covering accident scenes is\x01",
            "shocking, but... I must take\x01",
            "a lot of good pictures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It often happens that a\x01",
            "picture becomes some\x01",
            "kind of evidence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA4")

    TalkEnd(0xFE)
    Return()

    # Function_10_190F end

    def Function_11_1AA8(): pass

    label("Function_11_1AA8")

    OP_4B(0x8, 0x0)
    OP_4B(0x11, 0x0)
    OP_4B(0x12, 0x0)

    ChrTalk(
        0x8,
        (
            "#02000FYou all, how long until\x01",
            "the heavy machinery\x01",
            "arrives?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Right, it'll be here\x01",
            "within 30 minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Still, will we be all\x01",
            "right waiting for this\x01",
            "investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If we can't restore one\x01",
            "side of the railroad\x01",
            "tracks by evening, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02005FIf we can't do it...? No\x01",
            "need to worry about\x01",
            "that.\x02\x03",
            "#02001FWe absolutely must do\x01",
            "it, no matter what it\x01",
            "takes.\x02\x03",
            "#02003F...You are of course\x01",
            "aware of that, correct?\x02",
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
        "#00306F(Strict as always...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F(That's very like\x01",
            "Commander Sonya.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(She gave us this\x01",
            "chance...)\x02\x03",
            "#00001F(We must ascertain the\x01",
            "cause of this accident\x01",
            "no matter what.)\x02",
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

    # Function_11_1AA8 end

    def Function_12_1D73(): pass

    label("Function_12_1D73")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, getting too close\x01",
            "seems dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now it's balanced,\x01",
            "but what if it were to\x01",
            "fall for some reason?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1D73 end

    def Function_13_1DF2(): pass

    label("Function_13_1DF2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*siiigh*, glass and\x01",
            "other stuff is scattered\x01",
            "all around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's dangerous if even one\x01",
            "pebble is on the tracks so\x01",
            "I've got to pick them all up.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1DF2 end

    def Function_14_1E92(): pass

    label("Function_14_1E92")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "To think it ended up\x01",
            "derailing across both sides\x01",
            "of the tracks like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The passengers travelling\x01",
            "or returning home must've\x01",
            "been scared.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1E92 end

    def Function_15_1F30(): pass

    label("Function_15_1F30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_1FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F4E")
    Call(0, 11)
    Jump("loc_1FD8")

    label("loc_1F4E")


    ChrTalk(
        0xFE,
        (
            "The heavy machinery will\x01",
            "be here within 30\x01",
            "minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until then, we have to make\x01",
            "progress on the repairs,\x01",
            "even if just a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD8")

    TalkEnd(0xFE)
    Return()

    # Function_15_1F30 end

    def Function_16_1FDC(): pass

    label("Function_16_1FDC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_20AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFA")
    Call(0, 11)
    Jump("loc_20AB")

    label("loc_1FFA")


    ChrTalk(
        0xFE,
        (
            "The investigation is\x01",
            "needed, but the schedule\x01",
            "can't be delayed, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, there's nothing we can do\x01",
            "about it. It'll be really tough,\x01",
            "but all we can do is our best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AB")

    TalkEnd(0xFE)
    Return()

    # Function_16_1FDC end

    def Function_17_20AF(): pass

    label("Function_17_20AF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "When we were contacted, I\x01",
            "never imagined it'd be\x01",
            "this much of an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems a considerable amount\x01",
            "of materials will be needed to\x01",
            "repair the tracks as well.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_20AF end

    def Function_18_2164(): pass

    label("Function_18_2164")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The tracks ended up\x01",
            "being largely torn to\x01",
            "pieces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess the derailment\x01",
            "started around here...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2164 end

    def Function_19_21D5(): pass

    label("Function_19_21D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2542")
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
        (
            "#12P#00100FThis car is the\x01",
            "locomotive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FIt's the most important\x01",
            "car with respect to\x01",
            "operating an orbal train.\x02\x03",
            "#00200FThere should be a Reinford\x01",
            "orbal train engine and\x01",
            "driver's cab inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10305FHmm, even so, isn't\x01",
            "there something out of\x01",
            "place about this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FYeah. It's got far less\x01",
            "damage than I thought it\x01",
            "would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FI-Indeed... It seems\x01",
            "unnatural since it's the\x01",
            "lead car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah... If it collided with\x01",
            "something in front of the train,\x01",
            "it wouldn't be this clean.\x02\x03",
            "#00008FIn that case, it seems the cause\x01",
            "of the derailment lies\x01",
            "elsewhere...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 3)
    OP_29(0xA8, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2516")
    Call(0, 26)
    Return()

    label("loc_2516")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -6920, 0, -2370, 315)
    EventEnd(0x5)
    Jump("loc_25EE")

    label("loc_2542")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00003FIf it collided with something\x01",
            "in front of the train, it\x01",
            "wouldn't be this clean.\x02\x03",
            "#00008FIn that case, the cause of\x01",
            "the derailment should lie\x01",
            "elsewhere...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_25EE")

    Return()

    # Function_19_21D5 end

    def Function_20_25EF(): pass

    label("Function_20_25EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290B")
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
        "#6P#00005FWhat? This is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FIt's possible it was a fallen\x01",
            "rock... Could this be where\x01",
            "it collided with the train?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FIt seems likely based on\x01",
            "the spherical dent,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FHmm... If that's true, then\x01",
            "what's with the scratch marks in\x01",
            "the center of the dented part?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FAnd if you think about\x01",
            "it, it's in a rather\x01",
            "high position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FHmm... A simple fallen\x01",
            "rock wouldn't leave marks\x01",
            "like this, would it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FWhat in the world\x01",
            "collided with it, I\x01",
            "wonder?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 4)
    OP_29(0xA8, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28DF")
    Call(0, 26)
    Return()

    label("loc_28DF")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -13530, 0, -2950, 45)
    EventEnd(0x5)
    Jump("loc_299D")

    label("loc_290B")

    TalkBegin(0xFF)

    ChrTalk(
        0x102,
        (
            "#00108FHmm... A simple fallen\x01",
            "rock wouldn't leave marks\x01",
            "like this, would it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWhat in the world\x01",
            "collided with it, I\x01",
            "wonder?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_299D")

    Return()

    # Function_20_25EF end

    def Function_21_299E(): pass

    label("Function_21_299E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_21_299E end

    def Function_22_29AC(): pass

    label("Function_22_29AC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_22_29AC end

    def Function_23_29BA(): pass

    label("Function_23_29BA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_23_29BA end

    def Function_24_29C8(): pass

    label("Function_24_29C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_335B")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A67")
    SetChrPos(0x101, -35490, 0, 7260, 0)
    SetChrPos(0x102, -38000, 0, 7070, 300)
    SetChrPos(0x103, -36900, 0, 7230, 330)
    SetChrPos(0x104, -34470, 0, 6820, 60)
    SetChrPos(0x109, -34930, 0, 5800, 60)
    SetChrPos(0x105, -36170, 0, 6550, 0)
    Jump("loc_2B56")

    label("loc_2A67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE1")
    SetChrPos(0x101, -55340, 0, 8020, 30)
    SetChrPos(0x102, -57740, 0, 8050, 330)
    SetChrPos(0x103, -56530, 0, 8270, 0)
    SetChrPos(0x104, -54080, 0, 7400, 60)
    SetChrPos(0x109, -56190, 0, 6600, 30)
    SetChrPos(0x105, -57360, 0, 7060, 300)
    Jump("loc_2B56")

    label("loc_2AE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B56")
    SetChrPos(0x101, -62900, 0, 8740, 0)
    SetChrPos(0x102, -65170, 0, 7220, 300)
    SetChrPos(0x103, -64310, 0, 8130, 330)
    SetChrPos(0x104, -61540, 0, 8920, 30)
    SetChrPos(0x109, -61980, 0, 7950, 60)
    SetChrPos(0x105, -63300, 0, 7610, 0)

    label("loc_2B56")

    OP_68(-12460, 600, 9000, 0)
    MoveCamera(23, 46, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28500, 0)
    OP_68(-65230, 600, 11100, 11000)
    MoveCamera(23, 35, 0, 4000)
    Sleep(11500)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD8")
    OP_68(-35670, 600, 9060, 0)
    MoveCamera(14, 37, 0, 0)
    Jump("loc_2C33")

    label("loc_2BD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C08")
    OP_68(-54950, 600, 10680, 0)
    MoveCamera(21, 22, 0, 0)
    Jump("loc_2C33")

    label("loc_2C08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C33")
    OP_68(-63520, 600, 10610, 0)
    MoveCamera(353, 23, 0, 0)

    label("loc_2C33")

    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00005FThe scars on this rock\x01",
            "wall... They're quite\x01",
            "large.\x02\x03",
            "#00001FIt's like the whole\x01",
            "surface has been carved\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FThere are gouge marks on the ground\x01",
            "here as well. I suppose this means the\x01",
            "train derailed to the left side...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FBy the way, I wonder what\x01",
            "this blue stuff stuck to\x01",
            "the rock wall is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIt appears to be paint,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E07")
    OP_68(-30920, 800, 4590, 3000)
    MoveCamera(76, 34, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(22500, 3000)
    Jump("loc_2E86")

    label("loc_2E07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E49")
    OP_68(-30920, 800, 4590, 4000)
    MoveCamera(76, 34, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(22500, 3000)
    Jump("loc_2E86")

    label("loc_2E49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E86")
    OP_68(-30920, 800, 4590, 5000)
    MoveCamera(76, 34, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(22500, 5000)

    label("loc_2E86")


    def lambda_2E8B():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2E8B)
    Sleep(50)

    def lambda_2E9B():
        OP_93(0xFE, 0x64, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2E9B)
    Sleep(50)

    def lambda_2EAB():
        OP_93(0xFE, 0x6E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EAB)
    Sleep(50)

    def lambda_2EBB():
        OP_93(0xFE, 0x69, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2EBB)
    Sleep(50)

    def lambda_2ECB():
        OP_93(0xFE, 0x64, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2ECB)
    Sleep(50)

    def lambda_2EDB():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2EDB)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_307F")

    ChrTalk(
        0x109,
        (
            "#N#10100F#12PLooking at the train... It seems\x01",
            "to be some of its blue body paint.\x02\x03",
            "#10103FThe train contacted the rock wall\x01",
            "and remained in contact for some\x01",
            "distance... This is proof of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FYeah, but... Did it\x01",
            "scrape it long enough to\x01",
            "cause marks like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#N#6P#00003FIt seems we need to rethink what\x01",
            "kind of situation could have\x01",
            "caused these kinds of marks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3210")

    label("loc_307F")

    SetMessageWindowPos(220, 140, -1, -1)

    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10100FLooking at the train... It seems\x01",
            "to be some of its blue body paint.\x02\x03",
            "#10103FThe train contacted the rock wall\x01",
            "and remained in contact for some\x01",
            "distance... This is proof of that.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00301FYeah, but... Did it\x01",
            "scrape it long enough to\x01",
            "cause marks like this?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003FIt seems we need to rethink what\x01",
            "kind of situation could have\x01",
            "caused these kinds of marks.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3210")

    OP_5A()
    SetScenarioFlags(0x17A, 5)
    OP_29(0xA8, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32D6")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3264")
    OP_68(-35670, 600, 9060, 0)
    MoveCamera(14, 37, 0, 0)
    Jump("loc_32BF")

    label("loc_3264")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3294")
    OP_68(-54950, 600, 10680, 0)
    MoveCamera(21, 22, 0, 0)
    Jump("loc_32BF")

    label("loc_3294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32BF")
    OP_68(-63520, 600, 10610, 0)
    MoveCamera(353, 23, 0, 0)

    label("loc_32BF")

    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Call(0, 26)
    Return()

    label("loc_32D6")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_330F")
    SetChrPos(0x0, -35980, 0, 7690, 339)
    Jump("loc_3354")

    label("loc_330F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3334")
    SetChrPos(0x0, -56210, 0, 8260, 24)
    Jump("loc_3354")

    label("loc_3334")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3354")
    SetChrPos(0x0, -65200, 0, 8340, 294)

    label("loc_3354")

    EventEnd(0x5)
    Jump("loc_3449")

    label("loc_335B")

    TalkBegin(0xFF)

    ChrTalk(
        0x109,
        (
            "#10100FThe scars and paint on this rock wall...\x01",
            "Thinking about the situation, I can\x01",
            "conclude they're from the train itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt seems we need to rethink what\x01",
            "kind of situation could have\x01",
            "caused these kinds of marks.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_3449")

    Return()

    # Function_24_29C8 end

    def Function_25_344A(): pass

    label("Function_25_344A")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35AE")
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

    label("loc_35AE")

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
            "#02103F#6PAaah, what a horrible\x01",
            "accident!\x02\x03",
            "#02101FAnd what was the cause\x01",
            "of the derailment,\x01",
            "exactly!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAs you can see, it's\x01",
            "currently under\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAt present, we're thinking\x01",
            "the lead car collided with\x01",
            "a fallen rock on the track.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02003F#11PI'm terribly sorry, but\x01",
            "we're now asking the\x01",
            "mass media to leave.\x02\x03",
            "#02000FWe need to begin repair\x01",
            "work immediately.\x02",
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
        "#02105F#6PWHAAAT!?\x02",
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
            "#02006F#12PAs police, I understand that you want\x01",
            "to prioritize surveying the scene.\x02\x03",
            "#02001FHowever, this transcontinental railway\x01",
            "is one of the most important routes on\x01",
            "the entire continent...\x02\x03",
            "The rail company, Empire, Republic and\x01",
            "Mayor Dieter as well have all already\x01",
            "requested its immediate repair.\x02\x03",
            "As the CGF, we must comply with those\x01",
            "requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWell, I understand your\x01",
            "logic, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02101F#6PBut if the cause is not\x01",
            "understood, couldn't it\x01",
            "easily happen again?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#02003F#11PWith respect to that, we\x01",
            "can only do it in parallel\x01",
            "with the repairs.\x02\x03",
            "#02001FAt any rate, we need one\x01",
            "side of the tracks clear by\x01",
            "evening at the very latest.\x02\x03",
            "Before the heavy machinery\x01",
            "we've prepared arrives,\x01",
            "we──\x02",
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

    def lambda_3CFD():
        OP_93(0x8, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3CFD)
    Sleep(50)

    def lambda_3D0D():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3D0D)
    Sleep(50)

    def lambda_3D1D():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3D1D)
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

    def lambda_3D89():
        OP_9B(0x0, 0x101, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D89)
    Sleep(0)

    def lambda_3DA1():
        OP_9B(0x0, 0x109, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3DA1)
    Sleep(0)

    def lambda_3DB9():
        OP_9B(0x0, 0x102, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3DB9)
    Sleep(0)

    def lambda_3DD1():
        OP_9B(0x0, 0x103, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3DD1)
    Sleep(0)

    def lambda_3DE9():
        OP_9B(0x0, 0x104, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3DE9)
    Sleep(0)

    def lambda_3E01():
        OP_9B(0x0, 0x105, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3E01)
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
        "#02105F#5PMy, Lloyd and company?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5POh, so you came.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PExcuse me, Commander...\x02\x03",
            "#10113FYou're starting repairs\x01",
            "without even surveying\x01",
            "the scene?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11PBeing a CGF member yourself, you\x01",
            "should know the importance of this\x01",
            "railway.\x02\x03",
            "#02001FI don't want to say this, but...\x02\x03",
            "If we're late with the repairs,\x01",
            "the Empire and Republic could take\x01",
            "it as a sign of interference.\x02",
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
        (
            "#00106F#6P...You've thought about\x01",
            "this quite a bit,\x01",
            "haven't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P*sigh*, if you say that,\x01",
            "then there's nothing we\x01",
            "can really do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02106F#5PHmm, but we have a duty\x01",
            "to discover the truth...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#6P─Commander Sonya.\x02\x03",
            "#00001FCould you give us 30\x01",
            "minutes, no, just until the\x01",
            "heavy machinery arrives?\x02",
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
            "#00006F#6PYes. This accident\x01",
            "occurred in the present\x01",
            "Crossbell...\x02\x03",
            "#00001FI can't think it's a\x01",
            "simple coincidence.\x02\x03",
            "Don't we have a duty to\x01",
            "look into whether this\x01",
            "was really "inevitable"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02001F#11P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PThere may also be damage\x01",
            "from one of those\x01",
            "Cryptids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PWell, isn't it alright\x01",
            "to leave this to us even\x01",
            "just for peace of mind?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#02006F#11P...You're right. It\x01",
            "seems I, of all people,\x01",
            "was just bit hasty.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#02002F#12P─Inspector Donovan. Let's\x01",
            "prioritize surveying the\x01",
            "scene first.\x02\x03",
            "In return, we'll focus on\x01",
            "repairs once work has\x01",
            "begun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAgreed. I have no\x01",
            "objections.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x2D, 0x1F4)

    ChrTalk(
        0xA,
        (
            "#02109F#6PExcuse meeee... If\x01",
            "possible, I'd like to\x01",
            "cover this too...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#02003F#11PDo as you like, until\x01",
            "the repair work begins.\x02\x03",
            "#02000FHowever... Do not\x01",
            "interfere with the\x01",
            "survey of the scene.\x02",
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
            "#00001F#6PInspector, can we\x01",
            "participate in the\x01",
            "survey of the scene?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4615():
        OP_93(0x8, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_4615)
    Sleep(50)

    def lambda_4625():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_4625)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0xA, 0)

    ChrTalk(
        0x9,
        "#5PYeah, let's split up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5POh, right, the conductor\x01",
            "is resting over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThe driver's been taken to the\x01",
            "hospital, but I guess you can\x01",
            "ask him about what happened.\x02",
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
        (
            "#10302F#12PThen, let's begin the\x01",
            "investigation.\x02",
        )
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

    # Function_25_344A end

    def Function_26_4822(): pass

    label("Function_26_4822")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F...Alright, with this, we've\x01",
            "gathered the necessary info,\x01",
            "more or less.\x02",
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

    def lambda_4914():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4914)
    Sleep(50)

    def lambda_4924():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4924)
    Sleep(50)

    def lambda_4934():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4934)
    Sleep(50)

    def lambda_4944():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4944)
    Sleep(50)

    def lambda_4954():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4954)
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
        "#00202F...As expected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI didn't expect it. I\x01",
            "still don't know what's\x01",
            "what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FI noticed some things, I\x01",
            "guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FWhat do we do? Should we\x01",
            "review what we've\x01",
            "learned right away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... Let's call Commander\x01",
            "Sonya, Inspector Donovan and\x01",
            "the others as well.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Call(0, 27)
    Return()

    # Function_26_4822 end

    def Function_27_4AD2(): pass

    label("Function_27_4AD2")

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
            "#02001F#11PWell then... Did you\x01",
            "confirm anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYes. First, about the possibility\x01",
            "that a rock or something could\x01",
            "have fallen on the tracks...\x02\x03",
            "#00001FI think I can strongly deny that\x01",
            "possibility immediately.\x02",
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
            "#5PYou're saying you have\x01",
            "proof?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, about that─\x02",
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
            "#1KWhat proves the cause\x01",
            "isn't a falling rock?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "The driver's scream the conductor heard\x01",      # 0
            "Few scratches on the locomotive's front\x01",      # 1
            "The dent on the locomotive's right side\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F6C"),
        (1, "loc_50F7"),
        (2, "loc_519D"),
        (SWITCH_DEFAULT, "loc_532B"),
    )


    label("loc_4F6C")


    ChrTalk(
        0x105,
        (
            "#10306F#6P─Well, that isn't enough proof to\x01",
            "say it wasn't a fallen rock by\x01",
            "itself, right?\x02\x03",
            "#10301FIt's possible he screamed due to a\x01",
            "rock that suddenly fell along their\x01",
            "direction of travel, for instance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PI see... You're certainly\x01",
            "right about that.\x02\x03",
            "#00013F...Then, as expected, it's\x01",
            "the lack of scratches on\x01",
            "the locomotive's front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#6PYeah, I think so too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_532B")

    label("loc_50F7")

    OP_2C(0xA8, 0x2)

    ChrTalk(
        0x101,
        (
            "#00003F#6PWe found a lot of\x01",
            "questionable evidence.\x01",
            "However...\x02\x03",
            "#00013FThe decisive factor is the\x01",
            "lack of scratches on the\x01",
            "locomotive's front, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_532B")

    label("loc_519D")

    OP_2C(0xA8, 0x1)

    ChrTalk(
        0x105,
        (
            "#10306F#6P─Well, that may be an important clue,\x01",
            "but how does it disprove a falling\x01",
            "rock?\x02\x03",
            "#10300FIt's possible the train collided with\x01",
            "a rock that rolled down the right\x01",
            "side of the cliff, for instance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PI see... You're certainly\x01",
            "right about that.\x02\x03",
            "#00013F...Then, as expected, it's\x01",
            "the lack of scratches on\x01",
            "the locomotive's front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#6PYeah, I think so too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_532B")

    label("loc_532B")


    ChrTalk(
        0x8,
        "#02005F#11PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07901F#11PIt's true there aren't\x01",
            "many scratches on the\x01",
            "locomotive's front, but...\x02",
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
            "#00003FIn falling rock derailments, the lead\x01",
            "car normally collides with the fallen\x01",
            "rock, I think.\x02\x03",
            "As a result, the balance of the running\x01",
            "train's huge mass is disrupted, and the\x01",
            "train leaves the tracks and derails...\x02\x03",
            "#00001FIn addition, it's difficult to think it\x01",
            "derailed in such a flashy way.\x02",
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
        "#02101F#12POh, I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAnd yet, there's few\x01",
            "scratch marks on the\x01",
            "locomotive's front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAnd that means the first\x01",
            "and most likely cause\x01",
            "vanishes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11PIndeed. It really is a\x01",
            "fact we can't overlook.\x02\x03",
            "#02001FThen, is there another\x01",
            "possibility you can\x01",
            "think of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PYes... At the very beginning,\x01",
            "I thought some kind of\x01",
            "explosive had been used.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_56AE():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_56AE)
    Sleep(50)

    def lambda_56BE():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_56BE)
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
            "#10107F#6PA terrorist act by some\x01",
            "armed group!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6P─Well, that's what I first\x01",
            "thought too.\x02\x03",
            "#00301FBut after a general survey of\x01",
            "the area, there's no sign at\x01",
            "all that an explosive was used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07906F#11PRight, we haven't found\x01",
            "anything like that\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PThat being the case, if\x01",
            "there's something else I\x01",
            "can think of...\x02\x03",
            "#00013FIt's possible "something"\x01",
            "rammed the locomotive\x01",
            "from the right-hand side.\x02",
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
            "#11PR-Rammed... That's\x01",
            "absurd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02105F#12PThat kind of thing happens\x01",
            "in car races that are\x01",
            "extremely close, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00203F#12PI see...\x02\x03",
            "#00201FThat's the dent on the\x01",
            "locomotive's right side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PYeah. That's what most\x01",
            "likely happened.\x02",
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
            "#00003FThat "something" jumped\x01",
            "down beside the moving\x01",
            "train's locomotive.\x02\x03",
            "#00001FThat's probably when the\x01",
            "driver screamed.\x02",
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
            "#00008FWhile running alongside it,\x01",
            "that "something" rammed the\x01",
            "locomotive's right side...\x02\x03",
            "The locomotive derailed to\x01",
            "the left because of the\x01",
            "side impact.\x02",
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
            "#00013FThe "something" then continued\x01",
            "to push the locomotive against\x01",
            "the left rock wall...\x02\x03",
            "And the train finally came to\x01",
            "a stop after leaving those\x01",
            "long scars in the rock wall.\x02\x03",
            "#00003FEach of the following cars\x01",
            "then derailed in this same\x01",
            "way.\x02",
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
        "#11PHUUUH!?\x02",
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
            "#5PDear me, haven't you\x01",
            "surpassed your older brother\x01",
            "in reasoning ability?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02104F#12PIndeed... Guy was the\x01",
            "type to investigate with\x01",
            "a lot more instinct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PHey now, aren't you the\x01",
            "popular guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5P*giggle*... That's\x01",
            "something to be proud\x01",
            "of, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6POh man. I don't even\x01",
            "think I could've put it\x01",
            "together that well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02004F#11PHaha, impressive.\x02\x03",
            "#02001F─Then, Lloyd.\x02\x03",
            "The "something" that did\x01",
            "all that, may I suppose\x01",
            "it's a monster?\x02\x03",
            "Or else, one of those\x01",
            "Cryptids that appeared\x01",
            "recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PLet me think...\x02",
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
            "#1KThe "something" that\x01",
            "caused the accident is?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "It's likely a Cryptid\x01",       # 0
            "It's too early to tell\x01",      # 1
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
        (0, "loc_625A"),
        (1, "loc_6435"),
        (SWITCH_DEFAULT, "loc_65CF"),
    )


    label("loc_625A")


    ChrTalk(
        0x101,
        (
            "#00006F#6PYes, it had strength\x01",
            "enough to derail a\x01",
            "moving train.\x02\x03",
            "#00001FIt's most natural to\x01",
            "think this was the work\x01",
            "of a large Cryptid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#12PHowever, Lloyd.\x02\x03",
            "#00200FFor a Cryptid to appear,\x01",
            "I would need to sense\x01",
            "the higher elements...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#5PI see, I didn't consider\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11P...Hmm, it doesn't seem like\x01",
            "those Azure Flowers you reported\x01",
            "yesterday are blooming either...\x02\x03",
            "#02008FThat being the case, what kind\x01",
            "of being could it be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65CF")

    label("loc_6435")

    OP_2C(0xA8, 0x1)

    ChrTalk(
        0x101,
        (
            "#00006F#6PIndeed, it has strength\x01",
            "enough to derail a\x01",
            "moving train.\x02\x03",
            "#00008FIt's natural to think\x01",
            "it's a large Cryptid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PHowever, for a Cryptid to\x01",
            "appear, I would need to\x01",
            "sense the higher elements...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#6PThose Azure Flowers\x01",
            "don't seem to be\x01",
            "blooming nearby either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02006F#11PIndeed, you're\x01",
            "correct...\x02\x03",
            "#02008FThat being the case,\x01",
            "what kind of being could\x01",
            "it be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65CF")

    label("loc_65CF")

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
            "#00006F#6P(If I have to think about\x01",
            "something else, it could an\x01",
            "Ouroboros archaism, but...)\x02\x03",
            "#00008F(Are they the kind of\x01",
            "people to take such direct\x01",
            "action?)\x02",
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
        "#07905F#11PW-What was that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PA m-monster's howl!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PA-And I feel it was too\x01",
            "ominous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PActivating sensors!\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(300)
    OP_68(600, 900, 3450, 1500)

    def lambda_68F1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_68F1)

    def lambda_68FE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_68FE)

    def lambda_690B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_690B)

    def lambda_6918():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6918)

    def lambda_6925():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6925)

    def lambda_6932():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6932)

    def lambda_693F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_693F)

    def lambda_694C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_694C)

    def lambda_6959():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_6959)

    def lambda_6966():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_6966)

    def lambda_6973():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_6973)

    def lambda_6980():
        OP_95(0xFE, 2500, 0, 2050, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6980)
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
            "it somehow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PPlease, don't be\x01",
            "ridiculous!\x02",
        )
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
            "#00207F#12P─Distance, 10 selge and\x01",
            "rising! It's heading\x01",
            "west!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#5PTch...\x02\x03",
            "#00007FEveryone, let's chase it\x01",
            "down!\x02",
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

    def lambda_6B62():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_6B62)
    Sleep(50)

    def lambda_6B72():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6B72)
    Sleep(50)

    def lambda_6B82():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_6B82)
    Sleep(50)

    def lambda_6B92():
        OP_93(0xB, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_6B92)
    Sleep(50)

    def lambda_6BA2():
        OP_93(0xC, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6BA2)
    Sleep(50)

    def lambda_6BB2():
        OP_93(0xD, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6BB2)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)

    ChrTalk(
        0x9,
        (
            "#5PHey now, don't do\x01",
            "anything stupid!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#07907F#11PThe CGF will back you\x01",
            "up!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6C2C():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6C2C)
    Sleep(50)

    def lambda_6C3C():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6C3C)
    Sleep(50)

    def lambda_6C4C():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6C4C)
    Sleep(50)

    def lambda_6C5C():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6C5C)
    Sleep(50)

    def lambda_6C6C():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6C6C)
    Sleep(50)

    def lambda_6C7C():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6C7C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00013F#6PNo, please focus on the\x01",
            "repairs!\x02\x03",
            "We'll chase it down\x01",
            "first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#07906F#11PTch... You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02003F#11P...Our heavy machinery will arrive\x01",
            "soon, too. It seems we have no choice\x01",
            "but to accept your kind offer.\x02\x03",
            "#02001FIf anything happens, we'll be right\x01",
            "there, so please contact us!\x02",
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

    # Function_27_4AD2 end

    def Function_28_6E45(): pass

    label("Function_28_6E45")

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

    label("loc_6EE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F01")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("loc_6EE4")

    label("loc_6F01")

    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Fade(250)
    Sound(812, 0, 100, 0)
    StopSound(852, 500, 100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_28_6E45 end

    SaveToFile()

Try(main)
