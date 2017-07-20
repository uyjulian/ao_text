from ScenarioHelper import *

def main():
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
        "Voice of Jonah",               # 1
        "terrain",                   # 2
        "Water surface",                   # 3
        "SE control",                 # 4
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
        "Function_3_931",          # 03, 3
        "Function_4_96F",          # 04, 4
        "Function_5_140C",         # 05, 5
        "Function_6_143F",         # 06, 6
        "Function_7_2C30",         # 07, 7
        "Function_8_2D2E",         # 08, 8
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
            "#00203F#5P…… As per weather forecast,\x01",
            "It has been sunny since the afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PThis is also the goddess\x01",
            "It might be guided.\x02\x03",
            "#00301FTo be honest, what danger is\x01",
            "I do not know what I'm waiting for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#5PWell, rather than exploring in the rain\x01",
            "I guess it might be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5P…… If there is a possibility\x01",
            "Is it \"a phantom beast\", or is it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PHonestly, that's the situation now\x01",
            "It seems possible to think about any possibility ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P…… The arrival of Arios are\x01",
            "What time#4RWhen#I do not know if it will become.\x02\x03",
            "#00008FAs much as possible we are going ahead\x01",
            "Let's check Lin-san's safety.\x02\x03",
            "#00001FIn some cases ……\x01",
            "We need to also contact the guard\x01",
            "There may be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5P……Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PSisters ……\x01",
            "Please be safe.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00205F#5P……this is……\x02\x03",
            "#00207FConfirmed a sharp rise in humidity.\x01",
            "be careful……!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_6CE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6CE)
    Sleep(50)

    def lambda_6DE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6DE)
    Sleep(50)

    def lambda_6EE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6EE)
    Sleep(50)

    def lambda_6FE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6FE)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00011F#5Pwhat……! Is it?\x02",
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
        "#10301F#6PThis … … fog! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#6PSure, until a while ago\x01",
            "Even though it was sunny like that! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#5PRon, Mr. Lloyd … … What shall I do! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#5PDamn\x02\x03",
            "#00007FReduce the speed\x01",
            "Try cautiously!\x02\x03",
            "Tio, approaching the rock wall\x01",
            "Can you perceive it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#5PYes, somehow ……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#5PAs soon as this happens,\x01",
            "I only have to hang my belly …!\x02",
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

    def Function_3_931(): pass

    label("Function_3_931")

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

    # Function_3_931 end

    def Function_4_96F(): pass

    label("Function_4_96F")

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
            "#00106F#5P…… No way No \"Silver#2RIn#The identity of \"\x01",
            "It was Risha-san …\x02\x03",
            "#00108FJust a men clearly\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PApparently, at that time\x01",
            "He seems to have changed the sign.\x02\x03",
            "#10301FEven a body shape as well\x01",
            "It may have changed.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(250)

    ChrTalk(
        0x109,
        (
            "#10111F#5PThat's right.\x01",
            "Can you be a normal human?\x02\x03",
            "#10106F…… To a human who is not ordinary\x01",
            "Recently I have met many people …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PApparently, my sensitivity as well\x01",
            "It seems I was deceived … …\x02\x03",
            "#00200FMr. Lloyd said, as expected\x01",
            "I was not surprised …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P… Ah, that's right.\x02\x03",
            "#00008FA while ago with Lisha\x01",
            "I had a chance to talk ….\x02",
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
            "……From a young age……\x01",
            "For that I came alive.\x02\x03",
            "From an ancient period of time\x01",
            "The road the ancestor inherited …\x02\x03",
            "For what purpose now\x01",
            "I do not know the way I'm walking.\x07\x00\x02",
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
            "#00006F#5P─ ─ Because I thought it was nothing\x01",
            "I did not think any more … …\x02\x03",
            "#00001FSomewhere she is \"silver#2RIn#\"The possibility\x01",
            "It seems I did not throw it away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#5PSuch a thing ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#00306F#6P…… Think about it, just a layman\x01",
            "To the semi-protagonist of alkane shell\x01",
            "There is no way I can pick it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5POh, that Iria\x01",
            "Because it seems that they invited brute force and practiced special training\x01",
            "It would have been strange persuasive power.\x02\x03",
            "#00008FMoreover, the period when \"silver\" appeared\x01",
            "Even when Risha came to Crossbell\x01",
            "It seems to match exactly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6P\"Black moon#4RHayuue#\"Around Mr. Tsao\x01",
            "Do you know the identity?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, if it's her place\x01",
            "It would be normal to keep it secret.\x02\x03",
            "#10300FIf you know something wrong\x01",
            "It will only be used for good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5P…… In that sense\x01",
            "Those who do not touch the identity too much\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5POh, regardless of the section chief,\x01",
            "Let's see a state for a while.\x02\x03",
            "#00013FBesides …… now it is \"black moon\"\x01",
            "\"Red constellation\" takes precedence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PAh……\x02\x03",
            "#00301F── At this timing\x01",
            "If your uncle disappears\x01",
            "It would be behavior after preparing.\x02\x03",
            "Probably, it will start moving at a stretch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5PReally……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#5P…… Also for Sonya commanders\x01",
            "It seems necessary to contact you.\x02",
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

    # Function_4_96F end

    def Function_5_140C(): pass

    label("Function_5_140C")

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

    # Function_5_140C end

    def Function_6_143F(): pass

    label("Function_6_143F")

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
        "#00001F#5P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PSomehow the police boat\x01",
            "It was nice to have secured … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6P…… Apparently Michelam\x01",
            "It seems that it was completely blocked.\x02\x03",
            "#00201FOf theme parks and various shops\x01",
            "Resident staff also retired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PIn an example wetland belt\x01",
            "There was also the possibility of heading … …\x02\x03",
            "#00301FWell, definitely\x01",
            "Michelam may be the correct answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PErie …\x01",
            "What is Mariavell?\x01",
            "Did not get in touch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P…… Yeah, in the past few days,\x01",
            "It is hard to get caught.\x02\x03",
            "#00108FIn the aftertaste of the IBC building bomb\x01",
            "It seems I was busy ….\x02",
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
            "#00303F#5PHer aside\x02\x03",
            "#00301FLitora's dude and Ms. Kirika\x01",
            "Fiction#2RHo#Is the melee you true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PThe true masterpiece of crossbell raid\x01",
            "Not an Eleven Empire … …\x02\x03",
            "#00201FMayor of Dieter · Crois …\x01",
            "No, is there a possibility of being the president?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#5P…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00106F#12P…… Lloyd.\x01",
            "You do not have to worry about me.\x02\x03",
            "#00108FFrom yesterday, with the old man\x01",
            "I have not heard from you ….\x02\x03",
            "#00101FMr. Helmer, the butler\x01",
            "Maybe at the Orkis Tower\x01",
            "I might be detained … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#00005F#5P!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PThat is..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5PTotally messed up\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#5P── The mayor of Dieter\x01",
            "A masterpiece of a series of events ……\x02\x03",
            "Thinking that way, all the Tsuyoshi#4RStorm#But\x01",
            "It is certain that it will fit.\x02\x03",
            "#00008FIn that case, \"red constellation\" or \"association\"\x01",
            "The active labor force or cooperator he hired …\x02\x03",
            "#00013FWaldo who converted into a demon … …\x01",
            "In some cases even the \"cult\"\x01",
            "There is a possibility that it was only used.\x02",
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
        "#00107F#12PThe D G Society too!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PAnyway Waldo ……\x01",
            "Take it to Joachim! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PNo way.. But\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5POf course, direct connection\x01",
            "The chances of being there would be low.\x02\x03",
            "To the extent judged from Joachim's behavior,\x01",
            "There is no appearance that there was another masterpiece.\x02\x03",
            "#00001FBut in a form that he himself does not notice\x01",
            "There is a possibility that it was being used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#6P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PBy the way, from the sun 's fortress\x01",
            "People who took Kia-chan\x01",
            "I did not find out … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#5PAnd \"Black auctioneer#10RSchwarz Auction#\"To the exhibit\x01",
            "I was missed … …\x02\x03",
            "#00301FThink about it, who you are doing\x01",
            "It is impossible for \"ordinary human being\".\x02\x03",
            "\"Silver#2RIn#\"And\" association \"class people,\x01",
            "Otherwise ──\x02",
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
            "#00013FYes……!\x01",
            "The mission support department, Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a boy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Good, it got through!\x02\x03",
            "I want to let Tio also hear it\x01",
            "Put it in speaker mode!\x02",
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
            "#00005FJonah?\x01",
            "I understood, I switched it immediately.\x02",
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
            "#11P#2SAlthough it is a conductive net of the crossbell … …\x01",
            "There is a ridiculous thing lurking! Is it?\x07\x00\x02",
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
        "#00011F#5PMonster?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PW-what do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SAt the beginning of the network\x01",
            "I found a strange data structure!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SIt was an unknown sequence\x01",
            "I thought it was just garbage ….\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SIf you look closely well\x01",
            "The code used by the \"association\" of the example\x01",
            "Evolved things were used!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PAstral Code\"\x02\x03",
            "#00201FIn other words, \"association\" started\x01",
            "Is there some trap?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SNo, as far as the date is concerned,\x01",
            "It's from five years ago!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SCertainly the introduction of conductivity net\x01",
            "That was not it! Is it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#6PYes, it is..\x02\x03",
            "#00201F!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12PIntroduction of conductivity net\x01",
            "We propose to autonomous state government\x01",
            "IBC Group ……\x02\x03",
            "#00108FAs a result, the Foundation's technology was introduced\x01",
            "IBC has also deeply involved … …\x02\x03",
            "#00110FThat's the main part of the network\x01",
            "About as much as I know …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#5POi oi so that means\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5P── Jonah.\x01",
            "What is that gem?\x02\x03",
            "#00001FCan something happen becase of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SI'm looking into that now but\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SHowever,\x01",
            "It covers the whole area\x01",
            "It is certainly a huge system!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SAnd to work with it\x01",
            "A real system too\x01",
            "It seems to be prepared! Is it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6PReal sytem…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PWhat is real is\x01",
            "Is not it the world of the power net?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SYes, in every Geofront Block\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SBetween that and the Orkis Tower\x01",
            "A mechanism to connect to the Michelin direction\x01",
            "It looks like it is being built!\x07\x00\x02",
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
        "#00310F#5PSo that name came up\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S── Anyway!\x01",
            "I will contact you again if I can analyze!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2SI did not know what to do, but\x01",
            "Please be careful!\x07\x00\x02",
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
            "#00306F#5P…… Hey, well.\x01",
            "Is not it too tight …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6PWhat is the purpose system?\x01",
            "I do not know at the moment … …\x02\x03",
            "#00208FBesides Foundation and \"association\"\x01",
            "That's just a huge system\x01",
            "If there are human beings able to construct ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P#30W…\x02",
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
            "#00006F#5P─ ─ this way now\x01",
            "Let's aim Michelam.\x02\x03",
            "#00013FKea, Arios …\x01",
            "All the answers should be waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1800, -3000, 3000)

    def lambda_2B52():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B52)
    Sleep(50)

    def lambda_2B62():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2B62)
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

    # Function_6_143F end

    def Function_7_2C30(): pass

    label("Function_7_2C30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D2D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C89")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("loc_2D28")

    label("loc_2C89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD7")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_2D28")

    label("loc_2CD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D25")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(166)
    Jump("loc_2D28")

    label("loc_2D25")

    Sleep(233)

    label("loc_2D28")

    Jump("Function_7_2C30")

    label("loc_2D2D")

    Return()

    # Function_7_2C30 end

    def Function_8_2D2E(): pass

    label("Function_8_2D2E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D66")
    OP_82(0x0, 0xF, 0x1388, 0x3E8)
    Sleep(1000)
    OP_82(0x0, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("Function_8_2D2E")

    label("loc_2D66")

    Return()

    # Function_8_2D2E end

    SaveToFile()

Try(main)
