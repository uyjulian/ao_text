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
        "Function_4_273",          # 04, 4
        "Function_5_277",          # 05, 5
        "Function_6_3E1",          # 06, 6
        "Function_7_1DFB",         # 07, 7
        "Function_8_2BB5",         # 08, 8
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
            "It's a car magazine,\x01",
            ""Monthly Car Mania\x01",
            "Vol.2".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36F, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26F")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Learned the \x07\x02",
            ""Wild\x01",
            "Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36F, 1)

    label("loc_26F")

    TalkEnd(0xFF)
    Return()

    # Function_3_1C2 end

    def Function_4_273(): pass

    label("Function_4_273")

    Call(0, 5)
    Return()

    # Function_4_273 end

    def Function_5_277(): pass

    label("Function_5_277")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_359")

    ChrTalk(
        0x8,
        (
            "#02901FThe Rosenberg dolls\x01",
            "stolen by Phantom Thief B\x01",
            "are five in total.\x02\x03",
            "#02903FKidnapping my precious\x01",
            "children... It's an act I\x01",
            "can't possibly forgive.\x02\x03",
            "#02900FEveryone, please, I'm\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3DD")

    label("loc_359")


    ChrTalk(
        0x8,
        (
            "#02903FKidnapping my precious\x01",
            "children... It's an act I\x01",
            "can't possibly forgive.\x02\x03",
            "#02901FEveryone, please, I'm\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD")

    TalkEnd(0x8)
    Return()

    # Function_5_277 end

    def Function_6_3E1(): pass

    label("Function_6_3E1")

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
        "#12P#00100F─Bell, it's me.\x02",
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

    def lambda_546():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_546)
    Sleep(100)

    def lambda_563():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_563)

    def lambda_57D():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57D)

    def lambda_597():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_597)

    def lambda_5B1():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B1)

    def lambda_5CB():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5CB)
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
        "#12P#00102FLong time no see, Bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02904FElie... and the rest of\x01",
            "the Special Support\x01",
            "Section as well.\x02\x03",
            "#02900FI heard Tio got back\x01",
            "last night. How have you\x01",
            "been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00200FI'm fine, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02909FUhuhu. Very well then.\x02\x03",
            "#02900FThe conference is later today,\x01",
            "so I'm rather busy. Still, you\x01",
            "guys are giving it your all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FHaha, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FCome to think of it, are\x01",
            "you going to the tower\x01",
            "today too, Mariabell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02900FYes, I'll be representing\x01",
            "my father on behalf of\x01",
            "the bank.\x02\x03",
            "But my father has been\x01",
            "handling all of the trade\x01",
            "conference preparations.\x02\x03",
            "#02906FAnd... I must apologize\x01",
            "to you all.\x02\x03",
            "For calling all of you\x01",
            "here suddenly when you're\x01",
            "so busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FNo, it's not a big deal...\x01",
            "You've helped us so much. It's\x01",
            "really the least we could do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FI understand some\x01",
            "antique dolls were\x01",
            "stolen?\x02\x03",
            "#00301FCan you give us the\x01",
            "details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02903F...Understood.\x02\x03",
            "#02900FI am a huge fan of Rosenberg dolls,\x01",
            "and I'm sure you're all well aware\x01",
            "of that.\x02\x03",
            "#02900FI have been keeping five of my most\x01",
            "favorite dolls in my room here at\x01",
            "IBC.\x02\x03",
            "#02903FHowever, last night, just as I was\x01",
            "leaving on business, someone entered\x01",
            "the room and stole all of them.\x02",
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
            "#12P#10105FT-They must be worth a\x01",
            "fortune!\x02\x03",
            "#10106FThe larger ones are\x01",
            "worth a least a few\x01",
            "million mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02903FIt's not a matter of\x01",
            "money.\x02\x03",
            "I feel lost when my\x01",
            "precious children aren't\x01",
            "where they should be.\x02\x03",
            "#02910FAh, I want to tear that\x01",
            "despicable thief limb-\x01",
            "from-limb!\x02",
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
            "#12P#00105FYour room... It's next to this\x01",
            "one, right?\x02\x03",
            "#00103FAn intruder slipped through\x01",
            "IBC's security... How on earth\x01",
            "could they have done it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02903F...Ahem. I thought it was\x01",
            "strange too, but...\x02\x03",
            "#02901FWhen I saw what was left\x01",
            "at the scene of the crime,\x01",
            "I immediately understood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FSomething left behind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02901FAbout that... It might\x01",
            "be faster if I show you.\x01",
            "Take a look.\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1272")

    AnonymousTalk(
        0x101,
        "#00011FT-This is...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00105FA card from "Phantom\x01",
            "Thief B"!?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            "#02901FAn elusive, mysterious and skilled thief who\x01",
            "has stolen countless works of art across the\x01",
            "continent─ known as "Phantom Thief B".\x02\x03",
            "#02903FIt is said he uses mysterious magic to steal\x01",
            "his marks, and he always leaves a card at\x01",
            "the scene of the crime.\x02\x03",
            "#02901FInfiltrating our building might be right up\x01",
            "his alley.\x02\x03",
            "#02902FAnd, it seems you all have dealt with one of\x01",
            "his incidents before?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        "#10105FY-You do!?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00200FLast time, the statue in the\x01",
            "current City Meeting Hall was\x01",
            "stolen, if I remember correctly.\x02\x03",
            "#00203FIn the end, we couldn't capture\x01",
            "the thief.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00310FTch, so that means he\x01",
            "showed up in Crossbell\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10304FHaha. You guys get\x01",
            "tangled up in all sorts\x01",
            "of incidents, don't you?\x02\x03",
            "#10305FAnd... What does the\x01",
            "card say?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155F")

    label("loc_1272")


    AnonymousTalk(
        0x101,
        "#00011FThis is...!\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00101FCould it be...? A card\x01",
            "from "Phantom Thief B"!?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        (
            "#10105FPhantom Thief B? I feel\x01",
            "like I've heard that\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x8,
        (
            "#02900FElie, Lloyd. It seems you know him.\x02\x03",
            "#02901FAn elusive, mysterious and skilled thief who\x01",
            "has stolen countless works of art across the\x01",
            "continent─ known as "Phantom Thief B".\x02\x03",
            "#02903FIt is said he uses mysterious magic to steal\x01",
            "his marks, and he always leaves a card at\x01",
            "the scene of the crime.\x02\x03",
            "#02901FIn the Empire, where he's more active,\x01",
            "there's no one that doesn't know his name.\x02\x03",
            "#02906FInfiltrating our building might be right up\x01",
            "his alley.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#00200FI've at least heard the\x01",
            "name.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00301FTch. So he's showed up\x01",
            "in Crossbell, huh.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10305FAnd... What does the\x01",
            "card say?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_155F")


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
            "The five little girls who have received the favor of\x01",
            "the young lady here are under my control.\x02\x03",
            "If you would desire their freedom, throw open their\x01",
            "cells with the key of truth.\x02\x03",
            "The first cell is in the city. Search "where the\x01",
            "rear commander sits". ─Phantom Thief B\x07\x00\x02",
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
            "That's the reason I\x01",
            "called you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FPhantom Thief B is\x01",
            "challenging the Special\x01",
            "Support Section...\x02\x03",
            "That's the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FWould he really steal\x01",
            "five dolls for such a\x01",
            "petty reason?\x02\x03",
            "#10302FHehe. He's certainly an\x01",
            "oddball, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FAnyhow... You've been\x01",
            "harmed, so we can't let\x01",
            "this go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FThat's right... Bell's\x01",
            "precious Rosenberg dolls\x01",
            "have been stolen, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02902FHuhu, thank you Elie.\x01",
            "I'm counting on all of\x01",
            "you.\x02",
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
            "He's referring to the five dolls he\x01",
            "stole, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FThen, the "five\x01",
            "cells"...\x02\x03",
            "#00200FHe must be referring to\x01",
            "the five places he hid\x01",
            "the dolls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FSo we have to find those\x01",
            "places, huh?\x02\x03",
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
            "#00303FRear commander... Somehow, I\x01",
            "feel like I've heard that term\x01",
            "recently.\x02\x03",
            "#00300FAnyway, nothing will come of\x01",
            "worrying about it. Let's begin\x01",
            "the investigation immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02904FUhuhu. I'm expecting\x01",
            "great things of the\x01",
            "Special Support Section.\x02\x03",
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
            "#12P#00104FI'll write what was on\x01",
            "the card in our\x01",
            "detective notebook.\x02\x03",
            "#00100FLet's use this as a clue\x01",
            "and begin the\x01",
            "investigation.\x02",
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
            "Quest [The Missing\x01",
            "Collection]\x07\x00",
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

    # Function_6_3E1 end

    def Function_7_1DFB(): pass

    label("Function_7_1DFB")

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
            "#02903F─I understand what happened.\x02\x03",
            "#02901FI'm surprised to learn Phantom\x01",
            "Thief B is a member of Ouroboros,\x01",
            "though.\x02\x03",
            "#02906FIf that's the case, then it's no\x01",
            "wonder you couldn't capture him.\x02\x03",
            "#02910FIn the event he is ever captured,\x01",
            "I'll punish him so hard, he'll\x01",
            "regret ever being born.\x02",
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
        (
            "#00306F(S-She's kind of\x01",
            "scary...)\x02",
        )
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
            "Gave the five Rosenberg\x01",
            "doll trunks to\x01",
            "Mariabell.\x02",
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
        (
            "#12P#10105FYeah he did, now that\x01",
            "you mention it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FWell, it would have been\x01",
            "better if he hadn't stolen\x01",
            "them in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha, that's certainly\x01",
            "true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02903FAnyway, we have to strengthen\x01",
            "our security so this sort of\x01",
            "this doesn't happen again.\x02\x03",
            "#02900FThe Security Department will\x01",
            "need to work harder than\x01",
            "they've ever worked before.\x02\x03",
            "#02909FHuhu, you all really did help\x01",
            "me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109FHaha, don't worry about\x01",
            "it, Bell. That's what\x01",
            "friends are for.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2933")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00005F(That's right, I\x01",
            "remember last time...)\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, 54960, 30, 124080, 2000, 0x0)

    ChrTalk(
        0x101,
        "#12P#00001F(Wait, really?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FL-Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02905F...What are you planning,\x01",
            "staring off into space\x01",
            "all of sudden?\x02",
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
            "#00305FYeah, I forgot about\x01",
            "that.\x02",
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
            "#12P#00003FI'll get straight to the\x01",
            "point.\x02\x03",
            "#00001FYou are Mariabell,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)

    def lambda_2718():
        OP_99(0xFE, 0x101, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2718)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2745():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2745)

    def lambda_275E():
        OP_98(0xFE, 0x0, 0xC8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_275E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        "#12P#00011FGuah!?\x02",
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
            "#02902FUhuhu. Come now, Lloyd.\x02\x03",
            "#02909FIsn't that a bit rude,\x01",
            "given that I've honestly\x01",
            "thanked you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00011FS-Sorry... Ugh...\x02\x03",
            "#00006F(T-There's no mistake\x01",
            "then. She really is\x01",
            "Mariabell... Guh.)\x02",
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
        "#10309FMan, how dirty.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A9B")

    label("loc_2933")


    ChrTalk(
        0x101,
        (
            "#12P#00000FThen, it's about time\x01",
            "for us to be going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02909FHuhu. Thank you very much for your\x01",
            "help today.\x02\x03",
            "#02900FI heard you all were participating\x01",
            "in today's trade conference\x01",
            "security detail as well.\x02\x03",
            "#02904FPlease do your best to assist my\x01",
            "father from behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, please leave it to\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FSee you, Bell.\x02",
    )

    CloseMessageWindow()

    label("loc_2A9B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_2AB2")
    Call(0, 8)

    label("loc_2AB2")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd and the others\x01",
            "returned their authentication\x01",
            "card at the 1F reception desk.\x02",
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
            "Quest [The Missing\x01",
            "Collection]\x07\x00",
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

    # Function_7_1DFB end

    def Function_8_2BB5(): pass

    label("Function_8_2BB5")

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

    def lambda_2C80():
        OP_95(0xFE, 56930, 0, 14020, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C80)

    def lambda_2C9A():
        OP_95(0xFE, 56440, 0, 15190, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C9A)

    def lambda_2CB4():
        OP_95(0xFE, 56440, 0, 12670, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CB4)

    def lambda_2CCE():
        OP_95(0xFE, 55520, 0, 13810, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2CCE)

    def lambda_2CE8():
        OP_95(0xFE, 55020, 0, 15160, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CE8)

    def lambda_2D02():
        OP_95(0xFE, 55020, 0, 12580, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2D02)
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
            "─Ah, the lovely Miss\x01",
            "Mariabell. How have you\x01",
            "been?\x02",
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
            "#02912FJust short of excellent.\x02\x03",
            "#02913FI enjoyed your "sideshow"\x01",
            "or whatever that was\x01",
            "quite a bit, you know.\x02",
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
            "Hehe. Glad to hear it.\x02\x03",
            "Thank you for allowing me to borrow\x01",
            "your precious collection.\x02\x03",
            "I know the meister, but there aren't\x01",
            "many chances to see that many of his\x01",
            "works all at once, you know.\x02\x03",
            "Beauty at its finest─ And please,\x01",
            "allow me to thank you once more.\x02",
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
            "#02909FUhuhu... It seems you handled them\x01",
            "with care. That's a relief.\x02\x03",
            "#02911FIf any of them had gotten even a\x01",
            "single scratch, I would have had to\x01",
            "invite you to my own "castle", though.\x02",
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
            "Hahaha... That is a pity in its own\x01",
            "right.\x02\x03",
            "Well, let us be thankful to the\x01",
            "ladies and gentlemen of the Support\x01",
            "Section who recovered them quickly.\x02",
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
            "#02913FHaha... And so, what do\x01",
            "you plan to do now?\x02",
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
            "Crossbell immediately.\x02\x03",
            "It seems there are interesting\x01",
            "developments in the Empire. I\x01",
            "plan to go there.\x02",
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
            "#02912FI see... Well then, I\x01",
            "thank you.\x02",
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
            "Regarding your Plan, I\x01",
            "shall watch over it from\x01",
            "the Empire.\x02\x03",
            "Hehe. And your future\x01",
            "actions in Ouroboros as\x01",
            "well.\x02",
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
            "#02902FUhuhu... I haven't made\x01",
            "up my mind about that\x01",
            "yet, though.\x02\x03",
            "#02913FVery well then. Let us\x01",
            "meet again soon─\x02",
            "#02911F Phantom Thief.\x02",
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
            "Haha! I shall look\x01",
            "forward to it.\x02",
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

    # Function_8_2BB5 end

    SaveToFile()

Try(main)
