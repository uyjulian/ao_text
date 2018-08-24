from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9013.bin",                # FileName
        "m9013",                    # MapName
        "m9013",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 100000, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9013",                  # 0
        "Guy",                    # 1
        "SE制御",                 # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_124",          # 01, 1
        "Function_2_129",          # 02, 2
        "Function_3_2F52",         # 03, 3
        "Function_4_2F65",         # 04, 4
        "Function_5_2FAC",         # 05, 5
        "Function_6_2FD0",         # 06, 6
        "Function_7_2FF4",         # 07, 7
        "Function_8_308D",         # 08, 8
        "Function_9_30AE",         # 09, 9
        "Function_10_30D9",        # 0A, 10
        "Function_11_3140",        # 0B, 11
        "Function_12_3171",        # 0C, 12
        "Function_13_319C",        # 0D, 13
        "Function_14_31BD",        # 0E, 14
        "Function_15_31E8",        # 0F, 15
        "Function_16_320C",        # 10, 16
        "Function_17_3248",        # 11, 17
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_123")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_123")

    Return()

    # Function_0_114 end

    def Function_1_124(): pass

    label("Function_1_124")

    OP_F0(0x1, 0x320)
    Return()

    # Function_1_124 end

    def Function_2_129(): pass

    label("Function_2_129")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    Call(0, 17)
    LoadChrToIndex("chr/ch12100.itc", 0x1E)
    LoadChrToIndex("apl/ch51751.itc", 0x1F)
    SoundLoad(111)
    SoundLoad(125)
    SoundLoad(109)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07801.itp")
    OP_68(0, 2500, 0, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27000, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    SetChrPos(0x101, 0, -750, 750, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -750, -2750, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(111, 2, 80, 0)
    Sound(125, 2, 40, 0)
    Sound(109, 2, 30, 0)
    OP_68(40000, 150, -50000, 0)
    MoveCamera(306, 14, 8, 0)
    OP_6E(700, 0)
    SetCameraDistance(35000, 0)
    OP_68(-20000, 150, 25000, 16000)
    MoveCamera(306, 14, 6, 16000)
    OP_6E(700, 16000)
    SetCameraDistance(35000, 16000)
    PlaceName2(340, 200, "c_plac63", 0x0, 6000)
    FadeToBright(3000, 16777215)
    Sleep(15600)
    Fade(500)
    OP_68(0, 750, 250, 0)
    MoveCamera(210, 8, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_68(0, 750, 750, 7500)
    MoveCamera(135, 14, 5, 7500)
    OP_6E(700, 7500)
    SetCameraDistance(18500, 7500)
    OP_6F(0x79)
    SetCameraDistance(13600, 100000)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00005F#11P#30WThis is...\x02\x03",
            "#00008F...Where is everyone...\x01",
            "And where did KeA go?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_93(0x101, 0x59, 0x190)
    Sleep(800)
    OP_93(0x101, 0x10F, 0x190)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W...No matter how I think\x01",
            "about it, this isn't\x01",
            "anyplace normal.\x02\x03",
            "#00008FIt also doesn't seem\x01",
            "like a good idea to move\x01",
            "around recklessly...\x02\x03",
            "#00003F...............\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(135, 14, 4, 2000)
    SetCameraDistance(13600, 10000)
    Sleep(200)
    OP_93(0x101, 0x0, 0x190)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#11P#30W...I wonder why... It's\x01",
            "such an empty place, and\x01",
            "yet...\x02\x03",
            "#00000FFor some reason... I\x01",
            "strangely don't feel any\x01",
            "anxiety or fear...\x02\x03",
            "#00008F...What in the world is\x01",
            "this place?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3C─No matter the circumstances,\x01",
            "remain focused and work to\x01",
            "understand the scene...\x02\x03",
            "Someone's quite used to the\x01",
            "work of a detective, aren't\x01",
            "they.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(223, 0, 50, 0)
    Sound(920, 0, 50, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 750, 0, 1500)
    MoveCamera(135, 14, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(13600, 1500)

    def lambda_668():
        OP_95(0xFE, 0, -750, -1400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_668)

    def lambda_682():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_682)

    def lambda_693():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_693)
    OP_6F(0x79)
    CancelBlur(0)
    SetCameraDistance(13000, 3000)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#6P#30W────────────\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)

    NpcTalk(
        0x8,
        "???",
        "#11P#30WOh, what's wrong Lloyd?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "???",
        (
            "#11P#30WAre you so shocked after\x01",
            "not seeing me for so long\x01",
            "that you can't even speak?\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7534", 0)
    SetCameraDistance(11000, 100000)
    Sleep(500)
    BeginChrThread(0x9, 1, 0, 16)

    ChrTalk(
        0x101,
        (
            "#00011F#6P#40WB-Brother...\x02\x03",
            "#00002FIs that... you...?\x02",
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
        0x8,
        (
            "#30W#0CHaha, "brother"... Don't attach\x01",
            "such a cool name to a guy like me.\x02\x03",
            "You should just call me "big bro"\x01",
            "like you used to, right?\x02\x03",
            "It's just the two of us here. You\x01",
            "can act as spoiled as you like, you\x01",
            "know?\x02",
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
        0x101,
        (
            "#00006F#6P#30W...... Oh, leave me\x01",
            "alone!\x02\x03",
            "#00002FBut this backtalk...\x01",
            "There's no mistake... You\x01",
            "really are my brother...\x02\x03",
            "It doesn't even seem like\x01",
            "I'm dreaming... What's\x01",
            "the meaning of this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WWell, it seems this place is a\x01",
            "part of that child's interior.\x02\x03",
            "#07808FThe World of "Zero" that\x01",
            "comprehends every possibility\x01",
            "and can reorganize the world...\x02\x03",
            "#07800FIt seems that's the kind of\x01",
            "place this is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6P#30WThe World of "Zero"...\x02\x03",
            "#00013FSo even the fact that big bro...\x01",
            "...That my brother can show up\x01",
            "here is related to that?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 5)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#07803F#11P#30WYeah. That child probably learned\x01",
            "about me while tampering with the\x01",
            "space-time of the past.\x02\x03",
            "#07808FAlso, she probably tried to\x01",
            "revive me... For your, Cecil's...\x01",
            "Arios' and Tio's sake too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6P#30WYou've been... revived!?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 6)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#07800F#11P#30WWell, to be precise, she\x01",
            "probably created a new world,\x01",
            "one where I didn't die.\x02\x03",
            "#07802F─What do you say, Lloyd?\x02\x03",
            "#07809FWould you be happy if your\x01",
            "brother came back? Or would\x01",
            "you consider it annoying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#40W...Haha...\x02\x03",
            "#00004FIsn't it obvious... that\x01",
            "I'd be... happy for\x01",
            "that...?\x02\x03",
            "#00008F...However... that\x01",
            "would...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W─It would negate the entire time after\x01",
            "I died, and all the efforts of everyone\x01",
            "who did their best along with it...\x02\x03",
            "#07810FWell, of course that's how things would\x01",
            "turn out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#40W......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07803F#11P#30WThe Special Support Section,\x01",
            "eh?\x02\x03",
            "#07802FA possible world where I joined\x01",
            "and solved many different cases\x01",
            "with you all...\x02\x03",
            "#07804FThat's not your current\x01",
            "world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#40W...Yeah...\x02\x03",
            "#00006FIf there was really such a world,\x01",
            "I think it would be so much fun...\x01",
            "...And joyous, and pleasant...\x02\x03",
            "#00008F#50W...But even so... I...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    def lambda_1026():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1026)
    WaitChrThread(0x101, 2)
    Sleep(750)

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WYeah─ It's ok.\x02\x03",
            "#07800FI'm proud that you've\x01",
            "become able to say so.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 750, 500, 1500)
    MoveCamera(135, 14, 3, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(11000, 1500)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    OP_9B(0x1, 0x8, 0x0, 0x60E, 0x3E8, 0x0)
    OP_6F(0x79)
    BeginChrThread(0x8, 1, 0, 7)
    WaitChrThread(0x8, 1)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 8)
    WaitChrThread(0x8, 1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#07809F#11P#40WReally... That spoiled\x01",
            "brat has made it this\x01",
            "far and grown so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00015F#6P#50WI'm telling you, I- I don't\x01",
            "have any memories of being\x01",
            "spoiled by you, big bro...\x02\x03",
            "#00008F...Cecil is a different\x01",
            "story...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07804F#11P#40WHaha... You're right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#07803F#11P#30W...Cecil too... It's a good\x01",
            "time for Cecil to start\x01",
            "walking on her own path.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(120)
    SetChrSubChip(0x8, 0x10)
    Sleep(120)
    SetChrSubChip(0x8, 0x9)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#07802F#11P#30WIf you like, why don't\x01",
            "you try a bold attack?\x02\x03",
            "#07809FBut since she's a natural\x01",
            "airhead, she might not\x01",
            "realize it at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30WShut up... Don't make fun\x01",
            "of Cecil.\x02\x03",
            "#00013FShe's a great woman, and\x01",
            "would be wasted on someone\x01",
            "like you, big bro...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B1")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, for sure.\x02\x03",
            "#07800FWell, you seem to have found a\x01",
            "partner for yourself, so I might be\x01",
            "worrying over nothing.\x02\x03",
            "#07809FElie, is she called? She's a good\x01",
            "girl blessed with both intelligence\x01",
            "and beauty. Way too good for you.\x02\x03",
            "#07802FAlthough she's a rich girl, it seems\x01",
            "she has her own beliefs, ability to\x01",
            "take action and broad-mindedness too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#30WHaha... I think so too.\x02\x03",
            "#00006FIf possible, I would've\x01",
            "liked... For you to have\x01",
            "met Elie, brother.\x02\x03",
            "#00008FAnd Randy and Tio too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, huh? It seems a lot's\x01",
            "happened to her, but I'm glad\x01",
            "she's grown up into a fine kid.\x02\x03",
            "#07800FThat Randy too. He seems like\x01",
            "quite the funny and silly guy.\x02\x03",
            "#07809FYou're blessed with good\x01",
            "friends, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2923")

    label("loc_16B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A31")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, for sure.\x02\x03",
            "#07800FWell, you seem to have found a\x01",
            "partner for yourself, so I\x01",
            "might be worrying over nothing.\x02\x03",
            "#07809FWho would've thought you'd\x01",
            "become intimate with Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P#30WWe don't have that kind of\x01",
            "relationship...\x02\x03",
            "#00004FBut I guess it's true that\x01",
            "I want to protect her and\x01",
            "that she's a precious girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WI see... She's become able\x01",
            "to smile, and it's a\x01",
            "beautiful one at that.\x02\x03",
            "#07802FWell I'm certain she has a\x01",
            "promising future, so hold\x01",
            "on to her tightly, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#30WHaha... You're too\x01",
            "direct.\x02\x03",
            "#00006FIf possible, I would've\x01",
            "liked... for you to have\x01",
            "met Tio, brother.\x02\x03",
            "#00008FAnd Elie and Randy\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WElie is the intelligent,\x01",
            "beautiful and dynamic\x01",
            "young lady, eh?\x02\x03",
            "#07800FThat Randy too. He seems\x01",
            "like quite the funny and\x01",
            "silly guy.\x02\x03",
            "#07809FYou're blessed with good\x01",
            "friends, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2923")

    label("loc_1A31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D1E")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, for sure.\x02\x03",
            "#07800FWell, you seem to have found a\x01",
            "partner for yourself, so I\x01",
            "might be worrying over nothing.\x02\x03",
            "#07809FNoｱl, is she called? She's an\x01",
            "honest and nice girl. Way too\x01",
            "good for you.\x02\x03",
            "#07802FEven her one-track mind seems\x01",
            "to match yours well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#30WHaha... I think so too.\x02\x03",
            "#00006FIf possible, I would've\x01",
            "liked... For you to have\x01",
            "met Noｱl, brother.\x02\x03",
            "#00008FElie, Randy, and Tio\x01",
            "too, of course...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, huh? It seems a lot's\x01",
            "happened to her, but I'm glad\x01",
            "she's grown up into a fine kid.\x02\x03",
            "#07800FElie is the intelligent,\x01",
            "beautiful and dynamic young\x01",
            "lady, eh?\x02\x03",
            "That Randy too. He seems like\x01",
            "quite the funny and silly guy.\x02\x03",
            "#07809FYou're blessed with good\x01",
            "friends, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2923")

    label("loc_1D1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_205F")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, for sure.\x02\x03",
            "#07800FWell, you seem to have found a\x01",
            "partner for yourself, so I might\x01",
            "be worrying over nothing.\x02\x03",
            "#07809F─Rixia, is she called?\x02\x03",
            "#07802FIt seems she has a lot going on,\x01",
            "but she's a brave and nice girl.\x01",
            "Way too good for someone like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P#30WWe don't have that kind\x01",
            "of relationship...\x02\x03",
            "#00004FBut... I guess it's true\x01",
            "that she's someone I\x01",
            "want to protect.\x02\x03",
            "#00008FIf possible, I would've\x01",
            "liked... for you to have\x01",
            "met Rixia, brother.\x02\x03",
            "Elie, Randy, and Tio\x01",
            "too, of course...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, huh? It seems a lot's\x01",
            "happened to her, but I'm glad\x01",
            "she's grown up into a fine kid.\x02\x03",
            "#07800FElie is the intelligent,\x01",
            "beautiful and dynamic young\x01",
            "lady, eh?\x02\x03",
            "That Randy too. He seems like\x01",
            "quite the funny and silly guy.\x02\x03",
            "#07809FYou're blessed with good\x01",
            "friends, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2923")

    label("loc_205F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2362")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, for sure.\x02\x03",
            "#07802FWell, find a proper\x01",
            "partner for yourself,\x01",
            "okay?\x02\x03",
            "Although I understand\x01",
            "it's fun hanging out\x01",
            "with buddies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#30WAh, you mean Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHe looks quite silly but\x01",
            "seems to be a guy with\x01",
            "principles.\x02\x03",
            "#07800FHe seems to be in sync\x01",
            "with you, a serious\x01",
            "guy...\x02\x03",
            "#07809FI guess he's a nice\x01",
            "buddy for you, isn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WYeah... I think so too.\x02\x03",
            "#00008FIf possible, I would've\x01",
            "liked... for you to have\x01",
            "met Randy, brother.\x02\x03",
            "And Tio and Elie too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, huh? It seems a lot's\x01",
            "happened to her, but I'm glad\x01",
            "she's grown up into a fine kid.\x02\x03",
            "#07800FElie is the intelligent,\x01",
            "beautiful and dynamic young\x01",
            "lady, eh?\x02\x03",
            "#07809FYou're blessed with good\x01",
            "friends, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2923")

    label("loc_2362")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B6")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, for sure.\x02\x03",
            "#07802FWell, find a proper\x01",
            "partner for yourself,\x01",
            "okay?\x02\x03",
            "Although I understand\x01",
            "that it's fun hanging\x01",
            "out with guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#30WAh, you mean Wazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHe seems like a\x01",
            "mysterious guy, but\x01",
            "someone you can trust.\x02\x03",
            "#07800FI think he compliments a\x01",
            "serious guy like you\x01",
            "quite well.\x02\x03",
            "#07809FThis could be some kind\x01",
            "of fate, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WYeah... I think so too.\x02\x03",
            "#00008FIf possible, I would've\x01",
            "liked... for you to have\x01",
            "met Wazy, brother.\x02\x03",
            "Elie, Randy, and Tio\x01",
            "too, of course...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, huh? It seems a lot's\x01",
            "happened to her, but I'm glad\x01",
            "she's grown up into a fine kid.\x02\x03",
            "#07800FElie is the intelligent,\x01",
            "beautiful and dynamic young\x01",
            "lady, eh?\x02\x03",
            "That Randy too. He seems like\x01",
            "quite the funny and silly guy.\x02\x03",
            "#07809FYou're blessed with good\x01",
            "friends, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2923")

    label("loc_26B6")


    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, for sure.\x02\x03",
            "#07803FWell, find a proper\x01",
            "partner for yourself,\x01",
            "okay?\x02\x03",
            "#07802FAlthough I understand\x01",
            "that it's fun hanging\x01",
            "out between friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P#30WHaha... I can't deny it.\x02\x03",
            "#00008FIf possible, I would've\x01",
            "liked... for you to have\x01",
            "met everyone, big brother.\x02\x03",
            "Elie, Randy, and Tio too,\x01",
            "of course...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, huh? It seems a lot's\x01",
            "happened to her, but I'm glad\x01",
            "she's grown up into a fine kid.\x02\x03",
            "#07800FElie is the intelligent,\x01",
            "beautiful and dynamic young\x01",
            "lady, eh?\x02\x03",
            "That Randy too. He seems like\x01",
            "quite the funny and silly guy.\x02\x03",
            "#07809FYou're blessed with good\x01",
            "friends, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2923")


    ChrTalk(
        0x101,
        (
            "#00002F#6P#30WYeah... They're the best\x01",
            "friends anyone could ask\x01",
            "for.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 11)
    BeginChrThread(0x101, 1, 0, 12)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0xE)
    BeginChrThread(0x101, 0, 0, 3)
    OP_68(0, 750, 800, 1500)
    MoveCamera(135, 14, 3, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(12000, 1500)
    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W...Brother, it's time\x01",
            "for me to go.\x02\x03",
            "To get back what is\x01",
            "precious to me and\x01",
            "return to everyone.\x02\x03",
            "#00000FWill I... ever see you\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WYeah, of course.\x02\x03",
            "#07810FI'll always be by your\x01",
            "side.\x02\x03",
            "When you're crying, when\x01",
            "you want to be spoiled...\x01",
            "You can call me whenever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P#30WHaha... Got it.\x02\x03",
            "#00002FBut, I think that no matter\x01",
            "how painful it is, I'll get\x01",
            "over any Barrier...\x02\x03",
            "#00004FAs long as it's to grasp\x01",
            "the tomorrow that lies\x01",
            "beyond it, with everyone.\x02\x03",
            "#00000F─That's why I'll be fine.\x01",
            "So don't worry, and keep\x01",
            "watching over me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07809F#11P#30WHaha, just listen to how\x01",
            "cheeky you are.\x02\x03",
            "#07804F─With how you are now, you\x01",
            "should be able to find\x01",
            "that kid, in a real sense.\x02\x03",
            "#07800F#30W#11PFind the princess holed up\x01",
            "inside her shell and hug\x01",
            "her!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        (
            "#00000F#6P#30W#4SRight!\x02\x03",
            "#00014F#3SGoodbye─ brother!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(480, 350, 5260, 3500)
    MoveCamera(34, 8, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(13230, 3500)
    BeginChrThread(0x101, 0, 0, 4)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 350, 400, 0)
    MoveCamera(135, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(10500, 3000)
    Sleep(1500)
    BeginChrThread(0x8, 1, 0, 13)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    SetCameraDistance(10000, 15000)

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W...That's right. For as\x01",
            "long as you live, Barriers\x01",
            "will always appear.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    BeginChrThread(0x8, 1, 0, 14)
    WaitChrThread(0x8, 1)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#07810F#11P#30WWhat's important is to get\x01",
            "over them and discover the\x01",
            "light that lies beyond, eh?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 15)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WGo all out─ Lloyd\x01",
            "Bannings!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(12000, 3000)
    FadeToDark(2000, 0, -1)
    Sleep(300)
    SetChrSubChip(0x8, 0x16)
    Sleep(143)
    SetChrSubChip(0x8, 0x15)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    StopSound(111, 2000, 30)
    StopSound(125, 2000, 20)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9014", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_129 end

    def Function_3_2F52(): pass

    label("Function_3_2F52")

    OP_9B(0x1, 0x101, 0x0, 0xFFFFFD12, 0x320, 0x0)
    Sleep(400)
    Return()

    # Function_3_2F52 end

    def Function_4_2F65(): pass

    label("Function_4_2F65")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x1)

    def lambda_2F80():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F80)
    Sleep(3000)

    def lambda_2F98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F98)
    Sleep(1500)
    EndChrThread(0xFE, 0x1)
    Return()

    # Function_4_2F65 end

    def Function_5_2FAC(): pass

    label("Function_5_2FAC")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xE)
    Sleep(500)
    Return()

    # Function_5_2FAC end

    def Function_6_2FD0(): pass

    label("Function_6_2FD0")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xE)
    Sleep(150)
    SetChrSubChip(0xFE, 0xD)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Return()

    # Function_6_2FD0 end

    def Function_7_2FF4(): pass

    label("Function_7_2FF4")

    Sound(812, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    BeginChrThread(0x101, 1, 0, 10)
    Sound(898, 0, 50, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    WaitChrThread(0x101, 1)
    Return()

    # Function_7_2FF4 end

    def Function_8_308D(): pass

    label("Function_8_308D")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0x10)
    Sleep(120)
    SetChrSubChip(0xFE, 0x11)
    Return()

    # Function_8_308D end

    def Function_9_30AE(): pass

    label("Function_9_30AE")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x18)
    Sleep(120)
    SetChrSubChip(0xFE, 0x19)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(120)
    Return()

    # Function_9_30AE end

    def Function_10_30D9(): pass

    label("Function_10_30D9")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1F)
    Return()

    # Function_10_30D9 end

    def Function_11_3140(): pass

    label("Function_11_3140")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 30, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0x0)
    Sleep(429)
    Return()

    # Function_11_3140 end

    def Function_12_3171(): pass

    label("Function_12_3171")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(429)
    Return()

    # Function_12_3171 end

    def Function_13_319C(): pass

    label("Function_13_319C")

    Fade(250)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(812, 0, 30, 0)
    SetChrSubChip(0xFE, 0x12)
    Sleep(300)
    Return()

    # Function_13_319C end

    def Function_14_31BD(): pass

    label("Function_14_31BD")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x12)
    Sleep(120)
    SetChrSubChip(0xFE, 0x13)
    Sleep(120)
    SetChrSubChip(0xFE, 0x14)
    Sleep(120)
    SetChrSubChip(0xFE, 0x15)
    Sleep(300)
    Return()

    # Function_14_31BD end

    def Function_15_31E8(): pass

    label("Function_15_31E8")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x15)
    Sleep(150)
    SetChrSubChip(0xFE, 0x16)
    Sleep(150)
    SetChrSubChip(0xFE, 0x17)
    Sleep(500)
    Return()

    # Function_15_31E8 end

    def Function_16_320C(): pass

    label("Function_16_320C")

    StopSound(109, 1000, 20)
    OP_25(0x6F, 0x4B)
    Sleep(100)
    OP_25(0x6F, 0x46)
    Sleep(100)
    OP_25(0x6F, 0x41)
    Sleep(100)
    OP_25(0x6F, 0x3C)
    Sleep(100)
    OP_25(0x6F, 0x37)
    Sleep(100)
    OP_25(0x6F, 0x32)
    Sleep(100)
    OP_25(0x6F, 0x2D)
    Sleep(100)
    OP_25(0x6F, 0x28)
    Return()

    # Function_16_320C end

    def Function_17_3248(): pass

    label("Function_17_3248")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_326A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32EC")

    label("loc_326A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_3282")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32EC")

    label("loc_3282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_329A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32EC")

    label("loc_329A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_END)), "loc_32B2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32EC")

    label("loc_32B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_END)), "loc_32CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32EC")

    label("loc_32CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_END)), "loc_32E2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32EC")

    label("loc_32E2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32EC")

    Return()

    # Function_17_3248 end

    SaveToFile()

Try(main)
