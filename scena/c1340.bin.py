from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1340.bin",                # FileName
        "c1340",                    # MapName
        "c1340",                    # Location
        0x001D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 53000, 0, 20000, 0, 0, 1, 29, 0, 0, 0, 2],
    )

    BuildStringList((
        "c1340",                  # 0
        "Mariabell",              # 1
    ))

    AddCharChip((
        "chr/ch05502.itc",                   # 00
    ))

    DeclNpc(55029,   180,     128820,  180,  389,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)

    DeclActor(47960,   0,       123700,  1200,    47960,   800,     123700,  0x007C, 0,  3,  0x0000)
    DeclActor(53000,   0,       45600,   1200,    53000,   800,     45600,   0x007C, 0,  6,  0x0000)
    DeclActor(55000,   150,     128800,  2500,    55000,   1800,    128800,  0x007E, 0,  4,  0x0000)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_19E",          # 01, 1
        "Function_2_1A5",          # 02, 2
        "Function_3_1C2",          # 03, 3
        "Function_4_27B",          # 04, 4
        "Function_5_27F",          # 05, 5
        "Function_6_3ED",          # 06, 6
        "Function_7_1E8D",         # 07, 7
        "Function_8_2C60",         # 08, 8
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C")
    ClearScenarioFlags(0x25, 1)
    Call(0, 1)

    label("loc_15C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)

    label("loc_18E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_19D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 7)

    label("loc_19D")

    Return()

    # Function_0_144 end

    def Function_1_19E(): pass

    label("Function_1_19E")

    Sound(160, 0, 100, 0)
    Return()

    # Function_1_19E end

    def Function_2_1A5(): pass

    label("Function_2_1A5")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1")
    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x1, 0x1)

    label("loc_1C1")

    Return()

    # Function_2_1A5 end

    def Function_3_1C2(): pass

    label("Function_3_1C2")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a car magazine, "Monthly Car Mania Vol.2".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36F, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_277")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "You learned the\x01\x07\x02",
            ""Wild Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36F, 1)

    label("loc_277")

    TalkEnd(0xFF)
    Return()

    # Function_3_1C2 end

    def Function_4_27B(): pass

    label("Function_4_27B")

    Call(0, 5)
    Return()

    # Function_4_27B end

    def Function_5_27F(): pass

    label("Function_5_27F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_363")

    ChrTalk(
        0x8,
        (
            "#02901FThe Rosenberg dolls stolen by\x01",
            "Phantom Thief B are five in total.\x02\x03",
            "#02903FKidnapping my precious children...\x01",
            "That's an act I can't\x01",
            "possibly forgive.\x02\x03",
            "#02900FEveryone, please,\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3E9")

    label("loc_363")


    ChrTalk(
        0x8,
        (
            "#02903FKidnapping my precious children...\x01",
            "That's an act I can't\x01",
            "possibly forgive.\x02\x03",
            "#02901FEveryone, please,\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E9")

    TalkEnd(0x8)
    Return()

    # Function_5_27F end

    def Function_6_3ED(): pass

    label("Function_6_3ED")

    EventBegin(0x0)
    Fade(1000)
    OP_68(53250, 1500, 45110, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18430, 0)
    SetChrPos(0x102, 52950, 0, 44240, 0)
    SetChrPos(0x101, 52220, 0, 43070, 0)
    SetChrPos(0x104, 53710, 0, 43070, 0)
    SetChrPos(0x109, 51640, 0, 42010, 0)
    SetChrPos(0x103, 52930, 0, 42010, 0)
    SetChrPos(0x105, 54450, 0, 42010, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    OP_9B(0x0, 0x102, 0x0, 0x3E8, 0x5DC, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x102,
        "#12P#00100F──Bell, it's me.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Mariabell's Voice")

    AnonymousTalk(
        0xFF,
        "Yes, do come in.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#12P#00100FExcuse us.\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    Sleep(300)

    def lambda_554():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_554)
    Sleep(100)

    def lambda_571():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_571)

    def lambda_58B():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58B)

    def lambda_5A5():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A5)

    def lambda_5BF():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5BF)

    def lambda_5D9():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D9)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_68(54290, 1230, 126800, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 54960, 30, 125480, 0)
    SetChrPos(0x102, 53750, 30, 125480, 0)
    SetChrPos(0x104, 56190, 30, 125480, 0)
    SetChrPos(0x109, 54960, 30, 124330, 0)
    SetChrPos(0x103, 53750, 30, 124330, 0)
    SetChrPos(0x105, 56190, 30, 124330, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    SetMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x0)
    OP_65(0x1, 0x1)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x105, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#12P#00102F*giggle*, long time no see, Bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02904FElie... and the rest\x01",
            "of the Special\x01",
            "Support Section too.\x02\x03",
            "#02900FI heard Miss Tio got\x01",
            "back last night.\x01",
            "How have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00200FI am doing fine, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02909FUhuhu. Very well then.\x02\x03",
            "#02900FThe conference is later today,\x01",
            "so I think you're rather busy\x01",
            "but please, give it your all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10109FUh uh, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FCome to think of it, are\x01",
            "you going to the tower\x01",
            "today too, Miss Mariabell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02900FYes, I'll be\x01",
            "representing my father\x01",
            "on behalf of the bank...\x02\x03",
            "I left to him the handling of all\x01",
            "the Trade Conference preparations.\x02\x03",
            "#02906FAnd... I must\x01",
            "apologize to you all.\x02\x03",
            "For calling you here suddenly,\x01",
            "when you're so busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FNo, it's not a big deal...\x01",
            "You've helped us so much, Miss Mariabell.\x01",
            "It's really the least we could do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FI understand some antique\x01",
            "dolls were...stolen?\x02\x03",
            "#00301FCan you give us the details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02903F...Understood.\x02\x03",
            "#02900FI am a huge fan of Rosenberg\x01",
            "dolls and I am sure you're\x01",
            "all well aware of that...\x02\x03",
            "#02900FI have been keeping five\x01",
            "of my most favorite dolls\x01",
            "in my room here at IBC.\x02\x03",
            "#02903FHowever, last night, someone entered the room\x01",
            "and stole all of them taking the opportunity \x01",
            "while I had left to attend to some business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00205FAll five Rosenberg\x01",
            "antique dolls...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FT-They must be\x01",
            "worth a fortune...\x02\x03",
            "#10106FThe larger ones are worth at\x01",
            "least a few million mira...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02903FIt's not a matter of money.\x02\x03",
            "I feel lost when my precious children\x01",
            "aren't where they should be...\x02\x03",
            "#02910FAah, I want to tear that\x01",
            "despicable thief limb-from-limb!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FP-Please, calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FYour room... \x01",
            "It's next to this one, right?\x02\x03",
            "#00103FAn intruder slipped through\x01",
            "IBC's security... How on earth\x01",
            "could they have done it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02903F...*ahem*. \x01",
            "Yes, I thought it was\x01",
            "strange too, but...\x02\x03",
            "#02901FWhen I saw what was left at the scene\x01",
            "of the crime, I immediately understood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FSomething was left behind...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02901FAbout that... It might\x01",
            "be faster if I show you.\x01",
            "...Take a look.\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12D6")

    AnonymousTalk(
        0x101,
        "#00011FT-This is...!\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        "#00105FA card from "Phantom Thief B"...!?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            "#02901FAn elusive, mysterious and skilled thief who\x01",
            "has stolen countless works of art across the\x01",
            "continent── known as "Phantom Thief B".\x02\x03",
            "#02903FIt is said he uses mysterious magic to\x01",
            "steal his marks, and he always leaves\x01",
            "a card at the scene of the crime...\x02\x03",
            "#02901FInfiltrating our building\x01",
            "might be right up his alley.\x02\x03",
            "#02902FAnd, it seems you all have dealt with\x01",
            "one of his incidents before, right?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        "#10105FY-You did!?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00200FIndeed. Last time, the statue at\x01",
            "City Meeting Hall was stolen.\x02\x03",
            "#00203FIn the end, we couldn't capture the thief.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00310FTch, so that means he showed\x01",
            "up in Crossbell again.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10304FHu hu. You guys get tangled up in\x01",
            "all sorts of incidents, don't you?\x02\x03",
            "#10305FAnd... \x01",
            "What does the card say?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D8")

    label("loc_12D6")


    AnonymousTalk(
        0x101,
        "#00011FThis is...!\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00101FCould it be...\x01",
            "A card from "Phantom Thief B"...!?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        (
            "#10105FPhantom Thief B...\x01",
            "I feel like I've heard it somewhere.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            "#02900FElie and Mr. Lloyd\x01",
            "seem to know him.\x02\x03",
            "#02901FAn elusive, mysterious and skilled thief who\x01",
            "has stolen countless works of art across the\x01",
            "continent── known as "Phantom Thief B".\x02\x03",
            "#02903FIt is said he uses mysterious magic to\x01",
            "steal his marks, and he always leaves\x01",
            "a card at the scene of the crime...\x02\x03",
            "#02901FIn the Empire, the center of his activities,\x01",
            "there's no one who doesn't know him.\x02\x03",
            "#02906FInfiltrating our building\x01",
            "might be right up his alley.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00200FI too have at least\x01",
            "heard his name.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00301FTch, to think that guy\x01",
            "showed up in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10305FAnd... \x01",
            "What does the card say?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D8")


    AnonymousTalk(
        0x8,
        "#02903F...I'll read it for you.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ladies and gentlemen of the Special Support Section.\x01",
            "The five little girls who have received the favor\x01",
            "of the young lady here are in my hands.\x02\x03",
            "If you would desire their\x01",
            "freedom, throw open their\x01",
            "five cells with the key of truth.\x02\x03",
            "The first cell is in the city.\x01",
            "Search "where the \x01",
            "rear commander sits".\x01",
            "──Phantom Thief B\x07\x00\x02",
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
        0x8,
        (
            "#5P#02901F...Do you understand it?\x01",
            "That's the biggest reason\x01",
            "I called you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FPhantom Thief B is challenging\x01",
            "the Special Support Section...\x02\x03",
            "That's the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FWould he really\x01",
            "steal five dolls for\x01",
            "such a petty reason?\x02\x03",
            "#10302FHu hu. He's certainly\x01",
            "an oddball, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FAnyhow... \x01",
            "You've been harmed, \x01",
            "so we can't let this go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FThat's right... \x01",
            "Bell's precious Rosenberg dolls\x01",
            "have been stolen, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02902FUh uh, thank you Elie.\x01",
            "I am counting on all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FAlright then, before starting the\x01",
            "investigation, I want to consider\x01",
            "again what was written on the card.\x02\x03",
            "#00003FFirstly, the "five little girls"...\x02\x03",
            "He's referring to the five\x01",
            "dolls he stole, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FThen, the "five cells"...\x02\x03",
            "#00200FHe must be referring\x01",
            "to the five places where\x01",
            "he hid the dolls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FSo we have to\x01",
            "find five places\x01",
            "too, eh...?\x02\x03",
            "#10106FUgh, sounds tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FThe most important points then\x01",
            "are "in the city" and "where\x01",
            "the rear commander sits".\x02\x03",
            "#10304FMost likely, it's a hint to\x01",
            "one of the hiding places...\x01",
            "Can anyone think of anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F"Rear commander"...\x01",
            "Somehow, I feel like I've\x01",
            "heard that term...\x02\x03",
            "#00300FAnyway, nothing will come of worryin' about it\x01",
            "Let's begin the investigation immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02904FUhuhu. I am expecting great things\x01",
            "from the Special Support Section.\x02\x03",
            "#02900FPlease, recover my\x01",
            "precious, lost children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAlright. Leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FI'll write what was on the card\x01",
            "in the Detective Notebook.\x02\x03",
            "#00100FLet's use this as a clue and\x01",
            "begin the investigation.\x02",
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
            "Quest [The Missing Collection]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 54990, 30, 124960, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x7A, 0x1, 0x1)
    SetScenarioFlags(0x1C6, 3)
    EventEnd(0x5)
    Return()

    # Function_6_3ED end

    def Function_7_1E8D(): pass

    label("Function_7_1E8D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(54970, 1230, 123580, 0)
    MoveCamera(46, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 54960, 30, 123480, 0)
    SetChrPos(0x102, 53750, 30, 123480, 0)
    SetChrPos(0x104, 56190, 30, 123480, 0)
    SetChrPos(0x109, 54960, 30, 122330, 0)
    SetChrPos(0x103, 53750, 30, 122330, 0)
    SetChrPos(0x105, 56190, 30, 122330, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    ClearChrBattleFlags(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 54960, 30, 125480, 180)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#02903F──I understand what happened.\x02\x03",
            "#02901FI am surprised to learn Phantom Thief B\x01",
            "is a member of the "Society", though.\x02\x03",
            "#02906FIf that's the case, then it's no\x01",
            "wonder you couldn't capture him.\x02\x03",
            "#02910FIn the event he's ever captured,\x01",
            "I'll punish him so hard, \x01",
            "he'll regret ever being born.\x02",
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
        0x104,
        "#00306F(S-She's kind of scary...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FS-Sorry. We wanted to\x01",
            "capture him, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FFor now, allow us to\x01",
            "return your dolls.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You gave the five Rosenberg\x01",
            "doll trunks to Mariabell.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "#02909FUhuhu. Welcome home,\x01",
            "Alice, Canan, Liete,\x01",
            "Mistel and Sharon...\x02\x03",
            "#02904FWell whatever. I've no\x01",
            "complaints at this time.\x02\x03",
            "#02900FAfter all, my cute\x01",
            "Rosenberg dolls are all\x01",
            "home, safe and sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell, Phantom Thief B is\x01",
            "nothing if not thorough.\x02\x03",
            "#10300FHe put them in those trunks\x01",
            "and dragged them out to all\x01",
            "those places, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FYeah he did, now that you mention it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FWell, it would have been better if he\x01",
            "hadn't stolen them in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00009FHa ha, that's certainly true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02903FAnyway, we have to strengthen\x01",
            "our security so this sort of\x01",
            "thing doesn't happen again.\x02\x03",
            "#02900FThe security department will need to work\x01",
            "harder than they've ever worked before.\x02\x03",
            "#02909FUh uh, you all really\x01",
            "did help me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109F*giggle*, don't worry about it, Bell.\x01",
            "That's what friends are for.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_29F3")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#12P#00005F(That's right, I'm sure that last time...)\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 54960, 30, 124080, 2000, 0x0)

    ChrTalk(
        0x101,
        "#12P#00001F(No way...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FMr. L-Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02905F...What are you planning, \x01",
            "staring at me all of a sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FN-Nevermind.\x02\x03",
            "#00001FBefore, when we resolved the\x01",
            "incident, Phantom Thief B\x01",
            "disguised himself as the client...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FYeah, I forgot\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FBut this time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...I'll get straight to the point.\x02\x03",
            "#00001FYou're Miss Mariabell, aren't you──\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)

    def lambda_27C5():
        OP_99(0xFE, 0x101, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27C5)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_27F2():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27F2)

    def lambda_280B():
        OP_98(0xFE, 0x0, 0xC8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_280B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        "#12P#00011FGuah...!?\x02",
    )

    CloseMessageWindow()
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
        0x8,
        (
            "#02902FUhuhu. Come on, Mr. Lloyd.\x02\x03",
            "#02909FIsn't that a bit rude, \x01",
            "given that I have just\x01",
            "honestly thanked you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00011FS-Sorr...ugh...!\x02\x03",
            "#00006F(T-There's no mistake then.\x01",
            "She really is Miss Mariabell... Guh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FOh, Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FOh boy, how lax.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B44")

    label("loc_29F3")


    ChrTalk(
        0x101,
        (
            "#12P#00000FThen, it's time to\x01",
            "excuse ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02909FUh uh, thank you very\x01",
            "much for today.\x02\x03",
            "#02900FIt seems that you too\x01",
            "will take part as security in\x01",
            "today's Trade Conference.\x02\x03",
            "#02904FPlease, do as much as possible\x01",
            "to help my father from the shadows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, please count on us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FBye then, Bell.\x02",
    )

    CloseMessageWindow()

    label("loc_2B44")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_2B5B")
    Call(0, 8)

    label("loc_2B5B")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd and the others\x01",
            "returned their authentication\x01",
            "card at the 1F reception desk.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [The Missing Collection]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7A, 0x1, 0x6)
    OP_29(0x7A, 0x1, 0x7)
    OP_29(0x7A, 0x4, 0x10)
    SubItemNumber(0x324, 1)
    SubItemNumber(0x335, 1)
    SubItemNumber(0x336, 1)
    SubItemNumber(0x337, 1)
    SubItemNumber(0x338, 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c1310", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1E8D end

    def Function_8_2C60(): pass

    label("Function_8_2C60")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    OP_68(54590, 1500, 13640, 0)
    MoveCamera(55, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20420, 0)
    SetChrPos(0x101, 53930, 0, 14020, 90)
    SetChrPos(0x102, 53440, 0, 15190, 90)
    SetChrPos(0x104, 53440, 0, 12670, 90)
    SetChrPos(0x109, 52520, 0, 13810, 90)
    SetChrPos(0x103, 52020, 0, 15160, 90)
    SetChrPos(0x105, 52020, 0, 12580, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0xA, 0x1, 0x8)
    Sleep(1000)

    def lambda_2D2B():
        OP_95(0xFE, 56930, 0, 14020, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D2B)

    def lambda_2D45():
        OP_95(0xFE, 56440, 0, 15190, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D45)

    def lambda_2D5F():
        OP_95(0xFE, 56440, 0, 12670, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D5F)

    def lambda_2D79():
        OP_95(0xFE, 55520, 0, 13810, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2D79)

    def lambda_2D93():
        OP_95(0xFE, 55020, 0, 15160, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D93)

    def lambda_2DAD():
        OP_95(0xFE, 55020, 0, 12580, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2DAD)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x105, 0x1)
    LoadChrToIndex("apl/ch51274.itc", 0x1F)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(55700, 1400, 130699, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x8, 56030, 0, 130930, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    Sound(802, 0, 100, 0)
    Sleep(500)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x1, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02904FHello?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    Sleep(500)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Hi, lovely Miss Mariabell.\x01",
            "How are you faring?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02912FJust great now.\x02\x03",
            "#02913FI really enjoyed your "side show"\x01",
            "or whatever it was.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hu hu, I am glad to hear that.\x02\x03",
            "I am grateful for having allowed me\x01",
            "to borrow your precious collection.\x02\x03",
            "I am a Meister's acquaintance,\x01",
            "but I had never had the chance\x01",
            "to see that many of his works.\x02\x03",
            "Beauty at its finest──\x01",
            "Allow me to thank you again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02909FUhuhu...it seems you\x01",
            "treated them kindly,\x01",
            "so I was relieved.\x02\x03",
            "#02911FIf you had made them even a single scratch,\x01",
            "I would have had to invite you to my own\x01",
            ""castle", though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ha ha ha...\x01",
            "That is a pity in its own right.\x02\x03",
            "Well, let us be thankful to the ladies and gentlemen\x01",
            "of the Support Section who recovered them quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02913FUh uh...\x01",
            "So, what're you planning\x01",
            "to do from now on?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, I intend to leave\x01",
            "Crossbell very soon.\x02\x03",
            "Things seem to becoming\x01",
            "interesting in the Empire.\x01",
            "I plan to go over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02912FIs that so...?\x01",
            "Then, thank you for all you did.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As for your "plan",\x01",
            "I too will be watching it\x01",
            "attentively from the Empire.\x02\x03",
            "Hu hu, and also I will watch your\x01",
            "future actions in the "Society" too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02902FUhuhu... I haven't decided\x01",
            "if I'll join yet, though.\x02\x03",
            "#02913FThen, let us meet again\x01",
            "in the near future──\x02\x01",
            "#02911F"Gentleman Phantom Thief".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Phantom Thief Bleublanc")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ha ha, I will be looking\x01",
            "forward to that moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Return()

    # Function_8_2C60 end

    SaveToFile()

Try(main)
