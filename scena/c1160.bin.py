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
        "Function_3_F10",          # 03, 3
        "Function_4_2B08",         # 04, 4
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
            "#1P#N#00005FYour wife is having\x01",
            "clandestine meetings\x01",
            "with a host...?\x02",
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
            "#3PShe's gone to such clubs\x01",
            "many times recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIt seems she's meeting a\x01",
            "certain host in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FB-But, are you sure he's\x01",
            "a host?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FThat's right, shouldn't\x01",
            "you trust your wife?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PPrepared to pay with my very\x01",
            "life, I secretly looked in my\x01",
            "wife's purse and found proof!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIn her appointment book, it was\x01",
            "clearly written that she had a\x01",
            "meeting with a man named "Clyde"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PA housewife like her meeting man\x01",
            "like him somewhere other than a\x01",
            "host club is unthinkable, no!?\x02",
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
        (
            "#00206F(I understand what he's\x01",
            "trying to say, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Well, I get that he's\x01",
            "desperate at least.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F...Hm, still... A host\x01",
            "named "Clyde", eh?\x02\x03",
            "#10300FSorry, but I've never\x01",
            "heard that name even\x01",
            "once.\x02",
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

    def lambda_693():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_693)
    Sleep(50)

    def lambda_6A3():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A3)
    Sleep(50)

    def lambda_6B3():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B3)
    Sleep(50)

    def lambda_6C3():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C3)
    Sleep(50)

    def lambda_6D3():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6D3)

    ChrTalk(
        0x8,
        "#3PW-What?\x02",
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
            "He's could be a new one I've got no\x01",
            "information about, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PW-Wait. You seem to be\x01",
            "very knowledgeable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PDon't tell me the rumored\x01",
            "temporary member of the SSS\x01",
            "who works as a host is...\x02",
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
            "#3PTo think for even a second\x01",
            "that an indecent person like\x01",
            "a host is in the police!!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8EA():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EA)

    ChrTalk(
        0x101,
        (
            "#00006FN-Now, now... Please, calm\x01",
            "down.\x02\x03",
            "#00001FAnyhow, our first priority is\x01",
            "to ascertain the situation\x01",
            "your wife is in at present.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_981():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_981)
    Sleep(50)

    def lambda_991():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_991)
    Sleep(50)

    def lambda_9A1():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9A1)
    Sleep(50)

    def lambda_9B1():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9B1)

    ChrTalk(
        0x109,
        (
            "#10101FY-You're right...\x02\x03",
            "#10106FAs for Wazy, say what you\x01",
            "like, but I don't think\x01",
            "there's anything you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHehe, what she said.\x02",
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
            "#00100FBefore, you said you\x01",
            "looked in your wife's\x01",
            "purse, but...\x02\x03",
            "Was there anything there\x01",
            "that could be a clue in\x01",
            "our investigation?\x02",
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
            "#3PThe meeting's location\x01",
            "was also in my wife's\x01",
            "appointment book, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIt seems my wife has been\x01",
            "going to the Central Square\x01",
            "restaurant after noon lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThe Central Square\x01",
            "restaurant... Vingt Sept,\x01",
            "you mean?\x02\x03",
            "#00200FHowever, if our target is a\x01",
            "host, isn't it strange for\x01",
            "her to meet him after noon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FA secret rendezvous while the\x01",
            "husband is working... Maybe\x01",
            "it's like that.\x02\x03",
            "#10302FHehe, when hosts and customers\x01",
            "meet in private, it often\x01",
            "happens during the day...\x02",
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
            "...Also, Wazy, don't\x01",
            "encourage him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHehe, my apologies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F*ahem*, in any case, I\x01",
            "understand the\x01",
            "situation.\x02\x03",
            "#00000FCan you leave the\x01",
            "investigation to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PY-Yes. I leave\x01",
            "everything to all of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PExpose the truth no\x01",
            "matter what!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PHowever, very\x01",
            "confidentially.\x01",
            "...Understood!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FR-Roger that. ...Then,\x01",
            "excuse us.\x02",
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

    def Function_3_F10(): pass

    label("Function_3_F10")

    EventBegin(0x0)
    SoundLoad(812)
    FadeToDark(0, 0, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd contacted Elie\x01",
            "and the others who were tailing\x01",
            "the Vice Chief's wife...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They decided to sort out the\x01",
            "information at police HQ where\x01",
            "Vice Chief Pierre was waiting.\x07\x00\x02",
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
            "#3PAnd? How did the\x01",
            "investigation go!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWas my wife really\x01",
            "meeting with a host in\x01",
            "secret!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FUmm, Vice Chief...\x01",
            "Please calm down.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00000FBefore that... Girls,\x01",
            "how did your tail go?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00100FWell, we watched\x01",
            "attentively... But there\x01",
            "was nothing strange.\x02\x03",
            "She went back to her\x01",
            "home on Residential\x01",
            "Street.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(50)

    ChrTalk(
        0x109,
        (
            "#10100FShe didn't meet anyone\x01",
            "in particular either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt seems that she is\x01",
            "meeting this Clyde at Neue-\x01",
            "Blanc later, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PW-What!?\x02",
    )

    CloseMessageWindow()

    def lambda_12E1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12E1)
    Sleep(100)

    def lambda_12F1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12F1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#3PHeck, what does he plan to\x01",
            "do by bringing my wife to\x01",
            "such an unseemly place!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PI-If that's the case, I'll\x01",
            "form a police squad and\x01",
            "storm that Neue-Blanc!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I already told you,\x01",
            "please calm down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FConsidering who they're\x01",
            "up against, they'd just\x01",
            "get taken out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PT-Then... How can I\x01",
            "possibly keep calm!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PEven while we're here like\x01",
            "this, my wife could be falling\x01",
            "into that host's clutches...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe. I don't think that's\x01",
            "anything to worry about.\x02\x03",
            "#10302FNo need to worry about her\x01",
            "falling into the clutches\x01",
            "of that host, at least.\x02",
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
            "#00003FWazy's been telling you\x01",
            "from the very\x01",
            "beginning...\x02\x03",
            "#00001FI really don't think\x01",
            "this Clyde is a host.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PW-What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIn that case... Who is\x01",
            "he!?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188A")
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat is Clyde's true\x01",
            "identity?\x07\x00\x02",
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
        (0, "loc_1716"),
        (1, "loc_179E"),
        (2, "loc_1822"),
        (SWITCH_DEFAULT, "loc_1885"),
    )


    label("loc_1716")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00006F(...Wait, didn't I just\x01",
            "say he's not a host?)\x02\x03",
            "#00001F(Let's think calmly.\x01",
            "That Clyde's true\x01",
            "identity is...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1885")

    label("loc_179E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(No... Strictly\x01",
            "speaking, he's not\x01",
            "that.)\x02\x03",
            "#00001F(Let's think calmly.\x01",
            "That Clyde's true\x01",
            "identity is...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1885")

    label("loc_1822")


    ChrTalk(
        0x101,
        (
            "#00001FThe true identity of\x01",
            "that man is probably...\x01",
            "A "salesman".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1880")
    OP_2C(0x84, 0x1)

    label("loc_1880")

    Jump("loc_1885")

    label("loc_1885")

    Jump("loc_1684")

    label("loc_188A")


    ChrTalk(
        0x109,
        "#10105FA salesman, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIndeed, his polite way\x01",
            "of talkin' felt more pro\x01",
            "salesman than host...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe. There's also clear evidence that\x01",
            "he is not a host.\x02\x03",
            "#10302FWe hosts are existences who show lonely\x01",
            "mesdames a dream for a short while...\x02\x03",
            "A top class host, even one who politely\x01",
            "escorts, would never deprecate himself\x01",
            "any more than necessary.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FThere's Wazy's point of view too, but my\x01",
            "thoughts are similar.\x02\x03",
            "#00001FTo me, the meeting between this Clyde and your\x01",
            "wife didn't look at all like a "clandestine\x01",
            "meeting between host and customer".\x02\x03",
            "If pushed, I'd say they looked like a\x01",
            ""merchant" and "his customer"... That's the\x01",
            "impression that matches them.\x02\x03",
            "Even the fact that they've met several\x01",
            "times... It's natural to think they were\x01",
            "negotiations for some kind of transaction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PS-Still, assuming it's like\x01",
            "you say... What in the world\x01",
            "is he forcing my wife to buy!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIf we assume he's a\x01",
            "salesman working somewhere,\x01",
            "we can figure it out.\x02\x03",
            "#00001FThat man is most likely...\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F30")
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KClyde is a salesman\x01",
            "for...?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[A Jewelry Store]\x01",            # 0
            "[A Real Estate Company]\x01",      # 1
            "[A Brokerage Firm]\x01",           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D6C"),
        (1, "loc_1E1B"),
        (2, "loc_1E7C"),
        (SWITCH_DEFAULT, "loc_1F2B"),
    )


    label("loc_1D6C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(No... That's hard to imagine.)\x02\x03",
            "#00001F(The conversation at the restaurant,\x01",
            "and what we saw when we tailed him.\x01",
            "If I think about them together...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1E1B")


    ChrTalk(
        0x101,
        (
            "#00001FMost likely... He's a\x01",
            "salesman who deals in\x01",
            "real estate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E77")
    OP_2C(0x84, 0x1)

    label("loc_1E77")

    Jump("loc_1F2B")

    label("loc_1E7C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(No... That's hard to imagine.)\x02\x03",
            "#00001F(The conversation at the restaurant,\x01",
            "and what we saw when we tailed him.\x01",
            "If I think about them together...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1F2B")

    Jump("loc_1CBD")

    label("loc_1F30")

    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00103FReal estate...\x02\x03",
            "#00100FNow that you mention it, the topic\x01",
            "of Michelam came up in their\x01",
            "conversation at the restaurant.\x02\x03",
            "At first I thought it was about a\x01",
            "trip, but that "pamphlet" they\x01",
            "discussed...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000FIt most likely had information\x01",
            "on housing in Michelam's high-\x01",
            "class residential area.\x02\x03",
            "Then, when we tailed him to\x01",
            "Waterfront Area, Clyde received\x01",
            "something from a man in a suit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FBased on how they talked,\x01",
            "that suited man was\x01",
            "probably Clyde's superior.\x02\x03",
            "#10300FI guess he received some\x01",
            "important document such as\x01",
            "a sales contract.\x02",
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
            "#00000FClyde, a real estate agent, was\x01",
            "negotiating the sale of a property to\x01",
            "your wife.\x02\x03",
            "Your wife was favorable. She even went\x01",
            "to Michelam for a preview and the\x01",
            "negotiations were proceeding well.\x02\x03",
            "It's natural to think that's the\x01",
            "reason she met with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FI see... That all seems\x01",
            "to line up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FThen, in today's\x01",
            "negotiations, everything\x01",
            "was mostly settled...\x02\x03",
            "Soon, the final\x01",
            "negotiation will take\x01",
            "place at Neue-Blanc.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PY-Yes, I understand...\x02",
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
            "#3PMargaret is trying to buy a\x01",
            "Michelam property without telling\x01",
            "me anything. ...Am I right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PB-But... Our family doesn't\x01",
            "have anywhere close to that\x01",
            "kind of money!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PJust where does she\x01",
            "think she'll get it\x01",
            "from!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FC-Could it be that...\x01",
            "she took out a loan or\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThat's quite plausible.\x02\x03",
            "#00200FMaybe he induced her to\x01",
            "take out an unreasonable\x01",
            "loan.\x02",
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
            "#3PI-I've made up my\x01",
            "mind... I'll storm into\x01",
            "Neue-Blanc!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PAfter hearing all this, I\x01",
            "can't overlook my wife getting\x01",
            "tricked right under my nose!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PI'll yell at that Clyde youngster\x01",
            "there and bring my wife back even\x01",
            "if I have to slap her!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F(...The hen-pecked\x01",
            "husband certainly talks\x01",
            "big.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Rather, I feel we\x01",
            "pressed a strange\x01",
            "button...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. Since we're here,\x01",
            "we'll help you out.\x02\x03",
            "#10309FIt'd be a problem if we\x01",
            "just let you charge in\x01",
            "there alone, see?\x02",
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

    def lambda_2812():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2812)
    Sleep(50)

    def lambda_2822():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2822)
    Sleep(50)

    def lambda_2832():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2832)
    Sleep(50)

    def lambda_2842():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2842)
    Sleep(50)

    def lambda_2852():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2852)

    ChrTalk(
        0x101,
        (
            "#00006FIndeed, you're probably\x01",
            "right about that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWazy, aren't you\x01",
            "enjoying this more and\x01",
            "more, somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe. I have no idea\x01",
            "what you're talking\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FBut, well... It seems\x01",
            "we're the only ones who\x01",
            "can hold him in check.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FCan't be helped. I don't want\x01",
            "to, but I guess I'll try\x01",
            "negotiating at Neue-Blanc.\x02\x03",
            "#00300FMy ol' pal Sachs should be\x01",
            "guardin' the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PDamn, what are you\x01",
            "mumbling to each other!?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A35():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A35)
    Sleep(50)

    def lambda_2A45():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A45)
    Sleep(50)

    def lambda_2A55():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A55)
    Sleep(50)

    def lambda_2A65():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A65)
    Sleep(50)

    def lambda_2A75():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A75)

    ChrTalk(
        0x8,
        (
            "#3PI'm gonna go to Neue-\x01",
            "Blanc now!! And you're\x01",
            "all coming with me!\x02",
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

    # Function_3_F10 end

    def Function_4_2B08(): pass

    label("Function_4_2B08")

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
            "#3P...*cough*. Excellent work,\x01",
            "ladies and gentlemen of the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FAfter hearing the\x01",
            "circumstances, we're\x01",
            "relieved too.\x02\x03",
            "I'm really glad your\x01",
            "wife wasn't being\x01",
            "tricked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PW-Well in the end, it seems\x01",
            "we'll end up purchasing a\x01",
            "vacation home after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PSince divorce is off the table,\x01",
            "I believe we'll use it as a\x01",
            "married couple on weekends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha... It seems your\x01",
            "wife really liked the\x01",
            "house, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FWell, I think you should\x01",
            "go easy on her, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. She earned the\x01",
            "mira for it through\x01",
            "stocks, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PY-Yes... That part makes\x01",
            "my head hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3P*sigh*. With this case,\x01",
            "I'm even less of a match\x01",
            "for her than before...\x02",
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
        (
            "#00211F(...I think he reaped\x01",
            "what he sowed.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWell, in any case... I was\x01",
            "able to avoid the worst\x01",
            "situation, the divorce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PLet me earnestly thank\x01",
            "you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha. Please let us know\x01",
            "if you ever need our\x01",
            "help again.\x02\x03",
            "#00004F...Then, please excuse\x01",
            "us.\x02",
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
            "Quest [The Vice Chief's\x01",
            "Request]\x07\x00",
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

    # Function_4_2B08 end

    SaveToFile()

Try(main)
