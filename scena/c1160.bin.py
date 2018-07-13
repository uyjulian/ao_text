from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Vice Chief Pierre",      # 1
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
        "Function_3_F66",          # 03, 3
        "Function_4_2B1E",         # 04, 4
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
        (
            "#1P#N#00005FYour wife has clandestine \x01",
            "meetings with a host...?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#3PY-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PRecently, it appears she's been\x01",
            "going many times to such clubs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIt seems she's meeting\x01",
            "a certain host in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FB-But, are you sure\x01",
            "he's a host...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FRight, shouldn't you trust your wife...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PI was ready to die so I secretly\x01",
            "checked my wife's purse and I\x01",
            "could find definite evidence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIn her appointment book there\x01",
            "was clearly written she has a\x01",
            "meeting with a man called "Clyde"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWhere a housewife could ever\x01",
            "meet such a man if not at a\x01",
            "host club, don't you think!?\x02",
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
        "#00206F(I understand his point, but...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F(Well, I got it that he's desperate.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F...Hm, still...\x01",
            "A host called "Clyde", eh?\x02\x03",
            "#10300FIt's unfortunate, but I've never\x01",
            "heard such a name even once.\x02",
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

    def lambda_691():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_691)
    Sleep(50)

    def lambda_6A1():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A1)
    Sleep(50)

    def lambda_6B1():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B1)
    Sleep(50)

    def lambda_6C1():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C1)
    Sleep(50)

    def lambda_6D1():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6D1)

    ChrTalk(
        0x8,
        "#3PW-What...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FWell, I generally know at least the\x01",
            "names of the hosts who work at the\x01",
            "Entertainment District's clubs.\x02\x03",
            "It could also be that he's a new one\x01",
            "I've got no information about, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PW-Wait.\x01",
            "You seem to be very knowledgeable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PDon't tell me that the temporary\x01",
            "member who is a host and joined\x01",
            "the SSS whom I've heard about is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FOh, that would be me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#3PY-You!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PA person from an indecent business\x01",
            "like a host...!! In the police!\x01",
            "Consider our position for an instant...!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_927():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_927)

    ChrTalk(
        0x101,
        (
            "#00006FN-Now, now...\x01",
            "Please calm down.\x02\x03",
            "#00001FIn any case, the question we have to\x01",
            "settle first is to confirm the situation\x01",
            "your wife is in at present.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9D2():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9D2)
    Sleep(50)

    def lambda_9E2():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9E2)
    Sleep(50)

    def lambda_9F2():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9F2)
    Sleep(50)

    def lambda_A02():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A02)

    ChrTalk(
        0x109,
        (
            "#10101FY-You're right...\x02\x03",
            "#10106FAs for Wazy,\x01",
            "there's nothing that\x01",
            "can be done here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHu hu, what they say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FBefore, you said you looked \x01",
            "into your wife's purse, but...\x02\x03",
            "Wasn't there anything\x01",
            "that could be a clue\x01",
            "for the investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PW-Well, uhhm...\x02",
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
        "#3PO-Oh, now I remember!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWhen I looked at the appointment book, \x01",
            "there was also the destination written...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIt seems that recently she's been\x01",
            "going many times to the restaurant\x01",
            "in Central Square after noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThe Central Square restaurant...\x01",
            "The "Vingt Sept"...?\x02\x03",
            "#00200FHowever, if our man is a host,\x01",
            "doesn't it feel strange meeting\x01",
            "after noon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FA secret rendezvous during the\x01",
            "hours the husband is working...\x01",
            "Maybe it's like that.\x02\x03",
            "#10302FHu hu, when hosts and customers\x01",
            "meet in private, it often happens\x01",
            "during the day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PT-Then it's really...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FP-Please calm down.\x01",
            "...Also, Wazy, don't agitate him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHu hu, my apologies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F*cough*, in any case,\x01",
            "I understand the situation.\x02\x03",
            "#00000FCan you leave the\x01",
            "investigation to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PY-Yes. \x01",
            "I entrust everything to you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PExpose the truth\x01",
            "no matter what!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PHowever, very confidentially.\x01",
            "...Understood!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FR-Roger that.\x01",
            "...Then, excuse us.\x02",
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

    def Function_3_F66(): pass

    label("Function_3_F66")

    EventBegin(0x0)
    SoundLoad(812)
    FadeToDark(0, 0, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd contacted \x01",
            "Elie and the others who were\x01",
            "tailing the madam...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They decided to sort the information at police\x01",
            "HQ where Vice Chief Pierre was waiting.\x07\x00\x02",
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
            "#3PS-So...\x01",
            "How did the investigation go!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWas my wife really meeting\x01",
            "with a host in secret...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FEhm, Vice Chief...\x01",
            "Please calm down.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00000FBefore that...girls,\x01",
            "how did the tailing go?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00100FWell, we watched very attentively...\x01",
            "But there was nothing strange.\x02\x03",
            "She went back to her home\x01",
            "in Residential Street.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(50)

    ChrTalk(
        0x109,
        (
            "#10100FShe didn't meet\x01",
            "anyone in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt seems that she is meeting\x01",
            "that man called Clyde at\x01",
            ""Neue-Blanc" later, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PW-What!?\x02",
    )

    CloseMessageWindow()

    def lambda_1339():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1339)
    Sleep(100)

    def lambda_1349():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1349)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#3PHeck, what does he plan to do\x01",
            "by bringing my wife to such a\x01",
            "dubious place!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PI-If that's the case, I'll form a police squad\x01",
            "and storm that "Neue-Blanc"...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FL-Like I said before,\x01",
            "please calm down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWith them as enemies,\x01",
            "they'd just get taken out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PT-Then...\x01",
            "How can I keep calm!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PEven while we're here like this,\x01",
            "that host's evil clutches could...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, I believe you don't have to worry.\x02\x03",
            "#10302FAt least there won't be any clutches\x01",
            "on that madame from that "host".\x02",
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
        "#3PW-What do you mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWazy said it from\x01",
            "the very beginning...\x02\x03",
            "#00001FThat man, Clyde...\x01",
            "We really think he's not a host.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PW-What...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIn that case...\x01",
            "Who is he!?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18AC")
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat is Clyde's true identity?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Host]\x01",          # 0
            "[Swindler]\x01",      # 1
            "[Salesman]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1737"),
        (1, "loc_17C1"),
        (2, "loc_1844"),
        (SWITCH_DEFAULT, "loc_18A7"),
    )


    label("loc_1737")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00006F(...Wait, didn't \x01",
            "I just said he's\x01",
            "not a host?)\x02\x03",
            "#00001F(Let's think calmly.\x01",
            "That Clyde's true identity is...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A7")

    label("loc_17C1")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(No...strictly speaking, it's not that.)\x02\x03",
            "#00001F(Let's think calmly.\x01",
            "That Clyde's true identity is...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A7")

    label("loc_1844")


    ChrTalk(
        0x101,
        (
            "#00001FThe true identity of that\x01",
            "man is probably...\x01",
            "A "salesman".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A2")
    OP_2C(0x84, 0x1)

    label("loc_18A2")

    Jump("loc_18A7")

    label("loc_18A7")

    Jump("loc_16A5")

    label("loc_18AC")


    ChrTalk(
        0x109,
        "#10105FA...salesman?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIndeed, his polite way of talkin'\x01",
            "felt more that of a pro seller\x01",
            "than that of a host...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, there's also evidence\x01",
            "that he clearly is not a host.\x02\x03",
            "#10302FWe're someone who shows for a short\x01",
            "time a dream to lonely mesdames...\x02\x03",
            "A top class host, even if\x01",
            "he politely escorts, would never\x01",
            "abase himself more than necessary.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FThere's also this point\x01",
            "of view from Wazy, but...\x01",
            "Well, my conjecture is similar.\x02\x03",
            "#00001FTo me, Clyde and your wife didn't\x01",
            "look like they were having a "host and\x01",
            "customer clandestine meeting" at all.\x02\x03",
            "If pushed, I'd say they looked like\x01",
            "a "trader" and "his customer"...\x01",
            "That's the impression that matches them.\x02\x03",
            "Even the fact they've been meeting many times...\x01",
            "It's natural to think those were negotiations\x01",
            "for some kind of transaction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PS-Still, assuming it's like you say...\x01",
            "What in the world is he forcing my\x01",
            "wife to buy!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIf we assume he's a salesman\x01",
            "working somewhere, we can\x01",
            "figure it out.\x02\x03",
            "#00001FThat man, probably...\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F51")
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KClyde is a salesman for...?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[A Jewelry]\x01",                 # 0
            "[A Real Estate]\x01",             # 1
            "[A Securities Company]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D7F"),
        (1, "loc_1E32"),
        (2, "loc_1E99"),
        (SWITCH_DEFAULT, "loc_1F4C"),
    )


    label("loc_1D7F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(No...it's hard to imagine.)\x02\x03",
            "#00001F(The conversation at the restaurant...\x01",
            "And what we saw when we tailed him...\x01",
            "If I think putting those together...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4C")

    label("loc_1E32")


    ChrTalk(
        0x101,
        (
            "#00001FProbably...\x01",
            "I think he's a salesman\x01",
            "who deals in real estates.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E94")
    OP_2C(0x84, 0x1)

    label("loc_1E94")

    Jump("loc_1F4C")

    label("loc_1E99")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(No...it's hard to imagine.)\x02\x03",
            "#00001F(The conversation at the restaurant...\x01",
            "And what we saw when we tailed him...\x01",
            "If I think putting those together...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4C")

    label("loc_1F4C")

    Jump("loc_1CDA")

    label("loc_1F51")

    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00103FA real estate salesman...\x02\x03",
            "#00100FNow that you mention it, Michelam came up\x01",
            "as a topic during the restaurant conversation.\x02\x03",
            "At first I thought it was about a trip,\x01",
            "but that "pamphlet"...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FMaybe a pamphlet with information on houses\x01",
            "located at Michelam's high class residential area.\x02\x03",
            "Then, when we tailed him up to the\x01",
            "Waterfront Area, that Clyde received\x01",
            "something from a man in a suit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FBased on their way of speaking, that man\x01",
            "in a suit was probably Clyde's superior.\x02\x03",
            "#10300FHe could've received an important\x01",
            "document like a written contract.\x02",
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
            "#00000FClyde, as a real estate employee,\x01",
            "was negotiating the sale of a \x01",
            "property to your wife.\x02\x03",
            "Your wife was favorable.\x01",
            "She even went to Michelam for a preview\x01",
            "and the negotiations were proceeding well.\x02\x03",
            "It's natural to think she met \x01",
            "that man for that purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FI see...\x01",
            "Seems to make sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FThen, in today's negotiations,\x01",
            "everything was almost settled...\x02\x03",
            "Soon, the final negotiation will\x01",
            "take place at "Neue-Blanc".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PH-Hm, I understand...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#3PN-No, wait a moment!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PMargaret is trying to buy a Michelam's\x01",
            "property without telling me anything.\x01",
            "...Am I right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PB-But...we don't have such\x01",
            "a fortune at all, you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PHow does she plan to raise\x01",
            "that kind of mira!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FC-Could it be that...\x01",
            "She took a loan...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...It is very worrisome.\x02\x03",
            "#00200FMaybe he induced her to take\x01",
            "out an unreasonable loan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PI-Impossible...\x02",
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
            "#3PI-I've made up my mind...\x01",
            "I'll storm into "Neue-Blanc"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PAfter hearing all this I can't\x01",
            "overlook my wife getting\x01",
            "tricked under my eyes!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PI'll yell at that Clyde youngster there and bring\x01",
            "my wife back even if I have to slap her!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F(...The hen-pecked husband talks big.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Rather, I feel we pressed\x01",
            "a strange switch...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, since we're here,\x01",
            "we'll help you out.\x02\x03",
            "#10309FIf we left you be,\x01",
            "charging in alone at "Neue-Blanc"\x01",
            "would probably be a problem.\x02",
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

    def lambda_282F():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_282F)
    Sleep(50)

    def lambda_283F():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_283F)
    Sleep(50)

    def lambda_284F():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_284F)
    Sleep(50)

    def lambda_285F():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_285F)
    Sleep(50)

    def lambda_286F():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_286F)

    ChrTalk(
        0x101,
        (
            "#00006FI guess you can\x01",
            "really say that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F...Wazy, somehow...\x01",
            "Aren't you enjoying this more and more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHu hu, what're you talking about.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FWell, it seems that only us\x01",
            "can hold him in check...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FCan't be helped. \x01",
            "I'm not eager to do it, but\x01",
            "I guess I'll try to negotiate\x01",
            "at "Neue-Blanc"\x02\x03",
            "#00300FI guess my old pal Sachs\x01",
            "is doing the watchdog there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PDamn, what're you jumbling\x01",
            "and mumbling to each other!?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A48():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A48)
    Sleep(50)

    def lambda_2A58():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A58)
    Sleep(50)

    def lambda_2A68():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A68)
    Sleep(50)

    def lambda_2A78():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A78)
    Sleep(50)

    def lambda_2A88():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A88)

    ChrTalk(
        0x8,
        (
            "#3PI'm gonna go to\x01",
            ""Neue-Blanc" now!!\x01",
            "And you all will come along too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FR-Roger...!\x02",
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

    # Function_3_F66 end

    def Function_4_2B1E(): pass

    label("Function_4_2B1E")

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
            "#3P...*cough*.\x01",
            "Good job, ladies and gentlemen\x01",
            "of the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FAfter hearing the circumstances\x01",
            "we're relieved too.\x02\x03",
            "I'm really glad your wife\x01",
            "wasn't being tricked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PW-Well, in the end,\x01",
            "it seems we'll end up\x01",
            "purchasing a second house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PSince there's no divorce talking involved,\x01",
            "I believe we'll use it as a married couple\x01",
            "during the weekends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha...\x01",
            "It seems your wife too really\x01",
            "liked the second house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FWell, I think\x01",
            "you should go\x01",
            "easy on her, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, even the purchasing funds were,\x01",
            "to begin with, earned by your wife through stocks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PH-Hm... That story too\x01",
            "is concerning me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3P*haah*, due to this case, I ended up\x01",
            "being even more no match for her...\x02",
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
        "#00211F(...You sort of reaped what you sowed.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWell, in any case...\x01",
            "I was able to avoid the worst\x01",
            "situation, the divorce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PLet me earnestly\x01",
            "thank you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, if something happens again,\x01",
            "please consult with us anytime.\x02\x03",
            "#00004F...Then, please excuse us.\x02",
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
            "Quest [The Vice Chief's Request]\x07\x00",
            " completed!\x02",
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

    # Function_4_2B1E end

    SaveToFile()

Try(main)
