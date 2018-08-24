from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4400.bin",                # FileName
        "e4400",                    # MapName
        "e4400",                    # Location
        0x0000,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e4400",                  # 0
        "Elie",                   # 1
        "Rixia",                  # 2
        "Divine Wolf Zeit",       # 3
        "Grace",                  # 4
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch03200.itc",                   # 01
        "chr/ch02708.itc",                   # 02
        "chr/ch06000.itc",                   # 03
    ))

    DeclNpc(4294964366, 0,       509,     270,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(2589,    0,       4294967267, 90,   389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294965747, 0,       4294966337, 180,  405,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294964366, 0,       509,     270,  389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_2BE",          # 02, 2
        "Function_3_382",          # 03, 3
        "Function_4_5AF",          # 04, 4
        "Function_5_A31",          # 05, 5
        "Function_6_E32",          # 06, 6
        "Function_7_10FD",         # 07, 7
        "Function_8_1506",         # 08, 8
        "Function_9_16F5",         # 09, 9
        "Function_10_1F49",        # 0A, 10
        "Function_11_21A6",        # 0B, 11
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_17C"),
        (1, "loc_188"),
        (2, "loc_194"),
        (3, "loc_1A0"),
        (4, "loc_1AC"),
        (5, "loc_1B8"),
        (6, "loc_1C4"),
        (SWITCH_DEFAULT, "loc_1D0"),
    )


    label("loc_17C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_188")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_194")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1F3")

    Return()

    # Function_0_144 end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_207")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_21A")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22D")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_240")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2A8")

    label("loc_240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_253")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_2A8")

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_266")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_279")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_2A8")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_28C")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2A8")

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_29A")
    Jump("loc_2A8")

    label("loc_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2A8")
    ClearChrFlags(0xA, 0x80)

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2BD")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 11)

    label("loc_2BD")

    Return()

    # Function_1_1F4 end

    def Function_2_2BE(): pass

    label("Function_2_2BE")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E4")
    Sound(132, 1, 70, 0)
    Sound(497, 1, 30, 0)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_2F0")

    label("loc_2E4")

    Sound(132, 1, 100, 0)
    Sound(497, 1, 100, 0)

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_305")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_305")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    SetMapFlags(0x10000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_345")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C")
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_345")

    label("loc_33C")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_345")

    SetMapObjFrame(0x0, "door_l1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_l2", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r2", 0x0, 0x1)
    Return()

    # Function_2_2BE end

    def Function_3_382(): pass

    label("Function_3_382")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397")
    Call(0, 4)
    Jump("loc_5AB")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C9")

    ChrTalk(
        0xFE,
        (
            "#00103FThe "independent state" declaration of\x01",
            "invalidity... I still don't know if it\x01",
            "is the right thing to do. However...\x02\x03",
            "#00101FA peace obtained by sacrificing KeA is\x01",
            "absolutely wrong.\x02\x03",
            "#00103FTaking back KeA... Even just to do\x01",
            "that first step... We must make this\x01",
            "operation succeed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AB")

    label("loc_4C9")


    ChrTalk(
        0xFE,
        (
            "#00103FThe "independent state" declaration of\x01",
            "invalidity... I still don't know if it\x01",
            "is the right thing to do. However...\x02\x03",
            "#00100FTaking back KeA... Even just to do\x01",
            "that first step... We must make this\x01",
            "operation succeed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AB")

    TalkEnd(0xFE)
    Return()

    # Function_3_382 end

    def Function_4_5AF(): pass

    label("Function_4_5AF")


    ChrTalk(
        0x8,
        (
            "#00103FThe "Independent State of Crossbell"\x01",
            "declaration of invalidity... It seems\x01",
            "all that's left is to time the hacking.\x02\x03",
            "#00106F...*sigh*, I think I've gotten tense\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha... I can't blame you.\x02\x03",
            "#00003FAfter all, you could say this\x01",
            "temporary peace in Crossbell\x01",
            "will be shaken by our own hands.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#00108F...I wonder if what we're trying to do is\x01",
            "right.\x02\x03",
            "#00103FThe many people living in Crossbell enjoy\x01",
            "peace, protected from the major powers\x01",
            "thanks to "uncle" and the others...\x02\x03",
            "#00108FWe're trying to take that away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Yeah.\x02\x03",
            "#00001FHowever, the present peace\x01",
            "involves KeA being used by\x01",
            "President Dieter and the others.\x02\x03",
            "#00003FAlmost none of the citizens know\x01",
            "about it, but... To us, it's a\x01",
            "great problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00108F...Yes, you're right.\x02\x03",
            "#00103FA peace obtained by\x01",
            "sacrificing KeA is absolutely\x01",
            "wrong.\x02\x03",
            "#00100F...*giggle*, thank you, Lloyd.\x01",
            "Thanks to you I feel my doubts\x01",
            "have lessened a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, I'm glad I could help.\x02\x03",
            "#00000FTo take back KeA... Even just for\x01",
            "that, we must make this operation\x01",
            "a success, no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00100FYes... Let's do our\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 0)
    Return()

    # Function_4_5AF end

    def Function_5_A31(): pass

    label("Function_5_A31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_A42")
    Jump("loc_E2E")

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B80")

    ChrTalk(
        0x9,
        (
            "#10703FThe Steel Maiden...\x02\x03",
            "#10701FNow that I think about it, I\x01",
            "haven't yet repaid her for\x01",
            "breaking Yin's mask.\x02\x03",
            "#10706FI don't know how long I'll be\x01",
            "able to hold my ground against\x01",
            "a master like her, but...\x02\x03",
            "#10701FI'll never yield. I have a\x01",
            "mission I must accomplish.\x01",
            "...I can't lose.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_C43")

    label("loc_B80")


    ChrTalk(
        0x9,
        (
            "#10703FI don't know how how long I'll be\x01",
            "able to hold my ground against a\x01",
            "master like the Steel Maiden, but...\x02\x03",
            "#10701FI'll never yield. I have a mission I\x01",
            "must accomplish. ...I can't lose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C43")

    Jump("loc_E2E")

    label("loc_C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C63")
    Call(0, 6)
    Jump("loc_E2E")

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA2")

    ChrTalk(
        0x9,
        (
            "#10703FI obtained the resistance force intel\x01",
            "from the State Guard when I was\x01",
            "hiding in the Ancient Battlefield.\x02\x03",
            "#10708F...Come to think of it, I'm indebted\x01",
            "to Heiyue for many things as well.\x02\x03",
            "My contract ended up being broken\x01",
            "like that...\x02\x03",
            "#10703FOne day, I'll have to repay Cao and\x01",
            "the others.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_E2E")

    label("loc_DA2")


    ChrTalk(
        0x9,
        (
            "#10708F...Come to think of it,\x01",
            "I'm indebted to Heiyue\x01",
            "for many things as well.\x02\x03",
            "#10703FOne day, I'll have to\x01",
            "repay Cao and the\x01",
            "others.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2E")

    TalkEnd(0xFE)
    Return()

    # Function_5_A31 end

    def Function_6_E32(): pass

    label("Function_6_E32")


    ChrTalk(
        0x9,
        (
            "#10702FIlya... I'm glad she's\x01",
            "regained consciousness.\x02\x03",
            "#10703F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Rixia, when you want\x01",
            "to see Ilya again,\x01",
            "please just let us know.\x02\x03",
            "#00000FI'll definitely make\x01",
            "time for us to go to St.\x01",
            "Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10702FHaha. Thanks for your concern.\x02\x03",
            "#10703FHowever, for now I've decided\x01",
            "to focus my efforts on freeing\x01",
            "Crossbell City and Arc-en-Ciel.\x02\x03",
            "#10701FIt's also in order to stand\x01",
            "proudly before Ilya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...I see. Then, we must\x01",
            "accomplish that without\x01",
            "losing any time.\x02\x03",
            "#00004FI think we'll have to work\x01",
            "even harder so you can see\x01",
            "Ilya as well.\x02\x03",
            "#00000FFor KeA, Ilya and the rest of\x01",
            "our friends as well... Let's\x01",
            "both do our very best, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10702FYes...! Let's!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 3)
    Return()

    # Function_6_E32 end

    def Function_7_10FD(): pass

    label("Function_7_10FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_110E")
    Jump("loc_1502")

    label("loc_110E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1339")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128A")

    ChrTalk(
        0xA,
        (
            "#01203F#3CIt seems the Support Section\x01",
            "members are gathering one\x01",
            "after the next.\x02\x03",
            "#01200FWhen you no longer require\x01",
            "my support, I intend to stay\x01",
            "in the rear once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah... I know.\x02\x03",
            "#00000FHowever, until then,\x01",
            "I'll be counting on you,\x01",
            "Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01200F#3CHehe, that goes without\x01",
            "saying. I'll shall carry\x01",
            "out my role as police dog.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1334")

    label("loc_128A")


    ChrTalk(
        0xA,
        (
            "#01200F#3CWhen you no longer require\x01",
            "my support, I intend to stay\x01",
            "in the back once again.\x02\x03",
            "However, since I'll shall\x01",
            "carry out my role of police\x01",
            "dog, you can relax.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1334")

    Jump("loc_1502")

    label("loc_1339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1502")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1354")
    Call(0, 8)
    Jump("loc_1502")

    label("loc_1354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1471")

    ChrTalk(
        0xA,
        (
            "#01203F#3CI can't use that stuff... The\x01",
            "tactical orbments you all have,\x01",
            "but...\x02\x03",
            "#01200FAs a Divine Wolf, I know some skills\x01",
            "and even crafts that could be useful\x01",
            "to you as they have been in the past.\x02\x03",
            "Lloyd, once again I'll be looking at\x01",
            "your skills as a leader.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1502")

    label("loc_1471")


    ChrTalk(
        0xA,
        (
            "#01200F#3CLloyd, once again I'll\x01",
            "be looking at your\x01",
            "skills as a leader.\x02\x03",
            "#01203FHehe. You should freely\x01",
            "draw out my power as a\x01",
            "Divine Wolf.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1502")

    TalkEnd(0xFE)
    Return()

    # Function_7_10FD end

    def Function_8_1506(): pass

    label("Function_8_1506")


    ChrTalk(
        0xA,
        (
            "#01200F#3CSt. Ursula Hospital,\x01",
            "huh...\x02\x03",
            "#01203F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FZeit...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01203F#3CHehe, it's nothing. It\x01",
            "was just a memory from\x01",
            "my past.\x02\x03",
            "#01200FEven so, I have helped\x01",
            "you many times up to\x01",
            "now...\x02\x03",
            "But I think this was the\x01",
            "first time I travelled\x01",
            "the highway with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha... Indeed, you're\x01",
            "right.\x02\x03",
            "#00000FIt's nice to be working with\x01",
            "you for the time being. I'm\x01",
            "counting on you, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01200F#3CHehe. Once again I'll be\x01",
            "looking at your skills\x01",
            "as a leader.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 7)
    Return()

    # Function_8_1506 end

    def Function_9_16F5(): pass

    label("Function_9_16F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_18C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1713")
    Call(0, 10)
    Jump("loc_18C3")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1840")

    ChrTalk(
        0xB,
        (
            "#02105FI'd never imagined you\x01",
            "guys would've managed to\x01",
            "beat that Arios MacLaine.\x02\x03",
            "#02102FHaha. Your big sis here\x01",
            "is happy that you've\x01",
            "grown up a lot☆\x02\x03",
            "#02104FI think you'll be able to\x01",
            "overcome anything now.\x02\x03",
            "#02109FAt this rate, we'll\x01",
            "welcome the best happy\x01",
            "end with everyone!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_18C3")

    label("loc_1840")


    ChrTalk(
        0xB,
        (
            "#02104FI think you'll be able\x01",
            "to overcome anything\x01",
            "now.\x02\x03",
            "#02109FAt this rate, we'll\x01",
            "welcome the best happy\x01",
            "end with everyone!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C3")

    Jump("loc_1F45")

    label("loc_18C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_1A7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0C")

    ChrTalk(
        0xB,
        (
            "#02104FI'll take as many pictures as possible\x01",
            "while inside this Huge Tree.\x02\x03",
            "#02100FThen, when I return to the news\x01",
            "agency, I'll turn them into an article\x01",
            "about the truth of this case...\x02\x03",
            "#02102FAnd so, guys, do your best and solve\x01",
            "this case!\x02\x03",
            "#02109FLet me write the best page-three\x01",
            "article!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1A79")

    label("loc_1A0C")


    ChrTalk(
        0xB,
        (
            "#02100FLloyd, guys, do your\x01",
            "best and solve this\x01",
            "case!\x02\x03",
            "#02109FLet me write the best\x01",
            "page-three article!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A79")

    Jump("loc_1F45")

    label("loc_1A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C15")

    ChrTalk(
        0xB,
        (
            "#02106FI can't believe that Huge Tree appeared\x01",
            "in the Marshlands.\x02\x03",
            "#02100FIts height surpasses by far that of\x01",
            "Orchis Tower. I'm pretty sure it can be\x01",
            "seen even from the Empire and Republic.\x02\x03",
            "#02103FThe whole continent is most likely\x01",
            "observing what's going on in Crossbell\x01",
            "right now...\x02\x03",
            "#02102FThat being the case, I'll follow you\x01",
            "around as well, even at the risk of my\x01",
            "life!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1CD2")

    label("loc_1C15")


    ChrTalk(
        0xB,
        (
            "#02103FThe whole continent is most\x01",
            "likely observing what's going\x01",
            "on in Crossbell right now...\x02\x03",
            "#02102FThat being the case, I'll\x01",
            "follow you around as well,\x01",
            "even at the risk of my life!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD2")

    Jump("loc_1F45")

    label("loc_1CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1F45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E84")

    ChrTalk(
        0xB,
        (
            "#02103FSaving Chairman MacDowell, a state\x01",
            "representative, and announcing his words\x01",
            "inside and outside the country...\x02\x03",
            "#02100FIf that can be realized, the State Guard\x01",
            "will probably have to change to a wait-\x01",
            "and-see status.\x02\x03",
            "#02104FPreparations for the Chairman's\x01",
            "announcement will also be different than\x01",
            "usual... It'll be the biggest scoop ever!\x02\x03",
            "#02102FHaha. Do your best and rescue the\x01",
            "Chairman!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1F45")

    label("loc_1E84")


    ChrTalk(
        0xB,
        (
            "#02104FThe announcement of Chairman MacDowell's\x01",
            "views... I guess there's no other way to sway\x01",
            "the legitimacy of the state independence.\x02\x03",
            "#02102FHaha. Do your best and rescue the Chairman!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F45")

    TalkEnd(0xFE)
    Return()

    # Function_9_16F5 end

    def Function_10_1F49(): pass

    label("Function_10_1F49")


    ChrTalk(
        0xB,
        (
            "#02105FIt seems you beat that Arios\x01",
            "MacLaine, eh?\x02\x03",
            "#02106F*sigh*... To think that you guys\x01",
            "could do that much...\x02\x03",
            "#02109FI guess the time to call you guys\x01",
            ""Heroes of Crossbell" has finally\x01",
            "come. Maaan, isn't this a big scoop!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHaha... That's excessive\x01",
            "flattery, you know.\x02\x03",
            "#00000FAnd, I think the fact\x01",
            "that Arios is a hero to\x01",
            "Crossbell hasn't changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FHehe... You've grown up too,\x01",
            "Lloyd.\x02\x03",
            "#02102FSince you guys have surpassed\x01",
            "Arios, I think you'll be able\x01",
            "to overcome anything now.\x02\x03",
            "#02109FAt this rate, we'll welcome\x01",
            "the best happy end with\x01",
            "everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 0)
    Return()

    # Function_10_1F49 end

    def Function_11_21A6(): pass

    label("Function_11_21A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x5, 0xFF)
    SetChrFlags(0xB, 0x80)
    PlayBGM("ed7534", 0)
    SetChrPos(0x101, 0, 0, -2000, 180)
    SetChrPos(0x102, 1050, 0, -2950, 270)
    SetChrPos(0x103, -950, 0, -3250, 90)
    SetChrPos(0x104, 0, 0, -4250, 0)
    OP_68(1840, 1100, 14830, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(27300, 0)
    OP_68(0, 1100, -3000, 7000)
    MoveCamera(51, 25, 0, 7000)
    OP_6E(800, 7000)
    SetCameraDistance(18480, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1100, -3000, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10200, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00306F#12PCome to think of it, I\x01",
            "feel we've come real\x01",
            "far, haven't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PRight... Even though the\x01",
            "fact that we are inside tiny\x01",
            "Crossbell hasn't changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11P...I think that maybe it's not just because\x01",
            "of us, but because Crossbell... No, because\x01",
            "the entire continent has been set in motion.\x02\x03",
            "#00108FWe could be witnessing a historical turning\x01",
            "point...\x02\x03",
            "............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...Elie.\x02\x03",
            "#00008FAs I thought, you have difficulty\x01",
            "taking an aggressive position against\x01",
            "Miss Mariabell and the President?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PThat's right... After all, they're\x01",
            "people I'm very close with.\x02\x03",
            "#00108FAnd from a political point of view,\x01",
            "there's also a part of me that can't\x01",
            "deny what they're trying to do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell, there're a whole load of\x01",
            "guys doin' more dirty stuff like\x01",
            "the Blood and Iron Chancellor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11P─However, I can say only\x01",
            "this:\x02\x03",
            "#00101FNo matter how much the\x01",
            "situation changes, we're the\x01",
            ""Special Support Section".\x02\x03",
            "I think that part won't\x01",
            "change no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PElie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#6P... Elie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PHaha, what's with you\x01",
            "all of a sudden, milady?\x02\x03",
            "#00302FWasn't the police just a\x01",
            "temporary job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11P*giggle*, in the very beginning,\x01",
            "yes.\x02\x03",
            "#00104F... But not anymore. I've already\x01",
            "been taken in.\x02\x03",
            "Perhaps, no matter wich path I'd\x01",
            "decide to take in the future...\x02\x03",
            "#00102FI feel that the days I spent with\x01",
            "you all, would continue to be part\x01",
            "of my fundamentals even afterwards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5P...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PI too... feel the same\x01",
            "way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#12PHaha, in that sense, it was\x01",
            "fortunate that chief started\x01",
            "up this post, isn't it.\x02\x03",
            "#00305FNo, what started it all was\x01",
            "Lloyd's brother's idea, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PHaha. Though I think not\x01",
            "even he could've imagined\x01",
            "a situation like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00001F#5P... We'll take KeA back and\x01",
            "solve this case.\x02\x03",
            "That might be a metaphor for\x01",
            "the duties we must complete as\x01",
            "the Special Support Section.\x02\x03",
            "#00004FHowever, I don't think we have\x01",
            "to force ourselves to reason\x01",
            "like that.\x02\x03",
            "For now, we'll just proceed\x01",
            "facing forward...\x02\x03",
            "#00000FFor the sake of that which is\x01",
            "precious to us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PWe also must search for\x01",
            "chief, whose information\x01",
            "we lack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#12PHaha... Right.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(9200, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 70)
    StopSound(497, 1000, 30)
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie has joined the\x01",
            "party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x1, 0x11F)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie has learned the\x01\x07\x02",
            "Divine Crusade\x07\x05",
            " S-Craft.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Set "Divine Crusade"\x07\x05",
            " as S-Break?",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D01")
    SetChrChipPat(0x1, 0x6, 0x11F)

    label("loc_2D01")

    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because Elie joined, the\x01",
            "number of party members\x01",
            "has exceeded six.\x02\x03",
            "Please select the members\x01",
            "who will join the party\x01",
            "from the following screen.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PartySelect(0)
    PartySelect(2)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hereafter, you will be able to organize the\x01",
            "party formation by talking to Abbas on the\x01",
            "bridge.\x02\x03",
            "Furthermore, if you wish to advance the story,\x01",
            "please select the "Booster Site" at the east\x01",
            "corner of the Merkabah's navigation map.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A4, 1)
    OP_29(0xAF, 0x1, 0x14)
    SetScenarioFlags(0x31, 6)
    SetScenarioFlags(0x31, 7)
    EventEnd(0x5)
    NewScene("e3020", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_21A6 end

    SaveToFile()

Try(main)
