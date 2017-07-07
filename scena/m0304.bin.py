from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0304.bin",                # FileName
        "m0304",                    # MapName
        "m0304",                    # Location
        0x0000,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0304",                  # 0
        "Raines",               # 1
        "SE control",                 # 2
    ))

    AddCharChip((
        "chr/ch28100.itc",                   # 00
    ))

    DeclNpc(0,       0,       1629,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(232, 0)                                        # 0

    ScpFunction((
        "Function_0_E8",           # 00, 0
        "Function_1_198",          # 01, 1
        "Function_2_1A8",          # 02, 2
        "Function_3_1A9",          # 03, 3
        "Function_4_241",          # 04, 4
        "Function_5_1EE0",         # 05, 5
    ))


    def Function_0_E8(): pass

    label("Function_0_E8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_120"),
        (1, "loc_12C"),
        (2, "loc_138"),
        (3, "loc_144"),
        (4, "loc_150"),
        (5, "loc_15C"),
        (6, "loc_168"),
        (SWITCH_DEFAULT, "loc_174"),
    )


    label("loc_120")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_12C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_138")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_144")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_150")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_15C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_168")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_174")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_180")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_197")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_197")

    Return()

    # Function_0_E8 end

    def Function_1_198(): pass

    label("Function_1_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1A7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)

    label("loc_1A7")

    Return()

    # Function_1_198 end

    def Function_2_1A8(): pass

    label("Function_2_1A8")

    Return()

    # Function_2_1A8 end

    def Function_3_1A9(): pass

    label("Function_3_1A9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Also, anyway, with you\x01",
            "As a human in R & A research\x01",
            "I think that there is also opportunity to meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, first anyway,\x01",
            "I pray for a successful inrush operation.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_1A9 end

    def Function_4_241(): pass

    label("Function_4_241")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BeginChrThread(0x9, 1, 0, 5)
    OP_68(1090, 0, -8490, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, 0, 0, -10650, 0)
    SetChrPos(0x102, 1100, 0, -10650, 0)
    SetChrPos(0x103, -1100, 0, -10650, 0)
    SetChrPos(0x104, 0, 0, -10650, 0)
    SetChrPos(0xF4, -1100, 0, -10650, 0)
    SetChrPos(0xF5, 1100, 0, -10650, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)

    AnonymousTalk(
        0x101,
        (
            "#00001FAfter all, at the Geo Front\x01",
            "I was able to communicate ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00103FApparently, in one corner of D section\x01",
            "There seems to be no mistake … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#00205F…… The signs are getting stronger.\x02\x03",
            "#00203FAlthough the number is one ……\x01",
            "It seems to be certain that someone is there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_462")

    AnonymousTalk(
        0x10A,
        "#00601F(Inside of this door ……)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DB")

    label("loc_462")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A3")

    AnonymousTalk(
        0x109,
        "#10101F(This is the other side of the door …)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4DB")

    label("loc_4A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DB")

    AnonymousTalk(
        0x106,
        "#10701F(It is the back of this door, is not it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4DB")


    AnonymousTalk(
        0x103,
        "#00201F(Yes, there is no mistake.)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56B")

    AnonymousTalk(
        0x105,
        (
            "#10400F(Is this a warehouse or something?\x01",
            "It looks like the door has a window. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_636")

    label("loc_56B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D3")

    AnonymousTalk(
        0x106,
        (
            "#10705F(Is this a warehouse or something?\x01",
            "It seems that the door has a window. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_636")

    label("loc_5D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_636")

    AnonymousTalk(
        0x109,
        (
            "#10105F(Is this a warehouse or something?\x01",
            "It looks like the door has a window. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_636")


    AnonymousTalk(
        0x101,
        (
            "#00003F(I do not know but ….\x01",
            "Anyway it's convenient. )\x02\x03",
            "#00000F(A bit from here,\x01",
            "Let's look at the inside. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x9, 0x1)
    OP_68(950, 0, 3180, 0)
    MoveCamera(42, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16090, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(10)
    PlayBGM("ed7302", 0)

    NpcTalk(
        0x8,
        "Is it? Is it? Is it?",
        (
            "Yes, colonel …\x01",
            "Yes, yes …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Is it? Is it? Is it?",
        (
            "Well, did I say that?\x01",
            "Haha … I'm sorry, the director.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#N(That back figure is … …)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#N(Maybe … ….\x01",
            "Crossbell Times'\x01",
            "  Rainesさん？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00205F#N(What on earth …… in a place like this …)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PUmm … … There you are\x01",
            "You are the support department, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf you do not mind,\x01",
            "Would you like to talk lightly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#NWhew ……\x01",
            "You already realized it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#NI can not take care of it,\x01",
            "Do as you say.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(980, 900, -2510, 4500)
    MoveCamera(39, 16, 0, 4500)
    OP_6E(600, 4500)
    SetCameraDistance(18630, 4500)
    Sleep(2000)

    def lambda_939():
        OP_97(0xFE, 0x0, 0x0, 0x10CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_939)

    def lambda_953():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_953)
    Sleep(100)

    def lambda_967():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_967)

    def lambda_981():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_981)
    Sleep(100)

    def lambda_995():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_995)

    def lambda_9AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9AF)
    Sleep(500)

    def lambda_9C3():
        OP_97(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9C3)

    def lambda_9DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9DD)
    Sleep(100)

    def lambda_9F1():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9F1)

    def lambda_A0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A0B)
    Sleep(100)

    def lambda_A1F():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A1F)

    def lambda_A39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_A39)
    WaitChrThread(0xF5, 1)

    ChrTalk(
        0x8,
        "#5PAfter all, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo way,\x01",
            "To meet you in a place like this\x01",
            "I did not feel well.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(590, 400, 910, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16820, 3000)

    def lambda_AE4():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE4)
    Sleep(50)

    def lambda_B01():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B01)
    Sleep(50)

    def lambda_B1E():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B1E)
    Sleep(50)

    def lambda_B3B():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B3B)
    Sleep(50)

    def lambda_B58():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B58)
    Sleep(50)

    def lambda_B75():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B75)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00001FYeah, that is us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FCrossbell Times'\x01",
            "A newcomer, a photographer,\x01",
            "Grace's partner ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FWell, as I meet in a place like this,\x01",
            "It is certain that it is not only that.\x02\x03",
            "#00301FAnyway, do not wear a cat\x01",
            "Why do not you vomit a true identity quickly?\x02\x03",
            "While noticing us\x01",
            "That it was not hidden,\x01",
            "You thought so, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, but the personality is\x01",
            "But this is a nice thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PActually I am -\x01",
            "It is a human being of a private research company.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FA private research company … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, it is in Libert.\x01",
            "\"R & A research\"\x01",
            "A company with a name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F\"R & A research\" … …\x01",
            "I feel like I've heard it\x01",
            "I will do it ….\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E7B")

    ChrTalk(
        0x10A,
        "#12P#00603FHmm, I know about the name but … …\x02",
    )

    CloseMessageWindow()

    label("loc_E7B")


    ChrTalk(
        0x8,
        (
            "#5PWell, recently just made\x01",
            "It's a small company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PRichard Director as it is\x01",
            "I think that it is famous.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1070")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00105FCould it be … …\x01",
            "It belonged to the Kingdom army,\x01",
            "Is that about Richard's former colonel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#12P#00600FIndeed … … certainly will the intersection go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FMr. Dudley to Erie … …\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00603FOh, Alan Richard -\x02\x03",
            "#00600F…… Two years ago at Libert\x01",
            "Caused a coup d'etre\x01",
            "It is a former and information officer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1186")

    label("loc_1070")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00105FCould it be … …\x01",
            "It belonged to the Kingdom army,\x01",
            "Is that about Richard's former colonel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FEllie, do you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYes, Alain Richard -\x02\x03",
            "#00101F…… Two years ago at Libert\x01",
            "Caused a coup d'etre\x01",
            "Former and information officer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1186")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00005FThat coup d'etat … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103Fthat's right, but\x01",
            "When Libert's strange change\x01",
            "Showing a big success to save national security … …\x02\x03",
            "#00100FAfter that, officially from the Queen\x01",
            "It is a story that I was pardoned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FPardon …\x02\x03",
            "#00003FI see.\x01",
            "While exploiting his own career\x01",
            "Did you set up a research company?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_130C")

    ChrTalk(
        0x106,
        (
            "#12P#10703FSomehow ……\x01",
            "It looks like a considerable break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AB")

    label("loc_130C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_135D")

    ChrTalk(
        0x105,
        (
            "#12P#10402FGhost, apparently\x01",
            "It looks like a pretty good person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AB")

    label("loc_135D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13AB")

    ChrTalk(
        0x109,
        (
            "#12P#10106FWhat I should say …\x01",
            "It seems like a good person, is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AB")


    ChrTalk(
        0x8,
        (
            "#5PHmm, everyone in the support department.\x01",
            "It is also familiar to such topics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P- That's where I stand\x01",
            "Could you understand a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FYeah, for the most part.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FBut, why\x01",
            "Do you mind revealing your identity to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, everyone\x01",
            "Opportunities to let you work\x01",
            "Because I thought it was there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf so, I will reveal it now\x01",
            "It is the same to reveal later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBy the way, everyone in the company\x01",
            "Mr. Grace,\x01",
            "I have not talked to anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAs you can see,\x01",
            "Could you keep it confidential?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, as long as you talk\x01",
            "To the last you\x01",
            "It will be a third party.\x02\x03",
            "Dare to leak secrets\x01",
            "I do not mean to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThank you very much.\x01",
            "I thought that I could say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FBy the way, due to the influence of Moya\x01",
            "Conducted communication is difficult to connect\x01",
            "I was listening … ….\x02\x03",
            "#00205FIn that communication device,\x01",
            "Can you use it without problems?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POh, is this about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POf course there are influences of moya,\x01",
            "This communicator is simply a powerful\x01",
            "It is possible to output a wave of the wave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, the scope is still barely\x01",
            "It is about to cross the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBy the way, now the director himself\x01",
            "You are traveling to Altair City\x01",
            "I have you relay the communication.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1883")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FI see……\x01",
            "Under such circumstances it is a great partnership.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_1883")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18D2")

    ChrTalk(
        0x105,
        (
            "#12P#10404FI see……\x01",
            "Under such circumstances it is a great partnership.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_18D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_191E")

    ChrTalk(
        0x109,
        (
            "#12P#10105FI see……\x01",
            "Under this situation it is a beautiful collaboration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191E")


    ChrTalk(
        0x104,
        (
            "#12P#00303FThat communication device …\x01",
            "I saw it, until encrypted communication\x01",
            "It looks like a usable type.\x02\x03",
            "#00302FQuite how,\x01",
            "I guess the army is also going to face it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHahahahahahahahahahahahahahahahaha\x01",
            "Although it is overestimate to fluffy … ….\x01",
            "You know well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, for now, communicate with the Defense Forces\x01",
            "It can not be analyzed either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh yeah, by the way, this communicator\x01",
            "There is only high performance, that portion\x01",
            "Mira was also tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo matter what happens from the Deputy Director\x01",
            "Do not break, because you are stuck with a nail,\x01",
            "I am considerably concerned about carrying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSo I am here\x01",
            "To others, we will repay\x01",
            "Please keep it a secret.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C34")

    ChrTalk(
        0x106,
        "#12P#10703F…… It is quite private opinion.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1C34")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C85")

    ChrTalk(
        0x109,
        (
            "#12P#10103FWhat is it …?\x01",
            "It sounds like a very private opinion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_1C85")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CC8")

    ChrTalk(
        0x105,
        "#12P#10404FHuh, it is quite private opinion.\x02",
    )

    CloseMessageWindow()

    label("loc_1CC8")


    ChrTalk(
        0x8,
        (
            "#5PHaha, that's right.\x01",
            "There is absolutely no hardship either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P…… Anyway,\x01",
            "I have spoken very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI continued,\x01",
            "At this place with outside people\x01",
            "I am planning to contact you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PEveryone also to the Orkis Tower\x01",
            "When rushing in,\x01",
            "Please be careful again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FWell - that story\x01",
            "I think that it was not done.\x02\x03",
            "#00000FWell anyway, I have no time\x01",
            "We will rude around here.\x02\x03",
            "#00001FRainesさんもここでの活動には\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYes, of course.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 1)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_241 end

    def Function_5_1EE0(): pass

    label("Function_5_1EE0")

    Sound(32, 0, 30, 0)
    Sleep(700)
    Sound(33, 0, 20, 0)
    Sleep(700)
    Sound(32, 0, 40, 0)
    Sleep(700)
    Sound(33, 0, 30, 0)
    Sleep(700)

    label("loc_1F04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F26")
    Sound(32, 0, 50, 0)
    Sleep(700)
    Sound(33, 0, 40, 0)
    Sleep(700)
    Jump("loc_1F04")

    label("loc_1F26")

    Return()

    # Function_5_1EE0 end

    SaveToFile()

Try(main)
