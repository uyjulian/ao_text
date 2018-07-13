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
        "Function_4_59B",          # 04, 4
        "Function_5_A6C",          # 05, 5
        "Function_6_EA1",          # 06, 6
        "Function_7_118C",         # 07, 7
        "Function_8_15A2",         # 08, 8
        "Function_9_1794",         # 09, 9
        "Function_10_1FF6",        # 0A, 10
        "Function_11_2253",        # 0B, 11
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
    Jump("loc_597")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF")

    ChrTalk(
        0xFE,
        (
            "#00103FThe "Independent State" declaration\x01",
            "of invalidity... I don't know if \x01",
            "that's correct yet, however...\x02\x03",
            "#00101FA peace obtained by\x01",
            "sacrificing KeA is\x01",
            "absolutely wrong.\x02\x03",
            "#00103FTaking back KeA...\x01",
            "Even in order to do that first step...\x01",
            "We must make this operation succeed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_597")

    label("loc_4BF")


    ChrTalk(
        0xFE,
        (
            "#00103FThe "Independent State" declaration\x01",
            "of invalidity... I don't know if \x01",
            "that's correct yet, however...\x02\x03",
            "#00100FTaking back KeA...\x01",
            "Even in order to do that first step...\x01",
            "We must make this operation succeed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_597")

    TalkEnd(0xFE)
    Return()

    # Function_3_382 end

    def Function_4_59B(): pass

    label("Function_4_59B")


    ChrTalk(
        0x8,
        (
            "#00103FThe "Independent State of Crossbell"\x01",
            "declaration of invalidity... What seems to\x01",
            "remain is to time the timing of the hacking.\x02\x03",
            "#00106F...*sigh*, I think I've gotten tense somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha...I can't blame you.\x02\x03",
            "#00003FAfter all, you can say that the temporary\x01",
            "peace that exists in the land of Crossbell\x01",
            "is going to be shaken by our own hands.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#00108F...I wonder if what we're\x01",
            "trying to do is correct.\x02\x03",
            "#00103FThe many people living in Crossbell are\x01",
            "enjoying a peace protected from the two\x01",
            "major powers thanks to "uncle" and the others...\x02\x03",
            "#00108FWe're trying to\x01",
            "take that away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Yeah.\x02\x03",
            "#00001FHowever, the present peace\x01",
            "consists in KeA getting used by\x01",
            "President Dieter and the others.\x02\x03",
            "#00003FAlmost all the citizens don't\x01",
            "know about such a situation, but...\x01",
            "To us, it's a great problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00108F...Yes, you're right.\x02\x03",
            "#00103FA peace obtained by\x01",
            "sacrificing KeA is\x01",
            "absolutely wrong.\x02\x03",
            "#00100F...*giggle*, thank you, Lloyd.\x01",
            "Thanks to you I feel my doubts\x01",
            "have disappeared a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, I'm glad if I could help you.\x02\x03",
            "#00000FTo get back KeA...\x01",
            "Even for that, we must make this\x01",
            "operation succeed no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00100FYes...let's do our best.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 0)
    Return()

    # Function_4_59B end

    def Function_5_A6C(): pass

    label("Function_5_A6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_A7D")
    Jump("loc_E9D")

    label("loc_A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC4")

    ChrTalk(
        0x9,
        (
            "#10703FThe "Steel Maiden"...\x02\x03",
            "#10701FNow that I think about it, I\x01",
            "haven't paid her back yet for\x01",
            "having broken "Yin"'s mask.\x02\x03",
            "#10706FI don't know how much\x01",
            "I'll be able to stand my ground\x01",
            "against such a master, but...\x02\x03",
            "#10701FI'll never yield, I have a\x01",
            "mission I must accomplish.\x01",
            "...I won't lose.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_C87")

    label("loc_BC4")


    ChrTalk(
        0x9,
        (
            "#10703FI don't know how much I'll be \x01",
            "able to stand my ground against a\x01",
            "master like the "Steel Maiden", but...\x02\x03",
            "#10701FI'll never yield, I have a\x01",
            "mission I must accomplish.\x01",
            "...I won't lose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C87")

    Jump("loc_E9D")

    label("loc_C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA7")
    Call(0, 6)
    Jump("loc_E9D")

    label("loc_CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0B")

    ChrTalk(
        0x9,
        (
            "#10703FAbout the Resistance forces intel in the Mainz\x01",
            "area, I obtained that from the State Guard\x01",
            "when I was hiding in the Ancient Battlefield.\x02\x03",
            "#10708F...Come to think of it, I'm indebted\x01",
            "to the "Heiyue" for many things too.\x02\x03",
            "My contract ended up\x01",
            "being broken like that...\x02\x03",
            "#10703FOne day, I'll have to repay\x01",
            "Mr. Cao and the others.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_E9D")

    label("loc_E0B")


    ChrTalk(
        0x9,
        (
            "#10708F...Come to think of it, I'm indebted\x01",
            "to the "Heiyue" for many things too.\x02\x03",
            "#10703FOne day, I'll have to repay\x01",
            "Mr. Cao and the others.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9D")

    TalkEnd(0xFE)
    Return()

    # Function_5_A6C end

    def Function_6_EA1(): pass

    label("Function_6_EA1")


    ChrTalk(
        0x9,
        (
            "#10702FMiss Ilya... I'm glad she\x01",
            "has regained consciousness.\x02\x03",
            "#10703F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Rixia, when you want to meet\x01",
            "Miss Ilya again, please say it\x01",
            "without any reserve.\x02\x03",
            "#00000FI'll absolutely find some time\x01",
            "and direct to St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10702FUh uh, thank you\x01",
            "for your concern.\x02\x03",
            "#10703FHowever, for now I decided to \x01",
            "focus my efforts on freeing \x01",
            "Crossbell City and Arc-en-ciel.\x02\x03",
            "#10701FIt's also in order\x01",
            "to stand proudly\x01",
            "before Miss Ilya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...I see.\x01",
            "Then, we must accomplish\x01",
            "that without losing any time.\x02\x03",
            "#00004FI think we'll have to do more\x01",
            "of our best so that you can\x01",
            "meet Miss Ilya too.\x02\x03",
            "#00000FFor KeA, Miss Ilya and\x01",
            "our comrades too...\x01",
            "Let's both make our best, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10702FYes...!\x01",
            "Please!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 3)
    Return()

    # Function_6_EA1 end

    def Function_7_118C(): pass

    label("Function_7_118C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_119D")
    Jump("loc_159E")

    label("loc_119D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_13DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1324")

    ChrTalk(
        0xA,
        (
            "#01203F#3CIt seems that the Support Section\x01",
            "members are gathering one after the other.\x02\x03",
            "#01200FWhen you won't be in need of\x01",
            "my support anymore, I intend to\x01",
            "stay in the back once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah...I know.\x02\x03",
            "#00000FHowever, until then,\x01",
            "I'm counting on you, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01200F#3CHu hu, it goes without saying.\x01",
            "I'll carry out my role\x01",
            "of police dog firmly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_13D9")

    label("loc_1324")


    ChrTalk(
        0xA,
        (
            "#01200F#3CWhen you won't be in need of\x01",
            "my support anymore, I intend to\x01",
            "stay in the back once again.\x02\x03",
            "However, since I'll carry\x01",
            "out my role of police dog\x01",
            "firmly, you can relax.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D9")

    Jump("loc_159E")

    label("loc_13DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_159E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F9")
    Call(0, 8)
    Jump("loc_159E")

    label("loc_13F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1507")

    ChrTalk(
        0xA,
        (
            "#01203F#3CI can't use that stuff...\x01",
            "The Tactics Orbments\x01",
            "you all have, but...\x02\x03",
            "#01200FAs a Divine Wolf, I know some\x01",
            "skills and even crafts that could\x01",
            "be useful to you as in the past.\x02\x03",
            "Lloyd, once again I'll\x01",
            "be looking at your \x01",
            "skills as a leader.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_159E")

    label("loc_1507")


    ChrTalk(
        0xA,
        (
            "#01200F#3CLloyd, once again I'll\x01",
            "be looking at your \x01",
            "skills as a leader.\x02\x03",
            "#01203FHu hu, you can try to freely draw\x01",
            "out my power as a Divine Wolf.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159E")

    TalkEnd(0xFE)
    Return()

    # Function_7_118C end

    def Function_8_15A2(): pass

    label("Function_8_15A2")


    ChrTalk(
        0xA,
        (
            "#01200F#3CSt. Ursula Hospital, eh...?\x02\x03",
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
            "#01203F#3CHu hu, it's nothing.\x01",
            "I was slightly remembered of the past.\x02\x03",
            "#01200FEven so, I helped you\x01",
            "many times until now...\x02\x03",
            "But I think this was the first time\x01",
            "I travelled the highway with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha... Indeed, you're right.\x02\x03",
            "#00000FIt's nice to be working with you for the time being.\x01",
            "I'm counting on you, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01200F#3CHu hu, once again I'll\x01",
            "be looking at your \x01",
            "skills as a leader.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 7)
    Return()

    # Function_8_15A2 end

    def Function_9_1794(): pass

    label("Function_9_1794")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_1977")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B2")
    Call(0, 10)
    Jump("loc_1972")

    label("loc_17B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18EA")

    ChrTalk(
        0xB,
        (
            "#02105FI'd never imagined that you\x01",
            "guys would've managed to\x01",
            "beat that Arios MacLaine.\x02\x03",
            "#02102FUh uh, your big sis here\x01",
            "is happy that you've\x01",
            "grown up a lot☆\x02\x03",
            "#02104FI think that you'll be able\x01",
            "to overcome anything now.\x02\x03",
            "#02109FAt this rate, we'll welcome the\x01",
            "best happy end with everyone!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1972")

    label("loc_18EA")


    ChrTalk(
        0xB,
        (
            "#02104FI think that you'll be able\x01",
            "to overcome anything now.\x02\x03",
            "#02109FAt this rate, we'll welcome the\x01",
            "best happy end with everyone!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1972")

    Jump("loc_1FF2")

    label("loc_1977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_1B27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB7")

    ChrTalk(
        0xB,
        (
            "#02104FI'll take as many picture as\x01",
            "possible while in the " huge tree".\x02\x03",
            "#02100FThen, when I'll return to the\x01",
            "news agency, I'll turn them into\x01",
            "an article about this case truth...\x02\x03",
            "#02102FThat's why, guys, do your \x01",
            "best and solve this case!\x02\x03",
            "#02109FMake me write the best\x01",
            "page-three news!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1B22")

    label("loc_1AB7")


    ChrTalk(
        0xB,
        (
            "#02100FLloyd, guys, do your\x01",
            "best and solve this case!\x02\x03",
            "#02109FMake me write the best\x01",
            "page-three news!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B22")

    Jump("loc_1FF2")

    label("loc_1B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA3")

    ChrTalk(
        0xB,
        (
            "#02106FTo think that such a "huge tree" would\x01",
            "appear in the Marshlands, eh?\x02\x03",
            "#02100FIt's got a height that surpasse by far\x01",
            "Orchis Tower. I guess it can be seen \x01",
            "from the Empire and Republic too.\x02\x03",
            "#02103FProbably the whole continent is\x01",
            "observing Crossbell moves now...\x02\x03",
            "#02102FBeing this the case, I'll follow you\x01",
            "around too at the risk of my life!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1D40")

    label("loc_1CA3")


    ChrTalk(
        0xB,
        (
            "#02103FProbably the whole continent is\x01",
            "observing Crossbell moves now...\x02\x03",
            "#02102FBeing this the case, I'll follow you\x01",
            "around too at the risk of my life!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D40")

    Jump("loc_1FF2")

    label("loc_1D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1FF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F21")

    ChrTalk(
        0xB,
        (
            "#02103FSaving Chairman MacDowell who is one of the\x01",
            "autonomous state representatives and announcing\x01",
            "his words inside and outside the country...\x02\x03",
            "#02100FIf this can be realized, at least the\x01",
            "State Guard will probably have to\x01",
            "turn to a wait-and-see status.\x02\x03",
            "#02104FThe way the Chariman's words\x01",
            "will be announced needs to be\x01",
            "prepared differently than usual...\x01",
            "Seems it'll become the best scoop!\x02\x03",
            "#02102FUh uh, do your best and\x01",
            "rescue the Chairman!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1FF2")

    label("loc_1F21")


    ChrTalk(
        0xB,
        (
            "#02104FThe announcement of Chairman MacDowell's opinion...\x01",
            "I guess there's no other way to be able to sway\x01",
            "the rightfulness of the state independence.\x02\x03",
            "#02102FHu hu, do your best and\x01",
            "rescue the Chairman!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF2")

    TalkEnd(0xFE)
    Return()

    # Function_9_1794 end

    def Function_10_1FF6(): pass

    label("Function_10_1FF6")


    ChrTalk(
        0xB,
        (
            "#02105FIt seems you beat that\x01",
            "Arios MacLaine, eh?\x02\x03",
            "#02106F*haaah*...\x01",
            "To think that you guys\x01",
            "could do that much...\x02\x03",
            "#02109FI guess the moment to change\x01",
            ""Crossbell Hero" has come too.\x01",
            "Weeell, ain't this a big a scoop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHa ha...you praise us too much.\x02\x03",
            "#00000FAlso, I think that to Crossbell,\x01",
            "the fact that Mr. Arios is a\x01",
            "hero is still invariant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FHu hu...\x01",
            "You've grown up too, Lloyd.\x02\x03",
            "#02102FSince you guys have surpassed \x01",
            "Mr. Arios, I think that you'll be\x01",
            "able to overcome anything now.\x02\x03",
            "#02109FAt this rate, we'll welcome the\x01",
            "best happy end with everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 0)
    Return()

    # Function_10_1FF6 end

    def Function_11_2253(): pass

    label("Function_11_2253")

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
            "#00306F#12PAt any rate, come to think of it,\x01",
            "I feel we've come far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PRight...\x01",
            "Although it doesn't change the fact\x01",
            "that we are inside the small Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11P...I think that maybe it's not just\x01",
            "because of us, but because Crossbell...\x01",
            "No, because the entire continent has begun to act.\x02\x03",
            "#00108FIt could be that we're witnessing\x01",
            "a historical turning point...\x02\x03",
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
            "#00106F#11PYou're right... After all, to me they're\x01",
            "people I'm deeply familiar with.\x02\x03",
            "#00108FAlso, from a political point of view,\x01",
            "there's also a part of me who can't\x01",
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
            "guys doin' more dirty stuff like \x01",
            "the Blood and Iron Chancellor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11P──However, I can only say this.\x02\x03",
            "#00101FNo matter how much the situation changes,\x01",
            "we're the "Special Support Section".\x02\x03",
            "I think only that part won't\x01",
            "sway no matter what.\x02",
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
        "#00202F#6P...Miss Elie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PHa ha, what's with you, milady.\x02\x03",
            "#00302FWasn't the police just a\x01",
            "temporary employment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11P*giggle*, in the very beginning, yes.\x02\x03",
            "#00104F...But not anymore.\x01",
            "I've already been taken in.\x02\x03",
            "Perhaps, no matter wich path\x01",
            "I'd decide to take in the future...\x02\x03",
            "#00102FI feel that the days I spent\x01",
            "with you all would continue to be\x01",
            "my fundamentals even afterwards.\x02",
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
        "#00204F#6PI too...feel the same.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#12PHa ha, in that sense,\x01",
            "the Chief too started a\x01",
            "fortunate duty post.\x02\x03",
            "#00305FNo, what started it all was\x01",
            "Lloyd's big bro's idea, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PHa ha, though I think that\x01",
            "non even him would've\x01",
            "imagined such a situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00001F#5P...We'll take KeA back\x01",
            "and solve this case.\x02\x03",
            "That could be a metaphor of the missions we\x01",
            "have to complete as the Special Support Section.\x02\x03",
            "#00004FHowever, I believe we can even\x01",
            "not force us to reason like that.\x02\x03",
            "Now, we'll just proceed \x01",
            "facing forward...\x02\x03",
            "#00000FFor what's precious to us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PWe also must search for Chief\x01",
            "whose news we are lacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#12PHa ha...right.\x02",
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
            "Elie has joined the party.\x07\x00\x02",
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
            ""Divine Crusade"\x07\x05",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D90")
    SetChrChipPat(0x1, 0x6, 0x11F)

    label("loc_2D90")

    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because Elie joined, the fixed number of\x01",
            "party members has become more than six.\x02\x03",
            "Please select once again the \x01",
            "members who will join the party\x01",
            "from the following ones.\x07\x00\x02",
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
            "Hereafter, you will be able to \x01",
            "organise the party formation by \x01",
            "talking to Abbas on the bridge.\x02\x03",
            "Still more, when advancing the story,\x01",
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

    # Function_11_2253 end

    SaveToFile()

Try(main)
