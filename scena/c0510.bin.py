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
        "Function_4_13FD",         # 04, 4
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
        "#5P#3461V#30W──So you're here.\x02",
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

    def lambda_580():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_580)
    Sleep(50)

    def lambda_598():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_598)
    Sleep(50)

    def lambda_5B0():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B0)
    Sleep(50)

    def lambda_5C8():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C8)
    Sleep(50)

    def lambda_5E0():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E0)
    Sleep(50)

    def lambda_5F8():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5F8)
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
        "#5P*sigh*, you have finally arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PI am sorry.\x01",
            "We were a little busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PCan you tell us the situation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00606F#5PLike I informed you, there's no\x01",
            "one remaining in this building.\x02\x03",
            "#00600FWe believe there were about 100\x01",
            "members coming and going, but...\x02\x03",
            "It seems they went through the\x01",
            "Geofront and made themselves scarce.\x02",
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
            "#00205F#12PHowever...\x01",
            "There shouldn't have been such a way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P...It appears they used explosives\x01",
            "to penetrate inside by force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PA path exiting on the lower stratum of\x01",
            "Geofront B-Division was discovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#12PT-They did such a...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12POh boy...\x01",
            "What crazy guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00606F#5PNot only that.\x01",
            "They have remodeled in large part the old\x01",
            "warehouse Revache used for smuggling...\x02\x03",
            "#00610F...As a full-blown training and maintenance\x01",
            "facility for dealing with heavy weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#12P......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6P...Well, being uncle and the others,\x01",
            "that's what they'd normally do.\x02\x03",
            "#00301FAfter all, they're all battle crazy who\x01",
            "want to be always sharply ready so they\x01",
            "can deal with a real battle anytime.\x02",
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
            "#00603F#5POrlando, I'll frankly ask you.\x02\x03",
            "#00601FIs their objective the "Heiyue"?\x01",
            "Or terrorism at the station or at the airport?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C50():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C50)
    Sleep(50)

    def lambda_C60():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C60)
    Sleep(50)

    def lambda_C70():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C70)
    Sleep(50)

    def lambda_C80():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C80)
    Sleep(50)

    def lambda_C90():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C90)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x104,
        (
            "#00306F#6PI really don't know, but...\x01",
            "If they were aimin' at the "Heiyue", \x01",
            "they'd never vanish from here like that.\x02\x03",
            "#00308FAs for the station and the airport too...\x01",
            "They could occupy them without effort.\x02\x03",
            "#00311FIt's very likely they're plannin'\x01",
            "something way crazier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PSo that means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PDon't tell me they intend to\x01",
            "occupy Orchis Tower...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PThat's possible, but...\x02\x03",
            "#00306F...But I think that maybe it's\x01",
            "far from their preferences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#6PEeh, preferences you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#5P...A jaeger can display his specialties\x01",
            "on fields or guerrilla warfare...\x02\x03",
            "#00303FIn other words, they like intricate terrain battles\x01",
            "where they can trifle with the regular army.\x02\x03",
            "#00301FSo...the area of a whole town or...\x01",
            "Mountain areas with many undulations.\x02",
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
            "#10101F#12PT-That's true...\x01",
            "Vehicles movements would also be restricted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00610F#5PTsk, in that case──\x02",
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

    def lambda_10AF():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10AF)
    Sleep(30)

    def lambda_10BF():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10BF)
    Sleep(30)

    def lambda_10CF():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10CF)
    Sleep(30)

    def lambda_10DF():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10DF)
    Sleep(30)

    def lambda_10EF():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10EF)
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
            "#00603F#11PCrime Investigations Section One, Dudley speaking.\x02\x03",
            "#00605F──Ah, Section Chief.\x01",
            "Thank you for your hard work...\x02\x03",
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
        "#00607F#3462V#4S#11P──What did you say!?\x02",
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
        "#00108F#12P(With such a timing...)\x02",
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
            "#5PM-Mr. Dudley.\x01",
            "What could have...\x02",
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
            "#00603F#5P...A call from the CGF.\x02\x03",
            "#00608FAn unidentified armed group has\x01",
            "appeared on Mainz Mountain Path──\x02\x03",
            "#00610FThe unit on patrol seems\x01",
            "to have been crushed.\x02",
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

    def Function_4_13FD(): pass

    label("Function_4_13FD")

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

    def lambda_14AC():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14AC)
    Sleep(50)

    def lambda_14C9():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_14C9)
    Sleep(50)

    def lambda_14E6():
        OP_97(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_14E6)
    Sleep(50)

    def lambda_1503():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1503)
    FadeToBright(1000, 0)
    OP_68(0, 1500, 52000, 2000)
    Sleep(300)

    def lambda_153A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_153A)
    Sleep(50)

    def lambda_154E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_154E)
    Sleep(700)

    def lambda_1562():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1562)
    Sleep(50)

    def lambda_1576():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1576)
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
            "#00001FYeah...\x01",
            "Let's descend with prudence.\x02",
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

    # Function_4_13FD end

    SaveToFile()

Try(main)
