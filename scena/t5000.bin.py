from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t5000.bin",                # FileName
        "t5000",                    # MapName
        "t5000",                    # Location
        0x0000,                     # MapIndex
        "ed7102",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t5000",                  # 0
        "Father Kevin",           # 1
        "Girl in Nun's Clothes",  # 2
        "ダドリーの車",           # 3
        "車",                     # 4
        "車",                     # 5
        "Citizen",                # 6
        "Citizen",                # 7
        "Citizen",                # 8
        "Citizen",                # 9
        "Citizen",                # 10
        "Citizen",                # 11
        "Citizen",                # 12
        "Citizen",                # 13
        "Citizen",                # 14
        "共和国バス",             # 15
        "護送車",                 # 16
        "Fake Brand Trader",      # 17
        "Republican Soldier",     # 18
        "Republican Soldier",     # 19
        "Heiyue Member",          # 20
        "Heiyue Member",          # 21
        "SE制御",                 # 22
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(836, 0)                                        # 0

    ScpFunction((
        "Function_0_344",          # 00, 0
        "Function_1_3F4",          # 01, 1
        "Function_2_418",          # 02, 2
        "Function_3_419",          # 03, 3
        "Function_4_2BA6",         # 04, 4
        "Function_5_2C36",         # 05, 5
        "Function_6_2C6A",         # 06, 6
        "Function_7_2CC2",         # 07, 7
        "Function_8_2D42",         # 08, 8
        "Function_9_2D7C",         # 09, 9
        "Function_10_2DC3",        # 0A, 10
        "Function_11_2E1E",        # 0B, 11
        "Function_12_2E7F",        # 0C, 12
        "Function_13_2E9B",        # 0D, 13
        "Function_14_408F",        # 0E, 14
        "Function_15_41A8",        # 0F, 15
        "Function_16_41D5",        # 10, 16
        "Function_17_420F",        # 11, 17
    ))


    def Function_0_344(): pass

    label("Function_0_344")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_37C"),
        (1, "loc_388"),
        (2, "loc_394"),
        (3, "loc_3A0"),
        (4, "loc_3AC"),
        (5, "loc_3B8"),
        (6, "loc_3C4"),
        (SWITCH_DEFAULT, "loc_3D0"),
    )


    label("loc_37C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_388")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_394")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3F3")

    Return()

    # Function_0_344 end

    def Function_1_3F4(): pass

    label("Function_1_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_408")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_417")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_417")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)

    label("loc_417")

    Return()

    # Function_1_3F4 end

    def Function_2_418(): pass

    label("Function_2_418")

    Return()

    # Function_2_418 end

    def Function_3_419(): pass

    label("Function_3_419")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11400.itc", 0x1E)
    LoadChrToIndex("apl/ch51026.itc", 0x1F)
    LoadChrToIndex("chr/ch25600.itc", 0x20)
    LoadChrToIndex("chr/ch21102.itc", 0x21)
    LoadChrToIndex("chr/ch21302.itc", 0x22)
    LoadChrToIndex("chr/ch26000.itc", 0x23)
    LoadChrToIndex("chr/ch25000.itc", 0x24)
    LoadChrToIndex("chr/ch44200.itc", 0x25)
    LoadChrToIndex("chr/ch44100.itc", 0x26)
    LoadChrToIndex("chr/ch44000.itc", 0x27)
    LoadChrToIndex("chr/ch44400.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13800.itp")
    SetChrPos(0x101, 0, 0, 8400, 0)
    SetChrPos(0x109, -1300, 0, 8200, 0)
    SetChrPos(0x10A, -700, 0, 10900, 180)
    SetChrPos(0x108, 700, 0, 11200, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 1500, 0, 8200, 315)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    ClearChrFlags(0xA, 0x80)
    OP_78(0xA, 0xA)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 0, 0, 13500, 0)
    OP_D5(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x6, 0xB)
    OP_49()
    SetChrPos(0xB, 5000, 0, -3500, 0)
    OP_D5(0xB, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x6, 0x1000)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x7, 0xC)
    OP_49()
    SetChrPos(0xC, -19000, 0, 2200, 0)
    OP_D5(0xC, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x9, 0x16)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x16, -35000, 0, 17500, 0)
    OP_D5(0x16, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x20)
    SetChrPos(0xD, 5800, 0, -5400, 225)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x2)
    SetChrPos(0xE, -2300, 50, -2750, 225)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x1)
    SetChrPos(0xF, -2950, 50, -2200, 225)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrPos(0x10, 14700, 0, -6400, 270)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x24)
    SetChrPos(0x11, -22200, 0, 900, 270)
    BeginChrThread(0x11, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x25)
    SetChrPos(0x12, 0, 0, -23000, 0)
    BeginChrThread(0x12, 1, 0, 6)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x26)
    SetChrPos(0x13, 21500, 180, 6000, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x27)
    SetChrPos(0x14, 12000, 0, 9000, 0)
    BeginChrThread(0x14, 0, 0, 8)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x28)
    SetChrPos(0x15, -23500, 0, 900, 90)
    BeginChrThread(0x15, 0, 0, 0)
    OP_68(0, 1900, -21500, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    OP_68(0, 2000, 0, 8000)
    MoveCamera(30, 17, 0, 8000)
    SetCameraDistance(41000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    PlaceName2(100, 200, "c_plac35", 0x0, 0)
    Sleep(500)
    Sleep(1000)
    BeginChrThread(0x16, 0, 0, 4)
    BeginChrThread(0x16, 1, 0, 5)
    BeginChrThread(0x1D, 1, 0, 12)
    Sleep(2000)
    BeginChrThread(0x13, 0, 0, 7)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-11500, 1900, 7700, 0)
    MoveCamera(23, 27, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    WaitChrThread(0x16, 1)
    Sleep(1000)
    Fade(500)
    OP_68(0, 11000, 17800, 0)
    MoveCamera(31, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(26000, 0)
    OP_68(0, 5000, 17800, 7000)
    MoveCamera(39, 10, 0, 7000)
    SetCameraDistance(29000, 7000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1100, 9600, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00004F...Well, then. I'll leave\x01",
            "the escort of those two\x01",
            "to you, Dudley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600F#5PSure. Let me handle\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#00603F#5P...Father Kevin. Allow me\x01",
            "to express my gratitude.\x02\x03",
            "#00600FAlthough honestly, I would\x01",
            "have preferred it if you\x01",
            "contacted us beforehand.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E4)
    Sleep(50)

    def lambda_9F4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#04306F#11PWell... If I could I would,\x01",
            "but I couldn't so I didn't...\x01",
            "if ya catch my drift.\x02\x03",
            "#04300FIt's not like we Gralsritter\x01",
            "are ones to get a warm\x01",
            "welcome in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00606F#5PI guess we have Archbishop Eralda\x01",
            "to thank for that. He's the head\x01",
            "of the Crossbell parish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FAccording to Sister\x01",
            "Marble, he's an expert\x01",
            "in Thaumaturgy...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#04303F#11PYeah, that's what we do.\x02\x03",
            "#04300FStuff happened and now the\x01",
            "archbishop hates us big time.\x02\x03",
            "He pretty much prohibited the\x01",
            "Gralsritter from setting foot\x01",
            "in Crossbell, like, ever again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FArchbishop Eralda,\x01",
            "huh...\x02\x03",
            "#10106FI met him once and he\x01",
            "looked like a very\x01",
            "strict person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04306F#11PThere's strict, and then there's him.\x01",
            "Never met anyone like 'im.\x02\x03",
            "#04308FWell, with all the stuff we did, I can't\x01",
            "really blame him. Actually, his reaction\x01",
            "might've been kinda soft, thinking back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FS-Stuff you did...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01403FI think only the glossing\x01",
            "over of Artifact-connected\x01",
            "events counts as inexcusable.\x02\x03",
            "#01402F...Father Kevin. You really\x01",
            "helped us out today.\x02\x03",
            "Once again, thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#04302F#12PHey now Arios, didn't I owe you a\x01",
            "big one anyway?\x02\x03",
            "#04304FWhat I reeaaally wanted was to\x01",
            "join you on this trip related to\x01",
            "the cult.\x02\x03",
            "#04311FWell, I don't want you to provoke\x01",
            "the archbishop, but lemme know if\x01",
            "you learn anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01404FSure thing. I'll contact\x01",
            "you through the guild if\x01",
            "I find out anything.\x02\x03",
            "#01402F─Lloyd, Sergeant Major\x01",
            "Noｱl. You did a really\x01",
            "great job this time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FF2():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FF2)
    Sleep(50)

    def lambda_1002():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1002)
    Sleep(50)
    TurnDirection(0x109, 0x10A, 500)
    Sleep(200)

    ChrTalk(
        0x109,
        (
            "#6P#10112FAhaha, I didn't think I\x01",
            "was particularly useful,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FThat's not true. You really\x01",
            "helped us out today.\x02\x03",
            "#00006F...But I know that I still have\x01",
            "a long way to go.\x02\x03",
            "#00008FTo be honest, I shouldn't have\x01",
            "had to drag you guys along with\x01",
            "me just to make an arrest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5P#01405FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00606F#5PHmph, quite the pretentious one,\x01",
            "aren't you?\x02\x03",
            "#00601FYou already know that this arrest\x01",
            "by the Special Support Section was\x01",
            "merely a front for this operation.\x02\x03",
            "Moreover, do you really think you\x01",
            "haven't done a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F#5PSelf-admonition is fine, but objective\x01",
            "self-evaluation and situation assessment\x01",
            "are required of a first class detective.\x02\x03",
            "#00600FI'd expect you to know that already,\x01",
            "even if you are still in training for\x01",
            "Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FMr. Dudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FHehe... He should just\x01",
            "say how he really feels\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01404FHeh, you could at least\x01",
            "tell him he did a good\x01",
            "job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00610F#5POh, shut up you two.\x02\x03",
            "#00606F...At any rate, Bannings.\x01",
            "With this, your Section\x01",
            "One training is over.\x02\x03",
            "#00602FUse everything you've\x01",
            "learned on this case to\x01",
            "make a new start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FYes, sir... and thank\x01",
            "you very much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01404FWell then, we'll go on\x01",
            "ahead.\x02\x03",
            "#01402FI'll be counting on your\x01",
            "help in our future\x01",
            "collaborations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, likewise!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FThank you for your hard\x01",
            "work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04309F#12PByebyeeee～ See ya!\x02",
    )

    CloseMessageWindow()
    OP_71(0xA, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0xA)
    BeginChrThread(0x10A, 3, 0, 9)
    Sleep(1000)
    BeginChrThread(0x108, 3, 0, 9)
    WaitChrThread(0x108, 3)

    def lambda_15E2():

        label("loc_15E2")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_15E2")

    QueueWorkItem2(0x101, 2, lambda_15E2)

    def lambda_15F4():

        label("loc_15F4")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_15F4")

    QueueWorkItem2(0x109, 2, lambda_15F4)

    def lambda_1606():

        label("loc_1606")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_1606")

    QueueWorkItem2(0x8, 2, lambda_1606)
    OP_71(0xA, 0x14B, 0x168, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0xA)
    Sound(470, 0, 80, 0)
    OP_71(0xA, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0xA)
    Sound(494, 0, 90, 0)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-2000, 1100, 9600, 2000)

    def lambda_1665():
        OP_96(0xFE, 0xFFFFD6FC, 0x0, 0x34BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1665)
    Sleep(2000)
    Sound(457, 0, 100, 0)
    Fade(500)
    EndChrThread(0xA, 0x1)
    SetChrPos(0xA, -15000, 0, 18000, 0)

    def lambda_16A2():
        OP_96(0xFE, 0xFFFF3CB0, 0x0, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16A2)
    OP_68(-18000, 900, 18000, 0)
    MoveCamera(60, 27, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    OP_68(-30000, 900, 18000, 4000)
    MoveCamera(60, 21, 0, 4000)
    SetCameraDistance(23500, 4000)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x8, 0x2)
    Fade(500)
    StopSound(457, 500, 90)
    OP_68(500, 1000, 8500, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -800, 0, 8900, 270)
    SetChrPos(0x109, -900, 0, 7600, 270)
    SetChrPos(0x8, 1500, 0, 8500, 270)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#04309F#11PAren't you two a lucky\x01",
            "bunch?\x02\x03",
            "#04311FBeing blessed with such\x01",
            "wonderful mentors despite\x01",
            "the different professions?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_180D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_180D)
    Sleep(50)
    TurnDirection(0x109, 0x8, 500)

    ChrTalk(
        0x101,
        "#00002F#6PYes, we really are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10104FThat's right... Chief\x01",
            "Sergei said so too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04300F#11PSo, what's the plan?\x02\x03",
            "Are you taking the train\x01",
            "back to Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, we plan to.\x02\x03",
            "#00005FThat's right... Father Kevin, what\x01",
            "will you do now?\x02\x03",
            "#00000FThere's a station in Crossbell...\x01",
            "I'd like it if we could entertain\x01",
            "you there as thanks for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04306F#11PAppreciate the gesture, but\x01",
            "I've got a little something\x01",
            "to do after this.\x02\x03",
            "#04308FActually, I'd want to ask\x01",
            "you in detail about the\x01",
            "cult too, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013F#6PThe D∴G Cult?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FThe Church knows\x01",
            "something about them,\x01",
            "don't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04306F#11PNope, not a thing.\x02\x03",
            "#04300FThe last time we got involved\x01",
            "with the cult was during the\x01",
            "incident four years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FFour years ago...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PSo... It was after the simultaneous raid and\x01",
            "unmasking operation in which international\x01",
            "armies and the guild collaborated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04303F#11PYeah. We raided a lodge that wasn't\x01",
            "previously known about.\x02\x03",
            "#04308F...Just between you and me, it was a lodge\x01",
            "that could be said to be the worst of all of\x01",
            "them in the cult.\x02\x03",
            "#04301FTo be honest, they were a bunch who\x01",
            "conducted more crazy rituals involving human\x01",
            "experiments than you'd ever think possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FThey were really... the\x01",
            "lowest of scum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04304F#11PWell actually, Arios\x01",
            "really saved us back\x01",
            "then.\x02\x03",
            "#04311FSince I owed him, I felt\x01",
            "better knowing I could\x01",
            "help him out this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PI see.\x02\x03",
            "#00004FHowever, thanks to you,\x01",
            "we captured the criminal\x01",
            "alive.\x02\x03",
            "#00000FThank you very much.\x01",
            "...You really helped us\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04304F#11PNo, no.\x02\x03",
            "#04302FJust like four eyes said back\x01",
            "there, it was actually thanks\x01",
            "to you that we managed it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PThanks to... me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04304F#11PYeah. When things were looking\x01",
            "grim, you got through to him.\x01",
            "What rescued him were your words.\x02\x03",
            "#04300FIf not for those, even with my\x01",
            "treatment, I probably wouldn't\x01",
            "have been able to save him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PR-Really?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x109,
        (
            "#12P#10109FYes, I think so too!\x02\x03",
            "#10102FHe came to his senses\x01",
            "because you reached out\x01",
            "to him so desperately!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00005F#5PSergeant Major...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04309F#11PHaha... The "Special\x01",
            "Support Section", was\x01",
            "it?\x02\x03",
            "#04302FLet me hear the details\x01",
            "some other time.\x02\x03",
            "With this, the cult case\x01",
            "is closed, but something\x01",
            "else could come up.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_219B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_219B)
    Sleep(50)
    TurnDirection(0x109, 0x8, 500)

    ChrTalk(
        0x101,
        (
            "#00004F#6PI understand.\x02\x03",
            "#00000F...Then, we'll take our\x01",
            "leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FThanks for your hard\x01",
            "work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04311F#11PYeah! Good work\x01",
            "yourselves!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(500, 1000, 11400, 4000)

    def lambda_225D():

        label("loc_225D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_225D")

    QueueWorkItem2(0x8, 2, lambda_225D)
    BeginChrThread(0x101, 3, 0, 10)
    BeginChrThread(0x109, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x109, 3)
    EndChrThread(0x8, 0x2)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#04300F#11PLloyd, eh? He looks like\x01",
            "quite the promising\x01",
            "fellow.\x02\x03",
            "#04304FIt seems he even helped\x01",
            "Estelle and Joshua.\x02\x03",
            "#04308FEven still... Despite\x01",
            "his efforts, he was at a\x01",
            "disadvantage this time.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 7100, 0, 2300, 315)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x9,
        "Girl's Voice",
        "...Kevin.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(5300, 1000, 3800, 0)
    MoveCamera(83, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_68(2300, 1000, 7800, 3500)
    SetCameraDistance(16500, 3500)

    def lambda_23E6():
        OP_95(0xFE, 3100, 0, 7300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23E6)
    OP_0D()
    TurnDirection(0x8, 0x9, 500)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x8, 500)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#6P#04302FOh, a little late,\x01",
            "aren't you?\x02\x03",
            "#04305FUmm... What's in the\x01",
            "bag?\x02",
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
        0x9,
        (
            "That little stand over there sells\x01",
            "Altair's specialty, roasted\x01",
            "chestnuts.\x02\x03",
            "Fresh from the oven and exquisitely\x01",
            "sweetened. Really good. Really.\x02",
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
            "#6P#04306FThat's no reason to go\x01",
            "and buy an entire bag of\x01",
            "'em...\x02\x03",
            "#04301FMan. Are you really\x01",
            "going to be ok on your\x01",
            "own?\x02\x03",
            "I could tag along,\x01",
            "y'know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13806F#11P...No. Your reputation is\x01",
            "bad enough as it is,\x01",
            "Kevin.\x02\x03",
            "#13811FIf Archbishop Eralda finds\x01",
            "out that I snuck you in,\x01",
            "he'd burn me at the stake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04305FW-Would he really go THAT far!?\x02\x03",
            "#04308FIt's all thanks to that case with Owen\x01",
            "of the Congregation for Divine\x01",
            "Worship...\x02\x03",
            "#04306FTheir attitude toward the Congregation\x01",
            "for the Sacraments seems to have only\x01",
            "hardened after that incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13803F#11PAnd that's exactly why\x01",
            "it's ideal that I go alone\x01",
            "camouflaged like this.\x02\x03",
            "#13801FYou know that too, right\x01",
            "Kevin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04306FArgh... Fine!\x02\x03",
            "#04308FMan. Why did the grand\x01",
            "master have to pick her\x01",
            "of all people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13804F#11PShe made an appropriate\x01",
            "selection.\x02\x03",
            "#13802FKevin, don't worry too\x01",
            "much while I'm away,\x01",
            "okay?\x02\x03",
            "Caesar and Marcus will\x01",
            "be there, so no need to\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04303FFine, fine, I get it.\x02\x03",
            "#04301F...But really Ries. Be\x01",
            "careful, all right?\x02\x03",
            "To be honest, with where\x01",
            "you're headed, it wouldn't be\x01",
            "strange if something happened.\x02\x03",
            "If shit hits the fan, call me.\x01",
            "I'll be your trump card, all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13805F#11PI know, I know...\x02\x03",
            "#13801F...But is it the\x01",
            "situation really that\x01",
            "bad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04306FYeah... Within the\x01",
            "sacred-profane realm.\x02\x03",
            "#04301FIt seems that "they" have\x01",
            "also started to make\x01",
            "their moves in secret.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30WHeh. Looks like that name\x01",
            "rings true after all...\x01",
            "Crossbell, the Demon City.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    RemoveParty(0x9, 0xFF)
    RemoveParty(0x7, 0xFF)
    SetScenarioFlags(0x25, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1500)
    SetScenarioFlags(0x22, 2)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_419 end

    def Function_4_2BA6(): pass

    label("Function_4_2BA6")

    OP_96(0x16, 0xFFFFBF8C, 0x0, 0x445C, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFFBF8C, 0x30D4, 0x15F90, 0x1388, 0x1)
    OP_96(0x16, 0xFFFFD314, 0x0, 0x5DC, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFFBBA4, 0x5DC, 0x15F90, 0x1388, 0x1)
    OP_96(0x16, 0xFFFF9A70, 0x0, 0xFFFFEE6C, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFF9A70, 0xFFFFDAE4, 0xFFFEA070, 0x1388, 0x1)
    OP_96(0x16, 0xFFFF86E8, 0x0, 0xFFFF88DC, 0x1770, 0x0)
    Return()

    # Function_4_2BA6 end

    def Function_5_2C36(): pass

    label("Function_5_2C36")

    Sleep(5500)
    OP_68(-24960, 1900, -3590, 6000)
    MoveCamera(24, 19, 0, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(24000, 6000)
    OP_6F(0x79)
    Return()

    # Function_5_2C36 end

    def Function_6_2C6A(): pass

    label("Function_6_2C6A")

    OP_95(0x12, 0, 0, -10500, 2000, 0x0)
    OP_95(0x12, 4700, 0, -5400, 2000, 0x0)

    def lambda_2C97():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2C97)
    TurnDirection(0x12, 0xD, 500)
    BeginChrThread(0x12, 0, 0, 0)
    Sleep(1000)
    OP_63(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Return()

    # Function_6_2C6A end

    def Function_7_2CC2(): pass

    label("Function_7_2CC2")

    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_2CE0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2CE0)
    OP_95(0x13, 10500, 0, 6000, 2000, 0x0)
    OP_95(0x13, 10500, 0, -5000, 2000, 0x0)
    OP_9E(0x13, 0x7D0, 0xFFFFEC78, 0x15F90, 0x7D0, 0x1)
    OP_95(0x13, 2000, 0, -30000, 2000, 0x0)
    OP_70(0x0, 0x0)
    Return()

    # Function_7_2CC2 end

    def Function_8_2D42(): pass

    label("Function_8_2D42")

    OP_95(0x14, 12000, 0, 15500, 2000, 0x0)
    OP_95(0x14, 30000, 0, 15500, 2000, 0x0)

    def lambda_2D6F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2D6F)
    Return()

    # Function_8_2D42 end

    def Function_9_2D7C(): pass

    label("Function_9_2D7C")

    OP_92(0xFE, 0xFFFFFE70, 0x2EE0, 0x1F4)
    OP_95(0xFE, -400, 0, 12000, 2000, 0x0)

    def lambda_2DA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DA2)
    OP_95(0xFE, -400, 150, 13500, 1500, 0x0)
    Return()

    # Function_9_2D7C end

    def Function_10_2DC3(): pass

    label("Function_10_2DC3")

    OP_92(0xFE, 0xFFFFFE70, 0x4074, 0x1F4)
    OP_95(0xFE, -400, 0, 16500, 2500, 0x0)
    OP_95(0xFE, -400, 1100, 20500, 2500, 0x0)

    def lambda_2DFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DFD)
    OP_95(0xFE, -400, 1100, 22500, 2500, 0x0)
    Return()

    # Function_10_2DC3 end

    def Function_11_2E1E(): pass

    label("Function_11_2E1E")

    Sleep(100)
    OP_92(0xFE, 0xFFFFFDA8, 0x4074, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -600, 0, 16500, 2500, 0x0)
    OP_95(0xFE, -600, 1100, 20500, 2500, 0x0)

    def lambda_2E5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E5E)
    OP_95(0xFE, -600, 1100, 22500, 2500, 0x0)
    Return()

    # Function_11_2E1E end

    def Function_12_2E7F(): pass

    label("Function_12_2E7F")

    Sleep(2000)
    Sound(467, 0, 80, 0)
    Sleep(200)
    Sound(465, 0, 100, 0)
    Sleep(5300)
    Sound(471, 0, 100, 0)
    Return()

    # Function_12_2E7F end

    def Function_13_2E9B(): pass

    label("Function_13_2E9B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1960, 5600, 11900, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(13600, 0)
    SetChrPos(0x101, 80, 0, 15350, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F0C")
    SetChrPos(0x102, -1100, 0, 15350, 180)
    Jump("loc_2F9F")

    label("loc_2F0C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F32")
    SetChrPos(0x103, -1100, 0, 15350, 180)
    Jump("loc_2F9F")

    label("loc_2F32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F58")
    SetChrPos(0x104, -1100, 0, 15350, 180)
    Jump("loc_2F9F")

    label("loc_2F58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F7E")
    SetChrPos(0x109, -1100, 0, 15350, 180)
    Jump("loc_2F9F")

    label("loc_2F7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F9F")
    SetChrPos(0x105, -1100, 0, 15350, 180)

    label("loc_2F9F")

    SetChrPos(0x1A1, 1150, 0, 15350, 180)
    LoadChrToIndex("chr/ch24100.itc", 0x1E)
    LoadChrToIndex("chr/ch41200.itc", 0x1F)
    LoadChrToIndex("chr/ch31400.itc", 0x20)
    LoadChrToIndex("chr/ch31500.itc", 0x21)
    SetChrChipByIndex(0x18, 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -50, 0, 11950, 0)
    SetChrChipByIndex(0x19, 0x1F)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -840, 0, 11950, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 720, 0, 11950, 0)
    SetChrChipByIndex(0x1B, 0x20)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -20430, 0, 2990, 45)
    SetChrChipByIndex(0x1C, 0x21)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -21600, 0, 2950, 45)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xA, 0x17)
    OP_49()
    SetChrPos(0x17, -500, 0, 8940, 0)
    OP_D5(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    OP_68(-1960, 1900, 11900, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x19,
        (
            "That was great work,\x01",
            "Crossbell Police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "We'll take them into\x01",
            "custody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "T-Thanks for taking care\x01",
            "of this for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Come now, walk briskly.\x02",
    )

    CloseMessageWindow()

    def lambda_31A0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_31A0)

    def lambda_31AD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_31AD)
    Sleep(300)
    OP_93(0x18, 0xB4, 0x1F4)

    def lambda_31C4():
        OP_95(0xFE, -840, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_31C4)

    def lambda_31DE():
        OP_95(0xFE, 720, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_31DE)

    def lambda_31F8():
        OP_95(0xFE, -50, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_31F8)
    WaitChrThread(0x18, 1)
    Sleep(500)
    OP_93(0x18, 0x0, 0x1F4)

    ChrTalk(
        0x18,
        "Y-You guys...\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x18,
        (
            "#5SYou'll pay for this, so\x01",
            "look forward to it!!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x1A, 0x10E, 0x1F4)

    ChrTalk(
        0x1A,
        "Hey, no talking!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1A, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x18,
        (
            "#5SShut up! You damn piece\x01",
            "of shit of a soldier!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x18,
        (
            "#5STreat ladies with more\x01",
            "respect!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "P-Piece of shit!?\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0x5A, 0x1F4)

    ChrTalk(
        0x19,
        (
            "...That's enough, take\x01",
            "her away.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Sound(462, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x169, 0x186, 0x1, 0x8)
    Sleep(1500)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1A, 0x4)
    BeginChrThread(0x18, 1, 0, 15)
    BeginChrThread(0x1A, 1, 0, 16)
    WaitChrThread(0x1A, 1)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x1A, 0x80)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x187, 0x1A4, 0x1, 0x8)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00006FW-What can I say... I\x01",
            "really don't want her to\x01",
            "show up again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_349D")

    ChrTalk(
        0x102,
        "#00106FI agree...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3546")

    label("loc_349D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34C6")

    ChrTalk(
        0x103,
        "#00206FAgreed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3546")

    label("loc_34C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34F0")

    ChrTalk(
        0x104,
        "#00306FI agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3546")

    label("loc_34F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_351C")

    ChrTalk(
        0x109,
        "#10106FI agree...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3546")

    label("loc_351C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3546")

    ChrTalk(
        0x105,
        "#10302FHehe, agreed.\x02",
    )

    CloseMessageWindow()

    label("loc_3546")

    OP_93(0x19, 0x0, 0x1F4)

    ChrTalk(
        0x19,
        (
            "...We intend to deal with\x01",
            "them to make sure they don't\x01",
            "cause any more trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "At any rate, thank you.\x01",
            "Take care on your way\x01",
            "back to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh... Yes, thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0xB4, 0x1F4)
    Sound(462, 0, 100, 0)
    OP_71(0xA, 0xF1, 0x10E, 0x1, 0x8)
    Sleep(1500)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)

    def lambda_363E():
        OP_95(0xFE, -840, 150, 9610, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_363E)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x10F, 0x12C, 0x1, 0x8)
    Sleep(1500)
    Sound(470, 0, 50, 0)
    OP_71(0xA, 0x3C, 0x5A, 0x1, 0x8)
    Sleep(1000)
    Sound(457, 0, 100, 0)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    OP_68(-8150, 1900, 6710, 2500)
    MoveCamera(35, 31, 0, 2500)
    OP_6E(580, 2500)
    SetCameraDistance(18500, 2500)
    BeginChrThread(0x17, 1, 0, 17)
    OP_6F(0x79)
    Sleep(2000)
    StopSound(457, 1000, 90)
    Fade(500)
    EndChrThread(0x17, 0x1)
    SetMapObjFlags(0xA, 0x4)
    OP_68(-810, 1900, 13320, 0)
    MoveCamera(27, 23, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(13600, 0)
    SetChrPos(0x101, -200, 0, 15570, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_374D")
    SetChrPos(0x102, -1040, 0, 14270, 45)
    Jump("loc_37E0")

    label("loc_374D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3773")
    SetChrPos(0x103, -1040, 0, 14270, 45)
    Jump("loc_37E0")

    label("loc_3773")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3799")
    SetChrPos(0x104, -1040, 0, 14270, 45)
    Jump("loc_37E0")

    label("loc_3799")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37BF")
    SetChrPos(0x109, -1040, 0, 14270, 45)
    Jump("loc_37E0")

    label("loc_37BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37E0")
    SetChrPos(0x105, -1040, 0, 14270, 45)

    label("loc_37E0")

    SetChrPos(0x1A1, 750, 0, 14180, 315)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003F*sigh*... In the end, it\x01",
            "turned out like this.\x02\x03",
            "#00001FI would have liked to\x01",
            "arrest her ourselves,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38DF")

    ChrTalk(
        0x102,
        (
            "#00100FYes, but... It couldn't\x01",
            "be helped.\x02\x03",
            "#00104FI'm just glad we didn't\x01",
            "let her get away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2D")

    label("loc_38DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3987")

    ChrTalk(
        0x103,
        (
            "#00200FI understand how you feel,\x01",
            "but... I don't think there's\x01",
            "anything we could have done.\x02\x03",
            "#00204FI'm just glad we didn't let\x01",
            "her get away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2D")

    label("loc_3987")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A03")

    ChrTalk(
        0x104,
        (
            "#00306FI get what you're tryin'\x01",
            "to say...\x02\x03",
            "#00300FWell, I'm just glad we\x01",
            "didn't let her get away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2D")

    label("loc_3A03")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A91")

    ChrTalk(
        0x109,
        (
            "#10106FRight. That is a little\x01",
            "frustrating.\x02\x03",
            "#10100FBut in the end she\x01",
            "didn't get away, so it\x01",
            "turned out all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2D")

    label("loc_3A91")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B2D")

    ChrTalk(
        0x105,
        (
            "#10300FHehe, the fact that she was\x01",
            "captured hasn't changed, so\x01",
            "isn't that all right?\x02\x03",
            "#10304FI'm just glad we didn't let\x01",
            "her get away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B2D")


    ChrTalk(
        0x1A1,
        (
            "Right, right! You really\x01",
            "helped me a lot too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "Maaan, thank goodness, really. With\x01",
            "this, it seems I'll be able to make\x01",
            "a nice report to Inspector Donovan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... That's also\x01",
            "true.\x02\x03",
            "Well then... Shall we\x01",
            "head back to Crossbell\x01",
            "City?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C80")

    ChrTalk(
        0x102,
        (
            "#00100FYes, that's right. We\x01",
            "shouldn't stay here too\x01",
            "long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC1")

    label("loc_3C80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CC5")

    ChrTalk(
        0x103,
        (
            "#00200FRight. We can't stay\x01",
            "here too long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC1")

    label("loc_3CC5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D1E")

    ChrTalk(
        0x104,
        (
            "#00300FI know. Seems we don't\x01",
            "have time to stay here\x01",
            "too long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC1")

    label("loc_3D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D77")

    ChrTalk(
        0x109,
        (
            "#10100FYou're right. It seems\x01",
            "we don't have time to\x01",
            "stay long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC1")

    label("loc_3D77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DC1")

    ChrTalk(
        0x105,
        (
            "#10300FRight. I don't think we\x01",
            "should stay too long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC1")


    ChrTalk(
        0x1A1,
        (
            "Hmm, but we've come such\x01",
            "a long way to the\x01",
            "Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "I wanted to take this\x01",
            "opportunity to go\x01",
            "sightseeing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FP-Please, leave it for\x01",
            "another time...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x0, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x1, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x1A1, 1, 0, 14)
    Sleep(1000)
    OP_68(-18880, 1900, 2270, 5000)
    MoveCamera(41, 24, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(15100, 5000)
    OP_6F(0x79)

    ChrTalk(
        0x1B,
        (
            "This result was beyond\x01",
            "our expectations...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "...Well, we achieved the\x01",
            "minimum goal of not letting\x01",
            "the remnants get away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "For now, let's return\x01",
            "and report to Master\x01",
            "Cao.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Yeah, you're right...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1A1, 0x1)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x1A1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others\x01",
            "waited for the Crossbell-bound\x01",
            "train...\x02\x03",
            "After rebuking Raymond, who was\x01",
            "reluctant to leave the gift shop,\x01",
            "they left the Republic behind.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 6)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_13_2E9B end

    def Function_14_408F(): pass

    label("Function_14_408F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41A7")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_40D2"),
        (1, "loc_40EC"),
        (2, "loc_4106"),
        (3, "loc_4120"),
        (4, "loc_413A"),
        (5, "loc_4154"),
        (6, "loc_416E"),
        (SWITCH_DEFAULT, "loc_4188"),
    )


    label("loc_40D2")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_41A2")

    label("loc_40EC")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_41A2")

    label("loc_4106")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_41A2")

    label("loc_4120")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_41A2")

    label("loc_413A")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_41A2")

    label("loc_4154")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_41A2")

    label("loc_416E")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_41A2")

    label("loc_4188")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_41A2")

    label("loc_41A2")

    Jump("Function_14_408F")

    label("loc_41A7")

    Return()

    # Function_14_408F end

    def Function_15_41A8(): pass

    label("Function_15_41A8")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_41B4():
        OP_96(0xFE, 0xFFFFFFCE, 0x96, 0x258A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41B4)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_15_41A8 end

    def Function_16_41D5(): pass

    label("Function_16_41D5")

    OP_95(0xFE, -50, 0, 10950, 1000, 0x0)

    def lambda_41EE():
        OP_95(0xFE, -50, 150, 9610, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41EE)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_16_41D5 end

    def Function_17_420F(): pass

    label("Function_17_420F")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -500, 0, 8940)
    OP_9F(0x1, -6550, 0, 8940)
    OP_9F(0x1, -7500, 0, 8400)
    OP_9F(0x1, -8100, 0, 7000)
    OP_9F(0x1, -8200, 0, 4200)
    OP_9F(0x1, -8360, 0, -4860)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_17_420F end

    SaveToFile()

Try(main)
