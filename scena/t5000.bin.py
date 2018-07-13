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
        "Function_4_2BCC",         # 04, 4
        "Function_5_2C5C",         # 05, 5
        "Function_6_2C90",         # 06, 6
        "Function_7_2CE8",         # 07, 7
        "Function_8_2D68",         # 08, 8
        "Function_9_2DA2",         # 09, 9
        "Function_10_2DE9",        # 0A, 10
        "Function_11_2E44",        # 0B, 11
        "Function_12_2EA5",        # 0C, 12
        "Function_13_2EC1",        # 0D, 13
        "Function_14_4157",        # 0E, 14
        "Function_15_4270",        # 0F, 15
        "Function_16_429D",        # 10, 16
        "Function_17_42D7",        # 11, 17
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
            "#12P#00004F──Well, then. I'll leave the escort\x01",
            "of those two to you, Mr. Dudley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00600F#5PSure. I'll handle this.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#00603F#5P──Father Kevin.\x01",
            "Allow me to express my gratitude.\x02\x03",
            "#00600FAlthough honestly, I would've preferred\x01",
            "you contacted us beforehand.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E0)
    Sleep(50)

    def lambda_9F0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9F0)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#04306F#11PWell... I really wanted\x01",
            "to do that, but I couldn't.\x02\x03",
            "#04300FWe Gralsritter aren't warmly\x01",
            "welcomed in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00606F#5PI guess it's because of Archbishop Eralda?\x01",
            "He's the head of the Crossbell parish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FAccording to what teacher Marble said before,\x01",
            "you're experts in Thaumaturgy...\x02",
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
            "Archbishop hates us big time.\x02\x03",
            "He pretty much prohibited the\x01",
            "Gralsritter from setting foot into\x01",
            "Crossbell, like, ever again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FArchbishop Eralda...\x02\x03",
            "#10106FI met him once and he looked\x01",
            "like a very strict person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04306F#11PFor being strict, he sure is.\x01",
            "I've never met such a stubborn man.\x02\x03",
            "#04308FWell, because of all the stuff we did,\x01",
            "I hardly blame him for it. But still...\x01",
            "Guess we just gotta play the waiting game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FA-All the stuff you did...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01403FI think only the whitewashing of\x01",
            ""artifacts" counts as inexcusable.\x02\x03",
            "#01402F──Father Kevin.\x01",
            "You really helped us out today.\x02\x03",
            "Once again, thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#04302F#12PHa ha! Mr. Arios, didn't I\x01",
            "owe you a big one anyway?\x02\x03",
            "#04304FWhat I reeeally wanted was to join\x01",
            "you on this trip related to that Cult.\x02\x03",
            "#04311FWell, I don't want to upset the Archbishop,\x01",
            "so please lemme know if you learn something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01404FYes, I'll contact you through\x01",
            "the Guild if I find out something.\x02\x03",
            "#01402F──Lloyd, Master Sergeant Noｱl.\x01",
            "You really did a good job this time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FB9():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FB9)
    Sleep(50)

    def lambda_FC9():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_FC9)
    Sleep(50)
    TurnDirection(0x109, 0x10A, 500)
    Sleep(200)

    ChrTalk(
        0x109,
        (
            "#6P#10112FAhaha, I didn't think I was\x01",
            "particularly useful, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FThat's not true. You really\x01",
            "helped us out today.\x02\x03",
            "#00006F...But I agree that I still\x01",
            "have a long way to go.\x02\x03",
            "#00008FActually, I should've lead\x01",
            "you all until the proper\x01",
            "arrest, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5P#01405FHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00606F#5PHmph, don't be conceited.\x02\x03",
            "#00601FYou too should've bore in mind\x01",
            "that, after all, the official stance\x01",
            "was an arrest by the Support Section.\x02\x03",
            "Moreover, do you think that\x01",
            "you haven't really been useful?\x02",
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
            "#00603F#5PSelf-admonition is ok, but objective self-\x01",
            "evaluation and situation assessment are\x01",
            "required for a first class detective.\x02\x03",
            "#00600FKeep that in mind since you were in\x01",
            "Section One, although for training.\x02",
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
            "#6P#10112FUh uh...\x01",
            "He really doesn't express what he really thinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01404FHmph, you could at least\x01",
            "tell him he did a good job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00610F#5POh, shut up.\x02\x03",
            "#00606F──At any rate, Bannings.\x01",
            "With this, your Section One training is over.\x02\x03",
            "#00602FCombined with the things you learned, you can\x01",
            "make use of it for a new start in the next case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FYes...\x01",
            "Thank you very much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01404FThen, we will\x01",
            "go on ahead.\x02\x03",
            "#01402FI'll be counting on you if there're some\x01",
            "other things we can cooperate on.\x02",
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
        "#6P#10109FThank you for your hard work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04309F#12PBye, stay well!\x02",
    )

    CloseMessageWindow()
    OP_71(0xA, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0xA)
    BeginChrThread(0x10A, 3, 0, 9)
    Sleep(1000)
    BeginChrThread(0x108, 3, 0, 9)
    WaitChrThread(0x108, 3)

    def lambda_1591():

        label("loc_1591")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_1591")

    QueueWorkItem2(0x101, 2, lambda_1591)

    def lambda_15A3():

        label("loc_15A3")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_15A3")

    QueueWorkItem2(0x109, 2, lambda_15A3)

    def lambda_15B5():

        label("loc_15B5")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_15B5")

    QueueWorkItem2(0x8, 2, lambda_15B5)
    OP_71(0xA, 0x14B, 0x168, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0xA)
    Sound(470, 0, 80, 0)
    OP_71(0xA, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0xA)
    Sound(494, 0, 90, 0)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-2000, 1100, 9600, 2000)

    def lambda_1614():
        OP_96(0xFE, 0xFFFFD6FC, 0x0, 0x34BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1614)
    Sleep(2000)
    Sound(457, 0, 100, 0)
    Fade(500)
    EndChrThread(0xA, 0x1)
    SetChrPos(0xA, -15000, 0, 18000, 0)

    def lambda_1651():
        OP_96(0xFE, 0xFFFF3CB0, 0x0, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1651)
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
            "#04309F#11PAren't you two a lucky bunch? \x02\x03",
            "#04311FBeing blessed with such wonderful \x01",
            "mentors despite different professions?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17BA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17BA)
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
            "#6P#10104FThat's right...\x01",
            "Chief Sergei is one too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04300F#11PSo, what's the plan? \x02\x03",
            "Are you taking the train\x01",
            "back the Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, that's the plan.\x02\x03",
            "#00005FThat's right...\x01",
            "Father Kevin, what will you do now?\x02\x03",
            "#00000FIt's only one stop to Crossbell...\x01",
            "I'd like if you could drop by \x01",
            "our place and let us thank you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04306F#11PWell, I appreciate your thoughts, but\x01",
            "I have to meet someone after this.\x02\x03",
            "#04308FActually, I'd want to ask you in\x01",
            "detail about the Cult too, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013F#6PThe D∴G Cult...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FAs I suspected, does the\x01",
            "Church knows something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04306F#11PNope, not a thing.\x02\x03",
            "#04300FThe last time we got involved was\x01",
            "during the incident four years ago.\x02",
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
            "#00005F#6PAfter the simultaneous suppression and\x01",
            "unmasking operation in which all countries\x01",
            "armies and the Guild collaborated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04303F#11PYeah, after that we suppressed a \x01",
            "lodge they didn't have any info about.\x02\x03",
            "#04308F...Just between you and me, it was a lodge that\x01",
            "could be said to be the worst even among the Cult.\x02\x03",
            "#04301FFrankly speaking, they were a bunch of\x01",
            "guys who made crazy rituals with human\x01",
            "experiments more than you could think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P...Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FThey were really...\x01",
            "The lowest of scum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04304F#11PWell, actually, at that time\x01",
            "Mr. Arios helped us really a lot.\x02\x03",
            "#04311FSince I owed him a huge one, it really\x01",
            "helped me that I could aid him this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PI see...\x02\x03",
            "#00004FHowever, thanks to you we could\x01",
            "arrest the culprit still alive.\x02\x03",
            "#00000FThank you very much.\x01",
            "...You really helped us out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04304F#11PNo, no.\x02\x03",
            "#04302FJust like the four eyes said before, it was thanks\x01",
            "to you that we succeeded in a way or another.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PThanks to...me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04304F#11PYeah. What barely saved\x01",
            "that guy were your words.\x01\x02\x03",
            "#04300FIf not for those, even with my treatment,\x01",
            "I probably would've not been able to save him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PIs...that so...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x109,
        (
            "#12P#10109FYes, I'm sure it is!\x02\x03",
            "#10102FIt seemed that because Mr. Lloyd spoke to him\x01",
            "desperately, he was able to get his self back!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00005F#5PMaster Sergeant...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04309F#11PHa ha...\x01",
            "The "Special Support Section", was it?\x02\x03",
            "#04302FLet me hear the details\x01",
            "on another occasion.\x02\x03",
            "With this, the Cult incident\x01",
            "has been settled for now, but\x01",
            "something else could come up.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2173():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2173)
    Sleep(50)
    TurnDirection(0x109, 0x8, 500)

    ChrTalk(
        0x101,
        (
            "#00004F#6PHa ha, I understand.\x02\x03",
            "#00000F...Then, we'll\x01",
            "excuse us now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10109FThank you for your hard work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04311F#11PYeah!\x01",
            "Likewise, thank you too!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(500, 1000, 11400, 4000)

    def lambda_2241():

        label("loc_2241")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2241")

    QueueWorkItem2(0x8, 2, lambda_2241)
    BeginChrThread(0x101, 3, 0, 10)
    BeginChrThread(0x109, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x109, 3)
    EndChrThread(0x8, 0x2)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#04300F#11PLloyd, eh...? Looks like\x01",
            "quite the promising fellow.\x02\x03",
            "#04304FIt seems he even helped\x01",
            "dear Estelle and Joshua.\x02\x03",
            "#04308FStill... Just this time, the\x01",
            "odds were against him.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 7100, 0, 2300, 315)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x9,
        "Girl's Voice",
        "──Kevin.\x02",
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

    def lambda_23BD():
        OP_95(0xFE, 3100, 0, 7300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23BD)
    OP_0D()
    TurnDirection(0x8, 0x9, 500)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x8, 500)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#6P#04302FOoh, aren't you late?\x02\x03",
            "#04305FEhm... What's with the bag?\x02",
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
            "That little stand over there\x01",
            "sells Altair's specialty, \x01",
            "roasted chestnuts.\x02\x03",
            "Dry and nice with an exquisite\x01",
            "sweetness, a nice piece of work\x01",
            "they're.\x02",
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
            "#6P#04306FAnd so that's why you decided\x01",
            "to buy an entire bag of 'em?\x02\x03",
            "#04301FYou really leave me here wondering\x01",
            "whether you'll be fine on your own?\x02\x03",
            "I could tag along, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13806F#11P...No.\x01",
            "Your reputation is bad enough as it is, Kevin.\x02\x03",
            "#13811FIf Archbishop Eralda finds out that you\x01",
            "snuck in, he'd burn you at the stake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04305FW-Would he really\x01",
            "go THAT far!?\x02\x03",
            "#04308FWell, it's all thanks to that case with Owen\x01",
            "of the Congregation for Divine Worship...\x02\x03",
            "#04306FAfter that incident, their attitude toward\x01",
            "the Congregation for the Sacraments seems\x01",
            "to have only hardened more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13803F#11PAnd that is exactly why it's\x01",
            "ideal I go alone camouflaged.\x02\x03",
            "#13801FYou know that too, \x01",
            "right, Kevin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04306FArgh... Fine!\x02\x03",
            "#04308FHonestly, our secretary-general too,\x01",
            "why sending this one of all the people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13804F#11PIt was an appropriate decision.\x02\x03",
            "#13802FYou too Kevin, don't do anything\x01",
            "reckless while I'm not around.\x02\x03",
            "Don't cause worries for\x01",
            "Mr. Cesar and Mr. Marcus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04303FFine, fine. I get it.\x02\x03",
            "#04301F...But Ries.\x01",
            "Really, be careful, ok?\x02\x03",
            "The place where you're headed... Frankly speaking, \x01",
            "it wouldn't be strange if something were to happen.\x02\x03",
            "Call me in case of emergency\x01",
            "and trust on your trump card, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13805F#11PI'll keep that in mind...\x02\x03",
            "#13801F...But is the situation really that bad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04306FYeah... Due to the implication of\x01",
            "both the sacred and profane worlds.\x02\x03",
            "#04301FLooks like "they" also started\x01",
            "to make their moves in secret.\x02",
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
            "#30WThe Demon City, Crossbell──\x01",
            "It could really become like that name says.\x02",
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

    def Function_4_2BCC(): pass

    label("Function_4_2BCC")

    OP_96(0x16, 0xFFFFBF8C, 0x0, 0x445C, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFFBF8C, 0x30D4, 0x15F90, 0x1388, 0x1)
    OP_96(0x16, 0xFFFFD314, 0x0, 0x5DC, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFFBBA4, 0x5DC, 0x15F90, 0x1388, 0x1)
    OP_96(0x16, 0xFFFF9A70, 0x0, 0xFFFFEE6C, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFF9A70, 0xFFFFDAE4, 0xFFFEA070, 0x1388, 0x1)
    OP_96(0x16, 0xFFFF86E8, 0x0, 0xFFFF88DC, 0x1770, 0x0)
    Return()

    # Function_4_2BCC end

    def Function_5_2C5C(): pass

    label("Function_5_2C5C")

    Sleep(5500)
    OP_68(-24960, 1900, -3590, 6000)
    MoveCamera(24, 19, 0, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(24000, 6000)
    OP_6F(0x79)
    Return()

    # Function_5_2C5C end

    def Function_6_2C90(): pass

    label("Function_6_2C90")

    OP_95(0x12, 0, 0, -10500, 2000, 0x0)
    OP_95(0x12, 4700, 0, -5400, 2000, 0x0)

    def lambda_2CBD():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2CBD)
    TurnDirection(0x12, 0xD, 500)
    BeginChrThread(0x12, 0, 0, 0)
    Sleep(1000)
    OP_63(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Return()

    # Function_6_2C90 end

    def Function_7_2CE8(): pass

    label("Function_7_2CE8")

    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_2D06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2D06)
    OP_95(0x13, 10500, 0, 6000, 2000, 0x0)
    OP_95(0x13, 10500, 0, -5000, 2000, 0x0)
    OP_9E(0x13, 0x7D0, 0xFFFFEC78, 0x15F90, 0x7D0, 0x1)
    OP_95(0x13, 2000, 0, -30000, 2000, 0x0)
    OP_70(0x0, 0x0)
    Return()

    # Function_7_2CE8 end

    def Function_8_2D68(): pass

    label("Function_8_2D68")

    OP_95(0x14, 12000, 0, 15500, 2000, 0x0)
    OP_95(0x14, 30000, 0, 15500, 2000, 0x0)

    def lambda_2D95():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2D95)
    Return()

    # Function_8_2D68 end

    def Function_9_2DA2(): pass

    label("Function_9_2DA2")

    OP_92(0xFE, 0xFFFFFE70, 0x2EE0, 0x1F4)
    OP_95(0xFE, -400, 0, 12000, 2000, 0x0)

    def lambda_2DC8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DC8)
    OP_95(0xFE, -400, 150, 13500, 1500, 0x0)
    Return()

    # Function_9_2DA2 end

    def Function_10_2DE9(): pass

    label("Function_10_2DE9")

    OP_92(0xFE, 0xFFFFFE70, 0x4074, 0x1F4)
    OP_95(0xFE, -400, 0, 16500, 2500, 0x0)
    OP_95(0xFE, -400, 1100, 20500, 2500, 0x0)

    def lambda_2E23():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E23)
    OP_95(0xFE, -400, 1100, 22500, 2500, 0x0)
    Return()

    # Function_10_2DE9 end

    def Function_11_2E44(): pass

    label("Function_11_2E44")

    Sleep(100)
    OP_92(0xFE, 0xFFFFFDA8, 0x4074, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -600, 0, 16500, 2500, 0x0)
    OP_95(0xFE, -600, 1100, 20500, 2500, 0x0)

    def lambda_2E84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E84)
    OP_95(0xFE, -600, 1100, 22500, 2500, 0x0)
    Return()

    # Function_11_2E44 end

    def Function_12_2EA5(): pass

    label("Function_12_2EA5")

    Sleep(2000)
    Sound(467, 0, 80, 0)
    Sleep(200)
    Sound(465, 0, 100, 0)
    Sleep(5300)
    Sound(471, 0, 100, 0)
    Return()

    # Function_12_2EA5 end

    def Function_13_2EC1(): pass

    label("Function_13_2EC1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1960, 5600, 11900, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(13600, 0)
    SetChrPos(0x101, 80, 0, 15350, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F32")
    SetChrPos(0x102, -1100, 0, 15350, 180)
    Jump("loc_2FC5")

    label("loc_2F32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F58")
    SetChrPos(0x103, -1100, 0, 15350, 180)
    Jump("loc_2FC5")

    label("loc_2F58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F7E")
    SetChrPos(0x104, -1100, 0, 15350, 180)
    Jump("loc_2FC5")

    label("loc_2F7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FA4")
    SetChrPos(0x109, -1100, 0, 15350, 180)
    Jump("loc_2FC5")

    label("loc_2FA4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FC5")
    SetChrPos(0x105, -1100, 0, 15350, 180)

    label("loc_2FC5")

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
            "Officers of the Crossbell Police,\x01",
            "thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "We'll take them into custody\x01",
            "and bring them in.\x02",
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
        "T-Thank you, and please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Come now, walk briskly.\x02",
    )

    CloseMessageWindow()

    def lambda_31E1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_31E1)

    def lambda_31EE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_31EE)
    Sleep(300)
    OP_93(0x18, 0xB4, 0x1F4)

    def lambda_3205():
        OP_95(0xFE, -840, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3205)

    def lambda_321F():
        OP_95(0xFE, 720, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_321F)

    def lambda_3239():
        OP_95(0xFE, -50, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3239)
    WaitChrThread(0x18, 1)
    Sleep(500)
    OP_93(0x18, 0x0, 0x1F4)

    ChrTalk(
        0x18,
        "Y-You all...\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x18,
        (
            "#5SI'll pay you back for this,\x01",
            "so look forward to it!#3S\x02",
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
        "Come on, no private talks!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1A, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x18,
        (
            "#5SShut up!\x01",
            "You damn piece of shit of a soldier!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x18,
        (
            "#5SYou must treat ladies\x01",
            "with more courtesy!#3S\x02",
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
        "...Enough, take her away.\x02",
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
            "#00006FW-What can I say...\x01",
            "I don't really want to meet her again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34ED")

    ChrTalk(
        0x102,
        "#00106FI agree...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3598")

    label("loc_34ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3516")

    ChrTalk(
        0x103,
        "#00206FAgreed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3598")

    label("loc_3516")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3541")

    ChrTalk(
        0x104,
        "#00306FI agree. \x02",
    )

    CloseMessageWindow()
    Jump("loc_3598")

    label("loc_3541")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_356D")

    ChrTalk(
        0x109,
        "#10106FI agree...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3598")

    label("loc_356D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3598")

    ChrTalk(
        0x105,
        "#10302FHu hu, agreed.\x02",
    )

    CloseMessageWindow()

    label("loc_3598")

    OP_93(0x19, 0x0, 0x1F4)

    ChrTalk(
        0x19,
        (
            "...We intend to deal with the matter properly,\x01",
            "so that such a thing doesn't happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "At any rate, thank you. You too,\x01",
            "be careful when going back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAh...yes, thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0xB4, 0x1F4)
    Sound(462, 0, 100, 0)
    OP_71(0xA, 0xF1, 0x10E, 0x1, 0x8)
    Sleep(1500)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)

    def lambda_3696():
        OP_95(0xFE, -840, 150, 9610, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3696)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37A5")
    SetChrPos(0x102, -1040, 0, 14270, 45)
    Jump("loc_3838")

    label("loc_37A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37CB")
    SetChrPos(0x103, -1040, 0, 14270, 45)
    Jump("loc_3838")

    label("loc_37CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37F1")
    SetChrPos(0x104, -1040, 0, 14270, 45)
    Jump("loc_3838")

    label("loc_37F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3817")
    SetChrPos(0x109, -1040, 0, 14270, 45)
    Jump("loc_3838")

    label("loc_3817")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3838")
    SetChrPos(0x105, -1040, 0, 14270, 45)

    label("loc_3838")

    SetChrPos(0x1A1, 750, 0, 14180, 315)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003F*sigh*...\x01",
            "In the end, it turned out like this.\x02\x03",
            "#00001FAt least I would've liked to arrest her\x01",
            "with our hands, in a way or another.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3968")

    ChrTalk(
        0x102,
        (
            "#00100FYes, but...\x01",
            "It couldn't be helped.\x02\x03",
            "#00104FWe must consider a good thing even\x01",
            "only that she didn't run away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD8")

    label("loc_3968")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A0A")

    ChrTalk(
        0x103,
        (
            "#00200FI understand how you feel, but...\x01",
            "It couldn't be helped.\x02\x03",
            "#00204FLet's consider a good thing even\x01",
            "only that she didn't run away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD8")

    label("loc_3A0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A9C")

    ChrTalk(
        0x104,
        (
            "#00306FI can get you\x01",
            "sayin' that, but...\x02\x03",
            "#00300FWell, let's consider a good thing\x01",
            "even only that she didn't flee, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD8")

    label("loc_3A9C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B25")

    ChrTalk(
        0x109,
        (
            "#10106FYou're right...\x01",
            "It's a bit regrettable.\x02\x03",
            "#10100F...However, it ended\x01",
            "all right since she\x01",
            "didn't escape.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD8")

    label("loc_3B25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BD8")

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, the fact that she was\x01",
            "captured doesn't change, so\x01",
            "isn't it all right?\x02\x03",
            "#10304FWe must consider a good thing even\x01",
            "only that she didn't run away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD8")


    ChrTalk(
        0x1A1,
        (
            "Right, right!\x01",
            "You really helped me too a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "Maaan, thank goodness, really.\x01",
            "With this, it seems I can do a\x01",
            "nice report to Inspector Donovan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha...\x01",
            "That's also true.\x02\x03",
            "Well then...\x01",
            "Shall we go back\x01",
            "to Crossbell City?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D28")

    ChrTalk(
        0x102,
        (
            "#00100FYes, that's right.\x01",
            "Overstaying here maybe\x01",
            "is not a good idea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E82")

    label("loc_3D28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D71")

    ChrTalk(
        0x103,
        (
            "#00200FRight.\x01",
            "We can't overstay\x01",
            "here too much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E82")

    label("loc_3D71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DCB")

    ChrTalk(
        0x104,
        (
            "#00300FI know.\x01",
            "Seems we don't have the\x01",
            "time to overstay at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E82")

    label("loc_3DCB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E31")

    ChrTalk(
        0x109,
        (
            "#10100FYou're right. \x01",
            "It seems we don't have the\x01",
            "time to overstay too much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E82")

    label("loc_3E31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E82")

    ChrTalk(
        0x105,
        (
            "#10300FRight.\x01",
            "I don't think it's good\x01",
            "to overstay too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E82")


    ChrTalk(
        0x1A1,
        (
            "Uhhm, but since we've come\x01",
            "all the way to the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "With the occasion, I'd like\x01",
            "to go sightsee somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FP-Please leave it for another time...\x02",
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
            "This kind of conclusion was\x01",
            "beyond our expectations...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "...Well, we achieved the\x01",
            "minimum goal of not let\x01",
            "get away the remnants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "For now, let's return to\x01",
            "report to Master Cao.\x02",
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
            "Afterwards, Lloyd and the others waited\x01",
            "for the Crossbell-bound train...\x02\x03",
            "After rebuking Raymond, reluctant to part from \x01",
            "the gift shop, they left the Republic behind.\x07\x00\x02",
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

    # Function_13_2EC1 end

    def Function_14_4157(): pass

    label("Function_14_4157")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_426F")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_419A"),
        (1, "loc_41B4"),
        (2, "loc_41CE"),
        (3, "loc_41E8"),
        (4, "loc_4202"),
        (5, "loc_421C"),
        (6, "loc_4236"),
        (SWITCH_DEFAULT, "loc_4250"),
    )


    label("loc_419A")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_426A")

    label("loc_41B4")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_426A")

    label("loc_41CE")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_426A")

    label("loc_41E8")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_426A")

    label("loc_4202")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_426A")

    label("loc_421C")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_426A")

    label("loc_4236")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_426A")

    label("loc_4250")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_426A")

    label("loc_426A")

    Jump("Function_14_4157")

    label("loc_426F")

    Return()

    # Function_14_4157 end

    def Function_15_4270(): pass

    label("Function_15_4270")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_427C():
        OP_96(0xFE, 0xFFFFFFCE, 0x96, 0x258A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_427C)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_15_4270 end

    def Function_16_429D(): pass

    label("Function_16_429D")

    OP_95(0xFE, -50, 0, 10950, 1000, 0x0)

    def lambda_42B6():
        OP_95(0xFE, -50, 150, 9610, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_42B6)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_16_429D end

    def Function_17_42D7(): pass

    label("Function_17_42D7")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -500, 0, 8940)
    OP_9F(0x1, -6550, 0, 8940)
    OP_9F(0x1, -7500, 0, 8400)
    OP_9F(0x1, -8100, 0, 7000)
    OP_9F(0x1, -8200, 0, 4200)
    OP_9F(0x1, -8360, 0, -4860)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_17_42D7 end

    SaveToFile()

Try(main)
