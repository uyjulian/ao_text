from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0510.bin",                # FileName
        "c0510",                    # MapName
        "c0510",                    # Location
        0x0029,                     # MapIndex
        "ed7302",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0510",                  # 0
        "Detective Dudley",       # 1
        "Detective Emma",         # 2
        "Policeman",              # 3
        "Policeman",              # 4
        "Policeman",              # 5
        "Policeman",              # 6
        "Policeman",              # 7
    ))

    AddCharChip((
        "chr/ch30000.itc",                   # 00
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)

    ChipFrameInfo(368, 0)                                        # 0

    ScpFunction((
        "Function_0_170",          # 00, 0
        "Function_1_220",          # 01, 1
        "Function_2_24A",          # 02, 2
        "Function_3_260",          # 03, 3
        "Function_4_1367",         # 04, 4
    ))


    def Function_0_170(): pass

    label("Function_0_170")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1A8"),
        (1, "loc_1B4"),
        (2, "loc_1C0"),
        (3, "loc_1CC"),
        (4, "loc_1D8"),
        (5, "loc_1E4"),
        (6, "loc_1F0"),
        (SWITCH_DEFAULT, "loc_1FC"),
    )


    label("loc_1A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_208")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_21F")

    Return()

    # Function_0_170 end

    def Function_1_220(): pass

    label("Function_1_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_22F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)

    label("loc_22F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_249")
    Event(0, 4)

    label("loc_249")

    Return()

    # Function_1_220 end

    def Function_2_24A(): pass

    label("Function_2_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_END)), "loc_25F")
    ClearMapObjFlags(0x1F, 0x4)
    ClearMapObjFlags(0x20, 0x4)

    label("loc_25F")

    Return()

    # Function_2_24A end

    def Function_3_260(): pass

    label("Function_3_260")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("chr/ch30500.itc", 0x1F)
    LoadChrToIndex("apl/ch51258.itc", 0x20)
    SoundLoad(803)
    SoundLoad(3461)
    SoundLoad(3462)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    OP_68(-40, 1270, 8290, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 680, 30, -2029, 0)
    SetChrPos(0x103, 680, 30, -3530, 0)
    SetChrPos(0x109, 680, 30, -5030, 0)
    SetChrPos(0x102, -740, 30, -3060, 0)
    SetChrPos(0x104, -740, 30, -4560, 0)
    SetChrPos(0x105, -740, 30, -6060, 0)
    SetChrPos(0xA, 4740, 0, 6180, 225)
    SetChrPos(0xB, 4150, 0, 4200, 315)
    SetChrPos(0xC, 2490, 30, 4750, 89)
    SetChrPos(0xD, -4270, 0, 9250, 270)
    SetChrPos(0xE, -5740, 0, 9250, 89)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 660, 20, 8390, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -1000, 20, 8490, 90)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetCameraDistance(21000, 3000)
    FadeToBright(1000, 0)
    Sleep(2500)
    OP_64(0x8)
    OP_64(0x9)
    Sound(103, 0, 100, 0)
    Sleep(300)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "Excuse us.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4A8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4A8)
    Sleep(50)

    def lambda_4B8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4B8)
    WaitChrThread(0x8, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        "#5P#3461V#30W─So you're here.\x02",
    )

    CloseMessageWindow()
    OP_24(0xD85)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(-820, 1270, 6090, 3300)

    def lambda_57E():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57E)
    Sleep(50)

    def lambda_596():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_596)
    Sleep(50)

    def lambda_5AE():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5AE)
    Sleep(50)

    def lambda_5C6():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C6)
    Sleep(50)

    def lambda_5DE():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5DE)
    Sleep(50)

    def lambda_5F6():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5F6)
    OP_6F(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrPos(0x101, -20, 30, 6270, 0)
    SetChrPos(0x102, 770, 30, 5670, 0)
    SetChrPos(0x103, -950, 30, 4190, 0)
    SetChrPos(0x104, -1320, 30, 5770, 0)
    SetChrPos(0x109, 250, 30, 3960, 0)
    SetChrPos(0x105, -2050, 30, 4030, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrPos(0x8, -100, 20, 8400, 180)
    SetChrPos(0x9, -1000, 20, 8900, 180)
    OP_68(-510, 2280, 6790, 0)
    MoveCamera(38, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19700, 0)
    Sleep(1000)
    OP_68(-510, 1280, 6790, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#5P*sigh*, so you've\x01",
            "finally arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PSorry. We were a little\x01",
            "busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PCan you tell us the\x01",
            "situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00606F#5PLike I told you, there's\x01",
            "no one left inside the\x01",
            "building.\x02\x03",
            "#00600FWe believe there were\x01",
            "around 100 members\x01",
            "coming and going, but...\x02\x03",
            "It seems they went\x01",
            "through the Geofront and\x01",
            "made themselves scarce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PThrough the Geofront...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#12PHowever... There\x01",
            "shouldn't have been any\x01",
            "such path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P...It appears they used\x01",
            "explosives to force\x01",
            "their way in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PA secret path exiting at\x01",
            "B-Division lower stratum\x01",
            "was discovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#12PT-They did that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12POh man... What crazy\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00606F#5PThat's not all. They remodeled\x01",
            "most of the old warehouse\x01",
            "Revache used for smuggling...\x02\x03",
            "#00610F...Into a full-blown training\x01",
            "and maintenance facility for\x01",
            "handling heavy weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#12P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6P...Well uncle and the others 'd do\x01",
            "somethin' like that without battin' an\x01",
            "eye.\x02\x03",
            "#00301FAfter all, the whole lot of 'em are battle\x01",
            "crazies. They want to keep their senses\x01",
            "sharp to be ready for battle anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P...I see.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#00603F#5POrlando, I'll be direct.\x02\x03",
            "#00601FIs their objective\x01",
            "Heiyue? Or terrorism at\x01",
            "the station or airport?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C1F():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C1F)
    Sleep(50)

    def lambda_C2F():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C2F)
    Sleep(50)

    def lambda_C3F():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C3F)
    Sleep(50)

    def lambda_C4F():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C4F)
    Sleep(50)

    def lambda_C5F():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C5F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x104,
        (
            "#00306F#6PI really don't know, but... If\x01",
            "they were aimin' at Heiyue, they'd\x01",
            "never vanish from here like that.\x02\x03",
            "#00308FThe station and the airport too...\x01",
            "They could've occupied them\x01",
            "easily.\x02\x03",
            "#00311FI'd say it's likely they're\x01",
            "plannin' something way crazier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PThen that means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PDon't tell me they\x01",
            "intend to occupy Orchis\x01",
            "Tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PThat's possible, but...\x02\x03",
            "#00306F...But maybe that's not\x01",
            "really their style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#6PHuh, style you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#5P...A jaeger can really shine in\x01",
            "open battle or guerrilla\x01",
            "warfare...\x02\x03",
            "#00303FIn other words, they like to\x01",
            "battle in complex terrain where\x01",
            "they can toy with a regular army.\x02\x03",
            "#00301FSo urban areas, or mountainous\x01",
            "areas with lots of peaks and\x01",
            "valleys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12PT-That's true... Vehicle\x01",
            "movement would also be\x01",
            "restricted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00610F#5PTch, in that case─\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(300)
    TurnDirection(0x9, 0x8, 500)

    def lambda_104B():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_104B)
    Sleep(30)

    def lambda_105B():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_105B)
    Sleep(30)

    def lambda_106B():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_106B)
    Sleep(30)

    def lambda_107B():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_107B)
    Sleep(30)

    def lambda_108B():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_108B)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    SetChrSubChip(0x8, 0x1)
    Sound(804, 0, 100, 0)
    OP_24(0x323)

    ChrTalk(
        0x8,
        (
            "#00603F#11PIt's Dudley, Section\x01",
            "One.\x02\x03",
            "#00605F─Ah, Chief. Thank you\x01",
            "for your hard work...\x02\x03",
            "#30W............\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#00607F#3462V#4S#11P─What did you say!?\x02",
    )

    CloseMessageWindow()
    OP_24(0xD86)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00013F#12P(W-What the...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P(With this timing...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#6P............\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x8, 0x0)
    Sleep(600)

    ChrTalk(
        0x9,
        (
            "#5PDudley. What in the\x01",
            "world...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#00603F#5P...It's the CGF.\x02\x03",
            "#00608FAn unidentified armed\x01",
            "group has appeared on\x01",
            "Mainz Mountain Path─\x02\x03",
            "#00610FThe unit on patrol seems\x01",
            "to have been wiped out.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(250, 40, -1, -1)
    SetChrName("All")
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    AnonymousTalk(
        0xFF,
        "#5S!!!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(30000, 5000)
    Sleep(1500)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x323)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 4)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_260 end

    def Function_4_1367(): pass

    label("Function_4_1367")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1500, 50000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -600, 0, 47800, 0)
    SetChrPos(0x102, 600, 0, 47800, 0)
    SetChrPos(0x103, -600, 0, 46300, 0)
    SetChrPos(0x104, 600, 0, 46300, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1416():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1416)
    Sleep(50)

    def lambda_1433():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1433)
    Sleep(50)

    def lambda_1450():
        OP_97(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1450)
    Sleep(50)

    def lambda_146D():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_146D)
    FadeToBright(1000, 0)
    OP_68(0, 1500, 52000, 2000)
    Sleep(300)

    def lambda_14A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14A4)
    Sleep(50)

    def lambda_14B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_14B8)
    Sleep(700)

    def lambda_14CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_14CC)
    Sleep(50)

    def lambda_14E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14E0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(0, 100, 57000, 2000)
    MoveCamera(35, 35, 0, 2000)
    SetCameraDistance(19500, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#00201FIt looks like he went\x01",
            "further ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah... Let's descend\x01",
            "cautiously.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 51000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 4)
    EventEnd(0x5)
    Return()

    # Function_4_1367 end

    SaveToFile()

Try(main)
