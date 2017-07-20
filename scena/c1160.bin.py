from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1160.bin",                # FileName
        "c1160",                    # MapName
        "c1160",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1160",                  # 0
        "Pierre deputy director",         # 1
    ))

    AddCharChip((
        "chr/ch06402.itc",                   # 00
        "chr/ch06400.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(204, 0)                                        # 0

    ScpFunction((
        "Function_0_CC",           # 00, 0
        "Function_1_104",          # 01, 1
        "Function_2_161",          # 02, 2
        "Function_3_E85",          # 03, 3
        "Function_4_2928",         # 04, 4
    ))


    def Function_0_CC(): pass

    label("Function_0_CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E0")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_103")

    label("loc_E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F4")
    ClearScenarioFlags(0x22, 1)
    Event(0, 3)
    Jump("loc_103")

    label("loc_F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_103")
    ClearScenarioFlags(0x22, 2)
    Event(0, 4)

    label("loc_103")

    Return()

    # Function_0_CC end

    def Function_1_104(): pass

    label("Function_1_104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_137")
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_160")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_160")

    Return()

    # Function_1_104 end

    def Function_2_161(): pass

    label("Function_2_161")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(40930, 1200, -590, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24070, 0)
    SetChrPos(0x101, 40570, 0, -1240, 0)
    SetChrPos(0x102, 42040, 0, -1210, 0)
    SetChrPos(0x103, 40600, 0, -2730, 0)
    SetChrPos(0x104, 42020, 0, -2750, 0)
    SetChrPos(0x109, 40570, 0, -4150, 0)
    SetChrPos(0x105, 42000, 0, -4170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#1P#N#00005FMy wife is meeting with the host … ….?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#3PWell, yes ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PRecently, many times in such a club\x01",
            "You seem to be carrying legs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PApparently, with a host of whom.\x01",
            "It seems that we are in a secret meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FBut, even if it is a host\x01",
            "Is not it limited?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FThat's right, who you believed in your wife … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PStole my eyes at the preparedness of death\x01",
            "I examined the bag of the wife,\x01",
            "I found out certain evidence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIn her schedule book\x01",
            "The promise to meet a man like \"Clyde\"\x01",
            "Tell me that it was Bissiri!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PAs a housewife she met such a man,\x01",
            "Apart from the host club\x01",
            "I can not imagine it! Is it?\x02",
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
        0x103,
        "#00206F(I understand the situation, but … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F(Well, the desperate thing has been transmitted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F…… Hmm, but … …\x01",
            "Host \"Clyde\"?\x02\x03",
            "#10300FI am unfortunate, but such a name is\x01",
            "I have never heard of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_678():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_678)
    Sleep(50)

    def lambda_688():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_688)
    Sleep(50)

    def lambda_698():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_698)
    Sleep(50)

    def lambda_6A8():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A8)
    Sleep(50)

    def lambda_6B8():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6B8)

    ChrTalk(
        0x8,
        "#3PWhat, …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs it so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FWell, I enrolled in the club of the entertainment district\x01",
            "About the host name\x01",
            "I understand it all the way.\x02\x03",
            "Because it is a new entrance, there is no information\x01",
            "There is no possibility, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWait a moment.\x01",
            "It seems to be detailed but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PNo way, I got into the support section\x01",
            "Temporary members of active hosts,\x01",
            "It is rumored that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FOh, that's me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#3PKim, you guys! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PEven if it is a police officer,\x01",
            "Host\x01",
            "In an irresponsible business … …! It is!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A8():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A8)

    ChrTalk(
        0x101,
        (
            "#00006FWell, alright …\x01",
            "calm down please.\x02\x03",
            "#00001FAnyway, now my wife\x01",
            "What are the current situation?\x01",
            "To make sure is the first decision.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_936():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_936)
    Sleep(50)

    def lambda_946():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_946)
    Sleep(50)

    def lambda_956():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_956)
    Sleep(50)

    def lambda_966():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_966)

    ChrTalk(
        0x109,
        (
            "#10101FWell, is not it?\x02\x03",
            "#10106FAbout Wazi\x01",
            "Even if you say in this place\x01",
            "I think that it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHuh, that sort of thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PDamn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FA while ago, I looked into his wife's bag\x01",
            "I was saying that … ….\x02\x03",
            "Something of investigation\x01",
            "What is a clue\x01",
            "Was not there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PWell, yeah, I see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#3PWell, yes, I remembered!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWhen I saw the schedule book,\x01",
            "I wrote a note on the destination … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PRecently in the restaurant in the central square\x01",
            "What I am doing from daytime\x01",
            "It seemed to be much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FCentral square restaurant,\x01",
            "\"Van set\" is … …\x02\x03",
            "#00200FBut if the opponent is a host\x01",
            "I am seeing from the daytime\x01",
            "Is not it funny?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FIn the hours when my husband is working\x01",
            "I steal my eyes and see me …\x01",
            "Maybe it is.\x02\x03",
            "#10302FHuff, hosts and customers\x01",
            "When meeting in private,\x01",
            "There will be more in the daytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3POr, again … …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FPlease calm down.\x01",
            "…… Do not fuck up too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHuh, this is disrespect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FKohon, anyway\x01",
            "I understood the circumstances.\x02\x03",
            "#00000FInvestigation is here\x01",
            "Could you please leave it to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWell, yes.\x01",
            "Let's all leave it to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PAnyhow even the truth\x01",
            "You exposed us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PHowever, it is confidential again.\x01",
            "… … It was great! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FOK, OK.\x01",
            "…… Then excuse me.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1150", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_2_161 end

    def Function_3_E85(): pass

    label("Function_3_E85")

    EventBegin(0x0)
    SoundLoad(812)
    FadeToDark(0, 0, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's\x01",
            "With Elie who was tailing Mrs.\x01",
            "Communicate … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pierre is waiting for the police headquarters,\x01",
            "We decided to organize the information.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(40930, 1200, -590, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24070, 0)
    SetChrPos(0x101, 40570, 0, -1240, 0)
    SetChrPos(0x102, 42040, 0, -1210, 0)
    SetChrPos(0x103, 40600, 0, -2730, 0)
    SetChrPos(0x104, 42020, 0, -2750, 0)
    SetChrPos(0x109, 40570, 0, -4150, 0)
    SetChrPos(0x105, 42000, 0, -4170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(1500)
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#3PWell then … …\x01",
            "How did the survey go? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PAfter all, my wife\x01",
            "Meet the host … …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FUm, deputy director … …\x01",
            "calm down please.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00000FBefore that … … Eli,\x01",
            "How was your wife's train?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00100FYeah, I was watching carefully ….\x01",
            "I did not do anything unusual.\x02\x03",
            "In the residential area direction, at home\x01",
            "It seems I was getting back.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(50)

    ChrTalk(
        0x109,
        (
            "#10100FEspecially that I met someone\x01",
            "There was not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAfter this, \"Neue-Blanc\" in\x01",
            "With that Clyde man\x01",
            "It seems I am meeting you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PWhat is it! Is it?\x02",
    )

    CloseMessageWindow()

    def lambda_1260():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1260)
    Sleep(100)

    def lambda_1270():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1270)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#3PYeah, my wife\x01",
            "Bring it to such a wonderful place\x01",
            "What are you planning to do! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIn this way, organize the police force,\x01",
            "\"Noiee = Blanc\" to control everyone …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FSo\x01",
            "I should calm down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FThat pair of partners,\x01",
            "It 's Sekisuyama' s meeting to get back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PBut, that's it ……\x01",
            "Can this be settled down! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWhile doing this,\x01",
            "My wife is poisonous to the host … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, I do not think that 's a worry.\x02\x03",
            "#10302FAt least, that Madam\x01",
            "Worried about the toxicities of \"host\".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#3PWell, what does that mean …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWadi from the beginning\x01",
            "That is what I was talking about ……\x02\x03",
            "#00001FAfter all, the man named Clyde\x01",
            "I think that it is not a host.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PWhat? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIf so … …\x01",
            "Who are they supposed to be! Is it?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1805")
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat is the identity of Clyde?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【host】\x01",            # 0
            "【con man】\x01",            # 1
            "【salesman】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1665"),
        (1, "loc_1715"),
        (2, "loc_1795"),
        (SWITCH_DEFAULT, "loc_1800"),
    )


    label("loc_1665")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00006F(… … just now,\x01",
            "I am not a host by myself\x01",
            "I just said that. )\x02\x03",
            "#00001F(Let's keep calm and think.\x01",
            "The identity of the man named Clyde … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1800")

    label("loc_1715")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(No … exactly speaking it is different.\x02\x03",
            "#00001F(Let's keep calm and think.\x01",
            "The identity of the man named Clyde … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1800")

    label("loc_1795")


    ChrTalk(
        0x101,
        (
            "#00001FThe identity of a man named Clyde,\x01",
            "Probably …\x01",
            "It is \"salesman\".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FB")
    OP_2C(0x84, 0x1)

    label("loc_17FB")

    Jump("loc_1800")

    label("loc_1800")

    Jump("loc_15D5")

    label("loc_1805")


    ChrTalk(
        0x109,
        "#10105FA salesman, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FCertainly, that polite talk\x01",
            "Rather than a host\x01",
            "I felt like a merchant … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, but it obviously\x01",
            "It is also evidence that it can be said that it is not a host.\x02\x03",
            "#10302FWe are lonesome madams\x01",
            "Presence for showing a temporary dream ……\x02\x03",
            "If you are a first-class host,\x01",
            "Even if you carefully escort\x01",
            "I will not humble more than necessary.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FIf you try to do it\x01",
            "There will be such a point of view, though …\x01",
            "Well, it is a similar guess.\x02\x03",
            "#00001FA man named Clyde and his wife,\x01",
            "To \"hosts and customers who are secretly\"\x01",
            "I could not see it anyhow.\x02\x03",
            "If I had to choose one,\x01",
            "\"Merchant\" and \"that customer\" … …\x01",
            "It is an impression that the person is comfortable.\x02\x03",
            "Even I had met many times,\x01",
            "To do some transactions\x01",
            "It is natural to think that it is negotiations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PBut, as it seems so … …\x01",
            "Whatever the wife is bought\x01",
            "Are you doing it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FEven so, a man named Clyde\x01",
            "Where do you belong to a salesman?\x01",
            "I can tell by reasoning.\x02\x03",
            "#00001FThat man, probably …\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E00")
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere is Clyde a salesman?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Jewelry store】\x01",          # 0
            "【Real Estate Agent】\x01",      # 1
            "【Securities company】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C5E"),
        (1, "loc_1CF7"),
        (2, "loc_1D62"),
        (SWITCH_DEFAULT, "loc_1DFB"),
    )


    label("loc_1C5E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(No … that is hard to think.\x02\x03",
            "#00001F(Conversation at restaurant,\x01",
            "And the scene in the place where the tail went ……\x01",
            "Considering them comprehensively … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFB")

    label("loc_1CF7")


    ChrTalk(
        0x101,
        (
            "#00001FProbably …\x01",
            "Salesman dealing with real estate\x01",
            "It seems that it is not.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D5D")
    OP_2C(0x84, 0x1)

    label("loc_1D5D")

    Jump("loc_1DFB")

    label("loc_1D62")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(No … that is hard to think.\x02\x03",
            "#00001F(Conversation at restaurant,\x01",
            "And the scene in the place where the tail went ……\x01",
            "Considering them comprehensively … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFB")

    label("loc_1DFB")

    Jump("loc_1BC2")

    label("loc_1E00")

    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00103Freal estate……\x02\x03",
            "#00100FBy the way, in a restaurant conversation\x01",
            "The Michelin topic was out there.\x02\x03",
            "At first I thought he was talking about traveling,\x01",
            "\"Brochure\" who came out to talk is … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FProbably, it is in Mishram's luxury villa area\x01",
            "It would be a pamphlet of house information.\x02\x03",
            "Then, at the place where I caught up to the port area,\x01",
            "A man named Clyde is from a man in a suit\x01",
            "I received something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FFrom the mouth,\x01",
            "That guy 's man will be Clyde' s boss.\x02\x03",
            "#10300FProbably important documents such as contracts\x01",
            "I guess it was received.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(50)
    TurnDirection(0x102, 0x8, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FThe man named Clyde\x01",
            "In a real estate agent's office worker,\x01",
            "I was negotiating to sell the property to my wife.\x02\x03",
            "The wife likewise received it,\x01",
            "Also go to previewing to Michelin\x01",
            "We were progressing negotiations steadily.\x02\x03",
            "The wife was meeting that man,\x01",
            "That is why it is natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FI see……\x01",
            "The storm seems to fit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FAnd in today's negotiations\x01",
            "The story is largely unified … …\x02\x03",
            "Soon \"Neue-Blanc\" in\x01",
            "The last negotiation will be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PFuf, Hmm, I see … …\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#3PWell, please wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PMargaret told me\x01",
            "I'm trying to buy a Michelin property.\x01",
            "…… That kind of thing! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PHowever, …\x01",
            "There is nothing at home! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PHow do you like that miracle\x01",
            "You are going to face it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FWell, maybe ….\x01",
            "Is it debt …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F… … It seems like you can think enough.\x02\x03",
            "#00200FTry making an unreasonable loan\x01",
            "It may have been guided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PSounds like that … ….\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_0D()
    Fade(500)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sound(812, 0, 100, 0)
    SetChrPos(0x8, 42100, 0, 1700, 90)
    OP_0D()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#3PI decided, I decided,\x01",
            "I'm getting into \"Neue-Blanc\"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PTell me so far,\x01",
            "The wife is deceived to be deceived\x01",
            "There is no way I can overlook it! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PSo cheat on Young Builds like Clyde,\x01",
            "Take the cheek of the wife and bring it back! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F(… … the gods came out greatly.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Or rather, I do not want a switch\x01",
            "I feel like I got it … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, I have much time\x01",
            "Let's try to help you.\x02\x03",
            "#10309FLeave this as it is,\x01",
            "By 1 person \"Neue-Blanc\"\x01",
            "Even if it rushes in, it will be troubled.\x02",
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
    Sleep(1000)

    def lambda_2651():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2651)
    Sleep(50)

    def lambda_2661():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2661)
    Sleep(50)

    def lambda_2671():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2671)
    Sleep(50)

    def lambda_2681():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2681)
    Sleep(50)

    def lambda_2691():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2691)

    ChrTalk(
        0x101,
        (
            "#00006FIt might be true\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F…… Was this, somehow?\x01",
            "Are not you enjoying more and more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHuh, what shall I do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FWell, even if it can be a brake\x01",
            "We only want to … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, my mind does not move forward\x01",
            "\"Neue-Blanc\" has\x01",
            "Would you like to talk about me?\x02\x03",
            "#00300FPerhaps, Sachs is a familiar face\x01",
            "I'm supposed to be a watchdog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PEee, what are you foolish\x01",
            "Are you talking! Is it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2840():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2840)
    Sleep(50)

    def lambda_2850():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2850)
    Sleep(50)

    def lambda_2860():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2860)
    Sleep(50)

    def lambda_2870():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2870)
    Sleep(50)

    def lambda_2880():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2880)

    ChrTalk(
        0x8,
        (
            "#3PNow, even soon\x01",
            "I will go to \"Neue-Blanc\"! It is!\x01",
            "You guys followed too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FRyo, OK, thanks!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c0490", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_E85 end

    def Function_4_2928(): pass

    label("Function_4_2928")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(40930, 1200, -590, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24070, 0)
    SetChrPos(0x101, 40570, 0, -1240, 0)
    SetChrPos(0x102, 42040, 0, -1210, 0)
    SetChrPos(0x103, 40600, 0, -2730, 0)
    SetChrPos(0x104, 42020, 0, -2750, 0)
    SetChrPos(0x109, 40570, 0, -4150, 0)
    SetChrPos(0x105, 42000, 0, -4170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#3P…… Kohon.\x01",
            "It was a while for me,\x01",
            "Municipal office workers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWe listen to the end,\x01",
            "I was relieved for a while.\x02\x03",
            "Not that his wife was deceived\x01",
            "It was really nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWell, after all, the villa\x01",
            "It is supposed to purchase\x01",
            "It seems to be wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PHowever, since the story of a separate house has disappeared,\x01",
            "Perhaps per weekend\x01",
            "It will be used by a couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHaha ……\x01",
            "My wife also pretty villa\x01",
            "It seems I liked it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FWell, to that extent\x01",
            "Even if you tolerate it\x01",
            "Is not it something you want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuff, originally purchased funds\x01",
            "It is a story that my wife earned it with stocks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWell, yes ….\x01",
            "That point is also a story with a headache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PHa, this time more and more\x01",
            "My head did not go up … …\x02",
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
        0x103,
        "#00211F(…… I wonder if I am self-employed.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWell, whatever ……\x01",
            "The worst situation of divorce\x01",
            "I was able to escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PTo be honest here\x01",
            "Let me thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHahaha, if there is something again\x01",
            "Please contact us anytime.\x02\x03",
            "#00004F…… Then excuse me.\x02",
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
            "Quest 【Request of deputy director】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x84, 0x1, 0x1)
    OP_29(0x84, 0x1, 0x2)
    OP_29(0x84, 0x4, 0x10)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    SetScenarioFlags(0x22, 4)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_2928 end

    SaveToFile()

Try(main)
