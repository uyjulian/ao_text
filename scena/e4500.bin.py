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
        "Function_3_9CB",          # 03, 3
        "Function_4_A09",          # 04, 4
        "Function_5_15E7",         # 05, 5
        "Function_6_161A",         # 06, 6
        "Function_7_2FC2",         # 07, 7
        "Function_8_30C0",         # 08, 8
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
            "#00203F#5P...It cleared up this afternoon,\x01",
            "just as forecasted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PThis too could be the\x01",
            "Goddess' guidance.\x02\x03",
            "#00301FHonestly, we have no idea what\x01",
            "kind of danger is waitin' for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PWell, it's definitely better than\x01",
            "an investigation in the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5P...It's possible that there's\x01",
            "a "Cryptid", or maybe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PHonestly, anything is possible\x01",
            "given the current situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...We don't know when Mr. Arios and\x01",
            "the others are getting here either.\x02\x03",
            "#00008FAs the vanguard team, we need to\x01",
            "do everything we can to guarantee \x01",
            "Miss Ling and Miss Eolia's safety.\x02\x03",
            "#00001FDepending on the situation...\x01",
            "We might even need to call\x01",
            "the CGF for backup.\x02",
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
            "#00301F#5PThose girls... \x01",
            "I hope they're all right.\x02",
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
            "#00207FSudden increase in humidity confirmed. \x01",
            "Please be careful...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_758():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_758)
    Sleep(50)

    def lambda_768():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_768)
    Sleep(50)

    def lambda_778():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_778)
    Sleep(50)

    def lambda_788():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_788)
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
        "#10301F#6PThis is...fog!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#6PB-But, it was so clear\x01",
            "just moments ago!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#5PMr. L-Lloyd... What do we do!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#5PUgh...\x02\x03",
            "#00007FReduce speed and\x01",
            "proceed with caution!\x02\x03",
            "Tio, can you sense the\x01",
            "approaching shore!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#5PYes, somehow...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#5PConsidering the situation,\x01",
            "we need to be ready for anything...!\x02",
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

    def Function_3_9CB(): pass

    label("Function_3_9CB")

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

    # Function_3_9CB end

    def Function_4_A09(): pass

    label("Function_4_A09")

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
            "#00106F#5P...Who could have imagined that "Yin"'s\x01",
            "true identity would turn out to be Rixia...\x02\x03",
            "#00108FI was sure he was a\x01",
            "man this whole time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PIt seems that when she appears in that form, \x01",
            "she can change her presence.\x02\x03",
            "#10301FIt's possible that she's changing\x01",
            "the shape of her body as well.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(250)

    ChrTalk(
        0x109,
        (
            "#10111F#5PI-Is that something a\x01",
            "normal human can do?\x02\x03",
            "#10106F...Wait, it seems like we've been running into\x01",
            "humans who're anything but normal lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PIt is possible that our mental stress during\x01",
            "those times played a role too, but...\x02\x03",
            "#00200FYou aren't as surprised\x01",
            "as I thought, Mr. Lloyd...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...Yeah, that's right.\x02\x03",
            "#00008FI had a chance to speak with\x01",
            "Rixia not too long ago...\x02",
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
            "...Since I was a child...\x01",
            "I've been living for that.\x02\x03",
            "A path my ancestors inherited\x01",
            "since way, way in the past...\x02\x03",
            "A path I currently don't know\x01",
            "for what reason to walk on.\x07\x00\x02",
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
            "#00006F#5P──I thought it couldn't be, and never\x01",
            "thought anything more about it, but...\x02\x03",
            "#00001FSomehow, I never really threw away\x01",
            "the possibility that she could be "Yin".\x02",
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
            "selected as an Arc-en-ciel co-star.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah. The story about being forced\x01",
            "into it by Miss Ilya and given intensive\x01",
            "training was oddly persuasive, though.\x02\x03",
            "#00008FAnd the time when "Yin" appeared and\x01",
            "the time Rixia arrived in Crossbell\x01",
            "are almost exactly the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PI wonder if Mr. Cao of the "Heiyue"\x01",
            "knows her real identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, given her position, she'd want to\x01",
            "keep that secret as much as possible.\x02\x03",
            "#10300FIf she carelessly made her lineage known,\x01",
            "it could only be used for their good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5P...In that sense, it's better\x01",
            "if we don't tell her real\x01",
            "identity around too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah, aside to the Chief.\x01",
            "We'll watch the situation for a while.\x02\x03",
            "#00013FAnd... Right now, the "Red Constellation"\x01",
            "takes priority over the "Heiyue".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PYeah...\x02\x03",
            "#00301F──Uncle and the others have\x01",
            "disappeared. They're acting as if\x01",
            "their preparations are complete.\x02\x03",
            "They'll probably strike without warning.\x02",
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
            "#10101F#5P...Looks like we also need to\x01",
            "contact Commander Sonya.\x02",
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

    # Function_4_A09 end

    def Function_5_15E7(): pass

    label("Function_5_15E7")

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

    # Function_5_15E7 end

    def Function_6_161A(): pass

    label("Function_6_161A")

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
            "#00106F#6PI'm glad we could somehow\x01",
            "secure a police boat, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6P...It seems that Michelam has\x01",
            "been completely sealed off.\x02\x03",
            "#00201FThe theme park's and all\x01",
            "the shops' staff have left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PThere was also the possibility they\x01",
            "went to the Marshlands, but...\x02\x03",
            "#00301FWell, Michelam was the\x01",
            "right choice, without a doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PElie...\x01",
            "Were you able to reach\x01",
            "Miss Mariabell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P...No. I couldn't get hold\x01",
            "of her in the last days.\x02\x03",
            "#00108FDue to the measures for the blown up\x01",
            "IBC building, it seems she's busy...\x02",
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
            "#00303F#5PLeavin' aside that young lady...\x02\x03",
            "#00301FThe hint that Lechter jerk and Miss Kilika\x01",
            "have dropped on us...is it true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PThe true wirepuller of the Crossbell\x01",
            "raid is not the Erebonian Empire, but...\x02\x03",
            "#00201FThe Mayor, Dieter Crois... I mean,\x01",
            "the President. Is that possible?\x02",
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
            "#00106F#12P......Lloyd.\x01",
            "You don't need to worry about me.\x02\x03",
            "#00108FI haven't been able to contact\x01",
            "grandfather since yesterday...\x02\x03",
            "#00101FAccording to our butler, Mr. Helmer,\x01",
            "it could be that he has been\x01",
            "restrained at Orchis Tower...\x02",
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
        "#00306F#5PDoesn't that make him totally guilty...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#5P──Mayor Dieter is the wirepuller\x01",
            "of this series of incidents...\x02\x03",
            "For sure, if we think like that,\x01",
            "everything is coherent.\x02\x03",
            "#00008FIn that case, the "Red Constellation" and the\x01",
            ""Society" are accomplices with no actual\x01",
            "working units that were employed later...\x02\x03",
            "#00013FAnd Wald who demonized...\x01",
            "Depending on the situation, it's possible\x01",
            "that even the "Cult" was simply used.\x02",
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
        "#00107F#12PThe "D∴G Cult" too!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PAside from Wald...\x01",
            "Even Joachim!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PImpossible...however...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PNaturally, the probability they\x01",
            "had a direct connection is low.\x02\x03",
            "Judging by Joachim's speech and conduct,\x01",
            "it seems there was no other mastermind.\x02\x03",
            "#00001FHowever, it's possible he was used\x01",
            "in a way he himself hadn't noticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PBy the way, it wasn't identified\x01",
            "who took KeA away from the\x01",
            "Fort of Sun too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#5PAnd also who made her slip into\x01",
            "the "Schwarz Auktion" exhibit...\x02\x03",
            "#00301FThinkin' about it, no matter who did it,\x01",
            "it's an impossible feat for a "normal human".\x02\x03",
            "It must've been someone like "Yin"\x01",
            "or at the "Society"'s bunch level──\x02",
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
            "#00013FYes...!\x01",
            "Special Support Section, Lloyd's speaking!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Alright, it went through!\x02\x03",
            "I wanna Tio hear this too,\x01",
            "so put it on speaker mode!\x02",
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
            "#00005FJona?\x01",
            "Alright, I'm switching it now.\x02",
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
        "#00201F#6PJona, has something happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SSomething? Everything has!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SIt's about the Crossbell orbal net...\x01",
            "There's an absurd monster lying dormant in it!!\x07\x00\x02",
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
        "#00011F#5PA monster...?\x02",
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
            "#11P#2SAt first, I discovered a weird data\x01",
            "structure at the network margins!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SIt was a cryptic array, so I thought\x01",
            "it was mere garbage, but...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SWhen I researched it carefully,\x01",
            "it was being used as an evolved\x01",
            "code that "Society" was using!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PThe "Astral Code"...\x02\x03",
            "#00201FIn short, it was some kind of trap\x01",
            "devised by the "Society"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SNo, according to the date, it's\x01",
            "something of about 5 years ago!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SIf I'm not wrong, wasn't it around then\x01",
            "that the orbal net was introduced!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#6PYes, indeed...\x02\x03",
            "#00201F......!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12PIt was the IBC group that sponsored\x01",
            "the orbal net introduction to the\x01",
            "autonomous government...\x02\x03",
            "#00108FAs a result, the Foundation technology was\x01",
            "introduced and IBC got involved deeper...\x02\x03",
            "#00110FTo the extent that they know the\x01",
            "network key parts inside out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#5PHey now, that means...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5P──Jona.\x01",
            "What's that monster?\x02\x03",
            "#00001FWhat will happen because of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SI-I'm analyzing that...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SFor sure it's a giant system\x01",
            "that covers the whole\x01",
            "orbal net domain!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SAlso, it seems that a real\x01",
            "system was even prepared\x01",
            "to link with that!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PA real system...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P"Real" in the sense that it's\x01",
            "not in the orbal net world?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SYeah, it seems it was constructed...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SAs a device to link all the \x01",
            "Geofront divisions, Orchis\x01",
            "Tower and even Michelam!\x07\x00\x02",
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
        "#00007F#5PMichelam...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#5PThat too!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S──In any case!\x01",
            "I'll call you again when I've analyzed it!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SI dunno what you're doing,\x01",
            "but be very careful, got it?\x07\x00\x02",
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
            "#00306F#5P...Hey now.\x01",
            "Isn't that too much connected...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PAt this point I don't know what\x01",
            "this system is for, however...\x02\x03",
            "#00208FTo think there is someone who can\x01",
            "makes such a giant system aside\x01",
            "from the Foundation and "Society"...\x02",
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
            "#00006F#5P──Let's keep aiming\x01",
            "for Michelam.\x02\x03",
            "#00013FKeA, Mr. Arios...\x01",
            "All the answers are waiting there.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1800, -3000, 3000)

    def lambda_2EE4():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2EE4)
    Sleep(50)

    def lambda_2EF4():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2EF4)
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

    # Function_6_161A end

    def Function_7_2FC2(): pass

    label("Function_7_2FC2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30BF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_301B")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("loc_30BA")

    label("loc_301B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3069")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_30BA")

    label("loc_3069")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30B7")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(166)
    Jump("loc_30BA")

    label("loc_30B7")

    Sleep(233)

    label("loc_30BA")

    Jump("Function_7_2FC2")

    label("loc_30BF")

    Return()

    # Function_7_2FC2 end

    def Function_8_30C0(): pass

    label("Function_8_30C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30F8")
    OP_82(0x0, 0xF, 0x1388, 0x3E8)
    Sleep(1000)
    OP_82(0x0, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("Function_8_30C0")

    label("loc_30F8")

    Return()

    # Function_8_30C0 end

    SaveToFile()

Try(main)
