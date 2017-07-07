from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e3020_1.bin",                # FileName
        "e3020",                    # MapName
        "e3020",                    # Location
        0x0000,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [312, 2211, 3054, 7510, 8130, 9138, 9791, 13175, 14343, 0, 14961, 0, 15811, 16579, 17348, 20335, 0, 21233, 0, 80, 85, 0, 0],
    )

    BuildStringList((
        "e3020_1",                # 0
    ))

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_8A3",          # 01, 1
        "Function_2_BEE",          # 02, 2
        "Function_3_1D56",         # 03, 3
        "Function_4_1FC2",         # 04, 4
        "Function_5_23B2",         # 05, 5
        "Function_6_263F",         # 06, 6
        "Function_7_3377",         # 07, 7
        "Function_8_3807",         # 08, 8
        "Function_9_3A71",         # 09, 9
        "Function_10_3DC3",        # 0A, 10
        "Function_11_40C3",        # 0B, 11
        "Function_12_43C4",        # 0C, 12
        "Function_13_4F6F",        # 0D, 13
        "Function_14_52F1",        # 0E, 14
        "Function_15_5550",        # 0F, 15
        "Function_16_6D48",        # 10, 16
        "Function_17_6EFC",        # 11, 17
        "Function_18_736F",        # 12, 18
        "Function_19_7764",        # 13, 19
        "Function_20_8582",        # 14, 20
        "Function_21_8943",        # 15, 21
        "Function_22_8C72",        # 16, 22
        "Function_23_9AC5",        # 17, 23
        "Function_24_9D9D",        # 18, 24
        "Function_25_A444",        # 19, 25
        "Function_26_A778",        # 1A, 26
        "Function_27_C3C6",        # 1B, 27
        "Function_28_C67F",        # 1C, 28
        "Function_29_C776",        # 1D, 29
        "Function_30_CA1D",        # 1E, 30
        "Function_31_CD63",        # 1F, 31
        "Function_32_E6CD",        # 20, 32
        "Function_33_EB4B",        # 21, 33
        "Function_34_EDD0",        # 22, 34
        "Function_35_F74C",        # 23, 35
        "Function_36_F99A",        # 24, 36
        "Function_37_FBC0",        # 25, 37
        "Function_38_100B9",       # 26, 38
        "Function_39_10764",       # 27, 39
        "Function_40_10B7F",       # 28, 40
        "Function_41_10DFC",       # 29, 41
        "Function_42_111B4",       # 2A, 42
        "Function_43_111B8",       # 2B, 43
        "Function_44_12200",       # 2C, 44
        "Function_45_12537",       # 2D, 45
        "Function_46_1253B",       # 2E, 46
        "Function_47_13461",       # 2F, 47
        "Function_48_13657",       # 30, 48
        "Function_49_137AA",       # 31, 49
        "Function_50_13D4E",       # 32, 50
        "Function_51_13E89",       # 33, 51
        "Function_52_1442B",       # 34, 52
        "Function_53_14E4B",       # 35, 53
        "Function_54_157CA",       # 36, 54
        "Function_55_15B0D",       # 37, 55
        "Function_56_15CE5",       # 38, 56
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_38A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156")
    Call(1, 1)
    Jump("loc_385")

    label("loc_156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2")

    ChrTalk(
        0x11,
        (
            "#00101FBell probably for himself\x01",
            "I think that you are participating in this plan.\x02\x03",
            "#00108FTo such a personality of Bell\x01",
            "I was also often confused,\x01",
            "I felt that it was her charm … …\x02\x03",
            "#00103F…… But for whatever reason,\x01",
            "A way to sacrifice someone,\x01",
            "I think that I should never be forgiven.\x02\x03",
            "#00100FAs a close friend from a young bell … …\x01",
            "I'm sure I will correct her mistake.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_385")

    label("loc_2D2")


    ChrTalk(
        0x11,
        (
            "#00103FWhatever the reason,\x01",
            "A way to sacrifice someone,\x01",
            "I think that I should never be forgiven.\x02\x03",
            "#00100FAs a close friend from a young bell … …\x01",
            "I'm sure I will correct her mistake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_385")

    Jump("loc_89F")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_52D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494")

    ChrTalk(
        0x11,
        (
            "#00103FBell as the descendant of the Clois family,\x01",
            "It is quite deeply rooted in this plan as well\x01",
            "You should be involved.\x02\x03",
            "#00108FSurely, the truth we want is,\x01",
            "She and Mr. Ian should have it … …\x02\x03",
            "#00101F… … Let's go, Lloyd.\x01",
            "To regain Ka'a-chan …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_528")

    label("loc_494")


    ChrTalk(
        0x11,
        (
            "#00108FSurely, the truth we want is,\x01",
            "Bell and Ian must have it … …\x02\x03",
            "#00101F… … Let's go, Lloyd.\x01",
            "To regain Ka'a-chan …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_528")

    Jump("loc_89F")

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C")

    ChrTalk(
        0x11,
        (
            "#00108FBell …… Uncle from the beginning\x01",
            "I wonder if I intended to forsake you.\x02\x03",
            "Besides, Professor Ian\x01",
            "It was a masterpiece … ….\x02\x03",
            "#00106F… … It is useless,\x01",
            "It seems I am confused …\x01",
            "I can not make a good idea.\x02\x03",
            "#00100FAnyway, you have to go alone.\x01",
            "To that \"big tree of the blue sky\" …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6CA")

    label("loc_64C")


    ChrTalk(
        0x11,
        (
            "#00108F… …. Too much happening\x01",
            "I'm confused, but ….\x02\x03",
            "#00100FAnyway, you have to go alone.\x01",
            "To that \"big tree of the blue sky\" …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CA")

    Jump("loc_89F")

    label("loc_6CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_89F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F4")

    ChrTalk(
        0x11,
        (
            "#00103FBy my grandfather\x01",
            "By the invalid declaration of an independent country,\x01",
            "It seems that there have been considerable impacts in various places.\x02\x03",
            "#00108FIt seems that the defense army is withdrawing once,\x01",
            "Various disorder may have come out ……\x02\x03",
            "#00100FIn the meantime to stop stopping the \"big bell\"\x01",
            "Even if I look around each place again\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_89F")

    label("loc_7F4")


    ChrTalk(
        0x11,
        (
            "#00103FBy the invalid declaration of an independent country,\x01",
            "Various disorder may have come out ……\x02\x03",
            "#00100FIn the meantime to stop stopping the \"big bell\"\x01",
            "Even if I look around each place again\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89F")

    TalkEnd(0xFE)
    Return()

    # Function_0_138 end

    def Function_1_8A3(): pass

    label("Function_1_8A3")


    ChrTalk(
        0x11,
        (
            "#00100FFinally …\x01",
            "A place where Ka'aa waits\x01",
            "A way has opened up.\x02\x03",
            "#00108FThere, Mr. Ian sensei of the black curtain,\x01",
            "And there is a bell ………………\x02\x03",
            "#00103F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FErie …………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00103F…… Bell probably for himself\x01",
            "I think that you are participating in this plan.\x02\x03",
            "#00108FTo such a personality of Bell\x01",
            "I was also often confused,\x01",
            "I felt that it was her charm … …\x02\x03",
            "#00101F…… But for whatever reason,\x01",
            "A way to sacrifice someone,\x01",
            "I think that I should never be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F… Ah, that's right.\x02\x03",
            "#00001FMr. Maria Bell and Professor Ian's plan\x01",
            "No matter what, no more\x01",
            "I can not let him use Kea.\x02\x03",
            "#00003FEly, she will fight her\x01",
            "It might be painful, but …\x01",
            "Please lend me your strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00103F…… Yeah, I am prepared for it.\x02\x03",
            "#00101FAs a close friend from a young bell … …\x01",
            "I'm sure I will correct her mistake.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 1)
    Return()

    # Function_1_8A3 end

    def Function_2_BEE(): pass

    label("Function_2_BEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C12")
    Call(1, 56)
    Jump("loc_DEA")

    label("loc_C12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C32")
    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xB, 0x101, 0)

    label("loc_C32")


    ChrTalk(
        0xB,
        (
            "#00200FMr. Lloyd,\x01",
            "If you do not mind,\x01",
            "Please take it.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Tio's Account\"\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 1)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        "#00005F\"Pomutto! Account …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204FBecause of this situation,\x01",
            "I wonder if my relaxation is also important.\x02\x03",
            "#00202FI will be your opponent anytime\x01",
            "Please feel free to start a game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FI knew.\x02\x03",
            "#00004F(Tio is pretty\x01",
            "I think it's a strong enemy ….\x01",
            "Do you manage to work hard? )\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEA")
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DEA")

    Jump("loc_1D52")

    label("loc_DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0A")
    Call(1, 5)
    Jump("loc_F69")

    label("loc_E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EED")

    ChrTalk(
        0xB,
        (
            "#00208FProfessor Ian, even Mr. Guy\x01",
            "An opponent who did not arrive …\x01",
            "I am in doubt that preparation is made.\x02\x03",
            "#00203FThen, we\x01",
            "Beyond that\x01",
            "If you do not show maximum preparedness ……\x02\x03",
            "#00202FLet's do our best, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_F69")

    label("loc_EED")


    ChrTalk(
        0xB,
        (
            "#00203FWe are,\x01",
            "More than Mr. Ian\x01",
            "If you do not show maximum preparedness ……\x02\x03",
            "#00202FLet's do our best, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F69")

    Jump("loc_1D52")

    label("loc_F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_1172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A7")

    ChrTalk(
        0xB,
        (
            "#00200FAmong the \"big trees of the blue sky\"\x01",
            "A mysterious space is formed.\x02\x03",
            "#00203FIn the \"monastery\" and \"tower\" by the resonance of the big bell\x01",
            "It goes far beyond the \"place\" that was made,\x01",
            "A world completely ignoring the physical law … …\x02\x03",
            "#00201FWe have cultivated\x01",
            "Every common sense should not pass ……\x01",
            "You'd better go on cautiously.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_116D")

    label("loc_10A7")


    ChrTalk(
        0xB,
        (
            "#00203FAmong the \"big trees of the blue sky\"\x01",
            "I completely ignored the law of physics\x01",
            "A mysterious space is formed.\x02\x03",
            "#00201FWe have cultivated\x01",
            "Every common sense should not pass ……\x01",
            "You'd better go on cautiously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116D")

    Jump("loc_1D52")

    label("loc_1172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_131B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126E")

    ChrTalk(
        0xB,
        (
            "#00200FCertainly, from that \"big tree\"\x01",
            "I feel the wave like Kea.\x02\x03",
            "Mr. Maria Bell,\x01",
            "\"Taiki\" is the key itself\x01",
            "I was wondering … …\x02\x03",
            "#00206F……I do not understand.\x01",
            "Let me appear such things,\x01",
            "What on earth are you planning?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1316")

    label("loc_126E")


    ChrTalk(
        0xB,
        (
            "#00200FMr. Maria Bell,\x01",
            "\"Taiki\" is the key itself\x01",
            "I was wondering … …\x02\x03",
            "#00206F……I do not understand.\x01",
            "Let me appear such things,\x01",
            "What on earth are you planning?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1316")

    Jump("loc_1D52")

    label("loc_131B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_14F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1448")

    ChrTalk(
        0xB,
        (
            "#00200FThis time a new \"gap\" detection\x01",
            "Because it seems to be necessary, Jonah totally\x01",
            "I got the ship 's job taken over.\x02\x03",
            "#00203FThe other party is that \"association\" … …\x01",
            "What kind of steps will you take?\x01",
            "It is not understood.\x02\x03",
            "#00200FAlways include everything including magician\x01",
            "You must keep it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_14EB")

    label("loc_1448")


    ChrTalk(
        0xB,
        (
            "#00203FThe other party is that \"association\" … …\x01",
            "What kind of steps will you take?\x01",
            "It is not what I understood.\x02\x03",
            "#00200FAlways include everything including magician\x01",
            "You must keep it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EB")

    Jump("loc_1D52")

    label("loc_14F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1657")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150B")
    Call(1, 4)
    Jump("loc_1652")

    label("loc_150B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BB")

    ChrTalk(
        0xB,
        (
            "#00204FIt was a short while … ….\x01",
            "I was able to walk with Zeit\x01",
            "It was frankly delightful.\x02\x03",
            "#00202FTo reward him for his asylum,\x01",
            "From now on\x01",
            "I have to work hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1652")

    label("loc_15BB")


    ChrTalk(
        0xB,
        (
            "#00204FWell, I will go back later\x01",
            "Final preparation for hacking\x01",
            "Let's suppose we go to help.\x02\x03",
            "#00211FI trust Jonah's power,\x01",
            "I can not deny that the claws are somewhat sweet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1652")

    Jump("loc_1D52")

    label("loc_1657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1765")

    ChrTalk(
        0xB,
        (
            "#00200FIf you recover Ellie,\x01",
            "Members of the support department as a whole\x01",
            "You will be in line.\x02\x03",
            "#00203FMcDaely's chairman\x01",
            "As confined to confinement,\x01",
            "Security is also quite severe, but …\x02\x03",
            "#00202FZeit also has a dangerous role\x01",
            "It bought me out,\x01",
            "Let's make it absolutely successful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1813")

    label("loc_1765")


    ChrTalk(
        0xB,
        (
            "#00203FMr. Ellie and McDowell chairman\x01",
            "As confined to confinement,\x01",
            "Security is also quite severe, but …\x02\x03",
            "#00200FZeit also has a dangerous role\x01",
            "It bought me out,\x01",
            "Let's make it absolutely successful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1813")

    Jump("loc_1D52")

    label("loc_1818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1993")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F9")

    ChrTalk(
        0xB,
        (
            "#00200FFrom the West Crossbell Highway,\x01",
            "Belgard gate, police school ……\x02\x03",
            "#00206FIn a difficult position\x01",
            "I have found a \"gap\".\x02\x03",
            "#00200F…… But now anyway\x01",
            "You have no choice but to go where you can go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_198E")

    label("loc_18F9")


    ChrTalk(
        0xB,
        (
            "#00206FFrom the West Crossbell Highway,\x01",
            "Belgard gate, police school ……\x02\x03",
            "#00200FAlthough it is a difficult position …\x01",
            "Now I can go anyway\x01",
            "You have no choice but to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_198E")

    Jump("loc_1D52")

    label("loc_1993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AE")
    Call(1, 3)
    Jump("loc_1A2C")

    label("loc_19AE")


    ChrTalk(
        0xB,
        (
            "#00208FThe wolfs of the Zeit's subordinates ……\x01",
            "I wonder what I am doing now.\x02\x03",
            "#00203FIf they can get help\x01",
            "I am encouraged … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A2C")

    Jump("loc_1D52")

    label("loc_1A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1D52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4C")
    Call(1, 56)
    Jump("loc_1D52")

    label("loc_1A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC1")
    EndChrThread(0x8, 0x0)

    ChrTalk(
        0xB,
        (
            "#00203FThe foundation and the church had a cooperative relationship … …\x01",
            "I have heard about rumors,\x01",
            "Finally I got the confirmation.\x02\x03",
            "#00202FAnyway, if this is not a sense of incongruity\x01",
            "It seems to be able to handle terminals.\x02\x03",
            "If you also use the Aion system,\x01",
            "Whether the range of \"clearance\" measures widens considerably.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x8, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BE7")
    Jump("loc_1C31")

    label("loc_1BE7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C07")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C31")

    label("loc_1C07")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C27")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C31")

    label("loc_1C27")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C31")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#00200FMr. Abbas continues\x01",
            "Please teach how to use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12100FWell, I understand.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    SetScenarioFlags(0x0, 4)
    Jump("loc_1D52")

    label("loc_1CC1")


    ChrTalk(
        0xB,
        (
            "#00203FIf you also use the Aion system,\x01",
            "The search range of \"gap\" is also\x01",
            "It seems that it will spread significantly.\x02\x03",
            "#00200FThis is me and Fran\x01",
            "You can leave it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D52")

    TalkEnd(0xFE)
    Return()

    # Function_2_BEE end

    def Function_3_1D56(): pass

    label("Function_3_1D56")

    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0xB,
        (
            "#00205Fby the way……\x01",
            "In the mountain path Zeit's men\x01",
            "You were making a flock.\x02\x03",
            "#00200FAs with Zeit,\x01",
            "Was it a \"god of war\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CNo, they are ordinary wolves to the last.\x02\x03",
            "#01200FHowever, from the time Ursula was alive\x01",
            "While following alternatives, it is followed,\x01",
            "I can say it is my mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00203FThe family of the god of war … in the case of Rubache\x01",
            "It was easy to intimidate military dogs,\x01",
            "Naturally speaking it is natural.\x02\x03",
            "#00208FI hope they are safe too ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CAs for that, before leaving the herd\x01",
            "Because I have said it.\x01",
            "There is nothing to worry about.\x02\x03",
            "#01200FNow let's go ahead with this situation\x01",
            "I guess I'm watching.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_3_1D56 end

    def Function_4_1FC2(): pass

    label("Function_4_1FC2")

    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0xB,
        (
            "#00203F…, okay, and.\x01",
            "This is the end of the treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#01200F#3CWell, I'm going to wear you, Tio.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 500)

    ChrTalk(
        0x101,
        (
            "#00005FZeit ……\x01",
            "Hurt in the battle before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CWell, that 's what you do with that \"red constellation\".\x02\x03",
            "#01200FThe injury itself will be cured soon … …\x01",
            "After all, he and the defense army\x01",
            "It seems like a degree of difficulty to compare.\x02\x03",
            "Thanks to the surprise attack this time\x01",
            "Successfully went well,\x01",
            "The same hand will not work twice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FReally……\x02\x03",
            "#00002FBut I was really saved.\x01",
            "Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CHuff, it does not reach reward.\x02\x03",
            "#01200F…… Well, the strength is in place\x01",
            "Necessarily accompany you also need,\x01",
            "It will be gone.\x02\x03",
            "As before, I will keep it behind\x01",
            "Call me only when you need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00200FWith the magic wand as before\x01",
            "You send a conductive wave.\x01",
            "……OK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3CAlso from now on\x01",
            "With it returned to its original form\x01",
            "Let's rush to the front.\x02\x03",
            "#01203FIf there is a demon beast like that\x01",
            "I should be able to drink it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, in that figure\x01",
            "If you are rushed\x01",
            "It is quite reassuring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00202FWell then, Zeit.\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x1D7, 0)
    Return()

    # Function_4_1FC2 end

    def Function_5_23B2(): pass

    label("Function_5_23B2")


    ChrTalk(
        0xB,
        (
            "#00203F…… Professor Ian was supposed to be familiar\x01",
            "I heard that he picked up Mr. Guy ……\x01",
            "I was a little anxious.\x02\x03",
            "#00208FI have to do that far\x01",
            "\"Plan of Aiki zero\" is one … …\x02\x03",
            "#00206FAbove all, even Mr. Guy\x01",
            "To the opponent who did not arrive,\x01",
            "Will we reach …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F… … That's right\x01",
            "It certainly may be uneasy.\x02\x03",
            "#00008FMr. Ian's resolution is probably,\x01",
            "It will be more than that Arios.\x02\x03",
            "#00001FBut …. That's why,\x01",
            "We are prepared more than Ian sensei\x01",
            "I think that I have to show it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00208FI was prepared to over Professor Ian ……\x01",
            "……I agree.\x02\x03",
            "#00201FLet's do our best, Mr. Lloyd.\x01",
            "Now is the time to overcome Guy\x01",
            "What do you think it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh … Of course!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 2)
    Return()

    # Function_5_23B2 end

    def Function_6_263F(): pass

    label("Function_6_263F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_2850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_265D")
    Call(1, 11)
    Jump("loc_284B")

    label("loc_265D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B0")

    ChrTalk(
        0xE,
        (
            "#00300FThe last opponent is unknown\x01",
            "With Mary and Mary\x01",
            "I am Mr. Ian who is all the masterpieces.\x02\x03",
            "#00303FIt is \"treasure of zero\"\x01",
            "When you are using key people,\x01",
            "It would be a mistake that it is considerably troublesome.\x02\x03",
            "#00302FBut, of course, one step\x01",
            "I do not mean to retreat.\x02\x03",
            "#00309FOur lovely daughter is\x01",
            "I'm waiting for their parents.\x01",
            "Let 's go pick me up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_284B")

    label("loc_27B0")


    ChrTalk(
        0xE,
        (
            "#00302FWhatever he is,\x01",
            "一歩だってI do not mean to retreat.\x02\x03",
            "#00309FOur lovely daughter is\x01",
            "I'm waiting for their parents.\x01",
            "Let 's go pick me up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_284B")

    Jump("loc_3373")

    label("loc_2850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_291F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286B")
    Call(1, 10)
    Jump("loc_291A")

    label("loc_286B")


    ChrTalk(
        0xE,
        (
            "#00303FFrom now on, the scaffold that I found out\x01",
            "I have to prove it.\x02\x03",
            "#00302FThat was taken care of at the very latest\x01",
            "To dead father and uncle,\x01",
            "It is my greatest obligation that I can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_291A")

    Jump("loc_3373")

    label("loc_291F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_29C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_293A")
    Call(1, 9)
    Jump("loc_29BF")

    label("loc_293A")


    ChrTalk(
        0xE,
        (
            "#00303FBesides this,\x01",
            "Uncle yourself with a genuine authenticity\x01",
            "I have to settle the battle.\x02\x03",
            "#00301FWhile we have time,\x01",
            "I have to switch my head.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29BF")

    Jump("loc_3373")

    label("loc_29C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_2B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ACF")

    ChrTalk(
        0xE,
        (
            "#00301FAlthough the flying boat of \"Red constellation\" was rejected,\x01",
            "To the guys\x01",
            "It sounds like a small hand.\x02\x03",
            "#00303FBefore this, my uncle Takashi and Charlie\x01",
            "It's supposed to be waiting for me ……\x02\x03",
            "#00301FWhat will you set up?\x01",
            "I did not understand.\x01",
            "You must not take care of yourself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2B68")

    label("loc_2ACF")


    ChrTalk(
        0xE,
        (
            "#00303FBefore this, my uncle Takashi and Charlie\x01",
            "It's supposed to be waiting for me ……\x02\x03",
            "#00301FWhat will you set up?\x01",
            "I did not understand.\x01",
            "You must not take care of yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B68")

    Jump("loc_3373")

    label("loc_2B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C65")

    ChrTalk(
        0xE,
        (
            "#00300FI wonder what that \"big tree\"\x01",
            "It's a small thing for us.\x01",
            "… That's right, Lloyd?\x02\x03",
            "#00304FWe regain key people to us.\x01",
            "Everything is ok if you do not forget it.\x02\x03",
            "#00300FIf I have time to think\x01",
            "Let's hurry and let it in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2CDB")

    label("loc_2C65")


    ChrTalk(
        0xE,
        (
            "#00304FHalberd also \"Berserger\"\x01",
            "Maintenance is done perfectly.\x02\x03",
            "#00300FFinally to get back the keebou\x01",
            "Let's go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDB")

    Jump("loc_3373")

    label("loc_2CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2EEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2F")

    ChrTalk(
        0xE,
        (
            "#00303FIf you look only with the overall fighting strength,\x01",
            "I wonder whether \"Red constellation\" is upper … …\x02\x03",
            "#00301FThere are puppet weapons for the members of \"association\"\x01",
            "There is also a master of spears that spear.\x02\x03",
            "Even if you just stand up by force alone,\x01",
            "I guess it's easy to win.\x02\x03",
            "#00303F……Anyways,\x01",
            "You can never look down on them.\x01",
            "You should keep in mind, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2EE5")

    label("loc_2E2F")


    ChrTalk(
        0xE,
        (
            "#00303FTo those of \"association\"\x01",
            "Even if you just stand up by force alone,\x01",
            "I guess it's easy to win.\x02\x03",
            "#00301F……Anyways,\x01",
            "You can never look down on them.\x01",
            "You should keep in mind, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EE5")

    Jump("loc_3373")

    label("loc_2EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_30E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302D")

    ChrTalk(
        0xE,
        (
            "#00300FIf \"invalid declaration\" is issued,\x01",
            "At least the defense force\x01",
            "It will be in a wait-and-see state … …\x02\x03",
            "#00303FThe president hires on its own\x01",
            "The \"red constellation\"\x01",
            "It will strike as usual.\x02\x03",
            "#00308FNo … Rather than ever\x01",
            "Let's pretend to be no way\x01",
            "It might come in.\x02\x03",
            "#00300FAnyhow, vigilance is not negligible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_30DB")

    label("loc_302D")


    ChrTalk(
        0xE,
        (
            "#00303FEven if an invalid declaration is issued,\x01",
            "The \"red constellation\"\x01",
            "It will strike as usual.\x02\x03",
            "#00301FLet's pretend to be no way\x01",
            "There is also possibility to come.\x01",
            "We will not be alarmed in future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30DB")

    Jump("loc_3373")

    label("loc_30E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_31B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30FB")
    Call(1, 8)
    Jump("loc_31AE")

    label("loc_30FB")


    ChrTalk(
        0xE,
        (
            "#00300FTo the unit guarding the Michelam,\x01",
            "I wonder if my uncle or Shirley is …\x02\x03",
            "#00303FGareth club executive class\x01",
            "It is no mistake taking command.\x01",
            "… … Do not prepare thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AE")

    Jump("loc_3373")

    label("loc_31B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_3373")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CE")
    Call(1, 7)
    Jump("loc_3373")

    label("loc_31CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32DB")

    ChrTalk(
        0xE,
        (
            "#00304FMireille's side is\x01",
            "The Mainz people also cooperate,\x01",
            "I do not need to worry about it for the time being.\x02\x03",
            "#00300FThere are things that we do variously,\x01",
            "First of all, I have to do something before my eyes.\x02\x03",
            "#00309FYou have to depend on Gangan for a while.\x01",
            "Because your older brother rampant.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3373")

    label("loc_32DB")


    ChrTalk(
        0xE,
        (
            "#00303FThere are things that we do variously,\x01",
            "First of all, I have to do something before my eyes.\x02\x03",
            "#00300FYou have to depend on Gangan for a while.\x01",
            "Because your older brother rampant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3373")

    TalkEnd(0xFE)
    Return()

    # Function_6_263F end

    def Function_7_3377(): pass

    label("Function_7_3377")


    ChrTalk(
        0xE,
        (
            "#00309FNo way, until the workshop ….\x01",
            "No, ~ is Mercava\x01",
            "It is unlikely.\x02\x03",
            "#00300FWith this \"Berserger\"\x01",
            "Regular maintenance as well\x01",
            "It seems likely to be indispensable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat remarks Guillaume boss\x01",
            "I was asked to fix it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304FOh, there are also advice of that time\x01",
            "It is limiting the use time.\x02\x03",
            "#00300FTo my brother in Douglas\x01",
            "Halvard taught me, too,\x01",
            "I do not want to get rotten …\x02\x03",
            "#00300FIn the future Koitsu and Halberd's\x01",
            "I will let you go downstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FI do not know how to say it ….\x01",
            "That is why it is Randy.\x02\x03",
            "#00003FBut, Douglas deputy commander … ….\x01",
            "I wonder what I am doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303FAs it is about that older brother,\x01",
            "We will work as deputy commander as usual\x01",
            "I wonder what they are doing … …\x02\x03",
            "#00301FIncluding the command, really to the present condition\x01",
            "I do not know if I am convinced.\x02\x03",
            "#00303FEven if not convinced,\x01",
            "Cutting the forerunner like Mireille\x01",
            "I guess it 's impossible for me to turn the opposite flag.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FThat's right.\x01",
            "Somehow the intentions of the commanders\x01",
            "I hope you can check it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304FWell, I guess I have to do various things,\x01",
            "First of all, I have to do something before my eyes.\x02\x03",
            "#00300FYou have to depend on Gangan for a while.\x01",
            "Because your older brother rampant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa … … I understand.\x01",
            "I'm counting on you, Randy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 1)
    Return()

    # Function_7_3377 end

    def Function_8_3807(): pass

    label("Function_8_3807")


    ChrTalk(
        0xD,
        (
            "#10703FIt is said that he is in Mishram\x01",
            "Unit of \"red constellation\" ……\x02\x03",
            "#10708F…… \"Blood Dyeing#8RBladder#Shirley \"too\x01",
            "Is it there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303F…… No, keep confinement place of important people\x01",
            "I guess it '\x01",
            "I do not think he suits his sex.\x02\x03",
            "#00300FEven though there are executive classes,\x01",
            "Perhaps other guys are hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10703F……Is that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303FLisha-chan ……\x01",
            "Now to help your ladies\x01",
            "Let's concentrate.\x02\x03",
            "#00300FWith my uncle Takashi and Charlie,\x01",
            "Either way I'm confronted with confrontation\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10708F……Yeah, you are right.\x01",
            "Sorry, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#00309FHaha, I do not apologize, though.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_8_3807 end

    def Function_9_3A71(): pass

    label("Function_9_3A71")


    ChrTalk(
        0xE,
        (
            "#00303FCharlie, from the moment I arrived\x01",
            "I can only find joy in fighting\x01",
            "It was a genuine eating tiger.\x02\x03",
            "What I can do to meet him\x01",
            "Only the battlefield which kills or is killed ……\x02\x03",
            "#00302FSuch an eye, to Lisha-chan\x01",
            "I was defeated other than \"killed\" …\x01",
            "Well, I guess it was surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat's right.\x01",
            "Just before I lose my mind\x01",
            "It seemed to be unsatisfactory.\x02\x03",
            "#00002FBut, Randy a little\x01",
            "Do you feel relieved?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00302F…… Ha ha, well.\x01",
            "Even such a thing is no different to a cousin.\x02\x03",
            "#00303FTo be honest, considering what he did\x01",
            "Although I thought that it was no use no matter how vengeful it was … …\x02\x03",
            "#00300FTo Lisha who did not do\x01",
            "I must thank you once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHaha … that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303F…… I am ahead,\x01",
            "Uncle yourself with a genuine authenticity\x01",
            "I have to settle the battle.\x02\x03",
            "#00300FSometime, I will ask you to help me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, of course.\x01",
            "Everyone together to work together\x01",
            "I will surely overcome it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 2)
    Return()

    # Function_9_3A71 end

    def Function_10_3DC3(): pass

    label("Function_10_3DC3")


    ChrTalk(
        0xE,
        "#00303FFuu ……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FRandy's uncle ……\x01",
            "After all it is ridiculous\x01",
            "It was strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00302FOh … you guys\x01",
            "Thanks to lending me power\x01",
            "I managed to steal it.\x02\x03",
            "#00306FTo be honest, if I told you to do it again\x01",
            "I wonder if I can win again.\x02\x03",
            "#00300FThe name of the strongest hunter, \"red war demon\"\x01",
            "It is not Date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F…… If we put our strengths together,\x01",
            "I can surely overcome it many times.\x02\x03",
            "#00000FWe are attached to Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304F…… Ha ha, that's right.\x01",
            "That's the strength I got.\x02\x03",
            "#00300FFrom now on, the scaffold that I found out\x01",
            "I will not continue to prove it.\x02\x03",
            "#00303FThat was taken care of at the very latest\x01",
            "To dead father and uncle,\x01",
            "It is the largest obligation that I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FOh … and we too\x01",
            "I will cooperate with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#00309FHaha, thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 3)
    Return()

    # Function_10_3DC3 end

    def Function_11_40C3(): pass

    label("Function_11_40C3")


    ChrTalk(
        0xE,
        (
            "#00301FThe last opponent is unknown\x01",
            "With Mary and Mary\x01",
            "I am Mr. Ian who is all the masterpieces.\x02\x03",
            "#00303FIf only with simple combat strength\x01",
            "Uncle Taku and Arios' Osan are better\x01",
            "Well enough threat … …\x02\x03",
            "#00301FIt is \"treasure of zero\"\x01",
            "When you are using key people,\x01",
            "It would be a mistake that it is considerably troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FAh … … more than Arios\x01",
            "It may be a tough fight.\x02\x03",
            "#00001FHowever,\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304FThere are all the truths there ──\x01",
            "I can not absolutely draw, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FWell, do not say it before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00309FHa ha, I have a long relationship.\x01",
            "What you are saying is\x01",
            "It almost got it.\x02\x03",
            "#00304FOf course, one step\x01",
            "I do not mean to retreat.\x02\x03",
            "#00302FAnyway, our lovely daughter is\x01",
            "You should be waiting for their parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh … That's right.\x01",
            "Let's face Ka'a with everyone!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 4)
    Return()

    # Function_11_40C3 end

    def Function_12_43C4(): pass

    label("Function_12_43C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4559")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E2")
    Call(1, 14)
    Jump("loc_4554")

    label("loc_43E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44CB")

    ChrTalk(
        0x10,
        (
            "#10100FIf you come this far,\x01",
            "Believe me yourself\x01",
            "I think that it is just jumping in.\x02\x03",
            "#10104FFrom now on to defend the crossbell ……\x01",
            "Let's do our best, Mr. Lloyd.\x02\x03",
            "#10102FBefore being a police and security guard\x01",
            "As a friend to live in this place together … !.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4554")

    label("loc_44CB")


    ChrTalk(
        0x10,
        (
            "#10100FFrom now on to defend the crossbell ……\x01",
            "Let's do our best, Mr. Lloyd.\x02\x03",
            "Before being a police and security guard\x01",
            "As a friend to live in this place together … !.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4554")

    Jump("loc_4F6B")

    label("loc_4559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_46C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4650")

    ChrTalk(
        0x10,
        (
            "#10106FThe appearance of an amphibious assault ship\x01",
            "I was surprised … ….\x02\x03",
            "#10100FI managed to \"Taiki\" safely\x01",
            "It was nice to have arrived.\x02\x03",
            "#10103FHowever, that\x01",
            "It does not necessarily appear.\x02\x03",
            "#10101FWait members enough\x01",
            "You have to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_46C0")

    label("loc_4650")


    ChrTalk(
        0x10,
        (
            "#10103FIn the future the amphibious assault ship\x01",
            "It does not necessarily appear.\x02\x03",
            "#10101FWait members enough\x01",
            "You have to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C0")

    Jump("loc_4F6B")

    label("loc_46C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_48CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4836")

    ChrTalk(
        0x10,
        (
            "#10103FBecause Arios disappeared,\x01",
            "The command force of the entire Defense Army\x01",
            "I seem to have moved to Sonya command.\x02\x03",
            "#10100FFor a while in the emergence of \"Taiki\"\x01",
            "Confusion has occurred\x01",
            "It seems like I am chased by the correspondence of various places.\x02\x03",
            "#10104FI think it's hard … …\x01",
            "If you leave it to Sonya command\x01",
            "I think that it will be okay.\x02\x03",
            "#10100Fwe,\x01",
            "Toward the target in front of the eyes\x01",
            "Let's keep pushing!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_48CA")

    label("loc_4836")


    ChrTalk(
        0x10,
        (
            "#10104FAs for the defense army,\x01",
            "If you leave it to Sonya command\x01",
            "I think that it will be okay.\x02\x03",
            "#10100Fwe,\x01",
            "Toward the target in front of the eyes\x01",
            "Let's keep pushing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48CA")

    Jump("loc_4F6B")

    label("loc_48CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49EB")

    ChrTalk(
        0x10,
        (
            "#10101F\"Monaster Monastery\" and \"Star Tower Tower\"\x01",
            "Originally it was a ruin under the control of the guard.\x02\x03",
            "#10106FIf I managed to grasp the true identity of the bell,\x01",
            "To this point\x01",
            "It may not have been ……\x02\x03",
            "#10103F…… I regret it will not start.\x01",
            "Anyway, now I have to look forward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4A9C")

    label("loc_49EB")


    ChrTalk(
        0x10,
        (
            "#10108FAs long as you grab the identity of the bell in advance,\x01",
            "To this point\x01",
            "It may not have been ……\x02\x03",
            "#10103F…… I regret it will not start.\x01",
            "Anyway, now I have to look forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9C")

    Jump("loc_4F6B")

    label("loc_4AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_4C9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BDC")

    ChrTalk(
        0x10,
        (
            "#10103FThe fact that the legitimacy of an independent country shakes … …\x02\x03",
            "#10101FIt is the national defense army itself\x01",
            "It is nothing but a shake of legitimacy.\x02\x03",
            "#10108FThe Sonja command gathered well\x01",
            "I think that it will be given,\x01",
            "It will not be a big mess.\x02\x03",
            "#10103F…… 2 The two major powers can not move due to civil war or depression,\x01",
            "In a sense it may be a salvation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4C99")

    label("loc_4BDC")


    ChrTalk(
        0x10,
        (
            "#10101FIf an invalid declaration is issued,\x01",
            "Bellcard gate, Tangram gate ……\x01",
            "Any trouble will come to any unit ……\x02\x03",
            "#10103F…… 2 The two major powers can not move due to civil war or depression,\x01",
            "In a sense it may be a salvation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C99")

    Jump("loc_4F6B")

    label("loc_4C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_4F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB9")
    Call(1, 13)
    Jump("loc_4F6B")

    label("loc_4CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ECC")

    ChrTalk(
        0x10,
        (
            "#10105FAh, Ro, Mr. Lloyd … …\x02\x03",
            "#10111FHey, I …\x01",
            "It is told that \"I will receive you\"\x01",
            "Surely I was surprised … …\x02\x03",
            "#10106FThat is, Mr. Lloyd\x01",
            "I told you not in that sense\x01",
            "I know exactly! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUm, I mean \"that's the meaning\"\x01",
            "What does it mean?\x01",
            "I do not understand it at all … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#10106F(Well, I mean seriously …).\x02\x03",
            "#10100F…… Kohon, anyway.\x01",
            "Now I am trying to capture Michelam\x01",
            "First let's think about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, of course.\x01",
            "I'm counting on you, Noel.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4F6B")

    label("loc_4ECC")


    ChrTalk(
        0x10,
        (
            "#10100F…… Kohon, anyway.\x01",
            "Now I am trying to capture Michelam\x01",
            "First let's think about it!\x02\x03",
            "I am also with Ellie\x01",
            "For Mr. MacDaely,\x01",
            "I will do my best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F6B")

    TalkEnd(0xFE)
    Return()

    # Function_12_43C4 end

    def Function_13_4F6F(): pass

    label("Function_13_4F6F")

    OP_4B(0x10, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "#01912FOkay ….\x01",
            "I was able to see her older sister again.\x01",
            "It was truly good.\x02\x03",
            "#01911FUgh, somehow again\x01",
            "I cried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#10112FAlready, Fran? …\x02\x03",
            "#10104F…… But, me too\x01",
            "Fur injuries are completely cured\x01",
            "I'm really relieved.\x02\x03",
            "#10109FBesides, under Mr. Lloyd and Wazi\x01",
            "He seems to have worked firmly.\x01",
            "Huhuu, choirs are great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01906FWell, if you are older sister anymore,\x01",
            "Treat him like a child forever ~ ……\x02\x03",
            "#01905F… Ah, I see.\x01",
            "My sister to Mr. Lloyd\x01",
            "\"You got it\" You came.\x02\x03",
            "#01906FAbout 3 steps of stairs to adults\x01",
            "I went up, so I\x01",
            "It can not be helped looking like a child … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#10111FToo bad …!\x01",
            "What are you talking about, Fran?\x02\x03",
            "#10106FLloyd's also like that\x01",
            "I told you …! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909FWow, if you are older sister\x01",
            "I reminded you with my memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F(… … I do not know what the story is about ……\x01",
            "It is hard to get into a conversation delicately. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 5)
    OP_4C(0x10, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0xC, 0x10)
    Return()

    # Function_13_4F6F end

    def Function_14_52F1(): pass

    label("Function_14_52F1")


    ChrTalk(
        0x10,
        (
            "#10101FIt is finished in a long time …\x02\x03",
            "#10103FIf you come this far,\x01",
            "Believe me yourself\x01",
            "I think that it is just jumping in.\x02\x03",
            "#10108FEven if this incident ended,\x01",
            "There are many hardships in the crossbell\x01",
            "I think that it is awaiting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh … but,\x01",
            "After all it is\x01",
            "I have no choice but to pick them up one after another.\x02\x03",
            "#00000FTo solve this incident,\x01",
            "For protecting the crossbell from now on\x01",
            "I think that it will be the first step.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#10109FHuhu, if my father was alive\x01",
            "I think that he said the same thing.\x02\x03",
            "#10103FFrom now on to defend the crossbell ……\x01",
            "Let's do our best, Mr. Lloyd.\x02\x03",
            "#10102FBefore being a police and security guard\x01",
            "As a friend to live in this place together … !.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 6)
    Return()

    # Function_14_52F1 end

    def Function_15_5550(): pass

    label("Function_15_5550")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_572D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_556E")
    Call(1, 18)
    Jump("loc_5728")

    label("loc_556E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5678")

    ChrTalk(
        0xA,
        (
            "#10404FI felt a while staying together,\x01",
            "Keiya 's \"bond\" is real.\x02\x03",
            "#10402FNo matter what,\x01",
            "As long as you keep asking\x01",
            "I guess there is hope.\x02\x03",
            "#10409FWell, as soon as I am\x01",
            "I will have dinner together.\x01",
            "Even for the cute kea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5728")

    label("loc_5678")


    ChrTalk(
        0xA,
        (
            "#10404FNo matter what,\x01",
            "As long as you keep asking\x01",
            "I guess there is hope.\x02\x03",
            "#10409FWell, as soon as I am\x01",
            "I will have dinner together.\x01",
            "Even for the cute kea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5728")

    Jump("loc_6D44")

    label("loc_572D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_5805")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5748")
    Call(1, 17)
    Jump("loc_5800")

    label("loc_5748")


    ChrTalk(
        0xA,
        (
            "#10404FFinally to him, I am\x01",
            "I was able to add a start.\x01",
            "…… I will reward you.\x02\x03",
            "#10402FFrom here as a star cup knight,\x01",
            "As a member of the Special Affairs Support Division,\x01",
            "Let me help you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5800")

    Jump("loc_6D44")

    label("loc_5805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_END)), "loc_591F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5825")
    Call(1, 55)
    Jump("loc_591A")

    label("loc_5825")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_7B(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58A4")

    ChrTalk(
        0xA,
        (
            "#10403FApparently \"he\" is\x01",
            "It seems to have decided with me.\x02\x03",
            "#10400FWhen you are ready,\x01",
            "Let's head to the barrier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_591A")

    label("loc_58A4")


    ChrTalk(
        0xA,
        (
            "#10403FApparently \"he\" is\x01",
            "It seems to have decided with me.\x02\x03",
            "#10400FPut me in the explore member.\x01",
            "Let's face the barrier together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_591A")

    Jump("loc_6D44")

    label("loc_591F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_5A88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59FE")

    ChrTalk(
        0xA,
        (
            "#10404FWell, it's time to start exploring.\x02\x03",
            "#10401FI am sorry that we can not proceed with Merkaba ……\x01",
            "\"He\" is also waiting ahead.\x02\x03",
            "#10403FThe misplaced game\x01",
            "In order to attach it again,\x01",
            "I have to go on a steady road.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5A83")

    label("loc_59FE")


    ChrTalk(
        0xA,
        (
            "#10401FBefore going on \"Taiki\"\x01",
            "\"He\" is also waiting.\x02\x03",
            "#10403FThe misplaced game\x01",
            "In order to attach it again,\x01",
            "I have to go on a steady road.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A83")

    Jump("loc_6D44")

    label("loc_5A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5CF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C3A")

    ChrTalk(
        0xA,
        (
            "#10403FTo the emergence of that \"big tree\"\x01",
            "Alteria law nation also\x01",
            "It seems to be a big fuss.\x02\x03",
            "#10400FNone of the church's scriptures\x01",
            "It probably will not be mentioned\x01",
            "It is \"unexpected miracle\".\x02\x03",
            "#10408FThere is also one case of \"pile of salt\"\x01",
            "The upper part is also obliged to be careful\x01",
            "I guess I will not get it …\x02\x03",
            "#10400FBut, as there is a keya over there,\x01",
            "I could not take it easy.\x02\x03",
            "Because responsibility is given to me,\x01",
            "If you head for \"Taiki\" without hesitation\x01",
            "Tell Abbas.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5CF0")

    label("loc_5C3A")


    ChrTalk(
        0xA,
        (
            "#10404FAs there is a keya over there,\x01",
            "Alteria law instructions from the country\x01",
            "I have no time to wait too long.\x02\x03",
            "#10400FBecause responsibility is given to me,\x01",
            "If you head for \"Taiki\" without hesitation\x01",
            "Tell Abbas.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF0")

    Jump("loc_6D44")

    label("loc_5CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5F4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7A")

    ChrTalk(
        0xA,
        (
            "#10400F\"Society\" and the Order of the Knights,\x01",
            "I have been confronted with each other many times behind history.\x01",
            "It is a fate of so-called fate.\x02\x03",
            "#10403FI'm looking into the knight team for them,\x01",
            "Regarding \"clown\" and \"steel saint\"\x01",
            "Especially little information.\x02\x03",
            "Without effective countermeasures\x01",
            "I will face the battle, but ….\x02\x03",
            "#10402FIf it does not enter the tiger's hole, it says not to get a baby child,\x01",
            "Jump in anyway\x01",
            "Let's look at the winner.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5F48")

    label("loc_5E7A")


    ChrTalk(
        0xA,
        (
            "#10403FI've also examined the \"knight\" in the Knights,\x01",
            "Regarding \"clown\" and \"steel saint\"\x01",
            "Especially little information.\x02\x03",
            "#10402FIf it does not enter the tiger's hole, it says not to get a baby child,\x01",
            "Jump in anyway\x01",
            "Let's look at the winner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F48")

    Jump("loc_6D44")

    label("loc_5F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_60FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6082")

    ChrTalk(
        0xA,
        (
            "#10402FIf it is around the booster point,\x01",
            "There seems to be no particular warning.\x02\x03",
            "#10404FDefense forces and hunters are out of security range,\x01",
            "Even if you headed by Mercava in this case\x01",
            "It seems to be fine without interruption.\x02\x03",
            "#10408FBy this \"invalid declaration\"\x01",
            "How will the causal change in the future … …\x02\x03",
            "#10409FHuh, you know the god only knows.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_60F7")

    label("loc_6082")


    ChrTalk(
        0xA,
        (
            "#10404FBy this \"invalid declaration\"\x01",
            "How will the causal change in the future … …\x02\x03",
            "#10409FHuh, you know the god only knows.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60F7")

    Jump("loc_6D44")

    label("loc_60FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_6366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62BC")

    ChrTalk(
        0xA,
        (
            "#10402FMichelin's beach ……\x01",
            "I do not mean to go in this way.\x02\x03",
            "#10406FIf you can, moreover, everyone leisurely\x01",
            "I wanted to have a vacation, but.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FTake back Ka'a … …\x01",
            "…… When everything is over,\x01",
            "Let's all come again.\x02\x03",
            "#00000FNext time the section manager, Abbas,\x01",
            "Sonja command as well\x01",
            "You may invite me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10409FAhaha, that's cool!\x02\x03",
            "#10400FTo grab such a day in this hand,\x01",
            "I will try to make efforts at best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6361")

    label("loc_62BC")


    ChrTalk(
        0xA,
        (
            "#10404FMichelin's beach ……\x01",
            "This time there is a tough fight rather than vacation\x01",
            "I guess I'll be waiting.\x02\x03",
            "#10400FTo grab the calm days in this hand,\x01",
            "I will try to make efforts at best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6361")

    Jump("loc_6D44")

    label("loc_6366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_66D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65D8")

    ChrTalk(
        0xA,
        (
            "#10404FWell, if you take Mr. Grace\x01",
            "Anything will be an interview.\x02\x03",
            "Because Abbas gets angry\x01",
            "I can not say a big deal … …\x02\x03",
            "#10409FWhen pushed by this momentum,\x01",
            "There seems to be a thing that does not exist.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0xA, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64DB")
    Jump("loc_6525")

    label("loc_64DB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_64FB")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6525")

    label("loc_64FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_651B")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6525")

    label("loc_651B")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6525")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "#02109FOh no, yo!\x01",
            "You should limit it to \"something\"!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F(Do not struggle with Abbas …).\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x0, 7)
    Jump("loc_66CD")

    label("loc_65D8")


    ChrTalk(
        0xA,
        (
            "#10404FIn short, what is test?\x01",
            "From my my name \"Scripture#4Rtestament#\"\x01",
            "It was a suitably fiddling name.\x02\x03",
            "#10409FI am honest and I am good at anything\x01",
            "Abbas is loud.\x01",
            "Because he is a type who wants to enter from form.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_66CD")

    Jump("loc_6D44")

    label("loc_66D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_69EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6949")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_682E")

    ChrTalk(
        0xA,
        (
            "#10403FLisha, stand on the deck\x01",
            "You seem to be indulging in thought.\x02\x03",
            "Alcane shell, black moon,\x01",
            "And the mission of \"silver\" …\x01",
            "I guess there are many things to worry about.\x02\x03",
            "#10402FHuh, if you do not mind\x01",
            "What would you do as a consultant?\x02\x03",
            "#10409FMaybe some flag\x01",
            "You may stand up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, that's full of mind\x01",
            "Because I will not ride into consultation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6941")

    label("loc_682E")


    ChrTalk(
        0xA,
        (
            "#10403FLisha, stand on the deck\x01",
            "You seem to be indulging in thought.\x02\x03",
            "Alcane shell, black moon,\x01",
            "And the mission of \"silver\" …\x01",
            "I guess there are many things to worry about.\x02\x03",
            "#10402FHuh, so …\x01",
            "It seems I was on a consultation,\x01",
            "Have you flagged anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FSo, to set such a thing\x01",
            "Because I did not go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6941")

    SetScenarioFlags(0x0, 7)
    Jump("loc_69EA")

    label("loc_6949")


    ChrTalk(
        0xA,
        (
            "#10404FEven so,\x01",
            "Without the current clothes\x01",
            "I do not seem very \"silver\", do you?\x02\x03",
            "#10400FHuh, that character is so unique\x01",
            "It seems to be a natural seclusion technique.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69EA")

    Jump("loc_6D44")

    label("loc_69EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_6B7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AF9")

    ChrTalk(
        0xA,
        (
            "#10400FThanks to Tio's coming in,\x01",
            "It seems that the operation efficiency of the ship will rise greatly.\x02\x03",
            "#10404FEven if you find \"gaps\"\x01",
            "We only had limits.\x01",
            "This is a big step forward.\x02\x03",
            "#10400FHuhu, this is also a tour of the goddess\x01",
            "Maybe it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6B79")

    label("loc_6AF9")


    ChrTalk(
        0xA,
        (
            "#10404FI went to Ursula hospital first\x01",
            "What we were able to join with Tio … …\x02\x03",
            "#10400FHuhu, this is also a tour of the goddess\x01",
            "Maybe it is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B79")

    Jump("loc_6D44")

    label("loc_6B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6D44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B99")
    Call(1, 16)
    Jump("loc_6D44")

    label("loc_6B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CC2")

    ChrTalk(
        0xA,
        (
            "#10406FIt is quite hard to go ahead … …\x01",
            "Tomorrow I have to take it to the steady.\x02\x03",
            "#10400F…… Oh yeah, the facility inside Mercava\x01",
            "I do not mind being free to use it.\x02\x03",
            "Equipment · Fixtures · Studio functions ----\x01",
            "You can also use a sleeping room if you leave the upper corridor.\x02\x03",
            "#10409FAlso doubling as a visitor to the crew\x01",
            "How about once you check it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6D44")

    label("loc_6CC2")


    ChrTalk(
        0xA,
        (
            "#10400FThe facilities in Mercava\x01",
            "I do not mind being free to use it.\x02\x03",
            "#10409FAlso doubling as a visitor to the crew\x01",
            "How about once you check it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D44")

    TalkEnd(0xFE)
    Return()

    # Function_15_5550 end

    def Function_16_6D48(): pass

    label("Function_16_6D48")


    ChrTalk(
        0xA,
        (
            "#10403FTentatively, before an accident happens\x01",
            "Beyond Nakasu on the Ursula intertrial\x01",
            "I found a \"gap\" ….\x02\x03",
            "#10400FFrom now on I will be able to land \"gaps\"\x01",
            "It is necessary to detect and discover.\x02\x03",
            "#10406FMercapa is too lacking,\x01",
            "It seems quite difficult to go ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Still, step by step\x01",
            "I have no choice but to proceed.\x02\x03",
            "#00001FRetrieve fellows and Ka'a …\x01",
            "It is not easy to go\x01",
            "Because I am well-informed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10402FHuh, I know.\x01",
            "Tomorrow I have to take it to the steady.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 7)
    Return()

    # Function_16_6D48 end

    def Function_17_6EFC(): pass

    label("Function_17_6EFC")


    ChrTalk(
        0xA,
        "#10402FHi, I was tired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWas this review helpful?\x01",
            "Is the body okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404FOh, I do not need to worry anymore.\x01",
            "As you can see when you are off.\x02\x03",
            "#10408FBecause the reaction is big,\x01",
            "Usually as much power as possible\x01",
            "I try to suppress it, but ….\x02\x03",
            "#10404FHuh, I have not seen it for the first time in a while\x01",
            "I wonder if it got hot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FDo your best\x01",
            "Beat down Wald … …\x02\x03",
            "I guess it was necessary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404FOh, that's right.\x02\x03",
            "#10408F…… If you are doing your best from the beginning,\x01",
            "He also thinks over there\x01",
            "Perhaps it was not there.\x02\x03",
            "#10403FRegarding that point,\x01",
            "I will be totally responsible for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FSuch a thing ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10402FHuh, that's alright.\x01",
            "I do not regret it,\x01",
            "I should leave a lesson for the future.\x02\x03",
            "#10404FAnyways……\x01",
            "Finally to him, I am\x01",
            "I was able to add a start.\x02\x03",
            "Testers' leader,\x01",
            "Wazi · Hemisphere's mission is\x01",
            "This would have done a whole stroke.\x02\x03",
            "#10402FTo you guys who showed up,\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha … … You are welcome.\x02\x03",
            "#00000FThere is a considerable enemy in the future\x01",
            "I guess they are waiting … ….\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10402FHuh, I agree with the leader.\x02\x03",
            "#10404FFrom here as a star cup knight,\x01",
            "As a member of the Special Affairs Support Division,\x01",
            "Let me help you guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 1)
    Return()

    # Function_17_6EFC end

    def Function_18_736F(): pass

    label("Function_18_736F")


    ChrTalk(
        0xA,
        (
            "#10400FFrom the \"Wind Sword of the Wind\"\x01",
            "I got a lot of information,\x01",
            "Some still remain a mystery.\x02\x03",
            "#10403FAo#2RBlue#Ice#2Rzero#Plan \"… ….\x01",
            "Its full plan that Mr. Bear Bee has planned.\x02\x03",
            "#10408FLady Mary Bell should know\x01",
            "\"The treasure of zero\" With the potential of Kea,\x01",
            "How do you use it for your plan?\x02\x03",
            "#10406FI have to ask questions directly about this area\x01",
            "There seems to be no way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FOh … … Once you reach them\x01",
            "You should surely understand.\x02\x03",
            "#00008FWhy is Kea,\x01",
            "They may be following them ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404F…… Well, it's okay if you do not worry.\x02\x03",
            "#10402FI felt a while staying together,\x01",
            "Keiya 's \"bond\" is real.\x02\x03",
            "#10409FNo matter what,\x01",
            "As long as you keep asking\x01",
            "I guess there is hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F… … That's right.\x01",
            "I am sure that everything will be fine.\x02\x03",
            "#00005FBut I'm telling you like someone else's stuff\x01",
            "Wasi is also in that \"bond\"?\x02\x03",
            "#00004FI guess that's Kaea … …\x01",
            "Let's all pick up that girl together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404F… … Huh, I'm happy\x01",
            "Will not you tell me?\x02\x03",
            "#10402FIn this way I\x01",
            "I will have dinner together.\x01",
            "Even for the cute kea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 2)
    Return()

    # Function_18_736F end

    def Function_19_7764(): pass

    label("Function_19_7764")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_796A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7782")
    Call(1, 21)
    Jump("loc_7965")

    label("loc_7782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78AB")

    ChrTalk(
        0xD,
        (
            "#10708F\"Silver\" and the artist's way ……\x01",
            "How will we go yet?\x01",
            "Specifically, I have not decided … …\x02\x03",
            "#10704FTo me now, crossbell … ….\x01",
            "This land where Iria's are located\x01",
            "There are certainly feelings I want to protect.\x02\x03",
            "#10702FTo protect \"important things\" ……\x01",
            "Do your best with everyone\x01",
            "I will get you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7965")

    label("loc_78AB")


    ChrTalk(
        0xD,
        (
            "#10704FTo me now, crossbell … ….\x01",
            "This land where Iria's are located\x01",
            "There are certainly feelings I want to protect.\x02\x03",
            "#10702FTo protect \"important things\" ……\x01",
            "Do your best with everyone\x01",
            "I will get you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7965")

    Jump("loc_857E")

    label("loc_796A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_7A30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7985")
    Call(1, 20)
    Jump("loc_7A2B")

    label("loc_7985")


    ChrTalk(
        0xD,
        (
            "#10703FThanks to everyone,\x01",
            "Finally get on with her\x01",
            "I was able to attach.\x02\x03",
            "#10702FTo return that kindness ……\x01",
            "To this incident to the end\x01",
            "I think that I will get involved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A2B")

    Jump("loc_857E")

    label("loc_7A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_END)), "loc_7B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A50")
    Call(1, 54)
    Jump("loc_7B87")

    label("loc_7A50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_7B(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AF6")

    ChrTalk(
        0xD,
        (
            "#10703F…… I am ready.\x01",
            "Let's head to the barrier soon.\x02\x03",
            "#10701FI myself am going to the road ahead\x01",
            "To find out … ….\x01",
            "I have to see her again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B87")

    label("loc_7AF6")


    ChrTalk(
        0xD,
        (
            "#10703F…… I am ready.\x01",
            "Please add me to the exploration team.\x02\x03",
            "#10701FI myself am going to the road ahead\x01",
            "To find out … ….\x01",
            "I have to see her again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B87")

    Jump("loc_857E")

    label("loc_7B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_7D06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C64")

    ChrTalk(
        0xD,
        (
            "#10703F…… At last it came this far.\x02\x03",
            "Including \"her\", before this\x01",
            "There are quite a few users … …\x02\x03",
            "#10701FLet's tighten your mind.\x01",
            "Our important things,\x01",
            "To grab this hand … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7D01")

    label("loc_7C64")


    ChrTalk(
        0xD,
        (
            "#10703FIncluding \"her\", before this\x01",
            "There are quite a few users … …\x02\x03",
            "#10701FLet's tighten your mind.\x01",
            "Our important things,\x01",
            "To grab this hand … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D01")

    Jump("loc_857E")

    label("loc_7D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_807C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E60")

    ChrTalk(
        0xD,
        (
            "#10703FEven for my own rush ……\x01",
            "\"Taiki\" and wait \"with\"\x01",
            "It is necessary to settle.\x02\x03",
            "#10701F…… I am prepared for it.\x01",
            "Let's start as soon as preparation is ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I released the alkane shell\x01",
            "Now, maybe … …)\x02\x03",
            "(Before heading for \"Taiki\"\x01",
            "Lisha to \"the person\"\x01",
            "Maybe I should take him ……? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7F01")

    label("loc_7E60")


    ChrTalk(
        0xD,
        (
            "#10703FEven for my own rush ……\x01",
            "\"Taiki\" and wait \"with\"\x01",
            "It is necessary to settle.\x02\x03",
            "#10701F…… I am prepared for it.\x01",
            "Let's start as soon as preparation is ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F01")

    Jump("loc_8077")

    label("loc_7F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FF9")

    ChrTalk(
        0xD,
        (
            "#10704FIria gave me courage\x01",
            "There is nothing scary for me now.\x02\x03",
            "#10701FAlso, for my own rush\x01",
            "I have to settle \"her\" … …\x02\x03",
            "#10702F…… I am prepared for it.\x01",
            "As soon as we are ready,\x01",
            "Let's head to \"Taiki.\"\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8077")

    label("loc_7FF9")


    ChrTalk(
        0xD,
        (
            "#10704FIria gave me courage\x01",
            "There is nothing scary for me now.\x02\x03",
            "#10702FAs soon as we are ready,\x01",
            "Let's head to \"Taiki.\"\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8077")

    Jump("loc_857E")

    label("loc_807C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_8259")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8192")

    ChrTalk(
        0xD,
        (
            "#10708F\"Silver\" I will save the Crossbell\x01",
            "I am trying to help you … ….\x02\x03",
            "#10703FIt is somewhat surprising nowadays\x01",
            "I feel like being a role.\x02\x03",
            "#10701F…… But this is also Crossbell City\x01",
            "To release the alkane shell ……\x01",
            "I'd like you to do my best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8254")

    label("loc_8192")


    ChrTalk(
        0xD,
        (
            "#10708F\"Silver\" I will save the Crossbell\x01",
            "To help you,\x01",
            "I also feel it is a useful role ….\x02\x03",
            "#10701FCrossbell City and\x01",
            "To release the alkane shell ……\x01",
            "I'd like you to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8254")

    Jump("loc_857E")

    label("loc_8259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_8301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8274")
    Call(1, 8)
    Jump("loc_82FC")

    label("loc_8274")


    ChrTalk(
        0xD,
        (
            "#10708F\"Charlie of blood dyeing\" … ….\x01",
            "I am concerned about her trend, but …\x02\x03",
            "#10703F…… Now we have Ellie\x01",
            "Let's concentrate on rescuing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82FC")

    Jump("loc_857E")

    label("loc_8301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_857E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84C2")

    ChrTalk(
        0xD,
        (
            "#10705FReally, really about \"silver\"\x01",
            "Can you not make it an article?\x02\x03",
            "#10706FI am concerned somehow ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02103FA story behind everyone's theater company!\x01",
            "The history and behind the scenes of legendary \"silver\"!\x01",
            "Lisa Mao's Three Size!\x02\x03",
            "#02109FIt is a great opportunity,\x01",
            "I will have you talk about washing ~ ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10706FUu, Lloyd san ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FSomething,\x01",
            "Dodge well … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x1, 0)
    Jump("loc_857E")

    label("loc_84C2")


    ChrTalk(
        0xD,
        (
            "#10706FNormally the theater company manager is in a suitable place\x01",
            "I was cutting it up … ….\x01",
            "I was so persistent.\x02\x03",
            "#10709FDo not truly write an article\x01",
            "Can you get it?\x01",
            "I am concerned somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_857E")

    TalkEnd(0xFE)
    Return()

    # Function_19_7764 end

    def Function_20_8582(): pass

    label("Function_20_8582")


    ChrTalk(
        0xD,
        (
            "#10703F\"Charlie of blood dyeing\" … ….\x02\x03",
            "As its name implies, her road is\x01",
            "It probably was painted on the blood.\x02\x03",
            "It is worth living it,\x01",
            "Because I found pleasure in the battlefield\x01",
            "There is her present … …\x02\x03",
            "#10708FFor me who is \"silver\"\x01",
            "It is by no means other things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FLisha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10704FBut … I finally got it,\x01",
            "I feel like I was able to change in the real sense.\x02\x03",
            "#10702FIria and Lloyd's … …\x01",
            "Encounter with lots of people\x01",
            "I think that I changed me.\x02\x03",
            "#10703FI and she, who should be similar,\x01",
            "About to become a completely different path … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWhat people meet people ……\x02\x03",
            "#00000FIf you think about it, so far\x01",
            "It may not be causal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10702FYeah … I really think so.\x02\x03",
            "#10704F… … Thanks to everyone,\x01",
            "Finally get on with her\x01",
            "I was able to attach.\x02\x03",
            "#10702FTo return that kindness ……\x01",
            "To this incident to the end\x01",
            "I think that I will get involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I'm begging for you, Lisa.\x02\x03",
            "Help Kaoru together ……\x01",
            "Let's return to Ilya's place with a smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10709FHuhu, come on.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 5)
    Return()

    # Function_20_8582 end

    def Function_21_8943(): pass

    label("Function_21_8943")


    ChrTalk(
        0xD,
        (
            "#10708F…… The end of the trip\x01",
            "You are getting closer.\x02\x03",
            "#10703FTo that Mariavell,\x01",
            "How far is the power as \"silver\"\x01",
            "I do not know whether to pass ……\x02\x03",
            "#10701FAnyway, with you all\x01",
            "I just have to do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh … I'm counting on you.\x02\x03",
            "#00009FHaha, but now ….\x01",
            "Fighting and adjusting forces,\x01",
            "We also had various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10709FOh, haha ….\x01",
            "I am sorry for that theory.\x02\x03",
            "#10703F\"Silver\" and the artist's way ……\x01",
            "How will we go yet?\x01",
            "Specifically, I have not decided … …\x02\x03",
            "#10702FTo me now, crossbell … ….\x01",
            "This land where Iria's are located\x01",
            "There are certainly feelings I want to protect.\x02\x03",
            "#10704FThe power as \"silver\" I have cultivated\x01",
            "If it helps it … …\x01",
            "I will tremble without hesitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FThank you, Leisha ……\x01",
            "I will count on you.\x02\x03",
            "#00000FOur 'Important things'\x01",
            "Let's work hard together to defend!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10702FYes……!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 6)
    Return()

    # Function_21_8943 end

    def Function_22_8C72(): pass

    label("Function_22_8C72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_8E4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C90")
    Call(1, 23)
    Jump("loc_8E45")

    label("loc_8C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D88")

    ChrTalk(
        0x13,
        (
            "#01203F#3COnce a \"god of treachery#8RDemi-gols#The\x01",
            "I chose to annihilate myself …\x02\x03",
            "#01200FKa'a to the same conclusion\x01",
            "The possibility of arriving,\x01",
            "It can not be said that it is not there.\x02\x03",
            "Son of man, regain the splendid kea,\x01",
            "Please stop it and show it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8E45")

    label("loc_8D88")


    ChrTalk(
        0x13,
        (
            "#01203F#3CKa'a is \"the treasure of the phantom#8RDemi-gols#\"When\x01",
            "同じ結論にThe possibility of arriving,\x01",
            "It can not be said that it is not there.\x02\x03",
            "#01200FSon of man, regain the splendid kea,\x01",
            "Please stop it and show it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E45")

    Jump("loc_9AC1")

    label("loc_8E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_8FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F34")

    ChrTalk(
        0x13,
        (
            "#01203F#3CSomewhere in \"Taiki\"\x01",
            "There is no mistake that there is a kea.\x02\x03",
            "#01200FProbably the deepest place ……\x01",
            "That daughter of the Clois family, and\x01",
            "Together with a lawyer who is a masterpiece.\x02\x03",
            "If I need help\x01",
            "Call me at any time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8FB1")

    label("loc_8F34")


    ChrTalk(
        0x13,
        (
            "#01203F#3CSomewhere in \"Taiki\"\x01",
            "There is no mistake that there is a kea.\x02\x03",
            "#01200FIf I need help\x01",
            "Call me at any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FB1")

    Jump("loc_9AC1")

    label("loc_8FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9147")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90A2")

    ChrTalk(
        0x13,
        (
            "#01200F#3CTo that \"big tree\"\x01",
            "How far can you do?\x01",
            "I have no idea.\x02\x03",
            "Has the power comparable to the goddess …\x01",
            "It may not be an exaggeration to say so.\x02\x03",
            "#01203FThe Son of Man is at the End of Immersion\x01",
            "I will not be able to arrive at this point … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9142")

    label("loc_90A2")


    ChrTalk(
        0x13,
        (
            "#01200F#3CTo that \"big tree\"\x01",
            "Has the power comparable to the goddess …\x01",
            "It may not be an exaggeration to say so.\x02\x03",
            "#01203FThe Son of Man is at the End of Immersion\x01",
            "I will not be able to arrive at this point … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9142")

    Jump("loc_9AC1")

    label("loc_9147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_938C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C7")

    ChrTalk(
        0x13,
        (
            "#01203F#3CThe bells dotted in the crossbell are\x01",
            "\"Place\" to amplify the power of \"treasure\"\x01",
            "Things to produce ……\x02\x03",
            "#01200FEven with the current situation,\x01",
            "You can trust Jorg 's findings.\x02\x03",
            "#01203FHowever, the cradle of the example cult#4RCradle#To\x01",
            "It is good to have invented … …\x01",
            "I do not think I will make a business with you with the hands of a human child.\x02\x03",
            "#01200FAgain, Alchemists of the Cloy family\x01",
            "It seems that tremendous imagination appears.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9387")

    label("loc_92C7")


    ChrTalk(
        0x13,
        (
            "#01203F#3CHowever, the cradle of the example cult#4RCradle#To\x01",
            "It is good to have invented … …\x01",
            "I do not think I will make a business with you with the hands of a human child.\x02\x03",
            "#01200FAgain, Alchemists of the Cloy family\x01",
            "It seems that tremendous imagination appears.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9387")

    Jump("loc_9AC1")

    label("loc_938C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_9554")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93A7")
    Call(1, 4)
    Jump("loc_954F")

    label("loc_93A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94AF")

    ChrTalk(
        0x13,
        (
            "#01203F#3CIf you do not know now,\x01",
            "I do not need my amulet etc.\x02\x03",
            "#01200FAs before, I will keep it behind\x01",
            "Call it when you need it.\x02\x03",
            "これからはWith it returned to its original form\x01",
            "Let's rush to the front.\x02\x03",
            "#01203FIf it is on the order of Muju\x01",
            "Let me drink a bite.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_954F")

    label("loc_94AF")


    ChrTalk(
        0x13,
        (
            "#01200F#3CIf you call me when you need it,\x01",
            "これからはWith it returned to its original form\x01",
            "Let's rush to the front.\x02\x03",
            "#01203FIf it is on the order of Muju\x01",
            "Let me drink a bite.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_954F")

    Jump("loc_9AC1")

    label("loc_9554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_97A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9704")

    ChrTalk(
        0x13,
        (
            "#01200F#3CLet's honor the hunters.\x01",
            "If you return to the original figure, considerable strength\x01",
            "You should be attracted.\x02\x03",
            "While dismantling the dispersed troops during that time,\x01",
            "You should head for Eli.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThe other party is a hunter, Zeit also\x01",
            "I think there is considerable danger … …\x02\x03",
            "#00001FPlease be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CHuh, do not waste it.\x01",
            "I do not intend to do it easily with myself.\x02\x03",
            "#01200FBe proud as a god wolf,\x01",
            "Let's say that you want the enemy to trick you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_979D")

    label("loc_9704")


    ChrTalk(
        0x13,
        (
            "#01203F#3CReturning to its former state, it is said to be a hunter\x01",
            "かなりの戦力をYou should be attracted.\x02\x03",
            "#01200FBe proud as a god wolf,\x01",
            "Let's say that you want the enemy to trick you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_979D")

    Jump("loc_9AC1")

    label("loc_97A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_985D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97BD")
    Call(1, 3)
    Jump("loc_9858")

    label("loc_97BD")


    ChrTalk(
        0x13,
        (
            "#01200F#3CFrom the time Ursula was alive\x01",
            "It is my fellow who has seen the crossbells for generations.\x02\x03",
            "Now let's go ahead with this situation\x01",
            "You will be watching,\x01",
            "There is nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9858")

    Jump("loc_9AC1")

    label("loc_985D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_9AC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A2D")

    ChrTalk(
        0x13,
        "#01200F#3C… … The daughter of that nurse … …\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FEr …\x01",
            "What's wrong with Cecil's older sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3C…… Huh, hey.\x01",
            "I thought that it was just a causal factor.\x02\x03",
            "It's not a big deal\x01",
            "It does not have to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWhat……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3CAnyway, with Tio\x01",
            "I was able to achieve the reunion\x01",
            "It can be said that it is 僥 僥.\x02\x03",
            "With this tune you can help the companion of the support section\x01",
            "Go get it back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, ah, I do not really understand … …\x01",
            "I will do that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9AC1")

    label("loc_9A2D")


    ChrTalk(
        0x13,
        (
            "#01200F#3CAnyway, with Tio\x01",
            "I was able to achieve the reunion\x01",
            "It can be said that it is 僥 僥.\x02\x03",
            "It seems to be busy now ……\x01",
            "Huff, see you later\x01",
            "Would you like to go see it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AC1")

    TalkEnd(0xFE)
    Return()

    # Function_22_8C72 end

    def Function_23_9AC5(): pass

    label("Function_23_9AC5")


    ChrTalk(
        0x13,
        (
            "#01200F#3COnce a \"god of treachery#8RDemi-gols#The\x01",
            "I chose to annihilate myself …\x02\x03",
            "I told Lloyd, I told you so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FRunaway and protect people to protect\x01",
            "To prevent it from hurting ……\x01",
            "That was such a story.\x02\x03",
            "#00003F…… Ka'a that is \"the treasure of zero\"\x01",
            "Will it be so …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3C…… I do not know.\x02\x03",
            "However, Ka'a became \"the treasure of zero\"\x01",
            "Finally I have the power comparable to the goddess\x01",
            "\"Taiki\" also produced.\x02\x03",
            "A great deal of power,\x01",
            "In the meantime, the guarantee that can be controlled\x01",
            "As of now no where.\x02\x03",
            "#01203F\"The treasure of the vision#8RDemi-gols#\"The same conclusion as\x01",
            "The possibility of arriving,\x01",
            "I guess that's not true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FReally……\x02\x03",
            "#00001FNo, I absolutely will not.\x01",
            "As long as we are … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#01200F#3C…… Huh, that is all I do.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 0)
    Return()

    # Function_23_9AC5 end

    def Function_24_9D9D(): pass

    label("Function_24_9D9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DC4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7F), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9DC4")
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1DE, 3)

    label("loc_9DC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6B), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DDF")
    Call(1, 53)
    Jump("loc_A440")

    label("loc_9DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_9E90")

    ChrTalk(
        0x14,
        (
            "#00603FYou have the potential of you.\x01",
            "By extending it\x01",
            "I will bring it closer to an excellent investigator.\x02\x03",
            "#00602FAiming for my own investigator,\x01",
            "You better keep going further.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A440")

    label("loc_9E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_A00E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EAB")
    Call(1, 25)
    Jump("loc_A009")

    label("loc_9EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F8B")

    ChrTalk(
        0x14,
        (
            "#00603FDeath of Guy · Bannings …\x01",
            "Beyond 3 years, finally\x01",
            "The truth was revealed.\x02\x03",
            "Afterwards, this incident\x01",
            "It only makes it resolve in the true sense.\x02\x03",
            "#00602FLet's go, Bannings.\x01",
            "Now let 's cross your older brother.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A009")

    label("loc_9F8B")


    ChrTalk(
        0x14,
        (
            "#00603FAfterwards, this incident\x01",
            "It only makes it resolve in the true sense.\x02\x03",
            "#00602FLet's go, Bannings.\x01",
            "Now let 's cross your older brother.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A009")

    Jump("loc_A440")

    label("loc_A00E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_A225")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A154")

    ChrTalk(
        0x14,
        (
            "#00600FDo not stop your feet, Bannings.\x01",
            "In order to approach the truth\x01",
            "We have to step forward one step at a time.\x02\x03",
            "#00603FMore than anything, \"Taiki\" to crossbell\x01",
            "I do not know what effect it will have,\x01",
            "It is necessary to clean up this case as soon as possible.\x02\x03",
            "#00608FMr. Ian, McRae ……\x01",
            "Although it is a partner who is not straightforward,\x01",
            "I will surely get over it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A220")

    label("loc_A154")


    ChrTalk(
        0x14,
        (
            "#00600F\"Taiki\" to crossbell\x01",
            "I do not know what effect it will have,\x01",
            "It is necessary to clean up this case as soon as possible.\x02\x03",
            "#00608FMr. Ian, McRae ……\x01",
            "Although it is a partner who is not straightforward,\x01",
            "I will surely get over it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A220")

    Jump("loc_A440")

    label("loc_A225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A440")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A393")

    ChrTalk(
        0x14,
        (
            "#00608FNo way, Professor Ian\x01",
            "I guess it was a black line … …\x02\x03",
            "#00610FKu, I go to my office\x01",
            "What is it, Zama, whilst passing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FMr. Dudley …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#00603F…… Anyway, this is how\x01",
            "Meet the teacher and McLaughl directly\x01",
            "There is no other choice but to ask your true intention.\x02\x03",
            "#00601FIt is no longer a matter of the support section alone.\x01",
            "Anyway I will grab the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes……!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A440")

    label("loc_A393")


    ChrTalk(
        0x14,
        (
            "#00603FAnyway, over this\x01",
            "Meet the teacher and McLaughl directly\x01",
            "There is no other choice but to ask your true intention.\x02\x03",
            "#00600FIt is no longer a matter of the support section alone.\x01",
            "Anyway I will grab the truth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A440")

    TalkEnd(0xFE)
    Return()

    # Function_24_9D9D end

    def Function_25_A444(): pass

    label("Function_25_A444")


    ChrTalk(
        0x14,
        (
            "#00600FDeath of Guy · Bannings …\x01",
            "Three years after, finally\x01",
            "Was the truth revealed?\x02\x03",
            "#00603FMcRae's such a burden\x01",
            "I was carrying it until now.\x02\x03",
            "#00608F…… He is clumsy anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FLet everything be their own commandments,\x01",
            "By breaking the escape path\x01",
            "Go forward … …\x02\x03",
            "#00008FThat's why Mr. Arios\x01",
            "It might be strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#00603F…… But that is the wrong strength.\x02\x03",
            "#00608FThat guy should have known … …\x01",
            "That is why they opened the way.\x02\x03",
            "#00600FAnyway, Bannings.\x01",
            "With this you also death of Guy\x01",
            "You ought to be overcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F……Yes.\x01",
            "It would be necessary to organize again,\x01",
            "It is all right now.\x02\x03",
            "#00001FIt is the last \"wall\" ……\x01",
            "Mr. Ian and Mary Bell\x01",
            "I have to look over getting over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#00604FThat's fine.\x02\x03",
            "#00602FIn a true sense this incident\x01",
            "To solve it … ….\x01",
            "There is only a progress now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes……!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 2)
    Return()

    # Function_25_A444 end

    def Function_26_A778(): pass

    label("Function_26_A778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A786")
    Call(0, 11)
    Return()

    label("loc_A786")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7A8")
    Call(1, 56)
    TalkEnd(0xFE)
    Return()

    label("loc_A7A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A936")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7D6")
    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x8, 0x0, 0)

    label("loc_A7D6")


    ChrTalk(
        0x8,
        (
            "#12100F… … That's right, because it's a big problem\x01",
            "I will hand this over to you.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Abbas account\"\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 0)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        (
            "#00000F\"Pomutto! Account …?\x01",
            "Are you also doing Abbas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102FIt's only when time is available.\x02\x03",
            "#12100FI will do my partner if I feel like it,\x01",
            "You may apply for a match.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A931")
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A931")

    Jump("loc_A973")

    label("loc_A936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A94C")
    Call(1, 28)
    Jump("loc_A973")

    label("loc_A94C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A962")
    Call(1, 29)
    Jump("loc_A973")

    label("loc_A962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A973")
    Call(1, 30)

    label("loc_A973")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A984")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_A9DD")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                # 0
            "Move in Mercapa\x01",      # 1
            "Party organization\x01",            # 2
            "quit\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    Jump("loc_AA25")

    label("loc_A9DD")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                # 0
            "Move in Mercapa\x01",      # 1
            "quit\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA25")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA25")

    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AA44"),
        (1, "loc_C050"),
        (2, "loc_C394"),
        (SWITCH_DEFAULT, "loc_C3B0"),
    )


    label("loc_AA44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_AB6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB03")

    ChrTalk(
        0x8,
        (
            "#12100F\"Red constellation\" and the future\x01",
            "There may be things involved … …\x02\x03",
            "It is now to solve this case\x01",
            "It is more important than anything else.\x02\x03",
            "Towards the final battle\x01",
            "Prepare thorough preparation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AB6A")

    label("loc_AB03")


    ChrTalk(
        0x8,
        (
            "#12100FAs we also star cup knight,\x01",
            "Let's fulfill our mission until the end.\x02\x03",
            "Also,\x01",
            "Prepare thorough preparation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB6A")

    Jump("loc_C04B")

    label("loc_AB6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_ABFF")

    ChrTalk(
        0x8,
        (
            "#12100F…… Vipers also\x01",
            "That's right, Wald\x01",
            "It will be worried.\x02\x03",
            "If the Crossbell crisis has passed\x01",
            "I have to collect it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C04B")

    label("loc_ABFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_AE79")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACDD")

    ChrTalk(
        0x8,
        (
            "#12100FThe damage to the aircraft is minor.\x01",
            "There is no problem in flight.\x02\x03",
            "We are always\x01",
            "To be able to leave \"Taiki\"\x01",
            "I'm waiting inside the ship.\x02\x03",
            "In case of withdrawing \"Taiki\"\x01",
            "Instruct it so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AD48")

    label("loc_ACDD")


    ChrTalk(
        0x8,
        (
            "#12100FIn the meantime Mercapa\x01",
            "It seems that there is not much damage.\x02\x03",
            "In case of withdrawing \"Taiki\"\x01",
            "Instruct it so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD48")

    Jump("loc_AE74")

    label("loc_AD4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE07")

    ChrTalk(
        0x8,
        (
            "#12100FThe damage to the aircraft is minor.\x01",
            "There is no problem in flight.\x02\x03",
            "\"A big blue tree\" To the inside\x01",
            "We also secured a safe route.\x02\x03",
            "If you aim for \"Taiki\" again\x01",
            "Instruct it so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AE74")

    label("loc_AE07")


    ChrTalk(
        0x8,
        (
            "#12100FIn the meantime Mercapa\x01",
            "It seems that there is not much damage.\x02\x03",
            "If you aim for \"Taiki\" again\x01",
            "Instruct it so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE74")

    Jump("loc_C04B")

    label("loc_AE79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B035")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFA0")

    ChrTalk(
        0x8,
        (
            "#12100FThe appearance of \"Ao no Taiki\"\x01",
            "What does it mean, the church too\x01",
            "It is a situation I have not grasped yet.\x02\x03",
            "When you board over there,\x01",
            "No matter what happens\x01",
            "It is not amusing.\x02\x03",
            "Now in various parts of Crossbell\x01",
            "It is also possible to get off … …\x02\x03",
            "If there is something to do\x01",
            "Even if you give priority to that\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B030")

    label("loc_AFA0")


    ChrTalk(
        0x8,
        (
            "#12100FThe appearance of \"Ao no Taiki\"\x01",
            "What does it mean, the church too\x01",
            "It is a situation I have not grasped yet.\x02\x03",
            "Either way, before getting on\x01",
            "It is to prepare firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B030")

    Jump("loc_C04B")

    label("loc_B035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B477")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_B256")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1A7")

    ChrTalk(
        0x8,
        (
            "#12100FOne more bell to stop … …\x01",
            "Ursula is a tower of the stomach at the end of the interstate.\x02\x03",
            "But it is a pillar of the apostle\x01",
            "\"Steel's Saint\" with Ariane Road\x01",
            "The warriors of their subordinates are waiting.\x02\x03",
            "It would be a difficult task to get over it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F…… Anyway, there is no choice but to do.\x01",
            "Let's find a winner somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102FWell, I said well.\x01",
            "Let's face it as soon as the resolution is decided.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B251")

    label("loc_B1A7")


    ChrTalk(
        0x8,
        (
            "#12100F\"Tower of Hoshi\"\x01",
            "A \"pillar of steel\" and pillar of the apostle\x01",
            "The warriors of their subordinates are waiting.\x02\x03",
            "It would be a difficult task to get over it … …\x01",
            "You decide your mind and get over it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B251")

    Jump("loc_B472")

    label("loc_B256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3C1")

    ChrTalk(
        0x8,
        (
            "#12100FThe first destination is \"Monaster of the Moon\" … …\x01",
            "In Mainz direction,\x01",
            "It is one of medieval ruins.\x02\x03",
            "According to the elderly Jorg,\x01",
            "One of the enforcers waiting\x01",
            "\"Clown\" Campanella ……\x02\x03",
            "As usual it seems to be totally behind,\x01",
            "There is also little information here.\x01",
            "…… It is quite a creepy person.\x02\x03",
            "I do not know what to set up.\x01",
            "To accommodate every situation\x01",
            "Prepare enough for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B472")

    label("loc_B3C1")


    ChrTalk(
        0x8,
        (
            "#12100F\"Monastery Monastery\"\x01",
            "One of the enforcers waiting,\x01",
            "\"Clown\" Campanella ……\x02\x03",
            "I do not know what to set up.\x01",
            "To accommodate every situation\x01",
            "Prepare enough for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B472")

    Jump("loc_C04B")

    label("loc_B477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_B6CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5ED")

    ChrTalk(
        0x8,
        (
            "#12100FBy Makdael chairman being deprived,\x01",
            "By the defense forces and hunters on the ground\x01",
            "It seems that it was in a state of caution.\x02\x03",
            "In this situation, Mercava will be held everywhere\x01",
            "I will not be able to land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI see.\x01",
            "Now for a strategy at the booster\x01",
            "It seems better to concentrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FWell, after that the timing of the start\x01",
            "It is just to estimate.\x02\x03",
            "When you are ready, call out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B6C6")

    label("loc_B5ED")


    ChrTalk(
        0x8,
        (
            "#12100FUnder this extremely cautionary stance, Melkava is placed in various places\x01",
            "It can not be landed.\x02\x03",
            "Now heading to the booster point\x01",
            "To make the strategy successful\x01",
            "You'd better concentrate.\x02\x03",
            "This setup is attached.\x01",
            "When you are ready, call out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6C6")

    Jump("loc_C04B")

    label("loc_B6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_B92C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B856")

    ChrTalk(
        0x8,
        (
            "#12100FWhen arriving at Michelin,\x01",
            "Immediately after the hunter's interception\x01",
            "It is expected to start.\x02\x03",
            "To prevent shooting down by anti-aircraft weapons\x01",
            "Mercapa for a while\x01",
            "I will hide myself in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FOnce you get off, Eli and you\x01",
            "I can not return until I rescued …\x01",
            "After all it seems to be a tough fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FWell, probably more than you imagined.\x02\x03",
            "Equipment, an auction, a recovery drug ……\x01",
            "Prepare everything perfectly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B927")

    label("loc_B856")


    ChrTalk(
        0x8,
        (
            "#12100FWhen battle begins in Mishram\x01",
            "To prevent shooting down by anti-aircraft weapons\x01",
            "艦はしばらくI will hide myself in the sky.\x02\x03",
            "Meanwhile, you can not go back to the ship.\x01",
            "Equipment, an auction, a recovery drug ……\x01",
            "Prepare everything perfectly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B927")

    Jump("loc_C04B")

    label("loc_B92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_BB45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAC0")

    ChrTalk(
        0x8,
        (
            "#12100FThat reporter asked me about Mercapa and Wadi\x01",
            "It seems to be investigating in detail.\x02\x03",
            "…… Hello, those who are involved in the press\x01",
            "It's unheard of so far as to get on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, well … indeed\x01",
            "I think it's just curiosity,\x01",
            "Is not it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F… Well good.\x01",
            "That's what Waza has allowed.\x02\x03",
            "If there is something about you,\x01",
            "Bannings, you are also responsible\x01",
            "I'll get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Why am I … ….)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BB40")

    label("loc_BAC0")


    ChrTalk(
        0x8,
        (
            "#12100FWell, who is involved in the press\x01",
            "For example,\x01",
            "It is unheard of … …\x02\x03",
            "Well, that's what Wazi has allowed\x01",
            "There is no choice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB40")

    Jump("loc_C04B")

    label("loc_BB45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_BCAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC0D")

    ChrTalk(
        0x8,
        (
            "#12100FIt moves under another belief from \"Black moon\"\x01",
            "Resistance of the guard?\x02\x03",
            "Either way, over the opposite\x01",
            "I will not leave the President's side.\x02\x03",
            "行くなら急いだ方がIt might be nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BCA6")

    label("loc_BC0D")


    ChrTalk(
        0x8,
        (
            "#12100FRegardless of the resistance of the guard,\x01",
            "With the strength of defense army and hunter\x01",
            "It will be hard to endure long.\x02\x03",
            "行くなら急いだ方がIt might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCA6")

    Jump("loc_C04B")

    label("loc_BCAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_BEAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDFF")

    ChrTalk(
        0x8,
        (
            "#12100FIt is used in the engine section of Mercapa\x01",
            "\"Heavenly car\" has original flight function\x01",
            "It was a ride of artifacts … …\x02\x03",
            "After the power revolution, with the cooperation of the foundation\x01",
            "It was renovated to its present form.\x02\x03",
            "Besides that, the tactical auction\x01",
            "Partly in cooperation with development etc.\x02\x03",
            "…… But to the last\x01",
            "Secularly it is an informal matter.\x01",
            "Do not let it leak out to the outside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BEA7")

    label("loc_BDFF")


    ChrTalk(
        0x8,
        (
            "#12100FMercapa and tactical auctions\x01",
            "With the cooperation of the foundation and the church\x01",
            "Although it was born for the first time … ….\x02\x03",
            "……あくまでSecularly it is an informal matter.\x01",
            "Do not let it leak out to the outside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEA7")

    Jump("loc_C04B")

    label("loc_BEAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C04B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEC7")
    Call(1, 27)
    Jump("loc_C04B")

    label("loc_BEC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFC5")

    ChrTalk(
        0x8,
        (
            "#12100FWhen moving to a new place\x01",
            "Waji 's command and vigilance against \"shinkin\" are necessary,\x01",
            "This system will be sufficient under the current situation.\x02\x03",
            "I do not need worry about this,\x01",
            "Preparation of equipments and the auction\x01",
            "Keep it well.\x02\x03",
            "If you are ready to get off the ground\x01",
            "Tell a voice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C04B")

    label("loc_BFC5")


    ChrTalk(
        0x8,
        (
            "#12100FI do not need worry about this,\x01",
            "Preparation of equipments and the auction\x01",
            "Keep it well.\x02\x03",
            "If you are ready to get off the ground\x01",
            "Tell a voice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C04B")

    Jump("loc_C3BA")

    label("loc_C050")

    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_C385")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C173")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C0A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C16E")
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C169")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C169")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_C15A")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C14A")
    Call(0, 6)
    Jump("loc_C14D")

    label("loc_C14A")

    Call(0, 5)

    label("loc_C14D")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_C169")

    label("loc_C15A")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_C169")

    Jump("loc_C0A9")

    label("loc_C16E")

    Jump("loc_C37F")

    label("loc_C173")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C25A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C190")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C255")
    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C250")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C250")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_C241")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C231")
    Call(0, 6)
    Jump("loc_C234")

    label("loc_C231")

    Call(0, 5)

    label("loc_C234")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_C250")

    label("loc_C241")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_C250")

    Jump("loc_C190")

    label("loc_C255")

    Jump("loc_C37F")

    label("loc_C25A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C341")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C277")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C33C")
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C337")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C337")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_C328")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C318")
    Call(0, 6)
    Jump("loc_C31B")

    label("loc_C318")

    Call(0, 5)

    label("loc_C31B")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_C337")

    label("loc_C328")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_C337")

    Jump("loc_C277")

    label("loc_C33C")

    Jump("loc_C37F")

    label("loc_C341")

    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C35D")
    Call(0, 12)

    label("loc_C35D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C374")
    Call(0, 6)
    Jump("loc_C377")

    label("loc_C374")

    Call(0, 5)

    label("loc_C377")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)

    label("loc_C37F")

    Return()

    label("loc_C385")

    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_C3BA")

    label("loc_C394")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C3BA")

    label("loc_C3B0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C3BA")

    Jump("loc_A984")

    label("loc_C3BF")

    OP_60(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_A778 end

    def Function_27_C3C6(): pass

    label("Function_27_C3C6")


    ChrTalk(
        0x8,
        (
            "#12100FI got in touch with you earlier.\x01",
            "The Mercapa Unit successfully\x01",
            "It seems that he shook out the \"Shinto priest\".\x02\x03",
            "Sir Graham and the crew\x01",
            "It seems that there is no damage for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see … I was relieved.\x02\x03",
            "#00005FBy the way, Abbas.\x01",
            "Is it okay away from the cockpit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FDo not worry ……\x01",
            "In this seat most functions of \"Mercapa\"\x01",
            "You can grasp it.\x02\x03",
            "Besides, now we set the automatic piloting mode\x01",
            "Because I am stuck in the sky above the \"clearance\"\x01",
            "You do not have to sit in the cockpit.\x02\x03",
            "When moving to a new place\x01",
            "Waji 's command and vigilance against \"shinkin\" are necessary,\x01",
            "This system will be sufficient under the current situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see……\x01",
            "After all it seems to be considerably high performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FAnyway, while you are on the ship\x01",
            "準備をKeep it well.\x02\x03",
            "If you are ready to get off the ground\x01",
            "Tell a voice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 3)
    Return()

    # Function_27_C3C6 end

    def Function_28_C67F(): pass

    label("Function_28_C67F")


    ChrTalk(
        0x8,
        (
            "#12100FMirror armor of the aircraft and\x01",
            "Leave it to the impact field\x01",
            "I broke through, but …\x02\x03",
            "The damage to the aircraft is minor.\x01",
            "There is no problem in flight.\x02\x03",
            "We are always\x01",
            "To be able to leave \"Taiki\"\x01",
            "I'm waiting inside the ship.\x02\x03",
            "In case of withdrawing \"Taiki\"\x01",
            "Instruct it so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 5)
    Return()

    # Function_28_C67F end

    def Function_29_C776(): pass

    label("Function_29_C776")


    ChrTalk(
        0x8,
        (
            "#12100FI heard he dismissed Wald.\x02\x03",
            "…… With him, two years ago\x01",
            "Sneak into the cross bell with Wadi\x01",
            "Sincerely a relationship … …\x02\x03",
            "As a camouflage\x01",
            "Since we formed our tests,\x01",
            "Was this review helpful?\x02\x03",
            "For a while, Rubathe\x01",
            "In case of working conspiracy\x01",
            "Although it became slightly bad, … ….\x02\x03",
            "For Wadi, Waldo\x01",
            "It is a good fighting companion,\x01",
            "I guess it was also my best friend.\x02\x03",
            "#12102FOf course there are also Wadi for Wald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIt certainly breathed a lot though … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FI did not seriously serve him,\x01",
            "Such factors are one reason\x01",
            "It may be because it was.\x02\x03",
            "Well, Wadi will not put it in words\x01",
            "I do not know the truth, but …\x02\x03",
            "…… I wasted a useless story.\x01",
            "Do not speak anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, I see.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 6)
    Return()

    # Function_29_C776 end

    def Function_30_CA1D(): pass

    label("Function_30_CA1D")


    ChrTalk(
        0x8,
        (
            "#12100F… …. you guys\x01",
            "It's time to fight \"Sorority\" … …\x02\x03",
            "In this \"god area\"\x01",
            "The flying object intruded\x01",
            "The ship 's radar perceived.\x02\x03",
            "Apparently, the red constellation\x01",
            "It seems to be \"Beowulf.\"\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FOh … was it OK? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FWell, I will not give my eyes here\x01",
            "Drop down to another point, after a while\x01",
            "It seems that I left my family outside \"Taiki\".\x02\x03",
            "Probably, \"red war demon\" and\x01",
            "\"Blood Dyeing Charlie\"\x01",
            "It seems that they collected them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FReally……\x01",
            "As police they also\x01",
            "I wanted to listen to the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FWell, there is nothing it can do.\x01",
            "Even though the waiting team alone is trying to stop it\x01",
            "You did not have it.\x02\x03",
            "The goodness of the close,\x01",
            "It would be unique to hunting corps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI also encounter someday\x01",
            "There might be something ……\x02\x03",
            "#00001F…… But now,\x01",
            "To solve this incident\x01",
            "It seems better to concentrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FWell, that's right.\x02\x03",
            "Towards the final battle\x01",
            "Prepare thorough preparation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 7)
    Return()

    # Function_30_CA1D end

    def Function_31_CD63(): pass

    label("Function_31_CD63")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CE13")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6E), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD8E")
    Call(1, 52)
    TalkEnd(0xC)
    Return()

    label("loc_CD8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_CE13")

    ChrTalk(
        0xC,
        (
            "#01909FThat amulet,\x01",
            "Please take good care of ~ ~.\x02\x03",
            "Pray for your safety\x01",
            "Because it is made,\x01",
            "Surely the effect is outstanding!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_CE13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D067")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF32")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CEBE")
    Jump("loc_CF08")

    label("loc_CEBE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CEDE")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF08")

    label("loc_CEDE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEFE")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF08")

    label("loc_CEFE")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF08")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Jump("loc_CF42")

    label("loc_CF32")

    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xC, 0x0, 0)

    label("loc_CF42")


    ChrTalk(
        0xC,
        (
            "#01900FEveryone, \"Pomutto! \"\x01",
            "Do you know the guiding game?\x02\x03",
            "#01909FHuhu, in fact, I also started.\x01",
            "Please exchange your account if you do not mind.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Account of Franc\"\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 4)
    OP_E4(0x3)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D059")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D050")
    ClearChrFlags(0xC, 0x10)

    label("loc_D050")

    SetChrSubChip(0xC, 0x0)
    Jump("loc_D062")

    label("loc_D059")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D062")

    Jump("loc_E6C9")

    label("loc_D067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_D22E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D082")
    Call(1, 33)
    Jump("loc_D229")

    label("loc_D082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D19F")

    ChrTalk(
        0xC,
        (
            "#01904FTo wait with anxiety,\x01",
            "You are fighting with everyone\x01",
            "That's what it is ….\x02\x03",
            "#01902FThen,\x01",
            "I have one thing to do.\x02\x03",
            "#01909FFrustration, fran · seeker ……\x01",
            "Here's your sister and everyone's\x01",
            "I pray for safety!\x02\x03",
            "Absolutely, absolutely,\x01",
            "Please come home safely!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D229")

    label("loc_D19F")


    ChrTalk(
        0xC,
        (
            "#01909FFrustration, fran · seeker ……\x01",
            "Here's your sister and everyone's\x01",
            "I pray for safety!\x02\x03",
            "Absolutely, absolutely,\x01",
            "Please come home safely!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D229")

    Jump("loc_E6C9")

    label("loc_D22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_D3F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D369")

    ChrTalk(
        0xC,
        (
            "#01900FThe inside of \"Taiki\"\x01",
            "It's beautiful\x01",
            "I did not feel well thought ~.\x02\x03",
            "#01904FIf it is not such a time,\x01",
            "A landscape forever\x01",
            "I would like to have fun ~!\x02\x03",
            "#01905F…… Well, I dont wanna.\x01",
            "You should not let your guard down.\x02\x03",
            "#01909FAnyway, please do your best!\x01",
            "I support you here ~!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D3F3")

    label("loc_D369")


    ChrTalk(
        0xC,
        (
            "#01906FThe inside of \"Taiki\" is beautiful,\x01",
            "You should not let your guard down.\x02\x03",
            "#01909FAnyway, please do your best!\x01",
            "I support you here ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3F3")

    Jump("loc_E6C9")

    label("loc_D3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D548")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4CB")

    ChrTalk(
        0xC,
        (
            "#01905FThat thing that rushes into \"that big tree\"\x01",
            "I am a bit scared, but ….\x02\x03",
            "#01901F…… I am also a policeman.\x01",
            "If you do not show a chest like this\x01",
            "You can not!\x02\x03",
            "#01909FLloyd, let's do our best!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D543")

    label("loc_D4CB")


    ChrTalk(
        0xC,
        (
            "#01901F…… I am also a policeman.\x01",
            "If you do not show a chest like this\x01",
            "You can not!\x02\x03",
            "#01909FLloyd, let's do our best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D543")

    Jump("loc_E6C9")

    label("loc_D548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_D725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D677")

    ChrTalk(
        0xC,
        (
            "#01900FEven the barrier and the white \"god machine\"\x01",
            "Somehow, invade the city\x01",
            "It seems likely to add up on matters.\x02\x03",
            "#01904FSergey section chiefs in the city as well\x01",
            "\"Invalid declaration\" will have arrived,\x01",
            "You may have started to do that.\x02\x03",
            "#01909FAnyway, I'm doing my best!\x01",
            "Lloyds, please do their best!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D720")

    label("loc_D677")


    ChrTalk(
        0xC,
        (
            "#01900FEven the barrier and the white \"god machine\"\x01",
            "Somehow, invade the city\x01",
            "It seems likely to add up on matters.\x02\x03",
            "#01909FAnyway, I'm doing my best!\x01",
            "Lloyds, please do their best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D720")

    Jump("loc_E6C9")

    label("loc_D725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_DAD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA09")

    ChrTalk(
        0xC,
        (
            "#01904F(Rattling rattling … …)\x02\x03",
            "Ahh, testess …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FFranc, what are you doing?\x02",
    )

    CloseMessageWindow()
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D829")
    Jump("loc_D873")

    label("loc_D829")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D849")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D873")

    label("loc_D849")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D869")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D873")

    label("loc_D869")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D873")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        (
            "#01902FOh, Mr. Lloyd.\x01",
            "Mike and camera test\x01",
            "I am doing it ~.\x02\x03",
            "From Mercapa's monitoring system\x01",
            "Via the power net, to various places\x01",
            "I am planning to send video and audio.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    ChrTalk(
        0xC,
        (
            "#01904F\"I am Fran · Seeker.\x01",
            "I love you, Sister! \"\x02\x03",
            "#01909F…… Yes, speech recognition is good ~ is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(Even in this situation\x01",
            "I will not be able to be harmonized by the franc … …)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 4)
    Jump("loc_DAD1")

    label("loc_DA09")


    ChrTalk(
        0xC,
        (
            "#01902FFrom Mercapa's monitoring system\x01",
            "Via the power net, to various places\x01",
            "I am planning to send video and audio.\x02\x03",
            "#01909FMr. MacDaely's voice\x01",
            "In order to hear from the citizens well,\x01",
            "We have to check carefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAD1")

    Jump("loc_E6C9")

    label("loc_DAD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_DC6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAF1")
    Call(1, 13)
    Jump("loc_DC68")

    label("loc_DAF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBFC")

    ChrTalk(
        0xC,
        (
            "#01912FHuhu, old sister is coming back\x01",
            "I was really happy.\x02\x03",
            "#01901FMr. Lloyd ……\x01",
            "About my older sister,\x01",
            "Thank you!\x02\x03",
            "#01909FMe too\x01",
            "Because I will support you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Well, hmm … ….\x01",
            "I feel like I misunderstood something. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DC68")

    label("loc_DBFC")


    ChrTalk(
        0xC,
        (
            "#01901FAbout my older sister,\x01",
            "Thank you!\x02\x03",
            "#01909FMe too\x01",
            "Because I will support you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC68")

    Jump("loc_E6C9")

    label("loc_DC6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_DDF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD93")

    ChrTalk(
        0xC,
        (
            "#01908FWest Crossbell Highway ……\x01",
            "There is a Belgard gate.\x02\x03",
            "#01903FPerhaps there are older sisters ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#01906FWell, you can not do this.\x01",
            "I have to be firm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Fran, of course\x01",
            "I'm worried about Noel … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DDF1")

    label("loc_DD93")


    ChrTalk(
        0xC,
        (
            "#01908FPerhaps in the Belgard gate, my sister ……\x02\x03",
            "#01906F…… What are you doing now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDF1")

    Jump("loc_E6C9")

    label("loc_DDF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E4E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E322")

    ChrTalk(
        0xC,
        (
            "#01908F…… Onee-san, with us\x01",
            "Even accepting even conflicts,\x01",
            "I chose the current road ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FOh … honestly,\x01",
            "I think that it is not amusing.\x02\x03",
            "#00003FTo Noel to that place\x01",
            "What is it that made me commit … …\x02\x03",
            "#00008FOnly this series of cases\x01",
            "I feel that it is not a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01903F… … Maybe … …\x02\x03",
            "#01901FBy the time we were small,\x01",
            "That my father passed away\x01",
            "I think that it is in the root.\x02\x03",
            "#01908F…… During the exercises performed by the Republican Army,\x01",
            "By rifle 's \"firing\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHuh……! Is it?\x02\x03",
            "Your father,\x01",
            "In \"accident\" about ten years ago\x01",
            "It's a story about death …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01906FBecause I was still small,\x01",
            "I do not remember details, but ….\x02\x03",
            "#01908FThe Republican Army shot erroneously during exercises,\x01",
            "To a father who happens to be guarding it … ….\x01",
            "It seems that it was that it was that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F……Is that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01903FBut in the crossbell 's position,\x01",
            "I do not care about that\x01",
            "Of course I can not do it ….\x02\x03",
            "#01908FTherefore, as a mere \"accident\" to the end,\x01",
            "It seems that it has been processed.\x02\x03",
            "My mother seems to have grieved,\x01",
            "Because it is dangerous work originally\x01",
            "It seems I had no choice but to accept …\x02\x03",
            "#01903F… … But probably, Onee said,\x01",
            "I have not been convinced for a long time …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F… … Maybe so.\x02\x03",
            "#00003F(Noel wants to protect the crossbell\x01",
            "Strongly wish for reason … … somehow\x01",
            "I feel like I understood … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 7)
    Jump("loc_E4E1")

    label("loc_E322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E467")

    ChrTalk(
        0xC,
        (
            "#01908F……Excuse me.\x01",
            "Somehow it has been plain.\x02\x03",
            "#01903FI objected to the state of Defense Forces\x01",
            "Former Guard member ……\x02\x03",
            "#01900FNow I am going to join the people\x01",
            "First of all we have to think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh … That's right.\x02\x03",
            "#00000FFran, I'm begging for your backup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01909FYes, I will do my best ~!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E4E1")

    label("loc_E467")


    ChrTalk(
        0xC,
        (
            "#01903FI objected to the state of Defense Forces\x01",
            "Former Guard member ……\x02\x03",
            "#01900FIf you are not older sister,\x01",
            "Who the hell is she?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4E1")

    Jump("loc_E6C9")

    label("loc_E4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_E6C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E501")
    Call(1, 32)
    Jump("loc_E6C9")

    label("loc_E501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E613")

    ChrTalk(
        0xC,
        (
            "#01900FAs you search for \"gaps\"\x01",
            "The reaction of dangerous monsters is also\x01",
            "It seems to be detecting it.\x02\x03",
            "From now on I will take responsibility,\x01",
            "As an official support request\x01",
            "Because I will send information to the terminal ~.\x02\x03",
            "#01909FWhen you exterminate monsters,\x01",
            "Do not forget at the terminal in the cabin\x01",
            "Thank you for your report ~!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E6C9")

    label("loc_E613")


    ChrTalk(
        0xC,
        (
            "#01900FI am still immature,\x01",
            "How to help with Mercapa\x01",
            "I will do my utmost!\x02\x03",
            "#01909FEverybody, if you eradicate an arrangement devil\x01",
            "On the terminal in the cabin\x01",
            "Thank you for your report ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6C9")

    TalkEnd(0xC)
    Return()

    # Function_31_CD63 end

    def Function_32_E6CD(): pass

    label("Function_32_E6CD")


    ChrTalk(
        0xC,
        (
            "#01900FIn this Mercapa, it seems like it was in support section\x01",
            "I have a terminal for reporting … ….\x02\x03",
            "#01909FFrom now on, I will take responsibility\x01",
            "Send support request information\x01",
            "We decided to have ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, is that so?\x01",
            "Certainly to the cabin\x01",
            "I had such a terminal … ….\x02\x03",
            "#00003FBy the way, where is such information from\x01",
            "I wonder if they are coming in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01905FI also became obsessed,\x01",
            "I asked Abbas, but ….\x02\x03",
            "#01904FApparently, looking for \"gaps\"\x01",
            "The reaction of dangerous monsters is also\x01",
            "It seems to be detecting it.\x02\x03",
            "#01902FWhen Mercova performs a strategy action\x01",
            "Discover obstacles at an early stage,\x01",
            "It seems to be a function to cope, ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see……\x01",
            "Certainly, it's dangerous to leave it alone\x01",
            "It might be good to go get rid of it in between.\x02\x03",
            "#00009FBut, are you reporting to the fran …?\x01",
            "It's been a long time since I was a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909FHehe, it is true!\x01",
            "I am also deeply embarrassed ~.\x02\x03",
            "#01906FFrom the terminal of the cabin it is\x01",
            "It might be a bit of a challenge, but …\x02\x03",
            "#01900FWhen I came back to the police\x01",
            "In order to have a legitimate evaluation,\x01",
            "Please do it as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F… Ah, that's right.\x02\x03",
            "#00000FWell then, like before\x01",
            "Regrettably ask the operator, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01909FYes, this is it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 3)
    Return()

    # Function_32_E6CD end

    def Function_33_EB4B(): pass

    label("Function_33_EB4B")


    ChrTalk(
        0xC,
        (
            "#01903FTruly, truly, this is the last\x01",
            "It is a mountain, is not it ~ ……\x02\x03",
            "#01908FAt such times, in a safe place\x01",
            "What I can only do is wait\x01",
            "After all it is impolite …\x02\x03",
            "#01906FI am in the same place with you\x01",
            "It became to fight, how many times I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Nothing but battle with enemies only\x01",
            "It does not mean \"fight\".\x02\x03",
            "#00000FFran and all the others\x01",
            "Because it is waiting,\x01",
            "We can do our best.\x02\x03",
            "No matter how hot it is,\x01",
            "Absolutely go back to that place …\x01",
            "Because I think from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01900FMr. Lloyd ……\x01",
            "……I understand.\x02\x03",
            "#01909FFrustration, fran · seeker ……\x01",
            "Here's your sister and everyone's\x01",
            "I pray for safety!\x02\x03",
            "Absolutely, absolutely,\x01",
            "Please come home safely!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FAh……!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 3)
    Return()

    # Function_33_EB4B end

    def Function_34_EDD0(): pass

    label("Function_34_EDD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF08")

    ChrTalk(
        0x9,
        (
            "#02305FThat reminds me … …\x01",
            "\"Pomutto! Account\x01",
            "You have it?\x02\x03",
            "#02304FHuhun, this is because of this Jonah-sama\x01",
            "I will give you an account.\x02\x03",
            "#02309FI was involved from the development stage\x01",
            "If you can win, try winning.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Account of Yona\"\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 7)
    OP_E4(0x3)
    Jump("loc_F748")

    label("loc_EF08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_F08C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF23")
    Call(1, 36)
    Jump("loc_F087")

    label("loc_EF23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F007")

    ChrTalk(
        0x9,
        (
            "#02306FShey, what is it.\x01",
            "People are worried carelessly\x01",
            "Well ……\x02\x03",
            "#02300FHuh, well …\x01",
            "You'd better do your best at best.\x02\x03",
            "#02309FHurry up and it will be like before\x01",
            "Dedicated guiding net life\x01",
            "Please let me get it back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F087")

    label("loc_F007")


    ChrTalk(
        0x9,
        (
            "#02300Fまあ、You'd better do your best at best.\x02\x03",
            "#02309FHurry up and it will be like before\x01",
            "Dedicated guiding net life\x01",
            "Please let me get it back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F087")

    Jump("loc_F748")

    label("loc_F08C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_F254")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1CF")

    ChrTalk(
        0x9,
        (
            "#02301FThat innumerable light\x01",
            "Candy being sucked into the tree …\x01",
            "It seems like a conceptual image of a power net.\x02\x03",
            "#02303FThink about it, Croix family's guys\x01",
            "I was using the power net as a conspiracy.\x02\x03",
            "The figure of that \"big tree\"\x01",
            "I have something to do with their \"plan\".\x02\x03",
            "#02302FWell, the analysis of that area\x01",
            "I will leave it to you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F24F")

    label("loc_F1CF")


    ChrTalk(
        0x9,
        (
            "#02303FThe figure of that \"big tree\"\x01",
            "It may be related to their \"plan\".\x02\x03",
            "#02302FWell, the analysis of that area\x01",
            "I will leave it to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F24F")

    Jump("loc_F748")

    label("loc_F254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F39E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F325")

    ChrTalk(
        0x9,
        (
            "#02303FI am on the base of the geo front\x01",
            "I could have returned but ….\x02\x03",
            "#02302FNow this one looks interesting,\x01",
            "Because it's been troublesome to the end\x01",
            "I will go out with you.\x02\x03",
            "#02304FHello, thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F399")

    label("loc_F325")


    ChrTalk(
        0x9,
        (
            "#02302FNow this one looks interesting,\x01",
            "Because it's been troublesome to the end\x01",
            "I will go out with you.\x02\x03",
            "#02304FHello, thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F399")

    Jump("loc_F748")

    label("loc_F39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_F5A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F50C")

    ChrTalk(
        0x9,
        (
            "#02302FHacking to the power net\x01",
            "It worked better than I expected.\x02\x03",
            "#02306FHowever, the route from the radio booster\x01",
            "Since it was completely blocked,\x01",
            "I guess it will be unpleasant to do it again.\x02\x03",
            "#02309FWell, oh well.\x01",
            "For the time being to the towers\x01",
            "I guess I could have blown a bubble.\x02\x03",
            "#02302FThe rest is finally\x01",
            "Liberate Crossbell City,\x01",
            "I have to get back my base!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F5A2")

    label("loc_F50C")


    ChrTalk(
        0x9,
        (
            "#02300FIt seems there is somehow a strong partner,\x01",
            "I asked for your kindness.\x02\x03",
            "#02309FとっととLiberate Crossbell City,\x01",
            "I have to get back my base!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5A2")

    Jump("loc_F748")

    label("loc_F5A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_F748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5C2")
    Call(1, 35)
    Jump("loc_F748")

    label("loc_F5C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6BC")

    ChrTalk(
        0x9,
        (
            "#02306FAnyway, I am in a place without terminals\x01",
            "To the guys who got pushed in,\x01",
            "I have to get back the patch.\x02\x03",
            "#02310FEspecially that Mary Bell!\x01",
            "I'll let you know that Akuma!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(It seems there is considerable grudge … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F748")

    label("loc_F6BC")


    ChrTalk(
        0x9,
        (
            "#02302FHurry up here anytime\x01",
            "Ready to get started!\x02\x03",
            "#02309FLook at the terminal in the crossbell\x01",
            "I will deliver an invalid declaration!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F748")

    TalkEnd(0xFE)
    Return()

    # Function_34_EDD0 end

    def Function_35_F74C(): pass

    label("Function_35_F74C")


    ChrTalk(
        0x9,
        (
            "#02305FOkay, have not you started the strategy yet?\x02\x03",
            "Hurry up here anytime\x01",
            "Ready to get started!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FI guess it's kinda na …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02304FHehe, I am in a place without internet environment\x01",
            "To the guys who got pushed in,\x01",
            "I can finally get back the owner.\x02\x03",
            "#02302FLook at the terminal in the crossbell\x01",
            "The face and voice of that chairman Osassu\x01",
            "I will deliver it perfectly!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003FMcDowell, you know.\x02\x03",
            "#00001FJonah, even at such times\x01",
            "About courtesy is properly\x01",
            "You have to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02306FAh, already,\x01",
            "As usual it is Rusa.\x02\x03",
            "#02302FStop the strategy quickly\x01",
            "Please start!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 6)
    Return()

    # Function_35_F74C end

    def Function_36_F99A(): pass

    label("Function_36_F99A")


    ChrTalk(
        0x9,
        (
            "#02300FSomehow, last at last\x01",
            "Looking closer.\x02\x03",
            "#02303F… … Is that okay?\x01",
            "That Maria Bell and the other girl\x01",
            "I guess I'm waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, it is unusual …\x01",
            "Are you worried about us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02305FOh, you are near me!\x01",
            "If you do not like tons like this\x01",
            "Everyone worried!\x02\x03",
            "#02306FShey, what is it.\x01",
            "People are crazy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, I'm sorry.\x02\x03",
            "#00000F… …. Thank you, Jonah.\x01",
            "We will surely return safely.\x02\x03",
            "To be able to leave the outside at any time\x01",
            "I have asked for a lot of preparation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02303FHun, I understand.\x01",
            "You'd better do your best at best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 6)
    Return()

    # Function_36_F99A end

    def Function_37_FBC0(): pass

    label("Function_37_FBC0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_FBD1")
    Jump("loc_100B5")

    label("loc_FBD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_FBDF")
    Jump("loc_100B5")

    label("loc_FBDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FBED")
    Jump("loc_100B5")

    label("loc_FBED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_FD70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD02")

    ChrTalk(
        0xF,
        (
            "#02103FMysterious association \"Serving meat snake#10RUroboros#\"… ….\x01",
            "Even if the incident happened at Libert\x01",
            "Talk about it after daring.\x02\x03",
            "#02101FNot much in the case this time\x01",
            "I did not come out,\x01",
            "I protect important places so much ……\x02\x03",
            "#02106F…… Alright, what is their purpose?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_FD6B")

    label("loc_FD02")


    ChrTalk(
        0xF,
        (
            "#02103FSociety \"snake snake\" ……\x02\x03",
            "#02101FOnly the mystery bulges,\x01",
            "What is their true purpose?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD6B")

    Jump("loc_100B5")

    label("loc_FD70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_FF13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE63")

    ChrTalk(
        0xF,
        (
            "#02102FThe setup of \"invalid declaration\" is also\x01",
            "Finally it solidified.\x02\x03",
            "Mr. MacDaely also\x01",
            "I made a declaration statement,\x01",
            "Just move on to the rest …\x02\x03",
            "#02106F… … Well, I'm getting nervous somehow ~!\x01",
            "I wonder if I will also practice vocal exercises on the deck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_FF0E")

    label("loc_FE63")


    ChrTalk(
        0xF,
        (
            "#02102FMr. MacDaely also\x01",
            "I made a declaration statement,\x01",
            "Just move on to the rest …\x02\x03",
            "#02106F… … Well, I'm getting nervous somehow ~!\x01",
            "I wonder if I will also practice vocal exercises on the deck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF0E")

    Jump("loc_100B5")

    label("loc_FF13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_100B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF2E")
    Call(1, 38)
    Jump("loc_100B5")

    label("loc_FF2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10054")

    ChrTalk(
        0xF,
        (
            "#02109FWell then, Mr. Lisha to Waji.\x01",
            "I will continue the interview ~!\x02\x03",
            "It's just that I care.\x01",
            "Of course I will not post it\x01",
            "Please speak with confidence in various ways!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10706FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10409FWhew.\x01",
            "I love Toda Gossip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Well, I guess it's okay … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_100B5")

    label("loc_10054")


    ChrTalk(
        0xF,
        (
            "#02105F… … Hey ~ That's right!\x02\x03",
            "#02109FNo, that kind of story\x01",
            "It is my great favorite ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100B5")

    TalkEnd(0xFE)
    Return()

    # Function_37_FBC0 end

    def Function_38_100B9(): pass

    label("Function_38_100B9")


    ChrTalk(
        0xF,
        (
            "#02104FWith such an amazing flying boat,\x01",
            "On such a wonderful face\x01",
            "I can interview … ….\x02\x03",
            "#02109FOh, the spirit of journalists\x01",
            "I will be tickled!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FMr. G. Grace ……\x01",
            "You do not do it on articles, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02102FOh dear, do not worry.\x01",
            "Because it is a curiosity to the last.\x02\x03",
            "#02104FWhen I am following the resistance\x01",
            "I have to gather up the neta that I grabbed,\x01",
            "I will not post it so be relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHaha …\x02\x03",
            "#00005F…… That's right, Mr. Grace\x01",
            "History of Resistance#4RProminence#What …?\x02\x03",
            "#00003FSurely, something wrong with Crossbell City\x01",
            "I was saying that I woke you up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02106FWell, well.\x01",
            "The story will be a little longer ….\x02\x03",
            "#02101FActually, from the day of that independence declaration\x01",
            "Government censorship on my article\x01",
            "I got to get in.\x02\x03",
            "Like criticizing the president\x01",
            "An interview article of the opposition something\x01",
            "I definitely can not write it … …\x02\x03",
            "#02106FIn the case of using communication equipment\x01",
            "Until the covering act itself\x01",
            "I regulated it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FIt is thorough …\x02\x03",
            "#00003F… No, if President Dieter\x01",
            "It might be possible to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02103FWell, that's what I want\x01",
            "It is far from journalism,\x01",
            "As expected it is not convincing.\x02\x03",
            "#02102FIf you keep on interviewing ignoring the notice,\x01",
            "Finally I've been watching the Defense Forces.\x02\x03",
            "#02104FIt's getting hotter in Crossbell City at last,\x01",
            "I thought that I got past the resistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIs that so……\x01",
            "It was well safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02109FThat's what Rains is making better of\x01",
            "Please arrange escape route ~.\x01",
            "I am happy to have a good junior.\x02\x03",
            "#02100F…… Anyway, because of this\x01",
            "In me as well,\x01",
            "I will cooperate with the release of Crossbell City!\x02\x03",
            "#02109F\"Pen is stronger than the sword\"\x01",
            "Because we can not lose to Defense Army and Hunter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa … … that you can cooperate\x01",
            "There may be,\x01",
            "At that time I would appreciate your favor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 7)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x10)
    Return()

    # Function_38_100B9 end

    def Function_39_10764(): pass

    label("Function_39_10764")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_10946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10782")
    Call(1, 41)
    Jump("loc_10941")

    label("loc_10782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1088B")

    ChrTalk(
        0x12,
        (
            "#02503FNo more, I am your\x01",
            "It will not be useful but …\x02\x03",
            "#02500FAt the very least, as a person who issued invalid declaration\x01",
            "The impact on the future of Crossbell,\x01",
            "Let's say that we are thinking about that countermeasure.\x02\x03",
            "As the head of the autonomous state legislature … …\x01",
            "More than anything, I live in Crossbell\x01",
            "As a resident of one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_10941")

    label("loc_1088B")


    ChrTalk(
        0x12,
        (
            "#02503FAs a person who issued invalid declaration\x01",
            "The impact on the future of Crossbell,\x01",
            "Let's say that we are thinking about that countermeasure.\x02\x03",
            "#02500FAs the head of the autonomous state legislature … …\x01",
            "More than anything, I live in Crossbell\x01",
            "As a resident of one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10941")

    Jump("loc_10B7B")

    label("loc_10946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_10B7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10961")
    Call(1, 40)
    Jump("loc_10B7B")

    label("loc_10961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AD0")

    ChrTalk(
        0x12,
        (
            "#02500FMyself, anytime\x01",
            "\"Invalid Declaration of Independent State\"\x01",
            "I am ready to go out.\x02\x03",
            "#02503FLater on to the residents of Crossbell\x01",
            "How will this declaration arrive …\x01",
            "It will depend on that.\x02\x03",
            "#02500FAs much as Dieter\x01",
            "I can not do performance,\x01",
            "I will show it to my hard work.\x02\x03",
            "To each person living in the crossbell\x01",
            "In order to have the future of this place considered,\x01",
            "You must definitely do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_10B7B")

    label("loc_10AD0")


    ChrTalk(
        0x12,
        (
            "#02503F\"Invalid Declaration of Independent State\" … …\x01",
            "I will show it to my hard work.\x02\x03",
            "#02500FTo each person living in the crossbell\x01",
            "In order to have the future of this place considered,\x01",
            "You must definitely do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B7B")

    TalkEnd(0xFE)
    Return()

    # Function_39_10764 end

    def Function_40_10B7F(): pass

    label("Function_40_10B7F")


    ChrTalk(
        0x101,
        (
            "#00000FMcDowell … …\x01",
            "How is preparation of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02500FWell, anytime\x01",
            "\"Invalid Declaration of Independent State\"\x01",
            "I am ready to go out.\x02\x03",
            "The content of the declaration is also satisfactory\x01",
            "I intended to make things.\x02\x03",
            "#02503FOf course, the words of Dieter yourself\x01",
            "It reflects on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F……Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503FNo … not to thank you.\x02\x03",
            "#02501FLater on to the residents of Crossbell\x01",
            "How will this declaration arrive …\x01",
            "It should be hanging on it.\x02\x03",
            "For me, as much as Dieter\x01",
            "I can not do performance,\x01",
            "Let me tell you a word and phrase hard.\x02\x03",
            "#02503FTo each person living in the crossbell\x01",
            "In order to have the future of this place considered,\x01",
            "You must definitely do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah … well, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 1)
    Return()

    # Function_40_10B7F end

    def Function_41_10DFC(): pass

    label("Function_41_10DFC")


    ChrTalk(
        0x12,
        "#02503F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FMcDaill chair … ….?\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x101, 0)
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10EE8")
    Jump("loc_10F32")

    label("loc_10EE8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10F08")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10F32")

    label("loc_10F08")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10F28")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10F32")

    label("loc_10F28")

    OP_52(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10F32")

    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    ChrTalk(
        0x12,
        (
            "#02505F…… Oh, sorry.\x01",
            "Have a little thought.\x02\x03",
            "#02503FInvalid declaration of Crossbell independent country … ….\x01",
            "Although it is to break the present situation,\x01",
            "Was it really this right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503F…… Perhaps this problem\x01",
            "There is no such thing as a correct answer.\x02\x03",
            "#02500FBut it is something to ask for the correct answer\x01",
            "I think it is important.\x02\x03",
            "As the head of the autonomous state legislature … …\x01",
            "More than anything, I live in Crossbell\x01",
            "As a resident of one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……Thank you.\x02\x03",
            "#00000FOnce you get into the case,\x01",
            "Surely we also chair the\x01",
            "I will help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02509FHuh, I appreciate it.\x01",
            "I would like to ask for your help at that time.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x1DA, 2)
    Return()

    # Function_41_10DFC end

    def Function_42_111B4(): pass

    label("Function_42_111B4")

    Call(1, 43)
    Return()

    # Function_42_111B4 end

    def Function_43_111B8(): pass

    label("Function_43_111B8")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_111C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121FC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "Buy accessories\x01",      # 1
            "Buy expendable items\x01",      # 2
            "quit\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11230")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_11230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1124F")
    OP_AF(0xD8)
    Jump("loc_112A1")

    label("loc_1124F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1125F")
    OP_AF(0xD7)
    Jump("loc_112A1")

    label("loc_1125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1126F")
    OP_AF(0xD6)
    Jump("loc_112A1")

    label("loc_1126F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1127F")
    OP_AF(0xD5)
    Jump("loc_112A1")

    label("loc_1127F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1128F")
    OP_AF(0xD4)
    Jump("loc_112A1")

    label("loc_1128F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1129F")
    OP_AF(0xD3)
    Jump("loc_112A1")

    label("loc_1129F")

    OP_AF(0xD2)

    label("loc_112A1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_121F7")

    label("loc_112B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112D0")
    OP_AF(0xDC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_121F7")

    label("loc_112D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112E4")
    Jump("loc_121F7")

    label("loc_112E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121F7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_11491")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1141A")

    ChrTalk(
        0x15,
        (
            "To the battle over the cause of Crossbell\x01",
            "It is time for the settlement to finally arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "At first, the church members did not gather\x01",
            "I thought what would happen … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I managed to get here so far.\x01",
            "You guys are absolutely fine if you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Now, towards the end\x01",
            "Get ready for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_1148C")

    label("loc_1141A")


    ChrTalk(
        0x15,
        (
            "I have reached this point.\x01",
            "You guys are absolutely fine if you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Now, towards the end\x01",
            "Get ready for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1148C")

    Jump("loc_121F7")

    label("loc_11491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_115E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11565")

    ChrTalk(
        0x15,
        (
            "The way of \"Taiki\" is quite a deep place\x01",
            "It seems to be continuing …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "When it comes to danger,\x01",
            "Sometimes it is important to return to supply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The resolution of the incident depends on you.\x01",
            "Try to move as carefully as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_115E1")

    label("loc_11565")


    ChrTalk(
        0x15,
        (
            "When it comes to danger,\x01",
            "Sometimes it is important to return to supply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The resolution of the incident depends on you.\x01",
            "Try to move as carefully as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115E1")

    Jump("loc_121F7")

    label("loc_115E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_117C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11714")

    ChrTalk(
        0x15,
        (
            "Before heading for \"Taiki\"\x01",
            "I'd like to have prepared everything,\x01",
            "There is a limit to what can be aligned here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Go down to various places of the crossbell once\x01",
            "Visiting various facilities and having close friends\x01",
            "Maybe he is an ant to say hello.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I do not know what will happen … …\x01",
            "I have to regulate it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_117C3")

    label("loc_11714")


    ChrTalk(
        0x15,
        (
            "Go down to various places of the crossbell once\x01",
            "Visiting various facilities and having close friends\x01",
            "Maybe he is an ant to say hello.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I do not know what will happen … …\x01",
            "I have to regulate it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117C3")

    Jump("loc_121F7")

    label("loc_117C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_11944")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118B6")

    ChrTalk(
        0x15,
        (
            "Jorg Rosenberg ……\x01",
            "Human beings of \"association\" to us\x01",
            "It is not said that it will provide useful information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "As a star cup knight\x01",
            "I doubt if I can believe it easily,\x01",
            "There seems to be no lie in information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "There must be various people in the association\x01",
            "I wonder why … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_1193F")

    label("loc_118B6")


    ChrTalk(
        0x15,
        (
            "Jorg Rosenberg ……\x01",
            "I doubt if I can believe it easily,\x01",
            "There seems to be no lie in information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "There must be various people in the association\x01",
            "I wonder why … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1193F")

    Jump("loc_121F7")

    label("loc_11944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_11AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A2A")

    ChrTalk(
        0x15,
        (
            "By McDowell\x01",
            "If an independent country is declared invalid,\x01",
            "Impact will appear in various parts of the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The resistance latent in each place is also\x01",
            "I think it will be quite easy to move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "… … I feel like Yamaba is approaching.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_11AB0")

    label("loc_11A2A")


    ChrTalk(
        0x15,
        (
            "By McDowell\x01",
            "If an independent country is declared invalid,\x01",
            "Impact will appear in various parts of the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "… … I feel like Yamaba is approaching.\x02",
    )

    CloseMessageWindow()

    label("loc_11AB0")

    Jump("loc_121F7")

    label("loc_11AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_11C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BAF")

    ChrTalk(
        0x15,
        (
            "McDaely's rescue operation … …\x01",
            "Even though I am not singing\x01",
            "I was pretty nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "A partner is a piece of \"Red constellation\" squad … …\x01",
            "There is a tough fight as compared to the past\x01",
            "You should be waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You guys, please\x01",
            "Please come back safely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_11C36")

    label("loc_11BAF")


    ChrTalk(
        0x15,
        (
            "A partner is a piece of \"Red constellation\" squad … …\x01",
            "There is a tough fight as compared to the past\x01",
            "You should be waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You guys, please\x01",
            "Please come back safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C36")

    Jump("loc_121F7")

    label("loc_11C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_11D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D14")

    ChrTalk(
        0x15,
        (
            "Mercapa inside too\x01",
            "It has become lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Usually around the officials of the Knights,\x01",
            "The seclusion of human beings themselves\x01",
            "It is unusual ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "This story only, like this\x01",
            "It is surprisingly bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_11D91")

    label("loc_11D14")


    ChrTalk(
        0x15,
        (
            "Inside Mercapa\x01",
            "The seclusion of human beings themselves\x01",
            "It is unusual ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "This story only, like this\x01",
            "It is surprisingly bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D91")

    Jump("loc_121F7")

    label("loc_11D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_11EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E98")

    ChrTalk(
        0x15,
        (
            "Legendary assault \"silver\" … …\x01",
            "I have heard the rumor anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "But that\x01",
            "That you were such a girl … …\x01",
            "It is something the world does not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "… Well, for you guys\x01",
            "Lord Hemisphere is a clergy,\x01",
            "I think it was quite a shock.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_11EF7")

    label("loc_11E98")


    ChrTalk(
        0x15,
        (
            "Legendary assault \"silver\" … …\x01",
            "That is such a girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "It is something I do not know about the world.\x02",
    )

    CloseMessageWindow()

    label("loc_11EF7")

    Jump("loc_121F7")

    label("loc_11EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_12069")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FAE")

    ChrTalk(
        0x15,
        (
            "Were you able to join with a group ……\x01",
            "Apparently it seems to be a good start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "However, to keep prepared\x01",
            "I have never done it before.\x01",
            "Please be careful in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_12064")

    label("loc_11FAE")


    ChrTalk(
        0x15,
        (
            "Thanks to Sir Hemisphere's law\x01",
            "For a while without contacting the Defense Forces\x01",
            "You should be able to enter and leave the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Just because I start out\x01",
            "I'm prohibited from carelessness.\x01",
            "Please be careful in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12064")

    Jump("loc_121F7")

    label("loc_12069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_121F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12084")
    Call(1, 44)
    Jump("loc_121F7")

    label("loc_12084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1217A")

    ChrTalk(
        0x15,
        (
            "In any case, equipments and fixtures\x01",
            "Since we have procured a lot,\x01",
            "Please call out when you need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "…… Fuu, even so\x01",
            "To Sir Hemisphere\x01",
            "It has been swayed from long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "While we were away,\x01",
            "Abbas is really well\x01",
            "I think I followed it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_121F7")

    label("loc_1217A")


    ChrTalk(
        0x15,
        (
            "To Sir Hemisphere\x01",
            "It has been swayed from long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "While we were away,\x01",
            "Abbas is really well\x01",
            "I think I followed it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121F7")

    Jump("loc_111C5")

    label("loc_121FC")

    TalkEnd(0x15)
    Return()

    # Function_43_111B8 end

    def Function_44_12200(): pass

    label("Function_44_12200")


    ChrTalk(
        0x15,
        (
            "I am the Vendus of the knight.\x01",
            "Management of ship facilities\x01",
            "It is left over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Before operating the equipment and furniture\x01",
            "Since we have procured a lot,\x01",
            "Please call out when you need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FDo not judge … …\x01",
            "Even though manpower is not enough,\x01",
            "It looks quite tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Well, this time Lord Hemisphere\x01",
            "Actually resumed suddenly … Hey …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The number of personnel on the ship is also minimal\x01",
            "I could not get it right.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x15, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_123DA")
    Jump("loc_12424")

    label("loc_123DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_123FA")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12424")

    label("loc_123FA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1241A")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12424")

    label("loc_1241A")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12424")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(
        0xA,
        (
            "#10404FHuh, anything\x01",
            "It was an urgent situation.\x02\x03",
            "#10409FVentos is the first time in 2 years,\x01",
            "I will ask you again for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "…… Well, anyway I have to work hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Hmm, everything\x01",
            "It seems to have made me struggle … …)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x1DA, 3)
    Return()

    # Function_44_12200 end

    def Function_45_12537(): pass

    label("Function_45_12537")

    Call(1, 46)
    Return()

    # Function_45_12537 end

    def Function_46_1253B(): pass

    label("Function_46_1253B")

    TalkBegin(0x16)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12548")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1345D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",            # 0
            "To remodel and synthesize\x01",      # 1
            "quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125A8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_125A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125C8")
    OP_AF(0xDD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13458")

    label("loc_125C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125DC")
    Jump("loc_13458")

    label("loc_125DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13458")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_12768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126D6")

    ChrTalk(
        0x16,
        (
            "If you come this far, no longer you\x01",
            "There is nothing to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "The standing enemies are mighty,\x01",
            "The goddess of the sky will surely bring you guys\x01",
            "I will lead you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please be careful.\x01",
            "It seems there is Goddess' s protection …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12763")

    label("loc_126D6")


    ChrTalk(
        0x16,
        (
            "The standing enemies are mighty,\x01",
            "The goddess of the sky will surely bring you guys\x01",
            "I will lead you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please be careful.\x01",
            "It seems there is Goddess' s protection …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12763")

    Jump("loc_13458")

    label("loc_12768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_1292C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1287B")

    ChrTalk(
        0x16,
        (
            "\"Treasure of Zero\" ……\x01",
            "To create such a space,\x01",
            "It is exactly the work of the goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "…… I accompanied up to here,\x01",
            "The fate of this ship is to you\x01",
            "預けさせてI will get you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I can not do a big deal,\x01",
            "If it is necessary to prepare the auction\x01",
            "Please call out at any time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12927")

    label("loc_1287B")


    ChrTalk(
        0x16,
        (
            "I accompanied it up to here,\x01",
            "The fate of this ship is to you\x01",
            "預けさせてI will get you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I can not do a big deal,\x01",
            "If it is necessary to prepare the auction\x01",
            "Please call out at any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12927")

    Jump("loc_13458")

    label("loc_1292C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12A16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D4")

    ChrTalk(
        0x16,
        (
            "…… The tension inside the ship is\x01",
            "From the time of the Cross Bell City release strategy\x01",
            "I feel it has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "The last phase that I finally visited … …\x01",
            "I just pray for the protection of the goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12A11")

    label("loc_129D4")


    ChrTalk(
        0x16,
        (
            "The last phase that I finally visited … …\x01",
            "I just pray for the protection of the goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A11")

    Jump("loc_13458")

    label("loc_12A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_12BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B25")

    ChrTalk(
        0x16,
        (
            "Currently, receiving invalid declaration\x01",
            "Both of the crane outside the crossbell\x01",
            "I am in contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Towards the Crossbell City liberation,\x01",
            "Lord Graham also\x01",
            "It seems that preparation is proceeding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "To get their help,\x01",
            "The white \"god machine\" and \"barrier\" are\x01",
            "It is a place you want to manage.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12BC7")

    label("loc_12B25")


    ChrTalk(
        0x16,
        (
            "Towards the Crossbell City liberation,\x01",
            "Lord Graham also\x01",
            "It seems that preparation is proceeding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "To get their help,\x01",
            "The white \"god machine\" and \"barrier\" are\x01",
            "It is a place you want to manage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BC7")

    Jump("loc_13458")

    label("loc_12BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_12D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CC4")

    ChrTalk(
        0x16,
        (
            "During hacking,\x01",
            "From myself there too\x01",
            "I will help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Because the power net is not specialty\x01",
            "Only on the system side of Mercapa\x01",
            "I can not be a force … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Even for the mission as an Order,\x01",
            "全力を尽くさせてI will get you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12D5D")

    label("loc_12CC4")


    ChrTalk(
        0x16,
        (
            "自分はBecause the power net is not specialty\x01",
            "Only on the system side of Mercapa\x01",
            "I can not be a force … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Even for the mission as an Order,\x01",
            "全力を尽くさせてI will get you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D5D")

    Jump("loc_13458")

    label("loc_12D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_12EAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E1A")

    ChrTalk(
        0x16,
        (
            "Military troops in the Defense Forces\x01",
            "It does not seem to be ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Just hunting soldiers is dangerous\x01",
            "There is no change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Prepare for the auction\x01",
            "Please make every effort.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12EA7")

    label("loc_12E1A")


    ChrTalk(
        0x16,
        (
            "Military troops in the Defense Forces\x01",
            "It seems there is not, but even just a hunter\x01",
            "It does not change to danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Prepare for the auction\x01",
            "Please make every effort.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EA7")

    Jump("loc_13458")

    label("loc_12EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1307D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FC8")

    ChrTalk(
        0x16,
        (
            "Randy's have\x01",
            "A rifle named \"Berserger\" …\x01",
            "It seems to have considerable fire power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "It is one of the strongest hunting corps on the continent\x01",
            "I'm surprised to be around the \"red constellation\"\x01",
            "It should be quite severe, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Looking at that weapon, something\x01",
            "I was convinced.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_13078")

    label("loc_12FC8")


    ChrTalk(
        0x16,
        (
            "Randy's have\x01",
            "A rifle named \"Berserger\" …\x01",
            "It seems to have considerable fire power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "\"Red constellation\"\x01",
            "It was also said that he was around the other party\x01",
            "I was convinced.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13078")

    Jump("loc_13458")

    label("loc_1307D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_13244")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131AA")

    ChrTalk(
        0x16,
        (
            "Against the large organization called Defense Army\x01",
            "To conduct resistance activities is,\x01",
            "A considerable belief will be needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I will not be able to supply satisfactory,\x01",
            "Everywhere's a friend\x01",
            "It is an act of betraying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Who is the leader?\x01",
            "I do not know, but I have a temper\x01",
            "It is certainly a strong core person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_1323F")

    label("loc_131AA")


    ChrTalk(
        0x16,
        (
            "To conduct resistance activities is,\x01",
            "A considerable belief is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Who is the leader?\x01",
            "I do not know, but I have a temper\x01",
            "It is certainly a strong core person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1323F")

    Jump("loc_13458")

    label("loc_13244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_133CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1336A")

    ChrTalk(
        0x16,
        (
            "In the engine room there\x01",
            "No matter what happens, do not enter\x01",
            "Please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I can not show it to secular people\x01",
            "Because there are important things.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_END)), "loc_1333B")

    ChrTalk(
        0x101,
        (
            "#00005F(Abbas talked about a while ago)\x01",
            "It is called \"heavenly car\"\x01",
            "Artifact … Is it kana? )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13362")

    label("loc_1333B")


    ChrTalk(
        0x101,
        "#00005F(What is there … …?\x02",
    )

    CloseMessageWindow()

    label("loc_13362")

    SetScenarioFlags(0x2, 2)
    Jump("loc_133CA")

    label("loc_1336A")


    ChrTalk(
        0x16,
        (
            "It is about time in the engine room\x01",
            "Maintenance\x01",
            "I have to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "…… Please do not peek?\x02",
    )

    CloseMessageWindow()

    label("loc_133CA")

    Jump("loc_13458")

    label("loc_133CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_13458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133EA")
    Call(1, 47)
    Jump("loc_13458")

    label("loc_133EA")


    ChrTalk(
        0x16,
        (
            "…… As the association is on business,\x01",
            "The Knights also made this case\x01",
            "It can not be overlooked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Let's work hard.\x02",
    )

    CloseMessageWindow()

    label("loc_13458")

    Jump("loc_12548")

    label("loc_1345D")

    TalkEnd(0x16)
    Return()

    # Function_46_1253B end

    def Function_47_13461(): pass

    label("Function_47_13461")


    ChrTalk(
        0x16,
        (
            "If you crossbell police\x01",
            "You are the person in charge of support department?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I am a member of this organization department\x01",
            "I am responsible for management\x01",
            "My name is Juneau.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Synthesis of quartz and\x01",
            "Modification of tactical auction\x01",
            "Please leave it to yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOkay … … The ordinary knights are\x01",
            "Is it possible to do such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Hehe, I am special,\x01",
            "In the hands of dexterity\x01",
            "I have confidence.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x16,
        (
            "…… As the association is on business,\x01",
            "The Knights also made this case\x01",
            "It can not be overlooked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Let's work hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah … well, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 4)
    Return()

    # Function_47_13461 end

    def Function_48_13657(): pass

    label("Function_48_13657")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KA nursing room\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",      # 0
            "quit\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137A6")
    EventBegin(0x2)
    Fade(500)
    OP_68(2040, 1000, -91940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 90)
    OP_0D()
    Sound(100, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0xA, 0x1, 0x8)
    Sleep(500)

    def lambda_13711():
        OP_95(0xFE, 4300, 0, -92030, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13711)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFF, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    OP_70(0x3, 0x0)
    OP_68(1300, 1000, -92030, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 270)
    SetChrSubChip(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x3)

    label("loc_137A6")

    TalkEnd(0xFF)
    Return()

    # Function_48_13657 end

    def Function_49_137AA(): pass

    label("Function_49_137AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137C0")
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)

    label("loc_137C0")

    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_137D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D01")
    RunExpression(0x5, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_13812"),
        (1, "loc_13841"),
        (2, "loc_13CE5"),
        (3, "loc_13CED"),
        (SWITCH_DEFAULT, "loc_13CFC"),
    )


    label("loc_13812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_13831")
    OP_2B(0x9A, 0x9B, 0x9C, 0x96, 0x97, 0x98, 0x99, 0xFFFF)
    Jump("loc_1383C")

    label("loc_13831")

    OP_2B(0x96, 0x97, 0x98, 0x99, 0xFFFF)

    label("loc_1383C")

    Jump("loc_13CFC")

    label("loc_13841")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1391A")
    SetChrName("Automatic announcement")

    AnonymousTalk(
        0xFF,
        "This is Crosbell Police.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_138F3")

    AnonymousTalk(
        0xFF,
        "We will receive reports.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Automatic announcement")

    AnonymousTalk(
        0xFF,
        (
            "Finish report processing.\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13915")

    label("loc_138F3")


    AnonymousTalk(
        0xFF,
        "There are no reportable requests.\x02",
    )

    CloseMessageWindow()

    label("loc_13915")

    Jump("loc_13CD7")

    label("loc_1391A")

    SetChrName("Receptionist franc")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1396E")
    Sound(3062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Yes, here is the crossbell police ~!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1399A")

    label("loc_1396E")

    Sound(3061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Everyone, thank you very much.\x02",
    )

    CloseMessageWindow()

    label("loc_1399A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_13BE3")
    Sound(3067, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        "Well then we will receive a report ~.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B6E")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_13A0B"),
        (13, "loc_13A55"),
        (12, "loc_13A9D"),
        (SWITCH_DEFAULT, "loc_13AE7"),
    )


    label("loc_13A0B")

    Sound(3075, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Class 1st--\x01",
            "Mr. Lloyd is too amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AE7")

    label("loc_13A55")

    Sound(3074, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Class 2nd -\x01",
            "Mr. Lloyd is amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AE7")

    label("loc_13A9D")

    Sound(3073, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Class 3rd\x01",
            "Mr. Lloyd, you did it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AE7")

    label("loc_13AE7")

    Sound(3076, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Items of award also soon\x01",
            "I will deliver to you ~!\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Congratulations ~!\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BDB")

    label("loc_13B6E")

    Sound(3078, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        "The report is over.\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Then, once you have reached the request\x01",
            "nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BDB")

    SetScenarioFlags(0x2, 4)
    Jump("loc_13CD7")

    label("loc_13BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_13C68")
    Sound(3063, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "There …\x01",
            "It was just reported earlier?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Also, I hope you will be able to fulfill your request.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13CD7")

    label("loc_13C68")

    Sound(3065, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "There, reportable\x01",
            "It seems there is no request for it ~.\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Thank you again.\x02",
    )

    CloseMessageWindow()

    label("loc_13CD7")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_13CFC")

    label("loc_13CE5")

    Call(1, 50)
    Jump("loc_13CFC")

    label("loc_13CED")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13CFC")

    label("loc_13CFC")

    Jump("loc_137D9")

    label("loc_13D01")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D3E")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(1, 51)
    Return()

    label("loc_13D3E")

    FadeToBright(1000, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_49_137AA end

    def Function_50_13D4E(): pass

    label("Function_50_13D4E")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_13D70")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D70")
    ClearScenarioFlags(0x2A, 0)

    label("loc_13D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_13D8D")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D8D")
    ClearScenarioFlags(0x2A, 1)

    label("loc_13D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_13DAA")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DAA")
    ClearScenarioFlags(0x2A, 2)

    label("loc_13DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_13DC7")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DC7")
    ClearScenarioFlags(0x2A, 3)

    label("loc_13DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_13DE4")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DE4")
    ClearScenarioFlags(0x2A, 4)

    label("loc_13DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_13E01")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E01")
    ClearScenarioFlags(0x2A, 5)

    label("loc_13E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_13E0D")
    SetScenarioFlags(0x2A, 6)

    label("loc_13E0D")

    OP_24(0x1F2)
    RunExpression(0x9, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E52")
    Sound(498, 1, 50, 0)
    Jump("loc_13E58")

    label("loc_13E52")

    Sound(498, 1, 100, 0)

    label("loc_13E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E88")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E88")

    Return()

    # Function_50_13D4E end

    def Function_51_13E89(): pass

    label("Function_51_13E89")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0xB, 0x12)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_13EF2")
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 102700, 0, -102930, 180)

    label("loc_13EF2")

    OP_68(102970, 1000, -104740, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14560, 0)
    SetChrPos(0x101, 103020, 100, -105800, 90)
    SetChrPos(0xB, 101590, 0, -105440, 90)
    SetChrPos(0xC, 101470, 0, -104110, 135)
    SetChrPos(0x8, 103000, 0, -104100, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#00205FGee\x02\x03",
            "#00204FApparently Lloyd said,\x01",
            "\"Pomutto! 'From everyone\x01",
            "You seem to have won.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01905FWell, really? ~! Is it?\x02\x03",
            "#01909FMr. Lloyd is …\x01",
            "It's too amazing ~! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_14070")

    ChrTalk(
        0x9,
        (
            "#02302FOh, yes.\x01",
            "You do pretty well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14070")

    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00009FThank you.\x01",
            "It may be just luck but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FNo, in this puzzle game\x01",
            "Only luck is a factor of victory.\x02\x03",
            "#12102FBannings, you are the one\x01",
            "True \"Pomutto! Master \".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FWell, thanks.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('贤者', 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14315")

    ChrTalk(
        0x8,
        (
            "#12100FHm … … That's right.\x02\x03",
            "You should accept this if you do not mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '贤者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('贤者', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#12100FThe church and the Epstein Foundation\x01",
            "We jointly developed based on ancient techniques,\x01",
            "It's a forbidden master quartz.\x02\x03",
            "It is too strong to handle,\x01",
            "Although it was not able to be operated … …\x02\x03",
            "#12102FYou can handle it correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I understand.\x01",
            "I will be of use to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143F9")

    label("loc_14315")


    ChrTalk(
        0x8,
        (
            "#12100FHm … … That's right.\x02\x03",
            "#12102FLet's do this to you as a reward.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '水耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('水耀珠', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000FThank you.\x01",
            "I will be of use to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_143F9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2A, 7)
    OP_E0(0x35, 0x0)
    OP_E0(0x80, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_D7(0x1E)
    EventEnd(0x5)
    SetScenarioFlags(0x24, 3)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_13E89 end

    def Function_52_1442B(): pass

    label("Function_52_1442B")

    EventBegin(0x0)
    Fade(500)
    OP_68(4130, -1100, 7060, 0)
    MoveCamera(47, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14590, 0)
    SetChrPos(0x101, 4000, -1500, 5730, 315)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14502")
    Jump("loc_1454C")

    label("loc_14502")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14522")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1454C")

    label("loc_14522")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14542")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1454C")

    label("loc_14542")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1454C")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#6P#01905FMr. Lloyd ……\x01",
            "I guess you feel tired somehow.\x02\x03",
            "Are you okay~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FOh …… I will be told.\x02\x03",
            "#00003FBecause there were various things,\x01",
            "Maybe I'm getting tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01906FUm, absolutely impossible\x01",
            "Please do not do it ~.\x02\x03",
            "#01908FIf Lloyds and older sisters\x01",
            "If I think I will collapse … …\x01",
            "Because I am so worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FOh, thank you.\x01",
            "Be careful enough … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01901FYou can not just be careful!\x01",
            "I have to take a good day off at such times!\x02\x03",
            "#01902FHow come I\x01",
            "Shall I massage you?\x02\x03",
            "#01909FIf you press the points that work tired gorgly,\x01",
            "You can be healthy with a single shot ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F(No, it sounds awfully painful … …)\x02\x03",
            "#00002FLet me see……\x01",
            "I appreciate your thoughts, but I'm fine.\x02\x03",
            "#00009FJust talking with Fran\x01",
            "I feel like I was able to refresh somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01905FEr … Is that so …?\x02\x03",
            "#01909FErr …\x01",
            "I am glad if you say so.\x02\x03",
            "#01904FAs an operator,\x01",
            "Giving you all\x01",
            "Because I think that it is my mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00009FIf it were\x01",
            "I think that it is really a vocation.\x02\x03",
            "#00004FActually, to your smile reflected on the terminal,\x01",
            "I do not know how many times I was healed ……\x02\x03",
            "#00000FTo the people entering and leaving the police headquarters,\x01",
            "I think that there are quite a few people for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01906FUu, when it is said that much\x01",
            "It's a bit embarrassing though ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#6P#01904FBut, that's right.\x01",
            "To Mr. Lloyd\x01",
            "I hope you do your best ~ …\x02\x03",
            "#01902FIf you do not mind,\x01",
            "Would you please accept it?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '芙兰的护符'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('芙兰的护符', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#11P#00005FThis … can I get it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_END)), "loc_14D34")

    ChrTalk(
        0xC,
        (
            "#6P#01909FYes, certainly\x01",
            "Please have it.\x02\x03",
            "#01904FAnyway, Lloyd's future\x01",
            "To my brother-in-law\x01",
            "It is a person who may become … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00011FEr … um …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01909FMufu …\x01",
            "If I'm your sister\x01",
            "Everything is understood ~.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00012F(Hello … … you have come.\x01",
            "Do you expect prospects …?)\x02\x03",
            "#00000FWell then, then\x01",
            "I will thank you for using it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DF1")

    label("loc_14D34")


    ChrTalk(
        0xC,
        (
            "#6P#01909FYes, certainly\x01",
            "Please have it.\x02\x03",
            "Pray for your safety\x01",
            "Because it is made,\x01",
            "Surely the effect is outstanding!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00009FWell then,\x01",
            "I will thank you for using it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DF1")


    ChrTalk(
        0xC,
        "#6P#01909FPlease, take care, eh ~.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D9, 4)
    SetScenarioFlags(0x1, 5)
    SetChrSubChip(0xC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E48")
    OP_E0(0x34, 0x0)

    label("loc_14E48")

    EventEnd(0x5)
    Return()

    # Function_52_1442B end

    def Function_53_14E4B(): pass

    label("Function_53_14E4B")

    EventBegin(0x0)
    Fade(500)
    OP_68(97920, 1000, 600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15320, 0)
    SetChrPos(0x101, 97510, 0, -530, 0)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14F22")
    Jump("loc_14F6C")

    label("loc_14F22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14F42")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14F6C")

    label("loc_14F42")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F62")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14F6C")

    label("loc_14F62")

    OP_52(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14F6C")

    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "#5P#00603FHM……\x02\x03",
            "#00600F…… Bannings, you too\x01",
            "It seems that a little grew.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005Feh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00603FYou guys are here\x01",
            "I had you accompany me … …\x02\x03",
            "I am certain that the investigative and reasoning skills are good,\x01",
            "The odor like the previous one\x01",
            "I can say that I've completely exited.\x02\x03",
            "During the active era of Guy and McRae\x01",
            "I have said that yet … …\x02\x03",
            "#00602FHe looked after the investigation one section\x01",
            "That is worth it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00012FLet me see……\x01",
            "Suddenly, what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5P#00603FPlease listen silently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FHa, hi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00600F…… Earlier Guy and McLean's\x01",
            "I talked, but the same type as them\x01",
            "I do not say that I can aim for an investigator.\x02\x03",
            "You have the potential of you.\x01",
            "By extending it\x01",
            "I will bring it closer to an excellent investigator.\x02\x03",
            "#00604FAiming for my own investigator,\x01",
            "You better keep going further.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x14,
        "#5P#00605F…… What, are you complaining something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00011FNo……\x01",
            "Somehow surprised.\x02\x03",
            "#00006FI do not think that it will evaluate to that extent\x01",
            "I do not think he is like Dudley ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00603F…… How will the defense forces become\x01",
            "Depending on future trends,\x01",
            "Still the police will survive.\x02\x03",
            "#00600FIf this series of events converged,\x01",
            "At least you return to the police\x01",
            "It is supposed to be.\x02\x03",
            "In preparation for that, as chief investigator of department 1\x01",
            "Advice from now\x01",
            "I thought I should give it.\x02\x03",
            "#00603FIt's just that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIs that so……\x02\x03",
            "#00004F……Thank you.\x02\x03",
            "#00002FIn order to meet Mr. Dudley's expectation,\x01",
            "I think that I will continue to advance in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00606FHun, do not get me wrong.\x02\x03",
            "Analyze you to the last so far\x01",
            "Until I said objective facts.\x02\x03",
            "#00600FAnything, I solved this incident\x01",
            "To not grab all the truth\x01",
            "You can not move on to the next one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012F(Ha ha, as usual\x01",
            "I do not care … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        "#5P#00601F…… What are you getting on?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#12P#00011FNo, no, nothing!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156EF")
    Jump("loc_157B7")

    label("loc_156EF")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Dudley\x01",
            "I mastered Hearts of Iron 嘦.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Combi Craft of Lloyd and Dudley,\x01",
            "\"Hearts of Iron\" has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x9, 0x1AA)
    AddCraft(0x0, 0x1AA)

    label("loc_157B7")

    OP_E0(0x24, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1D9, 1)
    SetScenarioFlags(0x1, 3)
    SetChrSubChip(0x14, 0x0)
    EventEnd(0x5)
    Return()

    # Function_53_14E4B end

    def Function_54_157CA(): pass

    label("Function_54_157CA")

    EventBegin(0x0)
    Fade(500)
    OP_68(96790, 1200, -101940, 0)
    MoveCamera(48, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x101, 96960, 0, -100830, 180)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x101, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_158A1")
    Jump("loc_158EB")

    label("loc_158A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_158C1")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_158EB")

    label("loc_158C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_158E1")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_158EB")

    label("loc_158E1")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_158EB")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained to Barisa about the barriers.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xD,
        (
            "#12P#10704F…… Apparently I need to go\x01",
            "There seems to be one.\x02\x03",
            "#10701F\"She\" and as a causal … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Hello, Lisa.\x02\x03",
            "#00001FIf possible we can\x01",
            "Leave it to us …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12P#10706F─ ─ ─ No.\x02\x03",
            "#10708FIn a sense, I and she,\x01",
            "There are similar circumstances.\x02\x03",
            "I myself am going to the road ahead\x01",
            "To find out … ….\x02\x03",
            "#10701FI, once again with her,\x01",
            "You see#2RMami#Do not make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F………I understood.\x02\x03",
            "#00001FLet's go when we are ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D8, 4)
    SetChrSubChip(0xD, 0x0)
    EventEnd(0x5)
    Return()

    # Function_54_157CA end

    def Function_55_15B0D(): pass

    label("Function_55_15B0D")

    EventBegin(0x0)
    Fade(500)
    OP_68(101090, 1000, -93870, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 100220, 0, -93940, 90)
    SetChrPos(0xA, 101370, 150, -94090, 270)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the barrier to Wazi.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10404FWell … well.\x02\x03",
            "#10408F…… Completely.\x01",
            "Why is it like me\x01",
            "Are you sticking to the heir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FWadi\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10401FApparently \"he\" is\x01",
            "It seems to have decided with me.\x02\x03",
            "#10403FLloyd, I search for members\x01",
            "Will you put it in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FOh, I understand.\x02\x03",
            "#00000FLet's go when we are ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D8, 0)
    SetChrPos(0xA, 101790, 150, -93960, 90)
    EventEnd(0x5)
    Return()

    # Function_55_15B0D end

    def Function_56_15CE5(): pass

    label("Function_56_15CE5")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3010, -500, 6090, 0)
    MoveCamera(46, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, -3520, -1500, 5560, 0)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15DBC")
    Jump("loc_15E06")

    label("loc_15DBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15DDC")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15E06")

    label("loc_15DDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15DFC")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15E06")

    label("loc_15DFC")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15E06")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_93(0x8, 0x104, 0x0)
    EndChrThread(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#00200FMr. Abbas from before\x01",
            "Tell me how to use the terminal\x01",
            "I'm sorry, but …\x02\x03",
            "#00203FApparently, the system of \"Mercapa\"\x01",
            "It seems to be made by the Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FEr … Is that so! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00200FYes, I do not think there is any mistake.\x02\x03",
            "#00203FOnce in the church, people in the foundation headquarters\x01",
            "I have seen something … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x8, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15FFD")
    Jump("loc_16047")

    label("loc_15FFD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1601D")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16047")

    label("loc_1601D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1603D")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16047")

    label("loc_1603D")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16047")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#00200FPerhaps, the Foundation and the Church\x01",
            "Have you been in a cooperative relationship for some time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F…… It is informal.\x02\x03",
            "This Mercapa, originally\x01",
            "Have the flight function \"heavenly car\"\x01",
            "It was a ride of artifacts … …\x02\x03",
            "After the power revolution, in cooperation with the foundation,\x01",
            "I used \"heavenly car\" for the engine section\x01",
            "It was renovated to its present form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F\"Heavenly car\" … …\x01",
            "When Zeit looked at Mercapa\x01",
            "It's a muttering name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FIn other words, even the people of the church\x01",
            "Development of tactical orgement, etc.\x01",
            "Some are cooperating.\x02\x03",
            "You are using\x01",
            "Speaking of \"guiding magic\" also\x01",
            "It applied the technique of \"Law art\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00203FI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F…… I think that I know,\x01",
            "It is an informal matter to the last.\x01",
            "Do not let it leak out to the outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, of course I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00200FI understood that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 4)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    OP_93(0x8, 0x13B, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    EventEnd(0x5)
    Return()

    # Function_56_15CE5 end

    SaveToFile()

Try(main)
