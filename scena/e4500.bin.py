from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4500.bin",                # FileName
        "e4500",                    # MapName
        "e4500",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4500",                  # 0
        "Jona's Voice",           # 1
        "地形",                   # 2
        "水面",                   # 3
        "SE制御",                 # 4
    ))

    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(296, 0)                                        # 0

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_160",          # 01, 1
        "Function_2_161",          # 02, 2
        "Function_3_98C",          # 03, 3
        "Function_4_9CA",          # 04, 4
        "Function_5_1519",         # 05, 5
        "Function_6_154C",         # 06, 6
        "Function_7_2E03",         # 07, 7
        "Function_8_2F01",         # 08, 8
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_13C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_15F")

    label("loc_13C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_150")
    ClearScenarioFlags(0x22, 1)
    Event(0, 4)
    Jump("loc_15F")

    label("loc_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_15F")
    ClearScenarioFlags(0x22, 2)
    Event(0, 6)

    label("loc_15F")

    Return()

    # Function_0_128 end

    def Function_1_160(): pass

    label("Function_1_160")

    Return()

    # Function_1_160 end

    def Function_2_161(): pass

    label("Function_2_161")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map/mprain00.eff")
    LoadChrToIndex("chr/ch02902.itc", 0x1E)
    SoundLoad(483)
    SoundLoad(126)
    SetChrPos(0x101, -950, 210, -1600, 180)
    SetChrPos(0x109, 0, 210, -1750, 180)
    SetChrPos(0x102, 950, 210, -1600, 180)
    SetChrPos(0x105, 800, 900, 0, 180)
    SetChrPos(0x103, -1130, 900, -660, 180)
    SetChrPos(0x104, -70, 900, 360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    SetChrPos(0x9, 0, 0, 0, 180)
    OP_D5(0x9, 0x0, 0x2BF20, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 0, 180)
    OP_D5(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x1, 0x5A)
    OP_71(0x1, 0x3E8, 0x7CF, 0x0, 0x20)
    PlayBGM("ed7151", 0)
    BeginChrThread(0xB, 1, 0, 3)
    PlayEffect(0x0, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x9C4)
    OP_11(0x95, 0xA0, 0xB5, 0x1E, 0x190, 0x9C4)
    Sound(128, 1, 50, 0)
    OP_68(-770, 3300, -4220, 0)
    MoveCamera(150, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(28820, 0)
    FadeToBright(1000, 0)
    OP_68(-1940, 4000, 9830, 6500)
    MoveCamera(172, -3, 0, 6500)
    OP_6E(650, 6500)
    SetCameraDistance(21530, 6500)
    Sleep(4500)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    OP_11(0xB7, 0xDA, 0xDD, 0x1E, 0x190, 0x9C4)
    StopSound(128, 1000, 100)
    Sleep(500)
    StopEffect(0x7, 0x2)
    OP_6F(0x79)
    Sleep(1500)
    OP_68(-1080, 2150, -2460, 0)
    MoveCamera(44, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00203F#5PIt cleared up this\x01",
            "afternoon, just as\x01",
            "forecasted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PIt might be Aidios'\x01",
            "guidance.\x02\x03",
            "#00301FHonestly, we have no\x01",
            "idea what kind of danger\x01",
            "is waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PWell, it's definitely\x01",
            "better than an\x01",
            "investigation in the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5P...Is possible that it's\x01",
            "a Cryptid, or\x01",
            "possibly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PHonestly, anything is\x01",
            "possible given the\x01",
            "current situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PWe don't know when Arios' team is\x01",
            "getting here either.\x02\x03",
            "#00008FAs the vanguard team, we need to\x01",
            "do everything we can to guarantee\x01",
            "Ling and Eolia's safety.\x02\x03",
            "#00001FDepending on the situation... We\x01",
            "might even need to call the CGF\x01",
            "for backup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5P...Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PLing and Eolia... I hope\x01",
            "they're all right.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00205F#5P...This is...\x02\x03",
            "#00207FSudden increase in\x01",
            "humidity confirmed. Be\x01",
            "careful!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_721():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_721)
    Sleep(50)

    def lambda_731():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_731)
    Sleep(50)

    def lambda_741():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_741)
    Sleep(50)

    def lambda_751():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_751)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00011F#5PWhat...!?\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1F40)
    OP_7D(0xC0, 0xE0, 0xFF, 0x0, 0xAF0)
    OP_11(0x90, 0xB0, 0xD0, 0x1, 0x32, 0xAF0)
    Sleep(500)
    OP_68(-2630, 2150, -3190, 3000)
    MoveCamera(51, 12, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(19410, 3000)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x105,
        "#10301F#6PThis is... fog!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#6PB-But, it was clear just\x01",
            "a moment ago!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#5PL-Lloyd... What do we\x01",
            "do!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#5PUgh...\x02\x03",
            "#00007FReduce speed and proceed\x01",
            "with caution!\x02\x03",
            "Tio, can you sense the\x01",
            "approaching shore!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#5PYes, I think so!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#5PIf it's gonna be like\x01",
            "this, we need to be\x01",
            "ready for anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_11(0x90, 0xB0, 0xD0, 0x1, 0x1E, 0xAF0)
    SetCameraDistance(20410, 2800)
    Sleep(800)
    StopSound(126, 2000, 50)
    StopSound(483, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x105, 0x4)
    WaitBGM()
    OP_24(0x7E)
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 0)
    NewScene("m4200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_161 end

    def Function_3_98C(): pass

    label("Function_3_98C")

    Sound(126, 2, 50, 0)
    Sound(483, 2, 20, 0)
    Sleep(200)
    OP_25(0x1E3, 0x1E)
    Sleep(200)
    OP_25(0x1E3, 0x28)
    Sleep(200)
    OP_25(0x1E3, 0x32)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Sleep(200)
    OP_25(0x1E3, 0x46)
    Sleep(200)
    OP_25(0x1E3, 0x50)
    Sleep(200)
    OP_25(0x1E3, 0x5A)
    Return()

    # Function_3_98C end

    def Function_4_9CA(): pass

    label("Function_4_9CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02902.itc", 0x1E)
    SoundLoad(483)
    SoundLoad(126)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis265.itp")
    SetChrPos(0x101, -800, 210, -1600, 180)
    SetChrPos(0x109, 0, 210, -1750, 180)
    SetChrPos(0x102, 950, 210, -1600, 180)
    SetChrPos(0x105, -1100, 780, 1450, 180)
    SetChrPos(0x103, 300, 780, 450, 180)
    SetChrPos(0x104, 900, 780, 1250, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    PlayBGM("ed7560", 0)
    BeginChrThread(0xB, 1, 0, 5)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 0, 180)
    OP_74(0x1, 0x5A)
    OP_71(0x1, 0x7CF, 0x3E8, 0x0, 0x20)
    OP_68(250, 2150, 10000, 0)
    MoveCamera(345, 138, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(106500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 2150, 5750, 3000)
    SetCameraDistance(88650, 3000)
    OP_0D()
    Sleep(1500)
    OP_68(1470, 2150, -5770, 0)
    MoveCamera(320, 175, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(34500, 0)
    Fade(1000)
    OP_68(20, 2150, -4920, 4500)
    MoveCamera(332, 175, 0, 4500)
    SetCameraDistance(22000, 4500)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-810, 2150, 460, 0)
    MoveCamera(327, 158, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00106F#5P...I can't believe it.\x01",
            "To think Yin's true\x01",
            "identity was Rixia...\x02\x03",
            "#00108FI was sure he was a man\x01",
            "this whole time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PIt seems she can change\x01",
            "her presence when she is\x01",
            "in that form.\x02\x03",
            "#10301FIt's possible that she's\x01",
            "changing the shape of\x01",
            "her body as well.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(250)

    ChrTalk(
        0x109,
        (
            "#10111F#5PI-Is that something a normal\x01",
            "human can do?\x02\x03",
            "#10106F...But, it seems like we've been\x01",
            "running into people who are\x01",
            "anything but normal lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PIt's possible that our mental\x01",
            "stress during those times\x01",
            "played a role too, but...\x02\x03",
            "#00200FYou're not as surprised as I\x01",
            "thought you'd be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PNo, I'm not.\x02\x03",
            "#00008FI had a chance to speak\x01",
            "with Rixia not too long\x01",
            "ago...\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x1E3, 0x32)
    OP_25(0x7E, 0x14)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_25(0x1E3, 0x28)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "Ever since I was little...\x01",
            "I lived for that reason.\x02\x03",
            "The path my ancestors have\x01",
            "inherited for as long as\x01",
            "anyone can remember...\x02\x03",
            "Even now, I do not know\x01",
            "the reason I walk this\x01",
            "path.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x1E3, 0x32)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Sleep(200)
    OP_25(0x1E3, 0x46)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00006F#5P─I thought it couldn't be,\x01",
            "and never thought anything\x01",
            "more about it, but...\x02\x03",
            "#00001FSomehow, I never really\x01",
            "threw away the possibility\x01",
            "that she could be Yin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#5PI see...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#00306F#6P...Now that I think about it,\x01",
            "there's no way an amateur could be\x01",
            "selected as Arc-en-Ciel co-star.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah. The story about being forced\x01",
            "into it by Ilya and given intensive\x01",
            "training was oddly persuasive, though.\x02\x03",
            "#00008FAnd the time when Yin appeared and the\x01",
            "time Rixia arrived in Crossbell are\x01",
            "almost exactly the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PI wonder if Cao and his\x01",
            "men in Heiyue know her\x01",
            "real identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell given her position,\x01",
            "it'd be normal to keep\x01",
            "that secret.\x02\x03",
            "#10300FIf they knew, nothing\x01",
            "good would come of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PGiven that, it might be\x01",
            "best if we keep her\x01",
            "identity a secret, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah. Chief aside, let's\x01",
            "wait and see for a\x01",
            "while.\x02\x03",
            "#00013FAnd... Right now, Red\x01",
            "Constellation takes\x01",
            "priority over Heiyue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PYeah...\x02\x03",
            "#00301F─Uncle and the others have\x01",
            "disappeared. They're acting as if\x01",
            "their preparations are complete.\x02\x03",
            "They'll probably strike without\x01",
            "warning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#5PLooks like I need to\x01",
            "contact Commander Sonya\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-180, 2150, 7610, 3500)
    MoveCamera(327, 164, 0, 3500)
    OP_6E(950, 3500)
    SetCameraDistance(13010, 3500)
    Sleep(1500)
    StopSound(126, 3000, 50)
    StopSound(483, 3000, 70)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM(-1, -1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x7E)
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 0)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_9CA end

    def Function_5_1519(): pass

    label("Function_5_1519")

    Sound(126, 2, 50, 0)
    Sound(483, 2, 20, 0)
    Sleep(400)
    OP_25(0x1E3, 0x1E)
    Sleep(400)
    OP_25(0x1E3, 0x28)
    Sleep(300)
    OP_25(0x1E3, 0x32)
    Sleep(300)
    OP_25(0x1E3, 0x3C)
    Sleep(300)
    OP_25(0x1E3, 0x46)
    Sleep(300)
    Return()

    # Function_5_1519 end

    def Function_6_154C(): pass

    label("Function_6_154C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("chr/ch00302.itc", 0x1F)
    SoundLoad(483)
    SoundLoad(126)
    SoundLoad(803)
    SoundLoad(894)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    LoadEffect(0x0, "event\\ev315_00.eff")
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 800, 900, -100, 180)
    SetChrPos(0x102, -800, 900, 100, 180)
    SetChrPos(0x103, 100, 900, 1000, 180)
    SetChrPos(0x104, 0, 420, -1750, 180)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    SetChrPos(0x9, 0, 0, 0, 180)
    OP_D5(0x9, 0x0, 0x2BF20, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 0, 180)
    OP_D5(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x1, 0x5A)
    OP_71(0x1, 0x3E8, 0x7CF, 0x0, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 700, 300, -100, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x104, 0, 0, 7)
    OP_F0(0x0, 0xA)
    OP_F0(0x1, 0x1F4)
    OP_68(0, 1800, -10000, 0)
    MoveCamera(25, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    BeginChrThread(0xB, 1, 0, 3)
    FadeToBright(1000, 0)
    OP_68(0, 1800, 40000, 9000)
    MoveCamera(155, 10, 0, 5000)
    SetCameraDistance(24000, 5000)
    Sleep(7000)
    OP_0D()
    Fade(1000)
    OP_68(-20, 1800, -110, 0)
    MoveCamera(126, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18500, 2500)
    SetChrPos(0x104, 0, 420, -1450, 180)
    BeginChrThread(0x104, 1, 0, 8)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00001F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PThank goodness were were\x01",
            "able to secure a police\x01",
            "boat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6P...Looks like Michelam\x01",
            "is totally blockaded.\x02\x03",
            "#00201FThe resident theme park\x01",
            "and shop staff were\x01",
            "evacuated too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PThey might've headed for\x01",
            "those Marshlands...\x02\x03",
            "#00301FNo, I'm sure Michelam is\x01",
            "the right answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PElie... Did you hear\x01",
            "anything from Mariabell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PNo. I've haven't been able to\x01",
            "contact her for the past few\x01",
            "days.\x02\x03",
            "#00108FIt seems she's been busy dealing\x01",
            "with the aftermath of the\x01",
            "destroyed IBC building, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#00303F#5PThat young lady aside...\x02\x03",
            "#00301FWhat Lechter and Kilika\x01",
            "were implying, is it\x01",
            "true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PThen the real mastermind\x01",
            "behind the attack on Crossbell\x01",
            "isn't the Erebonian Empire...\x02\x03",
            "#00201FIt was Mayor... No, President\x01",
            "Dieter Crois.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#5P............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00106F#12PLloyd, you don't need to\x01",
            "worry about me.\x02\x03",
            "#00108F"Uncle" hasn't been\x01",
            "answering my calls since\x01",
            "yesterday but...\x02\x03",
            "#00101FHis butler Helmer may be\x01",
            "locked up in Orchis\x01",
            "Tower...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#00005F#5P...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6P...That would be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PDoesn't that make him\x01",
            "totally guilty...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#5P─Mayor Dieter was the mastermind\x01",
            "behind this chain of incidents...\x02\x03",
            "If you assume that, everything falls\x01",
            "into place, doesn't it.\x02\x03",
            "#00008FIn that case, he's not employing Red\x01",
            "Constellation and Ouroboros, they're\x01",
            "compatriots!\x02\x03",
            "#00013FWald's demonization too... Depending\x01",
            "on the situation, Ouroboros might\x01",
            "have just been using him.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00107F#12PThe D∴G Cult too!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PWald aside... Even\x01",
            "Joachim!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PNo way... But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PThe chance of a direct link\x01",
            "is low, of course.\x02\x03",
            "Based on Joachim's words\x01",
            "and actions, there was no\x01",
            "sign of another mastermind.\x02\x03",
            "#00001FHowever, it's possible he\x01",
            "was being used without even\x01",
            "knowing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#6P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PNow that you mention it, we never\x01",
            "did identify the person who\x01",
            "kidnapped KeA from the Fort of Sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#5PNor the person who\x01",
            "inserted KeA into the\x01",
            "Schwarz Auktion.\x02\x03",
            "#00301FThinking about it,\x01",
            "nobody normal could have\x01",
            "pulled that stunt.\x02\x03",
            "It would have to be\x01",
            "someone on the level of\x01",
            "Yin or Ouroboros...\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013FYes! Special Support\x01",
            "Section, Lloyd speaking!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, I got through!\x02\x03",
            "I want Tio to hear this\x01",
            "too, so switch to the\x01",
            "special mode!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FJona? Understood,\x01",
            "switching now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(804, 0, 100, 0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x101, 0x6)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x103,
        "#00201F#6PJona, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SWhat isn't wrong!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SThere's an terrible\x01",
            "monster lurking in\x01",
            "Crossbell's orbal net!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#5PA monster?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PW-What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SAt first I found some\x01",
            "weird data structures on\x01",
            "the edge of the network.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SIt was a cryptic\x01",
            "arrangement so I thought\x01",
            "it was simple junk, but...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SThe more I look at it, the more\x01",
            "it seems like an evolution code\x01",
            "created by those Ouroboros guys!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PAstral Code...\x02\x03",
            "#00201FIn other words, some\x01",
            "kind of trap set by\x01",
            "Ouroboros?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SNo, based on its date,\x01",
            "it was created around\x01",
            "five years ago!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SThat was around when the\x01",
            "orbal net was first\x01",
            "introduced, right!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#6PYes, indeed...\x02\x03",
            "#00201F...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12PThe ones who proposed introducing\x01",
            "the orbal net in Crossbell was\x01",
            "none other than the IBC Group...\x02\x03",
            "#00108FThanks to that, IBC had a strong\x01",
            "influence on the technology the\x01",
            "foundation introduced...\x02\x03",
            "#00110FThey even had full knowledge of\x01",
            "the network core...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#5PWhoa, then that means...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5P─Jona. What about that\x01",
            "monster?\x02\x03",
            "#00001FWhat will happen because\x01",
            "of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SI-I'm analyzing that\x01",
            "now, but...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SI'm certain it's a gargantuan\x01",
            "system that extends across\x01",
            "the whole of the orbal net!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SAnd it looks like it's\x01",
            "using it to prepare its\x01",
            "real system!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PReal system?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PReal meaning something\x01",
            "outside the orbal net?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SYeah, in all Geofront\x01",
            "divisions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SOrchis Tower ties them all\x01",
            "together. It looks like there's\x01",
            "even a linkage to Michelam!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#5PMichelam!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#5PWhy'd that name have to\x01",
            "come up now!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S─Anyway! I'll call you\x01",
            "again once my analysis\x01",
            "is complete!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SI don't know what's\x01",
            "waiting out there for you\x01",
            "guys, but be careful, ok!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(813, 0, 70, 0)
    Sleep(200)
    Sound(894, 2, 80, 0)
    Sleep(100)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    StopSound(894, 2000, 70)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#00306F#5PWhoa. This is all way\x01",
            "too connected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PWe don't know what the system\x01",
            "might be for at present, but...\x02\x03",
            "#00208FIf we think about someone outside\x01",
            "the foundation or Ouroboros who\x01",
            "could build such a huge system...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5P─Let's continue toward\x01",
            "Michelam.\x02\x03",
            "#00013FKeA, and Arios too... All\x01",
            "the answers are probably\x01",
            "waiting for us there.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1800, -3000, 3000)

    def lambda_2D25():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D25)
    Sleep(50)

    def lambda_2D35():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D35)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    Sleep(1000)
    EndChrThread(0x104, 0x1)
    Fade(1000)
    OP_68(0, 1800, -20000, 0)
    MoveCamera(180, 15, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(18500, 0)
    OP_68(0, 3800, 40000, 10000)
    MoveCamera(180, 0, 0, 7000)
    Sleep(5000)
    StopSound(126, 3000, 50)
    StopSound(483, 3000, 90)
    Sleep(2000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7565", "ed7561")
    ReplaceBGM("ed7160", "ed7561")
    OP_24(0x323)
    OP_24(0x37E)
    SetScenarioFlags(0x22, 1)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_154C end

    def Function_7_2E03(): pass

    label("Function_7_2E03")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F00")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E5C")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("loc_2EFB")

    label("loc_2E5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EAA")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_2EFB")

    label("loc_2EAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF8")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(166)
    Jump("loc_2EFB")

    label("loc_2EF8")

    Sleep(233)

    label("loc_2EFB")

    Jump("Function_7_2E03")

    label("loc_2F00")

    Return()

    # Function_7_2E03 end

    def Function_8_2F01(): pass

    label("Function_8_2F01")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F39")
    OP_82(0x0, 0xF, 0x1388, 0x3E8)
    Sleep(1000)
    OP_82(0x0, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("Function_8_2F01")

    label("loc_2F39")

    Return()

    # Function_8_2F01 end

    SaveToFile()

Try(main)
