from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e440b.bin",                # FileName
        "e440b",                    # MapName
        "e440b",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e440b",                  # 0
        "Lisha",               # 1
        "God wolf Zeit",           # 2
        "Erie",                 # 3
        "Tio",                 # 4
        "Randy",               # 5
        "Noel",                 # 6
        "Waji",                   # 7
        "SE control",                 # 8
    ))

    AddCharChip((
        "chr/ch03200.itc",                   # 00
        "chr/ch02708.itc",                   # 01
    ))

    DeclNpc(2589,    0,       4294967267, 90,   453,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4294965747, 0,       4294966337, 180,  405,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(456, 0)                                        # 0

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_278",          # 01, 1
        "Function_2_311",          # 02, 2
        "Function_3_385",          # 03, 3
        "Function_4_A15",          # 04, 4
        "Function_5_E14",          # 05, 5
        "Function_6_1804",         # 06, 6
        "Function_7_1CDF",         # 07, 7
        "Function_8_3696",         # 08, 8
        "Function_9_36D5",         # 09, 9
        "Function_10_5653",        # 0A, 10
        "Function_11_5670",        # 0B, 11
        "Function_12_56D1",        # 0C, 12
        "Function_13_56EE",        # 0D, 13
        "Function_14_79FC",        # 0E, 14
        "Function_15_7A18",        # 0F, 15
        "Function_16_96A8",        # 10, 16
        "Function_17_B99D",        # 11, 17
        "Function_18_DA16",        # 12, 18
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_200"),
        (1, "loc_20C"),
        (2, "loc_218"),
        (3, "loc_224"),
        (4, "loc_230"),
        (5, "loc_23C"),
        (6, "loc_248"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_200")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_20C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_218")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_224")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_230")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_23C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_248")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_254")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_260")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_277")

    Return()

    # Function_0_1C8 end

    def Function_1_278(): pass

    label("Function_1_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0")
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B")
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x40)

    label("loc_29B")

    ClearChrFlags(0x9, 0x80)

    label("loc_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_310")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_2C0")
    Event(0, 7)
    Jump("loc_310")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_2D1")
    Event(0, 9)
    Jump("loc_310")

    label("loc_2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_2E2")
    Event(0, 13)
    Jump("loc_310")

    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_2F3")
    Event(0, 15)
    Jump("loc_310")

    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_304")
    Event(0, 16)
    Jump("loc_310")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_310")
    Event(0, 17)

    label("loc_310")

    Return()

    # Function_1_278 end

    def Function_2_311(): pass

    label("Function_2_311")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF0A070D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    SetMapObjFrame(0x0, "door_l1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_l2", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r2", 0x0, 0x1)
    Sound(132, 1, 70, 0)
    Sound(497, 1, 40, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_384")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_384")

    Return()

    # Function_2_311 end

    def Function_3_385(): pass

    label("Function_3_385")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6A), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_42F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A8")
    Call(0, 5)
    Jump("loc_42A")

    label("loc_3A8")


    ChrTalk(
        0x8,
        (
            "#10704F…… For a while,\x01",
            "I am hitting the wind here.\x02\x03",
            "#10702FThere is no need to hurry,\x01",
            "Please prepare slowly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A")

    Jump("loc_A11")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_954")
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#10708F…… Finally, tomorrow ……\x01",
            "I'm sneaking into Cros Bell City.\x02\x03",
            "#10702FThat long period\x01",
            "Although it was not separated,\x01",
            "I feel quite nostalgic for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FReally……\x02\x03",
            "#00006FBecause the barrier disappeared, \"Shinkin\"\x01",
            "I'm concentrating on the defense of the city ….\x02\x03",
            "#00008FThe people of the alkane shell\x01",
            "I wonder what you are doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704FProbably … probably now,\x01",
            "I think that you are continuing practicing.\x02\x03",
            "No matter what happens,\x01",
            "To raise the perfection of the stage\x01",
            "I can not shake with just looking forward ……\x02\x03",
            "#10710FThat is Iria's will … …\x01",
            "Because it is Alkan shell's way of life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHaha, maybe it is.\x02\x03",
            "#00000F… … Liberate Cross Bell City,\x01",
            "If this incident resolves all the way … …\x01",
            "What are you planning to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704F…… I'd like to see Ms. Iria,\x01",
            "As a former artist\x01",
            "I want to continue dancing with the alkane shell …\x02\x03",
            "Although I have that intention,\x01",
            "I do not know yet.\x02\x03",
            "#10708FIria and Shri-chan\x01",
            "What do I have to say when I meet again …?\x01",
            "Even so it will not come out now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F……Really.\x02\x03",
            "#00000FBut even Iria\x01",
            "Alkan Shell, too,\x01",
            "I'm surely willing to accept you.\x02\x03",
            "Do not think hard, now that you are in front of you\x01",
            "You should focus more on it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10704F…… Hehe, it is true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyway, Cross Bell City\x01",
            "Nothing will start to not release.\x02\x03",
            "#00000FWe both have to work hard tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10702FYes……!\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x1DB, 2)
    Jump("loc_A11")

    label("loc_954")

    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#10704FTonight I looked at the moon slowly here,\x01",
            "I think that I will calm my mind.\x02\x03",
            "#10710FCrossbell City and Alcan Shell\x01",
            "To release … … tomorrow\x01",
            "I have to work hard to the utmost.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)

    label("loc_A11")

    TalkEnd(0xFE)
    Return()

    # Function_3_385 end

    def Function_4_A15(): pass

    label("Function_4_A15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D92")

    ChrTalk(
        0x9,
        (
            "#01200F#3CTomorrow's crossbell city liberation strategy ……\x01",
            "I also as a scout\x01",
            "I'm going to get down to the city.\x02\x03",
            "#01203FAlthough it will be a different point from Omira,\x01",
            "As soon as there is something, let 's rush soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I beg you.\x02\x03",
            "#00004Fby the way,\x01",
            "Gods in mountainous areas also\x01",
            "You helped me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3CWell, to them\x01",
            "The resistance of the guard\x01",
            "I am telling you to help.\x02\x03",
            "If they can take the terrain\x01",
            "Even a hunting opponent of \"red constellation\"\x01",
            "I will be able to bring it in the fight for five minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see……\x01",
            "The help of the three lieutenants of Mireille\x01",
            "It looks good to leave it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3CWell, we can do god wolves\x01",
            "It is that extent as a help.\x02\x03",
            "It is not until Ka'a regains\x01",
            "It will be the function of the other person to the last.\x02\x03",
            "#01203FBefore we get there\x01",
            "What difficulties are awaiting,\x01",
            "Although it can not be known variously … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh … but, Ka'aa\x01",
            "I will regain anything.\x02\x03",
            "#00000FWatch over Zeit, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3CWell …\x01",
            "Let's make it look.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 6)
    Jump("loc_E10")

    label("loc_D92")


    ChrTalk(
        0x9,
        (
            "#01200F#3CIt is not until Ka'a regains\x01",
            "It will be the function of the other person to the last.\x02\x03",
            "Can you accomplish that mission …?\x01",
            "Let's make it look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E10")

    TalkEnd(0xFE)
    Return()

    # Function_4_A15 end

    def Function_5_E14(): pass

    label("Function_5_E14")

    EventBegin(0x0)
    Fade(500)
    OP_68(3230, 200, 1330, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11810, 0)
    SetChrPos(0x101, 1070, 0, 280, 90)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_END)), "loc_E6E")
    OP_93(0x8, 0x10E, 0x0)

    label("loc_E6E")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1593")

    ChrTalk(
        0x101,
        (
            "#6P#00005FLisha …\x01",
            "What happened in a place like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11P#10712FAh …… Lloyd.\x02\x03",
            "#10710F… … Yes, as tomorrow's preparation is in place,\x01",
            "I was thinking a little.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#11P#10708F#5P…… Finally, tomorrow ……\x01",
            "I'm sneaking into Cros Bell City.\x02\x03",
            "#10702FThat long period\x01",
            "Although it was not separated,\x01",
            "I feel quite nostalgic for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FReally……\x02\x03",
            "#00006FBecause the barrier disappeared, \"Shinkin\"\x01",
            "I'm concentrating on the defense of the city ….\x02\x03",
            "#00008FThe people of the alkane shell\x01",
            "I wonder what you are doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10704F#5PProbably … probably now,\x01",
            "I think that you are continuing practicing.\x02\x03",
            "No matter what happens,\x01",
            "To raise the perfection of the stage\x01",
            "I can not shake with just looking forward ……\x02\x03",
            "#10710FThat is Iria's way of life ……\x01",
            "Because it is the style of alkane shell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FHaha, maybe it is.\x02\x03",
            "#00000F… … Liberate Cross Bell City,\x01",
            "If this incident resolves all the way … …\x01",
            "What are you planning to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#10704F…… I'd like to see Ms. Iria,\x01",
            "As a former artist\x01",
            "I want to continue dancing with the alkane shell …\x02\x03",
            "Although I have that intention,\x01",
            "I do not know yet.\x02\x03",
            "#10708FIria and Shri-chan\x01",
            "What do I have to say when I meet again …?\x01",
            "Even so it will not come out now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F……Really.\x02\x03",
            "#00000FBut even Iria\x01",
            "Alkan Shell, too,\x01",
            "I am sure you will accept you.\x02\x03",
            "Without thinking about difficult things,\x01",
            "As long as it is as it is\x01",
            "Is not it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#10712F…… as it is ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11P#10703F… … Well, Mr. Lloyd.\x02\x03",
            "#10701FAfter this, I have only a little\x01",
            "Could I have Lloyd's time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10704FHuhu, recently even myself,\x01",
            "I think that I was overwhelmed … …\x02\x03",
            "#10710FBefore the operation of tomorrow,\x01",
            "A little chatter\x01",
            "I'd like you to do it.\x02\x03",
            "Once you have completed the preparation,\x01",
            "Come again to this deck … …\x01",
            "Would you please tell me again?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 2)
    Jump("loc_1649")

    label("loc_1593")


    ChrTalk(
        0x8,
        (
            "#11P#10704FBefore the operation of tomorrow,\x01",
            "A little chatter\x01",
            "I'd like you to do it.\x02\x03",
            "#10710FOnce you have completed the preparation,\x01",
            "Come again to this deck … …\x01",
            "Would you please tell me again?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1649")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Receive invitation from Lisha\x01",      # 0
            "To give up\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176D")

    ChrTalk(
        0x101,
        "#6P#00002FOh, if I am OK with something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10709FHehe, thank you.\x02\x03",
            "#10704F…… For a while,\x01",
            "I am hitting the wind here.\x02\x03",
            "#10702FThere is no need to hurry,\x01",
            "Please prepare slowly.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 6)
    SetScenarioFlags(0x1AB, 0)
    Jump("loc_17F1")

    label("loc_176D")


    ChrTalk(
        0x8,
        (
            "#11P#10704F……Is that so.\x02\x03",
            "#10702FHuhu, I wish you were indeed.\x01",
            "Please give me a voice again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh, I understand.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_17F1")

    ClearChrFlags(0x8, 0x10)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_5_E14 end

    def Function_6_1804(): pass

    label("Function_6_1804")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_18C9")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(… … to Eli, that you can not go\x01",
            "I have to apologize properly. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd to Eli,\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 3)
    Jump("loc_1CDE")

    label("loc_18C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_1983")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(… … to Tio, you can not go\x01",
            "I have to apologize properly. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd to Tio,\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 4)
    Jump("loc_1CDE")

    label("loc_1983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_1A41")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(… … that Randy will not be able to go\x01",
            "I have to apologize properly. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is Randy,\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 5)
    Jump("loc_1CDE")

    label("loc_1A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_1AFB")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(… … to Noel, you can not go\x01",
            "I have to apologize properly. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd to Noel,\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 6)
    Jump("loc_1CDE")

    label("loc_1AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_1BB1")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(… … I will not be able to go to Waji\x01",
            "I have to apologize properly. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is indeed,\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 7)
    Jump("loc_1CDE")

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_1C6F")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(… … to Lisha, you can not go\x01",
            "I have to apologize properly. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd said to Lisha,\x01",
            "I apologized for losing my promise.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AB, 0)
    Jump("loc_1CDE")

    label("loc_1C6F")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F(…… one thing in a sleeping room\x01",
            "After preparing for tomorrow,\x01",
            "Let's face the deck. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1CDE")

    Return()

    # Function_6_1804 end

    def Function_7_1CDF(): pass

    label("Function_7_1CDF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00100.itc", 0x1E)
    LoadChrToIndex("apl/ch51800.itc", 0x1F)
    LoadChrToIndex("apl/ch5180A.itc", 0x20)
    LoadChrToIndex("apl/ch5180B.itc", 0x21)
    SoundLoad(3411)
    SoundLoad(3412)
    SoundLoad(3413)
    SoundLoad(3414)
    SoundLoad(3415)
    SoundLoad(3416)
    SoundLoad(3417)
    SoundLoad(3418)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xA, 500, 0, -3750, 180)
    OP_63(0xA, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(135, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(2000, 0)
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(135, 10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    OP_64(0xA)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00108F#5P#30W…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    SetChrPos(0xA, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(19500, 2000)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_1EC2():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EC2)

    def lambda_1ED7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1ED7)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00002F#5PAh……\x01",
            "Eli, were you coming before?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F24():

        label("loc_1F24")

        TurnDirection(0xA, 0x101, 500)
        Yield()
        Jump("loc_1F24")

    QueueWorkItem2(0xA, 2, lambda_1F24)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xA,
        (
            "#3411V#30WYup……\x01",
            "Lloyd, cheers for good work.\x02\x03",
            "#3412VPrepare for tomorrow, are you done?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD54)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(45, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0xF, 1, 0, 8)

    def lambda_2041():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2041)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_68(350, 1000, -3890, 50000)
    MoveCamera(44, 14, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(16880, 50000)

    ChrTalk(
        0x101,
        (
            "#00000F#5POh, the other way around.\x02\x03",
            "#00006FAs might be expected……\x01",
            "I can not say that it is perfect.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2179, 255, 100, 0)

    ChrTalk(
        0xA,
        "#00109F#11P#30WHehu ……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0xB4, 0x190)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00104F#5P#30W… Wonder …\x01",
            "It is such a crisis situation.\x02\x03",
            "For some reason,\x01",
            "My heart is calm.\x02\x03",
            "#00108FAbout Bell, Uncle's,\x01",
            "About Kea-chan ……\x02\x03",
            "#00102FAnxiety and worrying things\x01",
            "Even though there are many ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PI see……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00004F#5PI am the same ….\x02\x03",
            "#00008FA#2RHala#Is not it constricted\x01",
            "You said you saw something to do.\x02\x03",
            "#00002FThis, too, Eli and\x01",
            "I think thanks to everyone.\x02\x03",
            "#00009FThank you, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00102F#5PHehu ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00104F#11PThose who say thank you.\x02\x03",
            "#00108FIf true, with anxiety and impatience\x01",
            "Even though it may be collapsed … …\x02\x03",
            "#00102FBecause you stayed\x01",
            "I'm right here, like this\x01",
            "It can be standing … …\x02\x03",
            "#00104F……Thank you.\x01",
            "I am truly glad that you stayed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#6PErie …\x02\x03",
            "#00012Fmy mother……\x01",
            "It would be honor if I served you.\x02\x03",
            "#00004FAs a little leader\x01",
            "To the extent that everyone can rely on it\x01",
            "You mean you can grow up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#11PHuhu, you have long\x01",
            "It is a leader of all of us.\x02\x03",
            "If not, to this place\x01",
            "I think that we could not come together.\x02\x03",
            "#00108FBut ── What I am talking about\x01",
            "That does not mean that.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        "#00005F#6PHuh……\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -3750, 90)
    SetChrPos(0xA, 500, 0, -3750, 180)
    OP_68(250, 1000, -4400, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 1000, -3750, 50000)
    MoveCamera(135, 20, 0, 50000)
    OP_6E(800, 50000)
    SetCameraDistance(10000, 50000)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#00106F#5P…… This incident.\x02\x03",
            "No matter how you resolve\x01",
            "Crossbell will be serious.\x02\x03",
            "#00108FMaybe, our support department also\x01",
            "I can not stay as it is … …\x02\x03",
            "Each one has its own strength\x01",
            "In a position that makes the most of it\x01",
            "I need to work hard …\x02\x03",
            "#00101FTo rebuild the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P……Ah.\x02\x03",
            "#00008FI am the police like this …\x02\x03",
            "Randy maybe,\x01",
            "When the Defense Forces Return to the Guard\x01",
            "We may be asked for cooperation.\x02\x03",
            "#00003FThio might return to the Foundation\x01",
            "Perhaps in the direction of the power net ……\x02\x03",
            "#00001F…… And Eli is …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#5P… in an emergency\x01",
            "Crisis management in the administrative and diplomatic direction.\x02\x03",
            "Perhaps, if I were asked\x01",
            "I think such knowledge and ability.\x02\x03",
            "#00108FAnd I am a student\x01",
            "I have accumulated such studies.\x02\x03",
            "#00102FJust like this situation\x01",
            "In order to get the power that can be handled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P#30W……Really……\x02\x03",
            "#00006F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00104F#5PHuh … it was good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P……Huh……?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00102F#5PA little like that\x01",
            "He seems to miss me.\x02\x03",
            "#00106F\"Okay, I can do it if Eliya\"\x01",
            "I thought of what to do if encouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12Pmy mother……\x02\x03",
            "#00006F…… If it is true\x01",
            "I guess they have to say it … ….\x02\x03",
            "#00008FIt seems that it can not be divisible so easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#5PWhy is that …?\x02\x03",
            "#00100FTio and Randy are\x01",
            "For the same reason as I am gone …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12PWell, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00113F#5P─ ─ Answer, Lloyd.\x02\x03",
            "If I am worried right now\x01",
            "Only how you answer … …\x02\x03",
            "#00108FAlready … I do not know, right?\x02\x03",
            "#00116FHow come I ……\x01",
            "Did you say you want to talk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P………… Erie ………………\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_93(0x101, 0xB4, 0x1F4)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -4250, 180)
    SetChrPos(0xA, 500, 0, -4250, 270)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(0, 1000, -4250, 50000)
    MoveCamera(45, 15, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(15500, 50000)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#5PAt first it is ……\x01",
            "It was a vaguely longing.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x514, 0x5, 0x0, 0x1, 0x2, 0x1, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        "#00105F#11PHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PThat child is cuddly, dignified\x01",
            "Still it has tolerance … …\x02\x03",
            "#00000FFrom encounter, in various ways\x01",
            "A beautiful woman#4RHuman#I thought that it was.\x02\x03",
            "#00002FEven this, at first, parenthesized\x01",
            "I was talking about being pretty … ….\x02\x03",
            "#00012FWhen it is white, ……\x01",
            "I was excited all the time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0x4, 0x5, 0x6)
    Sleep(300)

    ChrTalk(
        0xA,
        "#00112F#11P#30WB, Lloyd …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PAs a matter of course,\x01",
            "The lady who lives in different world is in the wind\x01",
            "I have no idea ….\x02\x03",
            "Still though ….\x01",
            "That being a colleague of that child\x01",
            "It was a secret pride for me.\x02\x03",
            "#00002FHaving consulted with that child,\x01",
            "It's modest, but I got to use my strength\x01",
            "I was more than anything for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00102F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0x6, 0x7, 0x8)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#6PAnd nearly a year ago,\x01",
            "All fun and painful things,\x01",
            "Together with us ……\x02\x03",
            "Although it became separated,\x01",
            "At last we can meet again …\x02\x03",
            "#00008FEven now, as when we met …\x02\x03",
            "#00002FNo, she is throbbing any further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00116F#11P……… Lloyd ……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P── I like it, Eli.\x02\x03",
            "As a friend ……\x01",
            "Not just as a family.\x02\x03",
            "#00000FAs a girl, you.\x02",
        )
    )

    CloseMessageWindow()
    Sound(812, 0, 70, 0)
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0xB, 0xC, 0xD)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#00106F#3413V#11PLloyd …\x02",
    )

    CloseMessageWindow()
    OP_A1(0xA, 0x640, 0x4, 0xD, 0xE, 0xF, 0x10)

    def lambda_3192():

        label("loc_3192")

        OP_A0(0xFE, 1000, 0x10, 0x12)
        Yield()
        Jump("loc_3192")

    QueueWorkItem2(0xA, 3, lambda_3192)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00116F#3414V#11PI also like ── you.\x02",
    )

    CloseMessageWindow()
    OP_24(0xD56)
    Sleep(300)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x1)
    OP_68(400, 1000, -4250, 1200)

    def lambda_31FA():
        OP_9B(0x1, 0xFE, 0x0, 0x190, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31FA)
    Sleep(50)

    def lambda_3212():
        OP_A0(0xFE, 1000, 0x1, 0x5)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3212)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(812, 0, 100, 0)

    def lambda_3248():
        OP_A0(0xFE, 1000, 0x7, 0x9)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3248)

    def lambda_3255():
        OP_A0(0xFE, 1000, 0x7, 0x9)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3255)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Fade(800)
    SetCameraDistance(15000, 1000)

    def lambda_3278():
        OP_A0(0xFE, 1000, 0x9, 0xC)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3278)
    OP_A0(0xA, 1000, 0x9, 0xC)
    Sleep(300)
    OP_A0(0xA, 1000, 0x19, 0x1E)
    Sleep(300)

    ChrTalk(
        0xA,
        "#3415V#11P#40W#2S……………Hmm…………………\x02",
    )

    CloseMessageWindow()
    OP_24(0xD57)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    Sound(812, 0, 100, 0)

    def lambda_32DC():
        OP_A0(0xFE, 1000, 0xC, 0xF)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_32DC)

    def lambda_32E9():
        OP_A0(0xFE, 1000, 0xC, 0xF)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_32E9)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33EB")

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30Wmy mother……\x02\x03",
            "#00002F…… Continuation of that time,\x01",
            "I guess I could finally ……?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        (
            "#00104F#3416V#11P#40W…………Yup……………\x02\x03",
            "#00116F#3417VI have been waiting forever ……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD59)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        "#00012F#6P#40WSorry, let me wait.\x02",
    )

    CloseMessageWindow()
    Jump("loc_344D")

    label("loc_33EB")


    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WAlways ……\x01",
            "I wanted to do this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00104F#11P#40W…………Me too………………\x02",
    )

    CloseMessageWindow()

    label("loc_344D")

    Sleep(300)

    def lambda_3455():
        OP_A0(0xFE, 1000, 0xF, 0x12)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3455)
    Sleep(50)

    def lambda_3465():
        OP_A0(0xFE, 1000, 0xF, 0x12)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3465)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W─ ─ Even if you work the same way\x01",
            "Even if you can not walk … …\x02\x03",
            "#00004FWe always needed each other,\x01",
            "Like supporting one another to move forward ……\x02\x03",
            "#00002FDoes it become such a relationship?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xA, 1300, 0x12, 0x17)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00109F#3418V#11P#40W………Yes…………!\x02",
    )

    CloseMessageWindow()
    OP_24(0xD5A)
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(16500, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x157C)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_35A5")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_35A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35B7")
    Jump("loc_3673")

    label("loc_35B7")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Eli are\x01",
            "I mastered Star Blast..\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Combi Craft of Lloyd and Eli,\x01",
            "\"Star Blast\" has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x1, 0x1AE)
    AddCraft(0x0, 0x1AE)

    label("loc_3673")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x28, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 1)
    OP_29(0xB1, 0x1, 0x1)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1CDF end

    def Function_8_3696(): pass

    label("Function_8_3696")

    OP_25(0x84, 0x41)
    OP_25(0x1F1, 0x23)
    Sleep(300)
    OP_25(0x84, 0x3C)
    OP_25(0x1F1, 0x1E)
    Sleep(300)
    OP_25(0x84, 0x37)
    OP_25(0x1F1, 0x19)
    Sleep(300)
    OP_25(0x84, 0x32)
    OP_25(0x1F1, 0x14)
    Sleep(300)
    OP_25(0x84, 0x2D)
    Sleep(300)
    OP_25(0x84, 0x28)
    Sleep(300)
    OP_25(0x84, 0x23)
    Return()

    # Function_8_3696 end

    def Function_9_36D5(): pass

    label("Function_9_36D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00200.itc", 0x1E)
    LoadChrToIndex("apl/ch51801.itc", 0x1F)
    LoadChrToIndex("apl/ch51802.itc", 0x20)
    SoundLoad(2698)
    SoundLoad(2699)
    SoundLoad(2700)
    SoundLoad(2701)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00202.itp")
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xB, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(470, 800, 1980, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_3803():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3803)

    def lambda_3818():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3818)
    PlayBGM("ed7560", 0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5P(That, Tio … …??)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 1, 0, 8)
    Fade(1000)
    SetChrPos(0x101, 250, 0, 1250, 180)
    SetChrPos(0xB, 500, 0, -3750, 180)
    OP_68(500, 2300, -3750, 0)
    MoveCamera(125, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7500, 0)
    OP_68(500, 2300, -3750, 3000)
    MoveCamera(125, -5, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(8500, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xB,
        "#00208F#30W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00000F#6P#N── Tio?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_68(320, 1000, -2950, 5000)
    MoveCamera(115, 15, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9000, 5000)

    def lambda_39B4():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF92A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39B4)
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    OP_0D()

    def lambda_39FC():

        label("loc_39FC")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_39FC")

    QueueWorkItem2(0xB, 2, lambda_39FC)
    Sleep(1500)
    OP_64(0xB)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xB, 500)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xB,
        "#2698V#40WLloyd …… Mr. …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA8A)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PIt is unusual.\x02\x03",
            "#00002FUntil a voice calls\x01",
            "Tio does not notice.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        "#00204F#2699V#11P#40WHehe … … That's right.\x02",
    )

    CloseMessageWindow()
    OP_24(0xA8B)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -3750, 3000)
    MoveCamera(135, 20, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(9000, 3000)
    OP_95(0x101, -500, 0, -3750, 1200, 0x0)
    TurnDirection(0x101, 0xB, 500)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#12PPreparation for tomorrow, I made it through.\x02\x03",
            "#00000FI can not say that it is perfect\x01",
            "If you think about the difficulties of everyone else\x01",
            "I think this is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204F#5PYes……\x02\x03",
            "To meet with Kaoru and section chiefs too\x01",
            "I have to work hard.\x02\x03",
            "#00202FAlso, Koppe is worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PThat's right.\x02\x03",
            "#00005FBy the way, Jonah\x01",
            "I was sent to Mishram.\x02\x03",
            "Roberts' Chief of the Foundation\x01",
            "I wonder what I am doing now.\x02\x03",
            "#00008FThe situation is a situation ……\x01",
            "Did he return to Leman Autonomous Region?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00206F#5PNo, apparently the chief is\x01",
            "To withdraw from the Foundation\x01",
            "I do not seem to accept it.\x02\x03",
            "#00208FMarybele was robbed of us\x01",
            "To check the status of the power net\x01",
            "It seems to remain in the city ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    OP_A0(0xB, 1000, 0x1, 0x3)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#00206F#5PWell, it's about that person\x01",
            "Pursuit and pursuit\x01",
            "I think that it is escaping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PI see … a little worried.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0xB, 1200, 0x3, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00202F#5PYes……\x01",
            "Just a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(1000)
    SetChrSubChip(0xB, 0x4)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xB, 500, 0, -4250, 270)
    OP_68(0, 1100, -4250, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_68(0, 1000, -4250, 50000)
    MoveCamera(45, 25, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(16000, 50000)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00206F#11P── Mr. Lloyd.\x02\x03",
            "#00208FCan you consult me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6POh, of course.\x02\x03",
            "#00001FPossibly\x01",
            "Do you mean the letter you were looking at some time ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00206F#11PDid you notice it … ….\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    OP_A0(0xB, 1000, 0x4, 0x6)
    Sleep(500)
    Sound(802, 0, 100, 0)
    OP_A0(0xB, 1000, 0x7, 0x8)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00203F#11PYesterday, on the route of Abbas\x01",
            "A letter delivered to me ……\x02\x03",
            "#00201FI am in the Republic of Altair City\x01",
            "It is from my parents.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#6PHuh……! Is it?\x02\x03",
            "#00002FWell then, from Remiferia\x01",
            "All the way to meet Tio …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00206F#11PYes, since Crosbell became independent\x01",
            "I can not contact you by letter or communication … …\x02\x03",
            "Based on information from the Foundation\x01",
            "It seems that they are coming to the border town.\x02\x03",
            "#00208FCurrently, there is no movement other than cargo\x01",
            "Because it has been completely restricted\x01",
            "It seems to be stuck up … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PReally……\x02\x03",
            "#00000F… …. The story is quick!\x01",
            "With this ship till Altair City -\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0xB, 1300, 0x8, 0xA)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#00204F#11PIt is not necessary.\x02\x03",
            "The information that I am already safe is\x01",
            "I got told by the same route.\x02\x03",
            "#00208FBesides, my heart is disturbed when I see you\x01",
            "There may be troubles for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P……… but, even …………\x02\x03",
            "#00006F#30W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xB, 800, 0xA, 0x8)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00209F#11PWhatching\x01",
            "Please do not look like that.\x02\x03",
            "#00202FIf this incident resolves\x01",
            "I will definitely meet my parents.\x02\x03",
            "#00204FThanks to Mr. Lloyd,\x01",
            "A little relief came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0xB, 1000, 0xD, 0xB)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00208F#5P#30W… … Everyone is separated … …\x02\x03",
            "I am anxious, lonely,\x01",
            "Listening to Mr. Lloyd's wanted\x01",
            "Tightened my chest with worry ……\x02\x03",
            "#00206F…… I was really happy.\x02\x03",
            "I was able to see Mr. Lloyd again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30WAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204F#5P#30WAt that time, I thought.\x02\x03",
            "Oh ─ ─ I am alive.\x02\x03",
            "#00208FBy thinking carefully someone\x01",
            "It is said that it exists between people.\x02\x03",
            "#00202F…… How to live,\x01",
            "How come alive ……\x02\x03",
            "#00209FThree years ago, I tried to listen to Mr. Guy\x01",
            "I felt that I understood the answer to the question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6P#30W…… Tio ………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xB, 1300, 0xB, 0xD)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00206F#11P#30WThen, Erie and Mr.\x01",
            "Meet Randy's again … …\x02\x03",
            "#00208FEveryone try hard,\x01",
            "Come here for Ka'a … ….\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(812, 0, 60, 0)
    OP_A0(0xB, 1200, 0xD, 0x10)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00212F#11P#30W… and then read this letter\x01",
            "It looks like ice melts\x01",
            "An obedient feeling came up.\x02\x03",
            "#00213Fafter a long time……\x01",
            "I want to see my father and mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(400, 1000, -4250, 1200)
    OP_9A(0x101, 0xB, 0x258, 0x1F4, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)

    def lambda_487D():
        OP_A0(0xFE, 1000, 0x10, 0x13)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_487D)

    def lambda_488A():
        OP_A0(0xFE, 1000, 0x20, 0x23)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_488A)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sound(898, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 10)
    BeginChrThread(0x101, 3, 0, 12)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0xB,
        "#00216F#11P#40W#2S………….. Ah ………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W……Was good.\x01",
            "It is very nice……\x02\x03",
            "About the chance\x01",
            "I'm kind of embarrassed … ….\x02\x03",
            "#00002FBut, Tio\x01",
            "It became possible to think so\x01",
            "I'm more than anything above anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x4B0, 0x5, 0x13, 0x18, 0x19, 0x18, 0x13)
    Sleep(300)

    ChrTalk(
        0xB,
        "#00215F#11P#30W……… Mr. Lloyd …………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    Fade(1000)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 0, 0, -3750, 90)
    SetChrPos(0xB, 500, 0, -3750, 270)
    OP_68(0, 1000, -3750, 0)
    MoveCamera(140, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    MoveCamera(140, 20, 0, 50000)
    SetCameraDistance(9000, 50000)

    def lambda_4A5A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A5A)
    OP_0D()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_A1(0xB, 0x320, 0x3, 0x1, 0x2, 0x3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00204F#5P#30W…… There are two, please.\x02\x03",
            "Would you please listen to me?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00002F#12POh ─ anything.\x02\x03",
            "#00009FPlease do not hesitate to tell me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00208F#5P#30WThat one, … …\x02\x03",
            "#00208FIt is also possible to have your head stroked\x01",
            "I like it very much ….\x02\x03",
            "#00201FAs expected, in such a beautiful night\x01",
            "I feel that I am a little childish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#12PIs that so?\x02\x03",
            "#00012FWell, certainly I\x01",
            "Big brother or Randy\x01",
            "I feel like being treated like a child.\x02\x03",
            "#00000FWell then, then …\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 11)
    Sleep(1500)
    OP_63(0x101, 0x0, 1900, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 1950, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#12PTe, Tio …?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_A1(0xB, 0x3E8, 0x5, 0x1E, 0x2B, 0x2C, 0x2B, 0x1E)
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            "#40WWell, that … …\x02\x03",
            "When I reunited, I ran and hugged\x01",
            "Because it seemed a little painful ……\x02\x03",
            "…… This is okay, is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#12P#30WOh, ah ……\x02\x03",
            "#00004F…………………………………….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(250, 1000, -3750, 1000)
    OP_96(0x101, 0xFFFFFF9C, 0x0, 0xFFFFF15A, 0x1F4, 0x0)
    Fade(250)
    Sound(898, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_4E56():
        OP_A0(0xFE, 1000, 0x1E, 0x22)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_4E56)

    def lambda_4E63():
        OP_A0(0xFE, 1000, 0x36, 0x39)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4E63)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        (
            "#05524F#2700V#5P#40WHehe … … It is warm … …\x02\x03",
            "#05526F#2701VLike Ellie\x01",
            "I do not feel comfortable\x01",
            "I am sorry but ……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA8D)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00012F#12P#30WNo, this is this … …\x02\x03",
            "#00008F(I mean, I'm jealous ….\x01",
            "…… The sweet smell of Tio … …)\x02\x03",
            "#00011F(─ ─ ─ ─ not!)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(812, 0, 60, 0)

    def lambda_4FA6():
        OP_A0(0xFE, 1000, 0x22, 0x25)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_4FA6)

    def lambda_4FB3():
        OP_A0(0xFE, 1000, 0x39, 0x3C)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4FB3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00012F#12PKohon ……\x01",
            "So, is there another wish?\x02\x03",
            "#00000FIf this is the case,\x01",
            "Have them get involved?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x3E8, 0x5, 0x25, 0x2E, 0x2F, 0x2E, 0x25)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#05524F#5PYes, one more …\x02\x03",
            "#05522FSomehow the case has fallen to one point\x01",
            "When my parents came to Crossbell\x01",
            "I would like to see them together.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00009F#12POh, of course.\x01",
            "I wanted to say a greeting once.\x02\x03",
            "#00002FBut even though such a thing is said\x01",
            "I do not think so … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05526F#5PNo, it's not just a greeting … …\x02\x03",
            "#05528FThe reason why I remain on Crosbell\x01",
            "I want to explain it clearly.\x02\x03",
            "#05521FOtherwise both of us\x01",
            "I will not be convinced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PIs it? Is it? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05524F#5PEveryone is here, and you are mocking\x01",
            "Crossbell with power net also\x01",
            "Although I also love it … …\x02\x03",
            "#05528FMore than that, how to live,\x01",
            "How come alive ……\x02\x03",
            "#05522FOn the part of the important person who gave me the answer\x01",
            "I want to continue living in the future ─\x02\x03",
            "#05529FI am thinking to tell you so.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00007F#12P#4SWell! Is it?#3S\x02\x03",
            "#00011FWait a moment!\x01",
            "Well then … alright …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xB, 0x2E)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#05531F#5P\"Anything\"\x01",
            "I told you … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#00012F#12P── Oh, I already understood!\x02\x03",
            "#00002FIf the case has gone so far\x01",
            "I will greet you together!\x02\x03",
            "#00006FHaha, somehow now\x01",
            "I have to think about excuses … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xB, 0x3E)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0xB,
        (
            "#05529F#5PHehu ……\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(812, 0, 60, 0)
    SetChrSubChip(0xB, 0x2E)
    Sleep(50)
    SetChrSubChip(0xB, 0x25)
    Sleep(200)
    SetCameraDistance(10500, 3500)

    def lambda_550B():
        OP_A0(0xFE, 1000, 0x26, 0x29)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_550B)

    def lambda_5518():
        OP_A0(0xFE, 1000, 0x3C, 0x39)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5518)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_555C")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_555C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_556E")
    Jump("loc_5630")

    label("loc_556E")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Tio\x01",
            "Ω#2Romega#I mastered Strike.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Tio's combi craft,\x01",
            "\"Ω strike\" has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x2, 0x1AF)
    AddCraft(0x0, 0x1AF)

    label("loc_5630")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x29, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 2)
    OP_29(0xB1, 0x1, 0x2)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_36D5 end

    def Function_10_5653(): pass

    label("Function_10_5653")

    OP_A1(0xFE, 0x3E8, 0x6, 0x13, 0x14, 0x15, 0x16, 0x15, 0x14)
    OP_A1(0xFE, 0x3E8, 0x6, 0x13, 0x14, 0x15, 0x16, 0x15, 0x14)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_10_5653 end

    def Function_11_5670(): pass

    label("Function_11_5670")

    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A0(0xFE, 900, 0x0, 0x3)
    Sleep(300)
    Sound(898, 0, 100, 0)
    OP_A0(0xFE, 900, 0x4, 0xC)
    Sleep(300)
    OP_A0(0xFE, 1000, 0xC, 0xF)
    Sound(318, 0, 100, 0)
    Sleep(200)
    Sound(898, 0, 100, 0)
    OP_A0(0xFE, 1000, 0x10, 0x14)
    Sleep(500)
    Sound(812, 0, 100, 0)
    OP_A0(0xFE, 1000, 0x14, 0x1B)
    Sleep(300)
    OP_A0(0xFE, 1000, 0x1B, 0x1E)
    Return()

    # Function_11_5670 end

    def Function_12_56D1(): pass

    label("Function_12_56D1")

    OP_A1(0xFE, 0x3E8, 0x6, 0x23, 0x24, 0x25, 0x26, 0x25, 0x24)
    OP_A1(0xFE, 0x3E8, 0x6, 0x23, 0x24, 0x25, 0x26, 0x25, 0x24)
    SetChrSubChip(0xFE, 0x23)
    Return()

    # Function_12_56D1 end

    def Function_13_56EE(): pass

    label("Function_13_56EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00300.itc", 0x1E)
    LoadChrToIndex("apl/ch51804.itc", 0x1F)
    LoadChrToIndex("apl/ch51805.itc", 0x20)
    SoundLoad(2778)
    SoundLoad(2779)
    SoundLoad(2780)
    SoundLoad(2781)
    SoundLoad(2782)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis266.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis267.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis268.itp")
    CreatePortrait(4, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis316.itp")
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xC, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(470, 800, 1980, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_589F():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_589F)

    def lambda_58B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_58B4)
    PlayBGM("ed7560", 0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xC,
        "#00300F#2778V#12P#N#30WOh, have you come?\x02",
    )

    CloseMessageWindow()
    OP_24(0xADA)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00002F#5PRandy.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 1, 0, 8)
    Fade(1000)
    SetChrPos(0x101, 500, 0, 1250, 180)
    SetChrPos(0xC, 500, 0, -3750, 0)
    OP_68(500, 2300, -3750, 0)
    MoveCamera(125, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    OP_68(500, 1600, -3750, 5000)
    MoveCamera(125, 1, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9500, 5000)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xC,
        (
            "#2779V#40WWant to invite me, please\x01",
            "To a bastard in such a night\x01",
            "You do not have enough time.\x02\x03",
            "#2780VTears you up a sexy story\x01",
            "Does not he have a partner?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xADC)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(630, 1000, -3200, 3000)
    MoveCamera(120, 10, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(10000, 3000)
    Sound(100, 0, 100, 0)

    def lambda_5B10():

        label("loc_5B10")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5B10")

    QueueWorkItem2(0xC, 2, lambda_5B10)
    OP_95(0x101, 250, 0, -1750, 1200, 0x0)
    TurnDirection(0x101, 0xC, 500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6P…… It's extra care.\x02\x03",
            "#00001FAnd it's before the strategy ……\x01",
            "I can not afford to think about such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#11PBacca, that's the time for that\x01",
            "I guess it's a chance to drop it.\x02\x03",
            "#00308FMourning \"Lloyd, I am anxious …\"\x02\x03",
            "#00301F嘇 \"It's all right, I have it\"\x02\x03",
            "#00309F嘊 \"Gabba! \"\x01",
            "I could use a golden combo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PThe last one is leaping too much ….\x02\x03",
            "#00012FRandy is motivated\x01",
            "Though it seems to be some eyebrow spitting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00310F#11PWhat?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_68(110, 1000, -4070, 4000)
    MoveCamera(135, 15, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(10000, 30000)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(500)
    EndChrThread(0xC, 0x2)
    OP_93(0xC, 0xB4, 0x190)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xC,
        "#00300F#5P… … Are preparations for tomorrow done?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6POh, honest and perfect\x01",
            "I can not say that ….\x02\x03",
            "#00001FIf you think about Mireilleu\x01",
            "I can not say a luxury.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5PWell well\x02\x03",
            "#00303FResistance and Kuroketsu direction\x01",
            "Perhaps hunters will sortie.\x02\x03",
            "#00308FUncle Takashi or Charlie\x01",
            "It will not come out easily though … …\x02\x03",
            "#00301FStill garares come out\x01",
            "It will be a tough fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PReally……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    EndChrThread(0xC, 0x2)
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6P\"Red constellation\" ……\x01",
            "It's more fighting power than I heard.\x02\x03",
            "#00000FIt is said that the strongest in the western continent\x01",
            "I feel like I can nod.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5PWell, if you just say history\x01",
            "It goes back to the medieval age of darkness.\x02\x03",
            "#00301FBerserker#6RBerzerger#Orlando …\x02\x03",
            "From that time I knew my name\x01",
            "It seems that it was a family of warriors.\x02\x03",
            "#00308FAlways incorporate the latest battle techniques,\x01",
            "By strengthening the body with a special forging method\x01",
            "The warrior group continued to be called \"strongest\" ……\x02\x03",
            "#00303FIt became a hunting corps in modern times,\x01",
            "A red scorpion that was a coat of arms of the family\x01",
            "That's why I listed it as a name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PIs that so……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0xC, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#12PPossibly …\x02\x03",
            "#00001FBefore the race in the old city\x01",
            "Did you do it in such a format?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#00309F#5PHaha, well aware.\x02\x03",
            "#00300FThat is done in \"Red constellation\"\x01",
            "I arranged battle training.\x02\x03",
            "#00306FOriginally it is closer to actual war,\x01",
            "It is a funny thing to kill whenever it dies.\x02\x03",
            "From the time of a brat, like every day\x01",
            "It was a monstrous torture until I got blood breathing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PI see……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00000F#12P… … I charged it to Randy\x01",
            "Is it my father who was called \"fighting spirit\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5PAh\x01",
            "Bardelle Orlando.\x02\x03",
            "#00308FLike a steel lion\x01",
            "He was a tough and unforgiving father.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_93(0xC, 0xB4, 0x190)
    Fade(1000)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xC, 500, 0, -4250, 180)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#00303F#5P#30W─ ─ three years ago.\x02\x03",
            "From that \"fighting spirit\" I\x01",
            "I was given a duty.\x02\x03",
            "#00308FA hunting soldier who can also be called a nemesis,\x01",
            "Two squads of \"Western brigade\" …\x02\x03",
            "#00311FThey are in my troops\x01",
            "It was content to annihilate.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    SetCameraDistance(15000, 2500)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30WEnemy force is double this time …\x02\x03",
            "Considering that competence is competing\x01",
            "To be honest, it was a strength difference that was too strict.\x02\x03",
            "But here is a surprise attack\x01",
            "There was a strength to use terrain.\x02\x03",
            "And I …\x02\x03",
            "…… for daily supply\x01",
            "I used a village I had dropped by.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(280, 145, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30WIn the raid,\x01",
            "Pull one of the troops to the village … …\x02\x03",
            "Dividing by causing a cliff collapse,\x01",
            "I crushed the other at a stretch.\x02\x03",
            "And the barn out of the village\x01",
            "Invite the confusion of the enemies by blowing up … …\x02\x03",
            "Read the route to retreat from the village\x01",
            "I concentrated all the firepower there and destroyed it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30W…… The victim's sacrifice\x01",
            "I did not intend to give out one person.\x02\x03",
            "But, as for the prospect in the battlefield\x01",
            "It is fluid and it can not be counted on.\x02\x03",
            "After all, the point of destroying\x01",
            "Being close to the village as 50 age … …\x02\x03",
            "I brought up one goods store.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x7D0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(800)
    SetMessageWindowPos(280, 145, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#40W…… Maybe, other than hunt fellows\x01",
            "It was my first time to say nigga.\x02\x03",
            "When there is no duty, occasionally at the bar\x01",
            "Take a drink together and make a napping ……\x02\x03",
            "Go out to the city and shop your store\x01",
            "I told you to have a dream.\x02\x03",
            "All that dream and life, I took away.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(858, 0, 100, 0)
    Sleep(1500)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    Sleep(1300)
    SetMessageWindowPos(280, 170, -1, -1)
    SetChrName("Charlie")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WWow!\x01",
            "Randy brother, you do it ♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kibun Sigmund")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WKuku - Passed, Randolph.\x02\x03",
            "With this \"trial\"\x01",
            "You are determined to be the next \"fighting spirit\".\x02\x03",
            "In order to succeed the brother's trace,\x01",
            "Stay ahead with it from now on.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    MoveCamera(40, 20, 0, 50000)
    SetCameraDistance(16540, 50000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#6P#30W…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P#30W…… I guess it's a story, is not it?\x02\x03",
            "#00308FSeparately, with that shock dead\x01",
            "You did not wash your feet from the battlefield.\x02\x03",
            "How to live as a hunter\x01",
            "Even though I did not make mistakes.\x02\x03",
            "#00303FI am only … ….\x01",
            "I did not understand it.\x02\x03",
            "Someday I want to own my store\x01",
            "His little dream … …\x02\x03",
            "Become \"a fighting spirit\" either\x01",
            "I keep fighting until I die … in my life …\x02\x03",
            "#00311FWas it really meaningful either?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P#30W… … Randy ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00303F#5P#30WPerhaps it is ……\x01",
            "I carried on the \"business#2RLike this#\"I wonder what.\x02\x03",
            "Born as a family of Orlando\x01",
            "It can not be a shura, halfway halfway\x01",
            "I am the one who lived on the battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6PRandy said that \"work#2RLike this#The\x01",
            "I am planning to break it …\x02\x03",
            "#00001FBy overcoming that uncle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P… Well.\x02\x03",
            "#00308FNow that my father died, besides that\x01",
            "There is no way for me to cut off \"work\".\x02\x03",
            "With my own power and foothold\x01",
            "If I could overcome that word … …\x02\x03",
            "#00300FAt the time I finally got Kerry three years ago\x01",
            "I feel like I can attach it.\x02\x03",
            "#00304FNo more\x01",
            "Just not being swept away.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F29")

    ChrTalk(
        0x101,
        (
            "#00004F#6P……I see……\x02\x03",
            "#00000FOf course, as a buddy\x01",
            "I wonder if they will cooperate?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F8F")

    label("loc_6F29")


    ChrTalk(
        0x101,
        (
            "#00004F#6P……I see……\x02\x03",
            "#00000FThings that you told me like that\x01",
            "Of course, you can cooperate, do not you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F8F")

    TurnDirection(0xC, 0x101, 400)
    Sleep(250)

    ChrTalk(
        0xC,
        (
            "#00302F#11POh, I beg you.\x02\x03",
            "#00306FI wanted to kill him by myself if possible\x01",
            "To the contrary the partner is too bad.\x02\x03",
            "#00300FWhy do not you make it bad?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_709B")

    ChrTalk(
        0x101,
        (
            "#00004F#6POh, of course.\x02\x03",
            "#00002FI guess that it is exhausted as a buddy … …\x01",
            "It is nice to count on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FD")

    label("loc_709B")


    ChrTalk(
        0x101,
        (
            "#00004F#6POh, of course.\x02\x03",
            "#00002FIt is said that it is exhausted as a companion …\x01",
            "It is nice to count on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70FD")


    ChrTalk(
        0xC,
        (
            "#00315F#11PKuku … That's why it's strange\x01",
            "I do not mean to say that.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        "#00005F#6PWhat……?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Fade(1000)
    SetChrPos(0x101, -600, 0, -3750, 90)
    SetChrPos(0xC, 600, 0, -3750, 270)
    OP_68(0, 1000, -3750, 0)
    MoveCamera(135, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    MoveCamera(140, 15, 0, 70000)
    SetCameraDistance(9000, 70000)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x1)
    OP_0D()
    Sound(802, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x4, 0x1, 0x2, 0x2, 0x2)
    Sound(854, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x4, 0x2, 0x3, 0x3, 0x3)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0xC, 0x4)
    OP_0D()
    Sleep(300)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#00005FIs that … … sake?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xC,
        (
            "#00304F#5PIt's rum, it's a pretty good one.\x02\x03",
            "#00300FTogether with him, at the bar in the village\x01",
            "It was a bottle keeping.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00000F#12P……Really………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(812, 0, 100, 0)
    Sound(857, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x5, 0x4, 0x5, 0x6, 0x6, 0x6)

    ChrTalk(
        0xC,
        (
            "#00300F#5PI kept with my rifle\x01",
            "Somehow I can not hold a hand.\x02\x03",
            "#00304FBut now it's finally\x01",
            "I feel like I'm gonna drink the rest.\x02\x03",
            "#00302FIt is a boost on the night before the decisive battle.\x01",
            "Are not you going out for a cup only?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#00002F#12POh, you get it.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_741E():
        OP_A0(0xFE, 1000, 0x7, 0x8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_741E)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_7434():
        OP_A0(0xFE, 1000, 0x1, 0x2)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7434)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)
    Fade(250)
    Sound(855, 0, 100, 0)
    SetChrSubChip(0xC, 0x9)
    OP_0D()
    Sleep(1000)
    Sleep(1000)
    Fade(250)
    Sound(855, 0, 100, 0)
    SetChrSubChip(0xC, 0xA)
    SetChrSubChip(0x101, 0x4)
    OP_0D()
    Sleep(1000)
    Sleep(300)

    def lambda_7479():
        OP_A0(0xFE, 800, 0xA, 0xC)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7479)
    Sleep(100)

    def lambda_7489():
        OP_A0(0xFE, 1000, 0x4, 0x6)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7489)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#00304F#5P… … Just got free?\x02\x03",
            "#00300FDo not push yourself.\x01",
            "A little but why it is quite hard.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xC, 0x8)
    SetChrSubChip(0x101, 0x4)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00004F#12PWell, I'm grown up already.\x01",
            "This is all right.\x02\x03",
            "#00000FLet's make a toast, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00302F#5PAh.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_7581():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7581)

    def lambda_759A():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_759A)
    Fade(250)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0xC, 0xD)
    Sleep(50)
    Sound(856, 0, 100, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0xC, 3)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0xC, 0xE)
    SetChrSubChip(0x101, 0x8)
    OP_0D()
    Sleep(1000)

    def lambda_75E6():
        OP_A0(0xFE, 1000, 0xE, 0x10)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_75E6)
    Sound(2030, 255, 60, 0)
    OP_A0(0x101, 1000, 0x9, 0xB)
    OP_A0(0x101, 1000, 0x9, 0xB)
    OP_A0(0x101, 1000, 0x9, 0xB)
    WaitChrThread(0xC, 3)
    OP_A1(0xC, 0x3E8, 0x8, 0x10, 0x11, 0x12, 0x12, 0x13, 0x14, 0x13, 0x12)
    OP_A0(0x101, 1000, 0x9, 0xB)

    ChrTalk(
        0x101,
        (
            "#00015F#12P#40WKeo Ho …\x02\x01",
            "#00008F#30W… … It's quite busy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00309F#5PHaha, I can not say anything.\x02\x03",
            "#00302FWell that\x01",
            "It is an adult 's taste.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_76BC():
        OP_A0(0xFE, 1000, 0x15, 0x16)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_76BC)

    def lambda_76C9():
        OP_A0(0xFE, 1000, 0xC, 0xD)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_76C9)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00013F#12PKogu … so only yourself\x01",
            "I should not be adult.\x02\x03",
            "#00004F── Hey, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00305F#5PWhy?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(802, 0, 80, 0)
    OP_A0(0x101, 1000, 0xD, 0xE)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00002F#12POnce the case has fallen\x01",
            "Let's go to the back street jazz bar.\x02\x03",
            "So, a new sake\x01",
            "Do you not keep bottles?\x02\x03",
            "#00012FIf possible,\x01",
            "He is a quiet guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1950, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x8, 0x16, 0x17, 0x18, 0x18, 0x19, 0x1A, 0x19, 0x18)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xC,
        "#00302F#2781V#5P#40WHaha … That's right.\x02",
    )

    CloseMessageWindow()
    OP_24(0xADD)
    OP_57(0x0)
    OP_5A()
    OP_A1(0xC, 0x3E8, 0x3, 0x18, 0x19, 0x1A)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        "#00315F#2782V#5P#40WOh ─ ─ If you feed it out!\x02",
    )

    CloseMessageWindow()
    OP_24(0xADE)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(10500, 3000)
    FadeToDark(2000, 0, -1)
    OP_A1(0xC, 0x3E8, 0x3, 0x1A, 0x19, 0x18)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1194)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_7907")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_7907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7919")
    Jump("loc_79D9")

    label("loc_7919")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Randy\x01",
            "I got a burning rage 嘨.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Combi Craft of Lloyd and Randy,\x01",
            "Burning rage has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x3, 0x1B0)
    AddCraft(0x0, 0x1B0)

    label("loc_79D9")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x2A, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 3)
    OP_29(0xB1, 0x1, 0x3)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_56EE end

    def Function_14_79FC(): pass

    label("Function_14_79FC")

    OP_95(0x101, -500, 0, -3750, 1000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_14_79FC end

    def Function_15_7A18(): pass

    label("Function_15_7A18")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    LoadChrToIndex("apl/ch51020.itc", 0x1F)
    LoadChrToIndex("apl/ch51806.itc", 0x20)
    LoadChrToIndex("apl/ch51807.itc", 0x21)
    SoundLoad(3532)
    SoundLoad(3533)
    SoundLoad(3534)
    SoundLoad(3535)
    SoundLoad(4110)
    SoundLoad(3536)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis337.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis338.itp")
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xD, 500, 0, -3750, 180)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(135, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(135, 10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    BeginChrThread(0xF, 1, 0, 8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        (
            "#10106F#3532V#40WHaa ………\x01",
            "…………What should I do………\x02\x03",
            "#10108F#3533VIn such a case …#800W…\x01",
            "#10101F#40WNo, but if I let this escape …!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCD)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0xD, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(19500, 2000)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_7CAA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7CAA)

    def lambda_7CBF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7CBF)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        "#00002F#5PNoel, have you come before.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xD, 0x0, 1850, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7D30():

        label("loc_7D30")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_7D30")

    QueueWorkItem2(0xD, 2, lambda_7D30)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        (
            "#10112F#3534V#12P#40WB, Mr. Lloyd!\x01",
            "Congratulations!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCE)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(35, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_7DC0():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DC0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xD, 500)
    EndChrThread(0xD, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha, I am tired from there.\x02\x03",
            "#00000FAlso contact with Sonya command\x01",
            "You seem to have done it?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xD,
        (
            "#30WOh, yes.\x02\x03",
            "As you are in contact, tomorrow's strategy\x01",
            "Belgard gate · Tangram main unit\x01",
            "It seems to let me wait until early afternoon.\x02\x03",
            "As expected after passing it\x01",
            "It seems that we have to intervene, but …\x02",
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

    ChrTalk(
        0x101,
        (
            "#00006F#6PThat's right … Well temporarily\x01",
            "Just waiting will be helpful.\x02\x03",
            "#00013FThen, our role is\x01",
            "It seems to be increasingly important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10103F#11PYes……\x02\x03",
            "#10108F#30W…………………………………….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P… … Maybe the city's Defense Forces\x01",
            "It should be used for urban defense.\x02\x03",
            "#00001FIn the city area to interact with the Defense Army\x01",
            "I think I can avoid somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10106F#11PNo, about that\x01",
            "I am already prepared for it.\x02\x03",
            "#10108FJust for a moment\x01",
            "I thought that it was miserable ……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PWhat……?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -500, 0, -3750, 90)
    SetChrPos(0xD, 500, 0, -3750, 270)
    OP_68(250, 1000, -4400, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 1000, -3750, 50000)
    MoveCamera(135, 20, 0, 50000)
    OP_6E(800, 50000)
    SetCameraDistance(10000, 50000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10108F#5P#30WIn fact, independent countries and defense forces are\x01",
            "I thought it was wrong.\x02\x03",
            "#10106FBut I … like Mireille senpai\x01",
            "There is no spirit of investing in resistance,\x01",
            "Just follow a big flow … …\x02\x03",
            "How I am a guard\x01",
            "I wonder if I only lived in a narrow world\x01",
            "I was made aware.\x02\x03",
            "#10113FI will give you the opportunity to visit the support department\x01",
            "Even though the commander gave it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PThat … … everyone is the same.\x02\x03",
            "#00008FEven if I do not have Ka'a and everyone's things\x01",
            "I think that I could not resist the big flow.\x02\x03",
            "#00012FOriginally, it was great\x01",
            "It is not a personality that I can do.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#10112F#5PEr …\x01",
            "I do not think so.\x02\x03",
            "#10114FIf it was not so\x01",
            "\"You gotta get me\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10112F#5PNo!\x01",
            "It's nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PIs it? Is it? Is it?\x02\x03",
            "#00004FIn any case, what is important\x01",
            "I think whether there is a chance.\x02\x03",
            "And you grabbed that chance\x01",
            "They are with us.\x02\x03",
            "#00008FWhether it is correct or not\x01",
            "I will not let you decide … …\x02\x03",
            "#00002FIt is very helpful,\x01",
            "── I'm more than anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#10114F#5PRo, Mr. Lloyd ……\x02\x03",
            "#10106F~~~ っ ~~~ ……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x258)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10108F#11P#30W(Calm down,\x01",
            "Noel · seeker …! )\x02\x03",
            "#10103F(As in exercises)\x01",
            "Rapid and accurate situation judgment\x01",
            "Morale control ……! )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#12PBy the way, something to me\x01",
            "I was told you to be asked … …\x02\x03",
            "#00002FEr, what is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 500)

    ChrTalk(
        0xD,
        (
            "#10105F#5POh, yes!\x01",
            "That's it, but ─ ─\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0xD,
        (
            "#10106F#5P… … that … … well … …\x02\x03",
            "#10108FI hear strange things\x01",
            "Lloyd's ……\x02\x03",
            "#10101FOkay, the people we are referring to\x01",
            "Do you have time?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#12Peh……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10112F#5PNo!\x01",
            "It's not a deep meaning!\x02\x03",
            "#10102FThat's right, Fran and\x01",
            "Please talk about what it is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#12POh, oh, I see.\x02\x03",
            "#00012FHa ha, that story,\x01",
            "The girl seems to like it.\x02\x03",
            "#00006FWell, unfortunately there is no now.\x02\x03",
            "#00000FEven though there are lots of good children around\x01",
            "Though it is a little disgusting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10112F#5P#30WOh, haha … that kind of thing.\x01",
            "(It is not a bad idea … is it?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(1200)

    ChrTalk(
        0xD,
        "#10103F#5P#30WKohon ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xD, 500, 0, -4250, 270)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16500, 2000)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)
    OP_68(0, 1000, -4250, 70000)
    MoveCamera(35, 20, 0, 70000)
    OP_6E(500, 70000)
    SetCameraDistance(14500, 70000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        "#10103F#3535V#11P#40W── That's it.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xD, 0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#10101F#4110V#11P#40WFor a while,\x01",
            "Could you please take care?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x100E)
    OP_C9(0x1, 0x80000000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00005Fis this……\x02\x03",
            "#00001FCrossbell Guard's recognition tag?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xD,
        (
            "#10104F#11PYes, when I switched to Defense Forces\x01",
            "It is not needed anymore ….\x02\x03",
            "#10100FSomehow it is not thrown away\x01",
            "I used to have it all the time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#6PI see……\x02\x03",
            "#00005FBut why to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10106F#11P…… To be honest, tomorrow's strategy\x01",
            "I think that it will be tough.\x02\x03",
            "#10101FIf something happened to me ……\x02\x03",
            "#10112FNo - In order to safely carry out the mission,\x01",
            "Trial#2RKen#I want you to have it on the carrying side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PNoel …\x02\x03",
            "#00004F……I understood.\x01",
            "I will be happy to deposit you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    OP_0D()
    Sleep(800)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10109F#11PHo\x01",
            "Thank you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHello, thank you separately\x01",
            "It is not like being told.\x02\x03",
            "#00008FAnd Noel also with us\x01",
            "We will act together ……\x02\x03",
            "#00000FEven when you pinch\x01",
            "I do not think that one person will be sacrificed\x01",
            "Do not you think?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10111F#11P#30WHow, why …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI know that much.\x02\x03",
            "#00001FAs I said earlier,\x01",
            "About what I caught us\x01",
            "There is no need to be sick at all.\x02\x03",
            "#00002FAs a companion of the support department to the last\x01",
            "I want you to come with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10114F#11P#30WMr. Lloyd … ….\x02\x03",
            "#10116FGrueling\x01",
            "……Yes, I understand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6Pmy mother……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#6PBut my tag\x01",
            "Can you deposit it with someone ……\x02\x03",
            "#00012FHaha, something\x01",
            "It seems like a boyfriend's habit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10114F#11PHuh!\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x258)
    Sleep(300)

    def lambda_9142():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_9142)
    WaitChrThread(0xD, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#6PHuh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10106F#5P#40W…… ~~~ っ ~~~~ ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PNoel …\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    Fade(250)
    Sound(812, 0, 60, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    OP_A1(0x101, 0x320, 0x7, 0x0, 0x1, 0x2, 0x1, 0x2, 0x1, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00011F#6PEr, that … …\x02\x03",
            "#00012FEven if not,\x01",
            "Is that what it means?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10106F#5P#40W…………………… (Kokun)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WIs that so … ….\x02\x03",
            "#00000F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6PWhether or not to answer that\x01",
            "I do not know but …\x02\x03",
            "#00000FWill you keep this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10114F#5P#30WHuh……\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x10E, 0x1F4)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x3)
    OP_0D()
    Sleep(150)
    Sleep(300)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)

    AnonymousTalk(
        0xD,
        (
            "#10105F#11Pthat's……\x01",
            "… …. Crossbell Police … ….?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00002F#6POnce it's an incumbent police officer\x01",
            "It should be worn by myself ….\x02\x03",
            "#00004FUntil this incident is resolved\x01",
            "I would like Noel to have it.\x02\x03",
            "#00000FThen again ……\x01",
            "I want you to apply from me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)

    ChrTalk(
        0xD,
        "#10116F#11P#30W#2S……………Ah…………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        "#10117F#3536V#11P#30WYes, I'm pleased!\x02",
    )

    CloseMessageWindow()
    OP_24(0xDD0)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(16000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_95B7")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_95B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95C9")
    Jump("loc_9685")

    label("loc_95C9")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Noel\x01",
            "I mastered the Brave Hearts.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Noel Combi Craft,\x01",
            "\"Brave Hearts\" has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x0, 0x1A0)
    AddCraft(0x8, 0x1A0)

    label("loc_9685")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x25, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 4)
    OP_29(0xB1, 0x1, 0x4)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_7A18 end

    def Function_16_96A8(): pass

    label("Function_16_96A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03100.itc", 0x1E)
    LoadChrToIndex("apl/ch51808.itc", 0x1F)
    LoadChrToIndex("apl/ch51813.itc", 0x20)
    SoundLoad(2926)
    SoundLoad(2927)
    SoundLoad(2928)
    SoundLoad(2929)
    SoundLoad(2930)
    SoundLoad(2430)
    SoundLoad(2431)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10401.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis325.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis349.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis326.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis327.itp")
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xE, 500, 0, -4250, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(18500, 2000)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_9875():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9875)

    def lambda_988A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_988A)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        "#10402F#2926V#11P#30WHello, I came.\x02",
    )

    CloseMessageWindow()
    OP_24(0xB6E)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        "#00000F#5PAh……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xF, 1, 0, 8)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(45, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_992A():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_992A)

    def lambda_9944():

        label("loc_9944")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9944")

    QueueWorkItem2(0xE, 2, lambda_9944)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xE, 500)
    EndChrThread(0xE, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6PIf you were told to think like that\x01",
            "I think that I have no choice but to come.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xE,
        (
            "#2927V#30WHuff, although saying that way\x01",
            "I like you who will come to you.\x02\x03",
            "#2928VEven though I love you\x01",
            "It is not an exaggeration.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB70)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PThat's because it's good.\x02\x03",
            "#00001F… How about Kea?\x01",
            "Let me tell you a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#11PHuh, I understand.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    SetChrPos(0x101, -920, 0, -3910, 90)
    SetChrPos(0xE, 500, 0, -3750, 270)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9500, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    OP_6F(0x79)
    SetCameraDistance(9000, 50000)

    ChrTalk(
        0xE,
        (
            "#10408F#5PTo truly outsiders\x01",
            "I can not tell it ….\x02\x03",
            "#10400FRegarding treatment of \"treasure of zero\"\x01",
            "Apparently the church basically\x01",
            "It seems to be in the form of no touch.\x02\x03",
            "#10403F─ ─ Even if this case\x01",
            "Even if it ended in the end.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#11PReally! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10406F#5POh, the people of the \"snake\" withdrew,\x01",
            "Now that the original treasure is lost,\x01",
            "There is no basis to actively intervene.\x02\x03",
            "#10400FIn that sense, we need Kia\x01",
            "There is no choice to take away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PReally……\x01",
            "thanks for letting me know.\x02\x03",
            "#00005FBut, Wadi leaves this way\x01",
            "Is there no problem by cooperating with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10403F#5P\"Clown\" and the seventh pillar has left,\x01",
            "The withdrawal of the sixth pillar has not been confirmed.\x02\x03",
            "#10408FBesides that dolls,\x01",
            "The technology the association has offered to the Clois family\x01",
            "It still has a big influence ……\x02\x03",
            "#10400FUntil that influence disappears\x01",
            "I intend to continue minimal intervention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see……\x02\x03",
            "#00001F… … the more I hear it\x01",
            "A battle out of our common sense\x01",
            "You seem to be spreading?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10404F#5PHuh, what is the world you live in?\x01",
            "The story of the world that is the relationship between the front and back.\x02\x03",
            "#10402FAnd it's for me\x01",
            "Two years of crossbell infiltration mission\x01",
            "I think the closing is big.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#11Pby the way……\x01",
            "Wasi was 17 years old.\x02\x03",
            "#00003FTwo years ago,\x01",
            "By the age of 15 I got a mission … …\x02\x03",
            "#00001FBut, \"guardian knight\"\x01",
            "You are in a pretty important position, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10405F#5POh, what \"guardian knights\" is\x01",
            "It is not a proven track record.\x02\x03",
            "#10400FOnly a person whose \"sign\" is manifested can only be done,\x01",
            "It is doomed to be … …\x02\x03",
            "#10409FWell, at such occultic\x01",
            "It is a disgusting position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PDo not say it yourself …\x02\x03",
            "#00001F…… But \"Mark\"\x01",
            "Perhaps Wadi is in battle\x01",
            "Sometimes I show it … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#5PAh……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x190)
    Fade(500)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xE, 500, 0, -4250, 180)
    OP_68(430, 1000, -4460, 0)
    OP_68(430, 1000, -4460, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(40, 20, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(15000, 30000)
    OP_0D()
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#10403F#5P#30W\"Stigmata#4RStigma#\"──\x01",
            "That is the name of this \"seal\".\x02\x03",
            "#10408FEngraved on the soul … …\x01",
            "Something to detest as a source of power.\x02\x03",
            "#10400FThis was what manifested me\x01",
            "That was about seven years ago from now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P7 years ago ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10404F#5PApart from the D∴G organization\x01",
            "It's a story I have nothing to do with ……\x02\x03",
            "#10402FListen to killing time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PThat's right.\x01",
            "If you do not mind, be sure.\x02\x03",
            "#00000FIf you think about it, the past of Wadi\x01",
            "It is almost as good as I do not know …\x02\x03",
            "#00012FCharacter and behavioral pattern\x01",
            "I'm going to know roughly, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#5PHehe … … it would be nice.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    SetCameraDistance(15000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C── My birthplace was\x01",
            "It is a certain frontier of the continent of Zemria.\x02\x03",
            "Contact with the outside world was forbidden\x01",
            "It was, so to speak, a \"hidden\" place.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7568", 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, 155, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3CIn that village it is different from the goddess\x01",
            "Dedicate the ancient \"god\" … …\x02\x03",
            "I listen to the voice of \"God\" from an early age\x01",
            "She has taken on the role of \"shrine\".\x02\x03",
            "Of course, not spontaneously,\x01",
            "It was chosen without permission when I was at ease.\x02\x03",
            "The identity of \"God\" is incomprehensible\x01",
            "I knew that it was an ancient spell\x01",
            "To be honest, I was stupid and I could not help it.\x02\x03",
            "Liberated from the inevitable role\x01",
            "I always thought that I wanted to be free.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C…… At the village in the middle\x01",
            "Funny things started to happen.\x02\x03",
            "One villain and one person\x01",
            "I got into an unknown coma.\x02\x03",
            "As I explored,\x01",
            "\"God\" runaway, through the ground\x01",
            "I know that I started smoking … …\x02\x03",
            "I insisted on shutting down,\x01",
            "Eli's elders did not admit it,\x01",
            "I told you to offer a sacrifice.\x02\x03",
            "Well, in fact, with an enchantment with a terrible power\x01",
            "It was impossible to shut it down ….\x02\x03",
            "─ ─ From such time outside\x01",
            "The church knights came.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    SetMessageWindowPos(180, 160, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C── I contacted them\x01",
            "\"God\" is an ancient artifact#8RArtifact#Know that it is a kind of … …\x02\x03",
            "Knowing that it is not an absolute existence\x01",
            "I took a drastic action.\x02\x03",
            "The bluish lithogram \"God\"\x01",
            "I dropped it from the cliff and tried to destroy it.\x02\x03",
            "Liberate the village from the ancient curse,\x01",
            "I want to be free - just that one.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)
    SetMessageWindowPos(10, 150, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3CBut the resistance of \"God\" is terrible,\x01",
            "I tried to steal my powers up.\x02\x03",
            "The knights' help was not in time,\x01",
            "That time my life tried to run out ─\x02\x03",
            "That \"stamp\" appeared in my chest.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    FadeToDark(2500, 16777215, -1)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_0D()
    OP_68(-360, 2100, -3950, 0)
    MoveCamera(150, -49, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5667730, 0)
    Sleep(1500)
    FadeToBright(1500, 16777215)
    OP_0D()
    Sleep(800)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C── My stigmata is\x01",
            "Conversely robbing the power of \"God\" ……\x02\x03",
            "\"God\" turns into just old old slate,\x01",
            "It crumbled down and shattered.\x02\x03",
            "And I got the freedom ──\x01",
            "That was why Meitaku-ri was expelled.\x02\x03",
            "\"God\" that the villagers worshiped\x01",
            "\"Killed\" as a great sinister.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x1)
    OP_68(430, 1000, -4460, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(16000, 3000)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(150)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    OP_6F(0x79)
    MoveCamera(40, 20, 0, 50000)
    SetCameraDistance(16540, 50000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00008F#6P#30W……… such thing …………\x02\x03",
            "#00006F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10409F#5P#30WGiggle\x01",
            "It is quite absurd a story, is not it?\x02\x03",
            "#10400FTo the modern child-raised child\x01",
            "You can not believe it as expected?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PNo, when you are looking at the power of Wadi\x01",
            "It is understood that it was in reality.\x02\x03",
            "#00000FThere is also a living myth called Zeit\x01",
            "I have seen it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10402F#5PHaha, is that so?\x02\x03",
            "#10404FThat's why I was invited by the knights\x01",
            "Going to Alteria law country ……\x02\x03",
            "Owner of \"Stigmata\" with only 12 people,\x01",
            "\"Guardian Knight#8RDominion#\"It was greeted as.\x02\x03",
            "#10400FWhat is Abbas?\x01",
            "I wonder what I was going out with from that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PReally……\x02\x03",
            "#00006F…… But then,\x01",
            "Have you not been home anymore?\x02\x03",
            "#00001FDo not meet with family members …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10405F#5P#30WOh ─ ─ Naturally?\x02\x03",
            "#10403FThe foster base\x01",
            "I crushed into pieces.\x02\x03",
            "Just want to be free …\x01",
            "With not thinking about anything afterwards.\x02\x03",
            "#10400FThat's why it's punishment for me.\x02\x03",
            "#10404FEven things like being hated by family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10406F#5P#30WWell, as I heard it\x01",
            "A church enters from there to the village\x01",
            "He seems to care a lot.\x02\x03",
            "#10404FThe curse of \"God\"\x01",
            "It should weaken as past things.\x02\x03",
            "To the extent that the bloom got cold\x01",
            "I think that I will go home once.\x02\x03",
            "#10402FEven if you do not worry so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#30WWadi\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00008F#6PIf this incident is settled ……\x01",
            "Waddy leaves the crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10400F#5POh, that's my\x01",
            "It's a mission as a knight.\x02\x03",
            "#10409FHuh, what is it?\x01",
            "Will you get lonely now?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        "#00001F#6POh, such a natural reason?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x101, 400)
    Sleep(150)

    ChrTalk(
        0xE,
        "#10405F#11PWhat……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    Fade(1000)
    SetChrPos(0x101, -920, 0, -3910, 90)
    SetChrPos(0xE, 500, 0, -3750, 270)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    Sleep(500)
    OP_6F(0x79)
    SetCameraDistance(9000, 30000)

    ChrTalk(
        0x101,
        (
            "#00003F#11P#30WWald did it like that\x01",
            "I'm sure you can restore it.\x02\x03",
            "Everyone on the tests\x01",
            "It's in the crossbell.\x02\x03",
            "#00008FAnd though there was speculation,\x01",
            "He was a friend of us ……\x02\x03",
            "#00000FSo ──\x01",
            "You should come and see me anytime.\x02\x03",
            "#00009FCrossbell is already\x01",
            "Is it like a second hometown?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrSubChip(0xE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    Sleep(150)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrSubChip(0xE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    Sleep(300)

    ChrTalk(
        0xE,
        "#10405F#5P#30W…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x2)
    OP_0D()

    def lambda_B5D4():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B5D4)
    WaitChrThread(0xE, 2)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        "#10404F#2430V#5P#40W#12A… … Rugged ………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetChrSubChip(0xE, 0x3)

    def lambda_B632():
        OP_A6(0xFE, 0x0, 0x1E, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B632)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xE,
        "#10409F#2431V#50W#5P#4S#15AAhahahahaha Ha ha ha!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30WI am aware of it.\x02\x03",
            "#00000FBut, are you 100 serious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10411F#5P#40W… … Huh, I understand.\x01",
            "I'm going crazy if you are an opponent.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    OP_A0(0xE, 1000, 0x7, 0x5)
    OP_0D()
    Sleep(400)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#10402F#2929V#5P#40W── When mental attitude was attached\x01",
            "I do not hesitate to visit you.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB71)
    Sleep(150)
    OP_A0(0xE, 1000, 0x5, 0x7)
    Sleep(400)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#10404F#2930V#5P#40WInstead of returning to my hometown,\x01",
            "Please check the rotten relationship with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB72)
    OP_C9(0x1, 0x80000000)
    BlurSwitch(0x1770, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-360, 2100, -3950, 8000)
    MoveCamera(128, 27, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(40590, 8000)
    Sleep(500)
    OP_A0(0xE, 1000, 0x7, 0x5)
    Sleep(2500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_B8A8")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_B8A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8BE")
    Jump("loc_B97A")

    label("loc_B8BE")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Wadi\x01",
            "I mastered the strike heaven.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Wazi's combi craft,\x01",
            "\"Strike heaven\" has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x0, 0x1A1)
    AddCraft(0x4, 0x1A1)

    label("loc_B97A")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x26, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 5)
    OP_29(0xB1, 0x1, 0x5)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_96A8 end

    def Function_17_B99D(): pass

    label("Function_17_B99D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x40)
    LoadChrToIndex("chr/ch03200.itc", 0x1E)
    LoadChrToIndex("apl/ch51809.itc", 0x1F)
    LoadChrToIndex("apl/ch51810.itc", 0x20)
    SoundLoad(3265)
    SoundLoad(3266)
    SoundLoad(3267)
    SoundLoad(3268)
    SoundLoad(3269)
    SoundLoad(3270)
    SoundLoad(2634)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10701.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis321.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis322.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis323.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis324.itp")
    EndChrThread(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, -250, 120, 2750, 180)
    SetChrPos(0x8, 500, 0, -3750, 180)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(125, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8000, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(115, 15, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    Sound(100, 0, 100, 0)
    Sleep(800)

    ChrTalk(
        0x101,
        "#00002F#6P#30W#N…… It is a really full moon.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()

    def lambda_BBD5():

        label("loc_BBD5")

        TurnDirection(0xFE, 0x101, 400)
        Yield()
        Jump("loc_BBD5")

    QueueWorkItem2(0x8, 2, lambda_BBD5)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        "#3265V#11P#40WMr. Lloyd ……\x02",
    )

    CloseMessageWindow()
    OP_24(0xCC1)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    BeginChrThread(0xF, 1, 0, 8)
    OP_68(0, 1000, -4200, 4500)
    MoveCamera(130, 20, 0, 4500)
    OP_6E(800, 4500)
    SetCameraDistance(10000, 4500)
    Sound(100, 0, 100, 0)

    def lambda_BCC9():
        OP_95(0xFE, -500, 0, -3750, 1600, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCC9)
    WaitChrThread(0x101, 1)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    SetCameraDistance(9500, 30000)
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WSomehow, when you talk with you\x01",
            "I always feel the moon is beautiful.\x02\x03",
            "#00002FAfter all \"the princess of the month\"\x01",
            "Is there just there to play?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        "#10709F#2634V#5P#30WHehu ……\x02",
    )

    CloseMessageWindow()
    OP_24(0xA4A)
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0xB4, 0x190)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#10704F#3266V#40W#5PThe moon is a light and a shadow … …\x02\x03",
            "#3267VPerhaps it is, the existence of me\x01",
            "I think that it is similar to the moon.\x02\x03",
            "#10708F#3268VOriginally in a sunny place\x01",
            "It was not there to exist ……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCC4)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30WBut you, with this crossbell\x01",
            "I was able to grasp the light …\x02\x03",
            "#00001FIs that certain?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    OP_A1(0x8, 0x3E8, 0x5, 0x2, 0x25, 0x26, 0x25, 0x2)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30WYes, I've already done that\x01",
            "I will not deny it.\x02\x03",
            "#10708FBut I …\x01",
            "…… The flow that made the existence of me\x01",
            "There is something deeply unfamiliar.\x02\x03",
            "#10711F\"Silver#2RIn#\"The flow of a one-sided communication called … …\x02\x03",
            "#10703FThe secret road that inherited from my father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P#30WI was saying such a thing before ….\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30W……If it's not a problem\x01",
            "Can you tell me?\x02\x03",
            "#00008FYou until you came to the crossbell.\x02\x03",
            "#00001FI do not know, Lisha Mao.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30W……Yes.\x02\x03",
            "#10710FSomehow, to Mr. Lloyd\x01",
            "I will tell you anything\x01",
            "I was distracted.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    OP_93(0x8, 0xB4, 0x12C)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)
    OP_63(0x8, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#10708F#5P#30W─ ─ When I noticed\x01",
            "I stayed with my father.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(9000, 2500)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C── There is no memory of my mother.\x02\x03",
            "Probably, the way of \"silver\"\x01",
            "To inherit to me\x01",
            "I think that my father was away.\x02\x03",
            "But for me it is normal …\x02\x03",
            "Harsh exercise, training of dark bodies and techniques\x01",
            "It was only performing thoroughly.\x02\x03",
            "While attending various places, I went to Sunday school,\x01",
            "There was also a technique to get in touch with people.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(260, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CMy father was neither harsh nor gentle,\x01",
            "I just taught you.\x02\x03",
            "That's because as \"silver\"\x01",
            "It is because it was too enormous to inherit it.\x02\x03",
            "It's a memory of generations \"silver\" ……\x02\x03",
            "Under what circumstances doing what kind of work,\x01",
            "What targets and how did they detain ……\x02\x03",
            "Because it is the same existence throughout the times,\x01",
            "All that summary\x01",
            "I had to inherit it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CWhen we inherit everything ……\x01",
            "I became \"silver\" itself.\x02\x03",
            "Even so, as long as my father is alive\x01",
            "It will not be \"silver\".\x02\x03",
            "\"Silver\" is just one person …\x01",
            "That is because it will not change.\x02\x03",
            "For a while, waiting for my father's return\x01",
            "The days of gentle spending continued.\x02\x03",
            "And when my father comes home\x01",
            "When to succeed the \"silver\" so that there is no problem\x01",
            "I will tell you the overview of work …\x02\x03",
            "I already had a table face\x01",
            "That was all for the world to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(800)
    SetMessageWindowPos(20, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C── That world collapsed\x01",
            "It is because my father had fallen ill by an incurable disease.\x02\x03",
            "Among the generations of \"silver\"\x01",
            "It was my father with outstanding power … …\x01",
            "I could not get away from the disease.\x02\x03",
            "Without hurting again,\x01",
            "I did not undergo surgery for survival … …\x02\x03",
            "One day, I called and ordered.\x02\x03",
            "To kill yourself and to succeed \"silver\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C─ ─ It was not possible to do.\x02\x03",
            "Approximately, to my father\x01",
            "It was me who never got against it\x01",
            "It was impossible just for that.\x02\x03",
            "…… I became scared for the first time.\x02\x03",
            "Father's carefully finished that much \"that silver#2RI#\"But\x01",
            "I wonder if it was impossible.\x02\x03",
            "He may have disappointed his dying father.\x02\x03",
            "… … conspiracy#4RMorning#To me\x01",
            "My father laughed a bitter smile.\x02\x03",
            "\"─ ─ It is also you.\"\x02\x03",
            "\"You should decide on your silver.\"\x02\x03",
            "… and a month later my father left the world.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(800)
    SetMessageWindowPos(260, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CAnd I became \"silver\".\x02\x03",
            "I took over the connection my father had,\x01",
            "Masquerading the body shape with Kuroko and Inougoku … …\x02\x03",
            "I did not go to my father's arm\x01",
            "I was able to resume my work without delay.\x02\x03",
            "\"You should decide on your silver.\"\x02\x03",
            "I do not know the meaning of my father's words,\x01",
            "Just make it seductively … ….\x02\x03",
            "── Then two years passed,\x01",
            "I signed a long-term contract with Black Mun.\x02\x03",
            "West Western Calvert ……\x01",
            "To take over the hegemony of the cross-border trade city\x01",
            "A contract to cooperate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(1000)
    SetMessageWindowPos(250, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CI arrived at Crossbell\x01",
            "In preparation for the battle, while undergoing preview of the city,\x01",
            "I entered a certain theater in the entertainment district.\x02\x03",
            "There, exactly what is called public practice\x01",
            "Have been done ……\x02\x03",
            "… … From then on\x01",
            "Mr. Lloyd is also familiar.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    FadeToBright(2000, 0)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    OP_6F(0x79)
    SetCameraDistance(9000, 40000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30W……I see……\x02\x03",
            "#00000FAt that time, Mr. Ilya\x01",
            "You mean you got an eye?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10702F#5P#30WHuhuu, for the first reason, give a reason\x01",
            "I managed to refuse to join.\x02\x03",
            "#10704FBut Irria is terribly aggressive … …\x02\x03",
            "Finally, I will lose my roots\x01",
            "I was supposed to enter.\x02\x03",
            "I was confident in physical strength and impersonation,\x01",
            "I thought it would be a nice hiding place.\x02\x03",
            "#10710F…… Exercise harder than I expected\x01",
            "Although it was hard to balance with \"silver\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11P#30Wmy mother……\x02\x03",
            "#00004FThank you, Lisa.\x02\x03",
            "#00000FI was glad to hear it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30WHuhu, in an interesting story that I heard\x01",
            "I think that was nothing ……\x02\x03",
            "#10703FBut this is from ─ ─ father and ancestor\x01",
            "It is \"road\" inherited to me.\x02\x03",
            "#10708FThe light called alkane shell\x01",
            "Even if you get it ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    OP_A0(0x8, 1000, 0x2, 0x5)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30WTo throw away that \"road\" completely\x01",
            "Perhaps I can not do it.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    ChrTalk(
        0x101,
        (
            "#00003F#11P#30WReally……\x02\x03",
            "#00008F…………………………………….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    Fade(1000)
    SetChrSubChip(0x8, 0x6)
    SetChrPos(0x101, -1000, 0, -4250, 90)
    SetChrPos(0x8, 0, 0, -4250, 270)
    OP_68(-300, 1000, -4250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(-300, 1000, -4250, 50000)
    MoveCamera(45, 15, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(15500, 50000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7575", 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00003F#6P#30W\"You should decide on your silver.\"\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x3E8, 0x5, 0x6, 0x29, 0x2A, 0x29, 0x6)

    ChrTalk(
        0x8,
        "#10712F#11P#30W…………Huh……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W… \"Silver\" inherits everything.\x02\x03",
            "The light called alkane shell\x01",
            "More than you found out … …\x02\x03",
            "#00002F\"Silver\" also has the aspect of light\x01",
            "You do not have to accept it, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10717F#11P#30WWell, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30WIf the times change for anything\x01",
            "The way it changes … …\x02\x03",
            "#00003FNo, I have no choice but to change.\x02\x03",
            "#00008FAnd the history of people is inherited,\x01",
            "I will move forward …\x02\x03",
            "#00001FPerhaps, including that kind of thing\x01",
            "Dad might have said that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10708F#11P#30W…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WCriminal act as a policeman\x01",
            "I can not recommend it, but …\x02\x03",
            "Still, you, your \"silver\"\x01",
            "I think that it is good to aim.\x02\x03",
            "#00000FAlternatively, here the existence of \"silver\"\x01",
            "It is one way to completely cut off.\x02\x03",
            "#00002FEven if that happens … maybe ….\x01",
            "My father does not care.\x02\x03",
            "#00009FI smile witty that \"─ ─ it is you too\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10717F#11P#40W#2S………….. Ah ………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W…… It's a nice dad.\x02\x03",
            "#00008FIt is slightly different from the ordinary family\x01",
            "I loved my daughter properly …\x02\x03",
            "#00002FIt seems to me like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10718F#11P#50W………Dad…………\x02",
    )

    CloseMessageWindow()
    OP_68(-100, 1000, -4250, 1200)
    SetChrFlags(0x8, 0x20)

    def lambda_D590():
        OP_A0(0xFE, 1000, 0x6, 0x9)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_D590)
    OP_96(0x8, 0x96, 0x0, 0xFFFFEF66, 0x1F4, 0x0)
    Sound(812, 0, 60, 0)
    ClearChrFlags(0x8, 0x20)
    OP_A0(0x8, 1000, 0x18, 0x1A)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A1(0x8, 0x3E8, 0x6, 0x1A, 0x1E, 0x1F, 0x20, 0x21, 0x22)
    OP_A0(0x8, 1000, 0x18, 0x1A)
    OP_63(0x8, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(812, 0, 60, 0)
    OP_A0(0x8, 1000, 0xA, 0xC)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10719F#11P#50Wwhy……\x02\x03",
            "…… Even when my father died ……\x01",
            "This\x02\x03",
            "#10720F… … … tears ……\x01",
            "Even though it did not come out at all …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WPerhaps, with the days with Iria\x01",
            "You also changed again … …\x02\x03",
            "#00008FFrom now on, what kind of road will you go?\x01",
            "I do not know but ….\x02\x03",
            "#00000FIf possible I, too, instead of your father\x01",
            "I'll be watching.\x02\x03",
            "#00002FYou grabbed the light,\x01",
            "Let's see how it changes.\x02",
        )
    )

    CloseMessageWindow()
    OP_A0(0x8, 1000, 0xC, 0xF)
    Sleep(300)

    ChrTalk(
        0x8,
        "#10718F#11P#50WMr. Lloyd … ….\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(1000)
    OP_68(100, 1000, -4250, 1200)
    SetCameraDistance(15000, 1200)
    OP_9A(0x101, 0x8, 0x1F4, 0x258, 0x0)
    Sleep(300)
    Fade(250)
    Sound(898, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_D81E():
        OP_A0(0xFE, 1000, 0x14, 0x16)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_D81E)

    def lambda_D82B():
        OP_A0(0xFE, 1000, 0x5, 0x7)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D82B)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x101, 3)
    OP_0D()
    MoveCamera(44, 23, 0, 15000)
    SetCameraDistance(70000, 15000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        "#10720F#11P#3269V#70W#20A… …. Wow … ahh ………\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#10713F#11P#3270V#90W#30A#4S………… Ah ah …………!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1770)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_D927")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_D927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D939")
    Jump("loc_D9F3")

    label("loc_D939")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Lisha\x01",
            "I gained true · special wing Ssangyong shoots.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Combi Craft of Lloyd and Lisha,\x01",
            "\"Special wing Ssangyong shoot\" has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1A9)

    label("loc_D9F3")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x27, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 6)
    OP_29(0xB1, 0x1, 0x6)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_B99D end

    def Function_18_DA16(): pass

    label("Function_18_DA16")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA30")
    OP_A0(0xFE, 1000, 0x10, 0x12)
    Sleep(300)
    Jump("Function_18_DA16")

    label("loc_DA30")

    Return()

    # Function_18_DA16 end

    SaveToFile()

Try(main)
