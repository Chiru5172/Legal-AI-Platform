"""
law_data.py
-----------
Comprehensive Legal Knowledge Base for the Legal AI Platform.

Contains structured information (title, detailed description, and statutory
punishment/remedy) for a wide set of laws and sections commonly used in India:
- Constitution (Fundamental Rights)
- Indian Penal Code (IPC)
- Criminal Procedure Code (CrPC)
- Information Technology Act (IT Act)
- Indian Evidence Act / Evidence-related provisions
- Contract Act & Civil Provisions

Note: Descriptions are explanatory summaries intended for educational and
demo purposes. For verbatim statutory language and authoritative citation,
consult official sources such as https://www.indiacode.nic.in and court databases.
"""

LAW_SECTIONS = {

    # =====================================================
    # CONSTITUTION OF INDIA – FUNDAMENTAL RIGHTS & KEY ARTICLES
    # =====================================================
    "Constitution of India (Fundamental Rights & Key Articles)": {

        "Article 12": {
            "title": "Definition of State",
            "description": (
                "Defines 'State' for the purpose of Part III (Fundamental Rights). "
                "Includes the Government and Parliament of India, the Government and legislative "
                "bodies of each State, and other authorities within the territory of India. "
                "This article is critical for determining whether an action or omission can be "
                "challenged as a violation of fundamental rights; only acts attributable to the "
                "'State' fall under Part III remedies."
            ),
            "punishment": "Constitutional remedy — writ jurisdiction where applicable"
        },

        "Article 14": {
            "title": "Right to Equality",
            "description": (
                "Guarantees equal treatment under the law and equal protection of the laws "
                "to all persons within the territory of India. Prohibits arbitrary classification "
                "and mandates that any classification for legislation must be reasonable, "
                "intelligible and have a rational nexus to legislative objective. Courts apply "
                "a proportionality and reasonableness test when reviewing state action under this article."
            ),
            "punishment": "Remedy by writs (Article 32/226) — declaratory, injunctive or compensatory relief"
        },

        "Article 15": {
            "title": "Prohibition of Discrimination",
            "description": (
                "Prohibits discrimination by the State against citizens on grounds such as religion, "
                "race, caste, sex, place of birth or any of them. Allows for reasonable classification "
                "and affirmative action under specified clauses (e.g., reservation of seats). "
                "Laws impinging these protections are subject to strict judicial scrutiny if they lack "
                "a clear public purpose or are manifestly arbitrary."
            ),
            "punishment": "Constitutional remedy — judicial relief including declarations and injunctions"
        },

        "Article 19": {
            "title": "Freedom of Speech and Expression and Other Freedoms",
            "description": (
                "Enumerates six freedoms available to citizens: (a) speech and expression; "
                "(b) assembly without arms; (c) forming associations or unions; (d) movement; "
                "(e) residence; and (f) profession. These freedoms are subject to 'reasonable restrictions' "
                "in the interest of sovereignty, public order, morality, security of the State, defamation, "
                "contempt of court, etc. Balancing tests are used to adjudicate conflicts between "
                "individual rights and permissible restrictions."
            ),
            "punishment": "Enforceable by courts — may lead to striking down statutes or restraining state action"
        },

        "Article 20": {
            "title": "Protection in Respect of Conviction for Offences",
            "description": (
                "Provides criminal law protections: (1) no retrospective criminalization (ex post facto); "
                "(2) protection against double jeopardy; and (3) protection against compelled self-incrimination. "
                "These safeguards are engaged in criminal prosecutions and ensure fairness in penal processes."
            ),
            "punishment": "Relief via criminal remedies and constitutional writs where applicable"
        },

        "Article 21": {
            "title": "Protection of Life and Personal Liberty",
            "description": (
                "Guarantees that no person shall be deprived of life or personal liberty except according "
                "to procedure established by law. Judicial interpretation has expanded Article 21 to include "
                "rights to privacy, livelihood, health, clean environment, legal aid, and fair trial. Courts "
                "apply a substantive due process standard to state action depriving life or liberty."
            ),
            "punishment": "Constitutional remedies including compensatory orders, directions for systemic reform"
        },

        "Article 22": {
            "title": "Protection against Arrest and Detention",
            "description": (
                "Specifies procedural safeguards for persons arrested or detained: prompt production before "
                "a magistrate, the right to be informed of grounds of arrest, the right to counsel, and "
                "limits on detention without trial. Certain protections differ for preventive detention regimes."
            ),
            "punishment": "Remedies through writs and criminal procedure review; compensation in some cases"
        },

        "Article 32": {
            "title": "Right to Constitutional Remedies",
            "description": (
                "Grants the right to move the Supreme Court directly for enforcement of fundamental rights "
                "by means of writs including habeas corpus, mandamus, prohibition, quo warranto, and certiorari. "
                "Article 32 is a fundamental feature of the Constitution and central to rights enforcement."
            ),
            "punishment": "Supreme Court may issue appropriate writs and make necessary orders including damages"
        }
    },

    # =====================================================
    # INDIAN PENAL CODE (IPC) – KEY CRIMINAL OFFENCES
    # =====================================================
    "Indian Penal Code (IPC) - Key Sections": {

        # Homicide & Related
        "IPC 299": {
            "title": "Culpable Homicide not amounting to Murder",
            "description": (
                "Defines culpable homicide which causes death with the intention of causing death "
                "or of causing such bodily injury as is likely to cause death, or with the knowledge "
                "that the act is likely to cause death. Distinguishes from murder based on the presence "
                "of additional elements such as premeditation, severity, and special circumstances."
            ),
            "punishment": "Varies — if culpable homicide not amounting to murder, imprisonment; exact term depends on section applied (e.g. IPC 304)"
        },

        "IPC 300": {
            "title": "Murder - Definition",
            "description": (
                "Defines murder; certain culpable homicides are classified as murder when the act is "
                "done with the intention of causing death, or cause bodily injury likely to cause death, "
                "or done with knowledge that it is so imminently dangerous that it must in all probability "
                "cause death. Exceptions are enumerated that reduce the offense to culpable homicide not amounting to murder."
            ),
            "punishment": "Death or life imprisonment and fine (if convicted under IPC 302)"
        },

        "IPC 302": {
            "title": "Punishment for Murder",
            "description": (
                "Prescribes punishment where an accused is convicted of murder: the law prescribes death "
                "or life imprisonment and liability to fine. Sentencing courts exercise discretion guided by "
                "principles such as 'rarest of rare' in capital punishment jurisprudence."
            ),
            "punishment": "Death or life imprisonment and fine"
        },

        "IPC 304": {
            "title": "Punishment for Culpable Homicide not amounting to Murder",
            "description": (
                "Section 304 deals with culpable homicide not amounting to murder; it distinguishes "
                "cases based on the degree of culpability (e.g., IPC 304 Part I and Part II in some jurisdictions) "
                "and prescribes imprisonment terms that may be less than murder."
            ),
            "punishment": "Imprisonment which may extend to 10 years, or life imprisonment, or fine, depending on facts"
        },

        # Offences causing hurt and grievous hurt
        "IPC 323": {
            "title": "Punishment for Voluntarily Causing Hurt",
            "description": (
                "Covers causing bodily pain, injury, disease or infirmity to another voluntarily."
            ),
            "punishment": "Imprisonment up to 1 year, or fine, or both"
        },

        "IPC 325": {
            "title": "Punishment for Voluntarily Causing Grievous Hurt",
            "description": (
                "Addresses cases where grievous hurt is caused, such as severe bodily injuries, loss of limb, permanent disfigurement, or other serious consequences."
            ),
            "punishment": "Imprisonment up to 7 years and fine"
        },

        # Sexual offences
        "IPC 375": {
            "title": "Rape - Definition (Historic)",
            "description": (
                "Sets out elements constituting rape; statutory definitions have evolved via amendment and judicial interpretation. Modern jurisprudence expands understanding of consent and coercion."
            ),
            "punishment": "See IPC 376 (punishment for rape)"
        },

        "IPC 376": {
            "title": "Punishment for Rape",
            "description": (
                "Prescribes punishment for rape offences. Amendments have increased minimum punishments and introduced aggravated categories for custodial rape, gang rape, sexual violence against minors and other vulnerable persons."
            ),
            "punishment": "Rigorous imprisonment for a term not less than 7–10 years and which may extend to life imprisonment, plus fine (statutory minimums vary)"
        },

        # Property and fraud
        "IPC 379": {
            "title": "Theft",
            "description": (
                "Defines theft as dishonest removal of movable property out of the possession of another without consent."
            ),
            "punishment": "Imprisonment up to 3 years, or fine, or both"
        },

        "IPC 404": {
            "title": "Dishonest Misappropriation of Property",
            "description": (
                "When a person dishonestly misappropriates property entrusted to them, they commit an offense; this covers cases where fiduciary duty or trust is violated leading to unlawful conversion."
            ),
            "punishment": "Imprisonment up to 3 years, or fine, or both"
        },

        "IPC 406": {
            "title": "Criminal Breach of Trust",
            "description": (
                "Covers breach of trust by a person entrusted with property or with dominion over property, where the person dishonestly misappropriates or converts it."
            ),
            "punishment": "Imprisonment up to 3 years, or fine, or both; higher punishments in aggravated cases"
        },

        "IPC 420": {
            "title": "Cheating and Dishonestly Inducing Delivery of Property",
            "description": (
                "A widely used provision in fraud cases; cheating requires deception with intent to cause delivery of property or to induce action that causes loss."
            ),
            "punishment": "Imprisonment up to 7 years and fine"
        },

        # Threats and intimidation
        "IPC 503": {
            "title": "Criminal Intimidation",
            "description": (
                "When an individual threatens another to cause alarm or prevent them from doing something they have a right to do, it falls under criminal intimidation. The section covers threats to person, reputation or property."
            ),
            "punishment": "Imprisonment up to two years, or fine, or both; aggravated offences may attract higher terms"
        },

        "IPC 506": {
            "title": "Punishment for Criminal Intimidation",
            "description": (
                "Provides the penal consequences for acts of criminal intimidation and addresses cases where such threats amount to an offence."
            ),
            "punishment": "Imprisonment up to two years, or fine, or both; where threat is to cause death or grievous hurt, term may be higher"
        },

        # Public order and offences against state
        "IPC 121": {
            "title": "Waging War against the Government of India",
            "description": (
                "One of the most serious public order offences; involves acts intended to wage war against the State or to resist lawful authority by force."
            ),
            "punishment": "Death or imprisonment for life"
        },

        "IPC 124A": {
            "title": "Sedition",
            "description": (
                "Provision historically used against speech and acts deemed to incite disaffection against the Government; judicial review has curtailed overbroad application and required incitement to violence for conviction."
            ),
            "punishment": "Imprisonment which may extend to three years, with fine; severity depends on additional circumstances"
        }
    },

    # =====================================================
    # CRIMINAL PROCEDURE CODE (CrPC) – PROCEDURAL SAFEGUARDS
    # =====================================================
    "Criminal Procedure Code (CrPC) - Key Sections": {

        "CrPC 2": {
            "title": "Definitions",
            "description": (
                "Contains definitions and interpretation clauses for key terms used throughout the Code: cognizable offence, non-cognizable offence, police officer, public servant, etc."
            ),
            "punishment": "N/A (interpretive provisions)"
        },

        "CrPC 41": {
            "title": "When Police May Arrest without Warrant",
            "description": (
                "Provides the authority and conditions under which a police officer may arrest a person without a warrant, including reasonable suspicion of committing a cognizable offence or breach of peace. Emphasizes necessity, legality and safeguards to prevent arbitrary detention."
            ),
            "punishment": "Procedural; misuse may attract departmental or judicial remedies"
        },

        "CrPC 50": {
            "title": "Information of Grounds of Arrest",
            "description": (
                "Entitles arrested persons to be informed of the grounds of arrest and the right to bail; fundamental to fair treatment and protection against arbitrary detention."
            ),
            "punishment": "Violation may lead to declaration of illegality of detention and compensation"
        },

        "CrPC 56-60": {
            "title": "Rights of Detained Persons and Procedure",
            "description": (
                "Covers duties to take persons before magistrates, limits on detention without judicial oversight, safeguards against forced confessions, and rights to legal counsel."
            ),
            "punishment": "Procedural safeguards; remedies include writs and inquiries"
        },

        "CrPC 154": {
            "title": "Information in Cognizable Cases (Registration of FIR)",
            "description": (
                "Mandates registration of First Information Report (FIR) by police upon receiving information about the commission of cognizable offences. The FIR initiates criminal investigation procedures and marks the beginning of the formal criminal process."
            ),
            "punishment": "Non-registration can be challenged judicially; may attract departmental action"
        },

        "CrPC 167": {
            "title": "Procedure When Investigation Cannot Be Completed in 24 Hours",
            "description": (
                "Authorizes police remand and judicial remand procedures when investigation requires detention beyond 24 hours, with requirements for magistrate oversight and reasons for continued custody."
            ),
            "punishment": "Procedural safeguards; unlawful remand may lead to remedies"
        },

        "CrPC 197": {
            "title": "Prosecution of Judges and Public Servants",
            "description": (
                "Requires prior sanction for prosecution of judges and certain public servants for acts done in good faith in discharge of official duty; designed to avoid frivolous suits against officials performing their functions."
            ),
            "punishment": "Sanction procedures; absence of sanction may invalidate prosecution"
        }
    },

    # =====================================================
    # INFORMATION TECHNOLOGY ACT, 2000 (CYBER LAWS)
    # =====================================================
    "Information Technology Act (IT Act) - Key Provisions": {

        "IT Act 43": {
            "title": "Penalty and Compensation for Damage to Computer, Computer System etc.",
            "description": (
                "Civil liability provisions providing for compensation to persons affected by cyber incidents including damage, loss or unauthorized access to computer systems. Enables aggrieved parties to claim compensation via civil proceedings."
            ),
            "punishment": "Compensation to affected persons; civil remedies"
        },

        "IT Act 65A / 65B": {
            "title": "Admissibility of Electronic Records",
            "description": (
                "Section 65B of the Evidence Act (as amended) and related IT Act provisions govern admissibility of electronic records in court, setting out conditions for reliable electronic evidence and certification processes for digital documents."
            ),
            "punishment": "Admissibility rules — evidentiary weight determined by courts"
        },

        "IT Act 66": {
            "title": "Computer-Related Offences (Hacking etc.)",
            "description": (
                "Penalizes hacking and unauthorized access or modification of computer material; includes acts such as bypassing security, altering data, or causing loss through cyber actions."
            ),
            "punishment": "Imprisonment up to 3 years and fine; may be higher for aggravated offences"
        },

        "IT Act 66C": {
            "title": "Identity Theft",
            "description": (
                "Punishes fraudulent or dishonest use of electronic signature, password or any other unique identification feature of a person, essentially capturing online identity theft and unauthorized use of credentials."
            ),
            "punishment": "Imprisonment up to 3 years and fine"
        },

        "IT Act 66D": {
            "title": "Cheating by Personation by using Computer Resource",
            "description": (
                "Addresses online cheating through impersonation using electronic means — for example, posing as another person to induce transfer of property or access to resources."
            ),
            "punishment": "Imprisonment up to 3 years and fine"
        },

        "IT Act 66E": {
            "title": "Violation of Privacy",
            "description": (
                "Specifically addresses the capturing, publishing or transmission of images of private areas of a person without consent, thereby invading privacy through electronic means."
            ),
            "punishment": "Imprisonment up to 3 years and fine"
        },

        "IT Act 67 / 67A": {
            "title": "Publishing Obscene Material in Electronic Form",
            "description": (
                "Criminalizes publishing or transmitting obscene material online and in electronic formats. Section 67A deals with sexually explicit acts and prescribes stricter penalties."
            ),
            "punishment": "Section 67: up to 3–5 years and fine; Section 67A: higher punishment including up to 5–7 years and fine"
        },

        "IT Act 66F": {
            "title": "Cyber Terrorism",
            "description": (
                "Defines cyber terrorism as acts which threaten the unity, integrity, security or sovereignty of the State, or cause death, bodily injury, or damage to property by cyber means. It covers serious cyber offences intended to cause widespread harm."
            ),
            "punishment": "Rigorous imprisonment which may extend to life and fine"
        }
    },

    # =====================================================
    # INDIAN EVIDENCE ACT & ELECTRONIC EVIDENCE
    # =====================================================
    "Indian Evidence Act (Selected Provisions)": {

        "Section 65B (Evidence Act)": {
            "title": "Admissibility of Electronic Records",
            "description": (
                "Defines the rules for admissibility of electronic records as evidence, requiring a certificate in certain cases to show that electronic information was produced by a reliable process. This section is central to admitting emails, logs, and other digital evidence in court."
            ),
            "punishment": "Evidentiary — affects admissibility and weight of proof in proceedings"
        },

        "Section 27 (Evidence Act)": {
            "title": "Discovery of Facts by Accused's Statement",
            "description": (
                "Deals with the admissibility of facts discovered as a result of information given by an accused person while in custody, and the conditions under which such facts are receivable as evidence."
            ),
            "punishment": "Evidentiary rules — may lead to corroboration or exclusion depending on voluntariness"
        }
    },

    # =====================================================
    # CONTRACT & CIVIL LAW (SELECTED PROVISIONS)
    # =====================================================
    "Civil & Contract Law (Selected Provisions)": {

        "Contract Act 10": {
            "title": "What Agreements are Contracts",
            "description": (
                "Sets out conditions under which agreements become enforceable contracts: offer, acceptance, lawful consideration, capacity to contract, and free consent. Void agreements and statutory exceptions are enumerated."
            ),
            "punishment": "Civil remedies: damages, specific performance or injunctions"
        },

        "Contract Act 73": {
            "title": "Consequences of Breach of Contract",
            "description": (
                "Explains compensation for loss or damage caused by breach of contract. Courts assess quantum of damages based on reasonably foreseeable consequences of the breach and contractual terms."
            ),
            "punishment": "Award of damages; specific performance in certain circumstances"
        },

        "Limitation Act (Selected)": {
            "title": "Limitation Periods for Civil Suits",
            "description": (
                "Statute prescribes time-limits for filing civil suits, appeals, and execution applications. Limitation plays a critical role in admissibility of civil claims and defenses."
            ),
            "punishment": "Time-bar (defense) leading to dismissal on limitation grounds"
        }
    },

    # =====================================================
    # ADDITIONAL CRIMINAL LAW SECTIONS (COMMONLY CITED)
    # =====================================================
    "Additional IPC & Related Provisions": {

        "IPC 307": {
            "title": "Attempt to Murder",
            "description": (
                "Punishes attempts to commit murder where the intention and actus reus demonstrate conduct likely to cause death, even if death does not result. Courts examine intention and probability of death in sentencing."
            ),
            "punishment": "Imprisonment which may extend to 10 years, and fine; more serious cases may attract greater penalties"
        },

        "IPC 308": {
            "title": "Attempt to Commit Suicide (Deprecated / Repealed contextually)",
            "description": (
                "Historical provisions criminalized attempted suicide in some jurisdictions; public policy and amendments in many places have moved towards decriminalization and treatment-based responses."
            ),
            "punishment": "Policy-based — modern approach focuses on mental health interventions"
        },

        "IPC 312": {
            "title": "Causing Miscarriage (when not murder)",
            "description": (
                "Deals with causing miscarriage without justification; exceptions exist for medical necessity and to save life of the mother in certified circumstances."
            ),
            "punishment": "Imprisonment which may extend to 3 years, and fine"
        },

        "IPC 315-316": {
            "title": "Death from Dangerous Acts or Injury",
            "description": (
                "Sections dealing with consequences where acts lead to death or result in grievous outcomes due to the perpetrator's actions."
            ),
            "punishment": "Varying terms depending on offense classification"
        },

        "IPC 375A/376A (Amendments)": {
            "title": "Aggravated Sexual Offences",
            "description": (
                "Statutory amendments create aggravated categories for sexual offences occurring in custody, involving minors, or where violence is extreme—triggering higher minimum sentences and special procedural safeguards."
            ),
            "punishment": "Higher minimum sentences up to life imprisonment in aggravated cases"
        },

        "IPC 377": {
            "title": "Unnatural Offences (Historical context)",
            "description": (
                "Historically criminalized certain consensual sexual acts; developments in judicial review have narrowed or invalidated its application to private consensual acts between adults while maintaining offenses for non-consensual acts."
            ),
            "punishment": "Varies by legal status and judicial interpretation"
        },

        "IPC 498A": {
            "title": "Cruelty by Husband or Relatives",
            "description": (
                "Addresses cruelty causing mental or physical harm to married women, often invoked in domestic violence and dowry-related harassment cases. Section includes both physical and mental cruelty aspects."
            ),
            "punishment": "Imprisonment up to 3 years and fine; measures for protection orders and civil remedies also available"
        },

        "IPC 506/507": {
            "title": "Criminal Intimidation and Criminal Threats",
            "description": (
                "Deals with threats intended to cause alarm or to coerce a person into action; section 507 addresses criminal intimidation by anonymous communication."
            ),
            "punishment": "Imprisonment terms vary according to severity, including up to 7 years in aggravated circumstances"
        },

        "IPC 498B (Dowry Prohibition Act related)": {
            "title": "Dowry Offences",
            "description": (
                "Dowry Prohibition Act and related IPC provisions address the giving, taking or demanding of dowry and harassment of brides; relevant in matrimonial complaints involving demands, cruelty and harassment."
            ),
            "punishment": "Imprisonment and fine under respective statutes"
        }
    },

    # =====================================================
    # SELECTED SECTIONS FROM SPECIAL LAWS & PROCEDURAL ACTS
    # =====================================================
    "Special & Procedural Laws (Selected)": {

        "Maintenance & Welfare (Maintenance Act provisions)": {
            "title": "Maintenance of Wives, Children and Parents",
            "description": (
                "Statutes ensure maintenance obligations in family law contexts, and provide summary remedy procedures to claim maintenance from obligated family members."
            ),
            "punishment": "Enforcement orders including attachment of earnings, penal consequences for non-compliance"
        },

        "NDPS Act (Selected Provisions)": {
            "title": "Narcotic Drugs and Psychotropic Substances Offences",
            "description": (
                "Special law dealing with trafficking, cultivation and consumption of narcotics; contains stringent provisions for possession and commercial quantities with mandatory minimum sentences."
            ),
            "punishment": "Stringent imprisonment and fines depending on quantities (may include life imprisonment for commercial quantities)"
        },

        "Motor Vehicles Act (Selected)": {
            "title": "Traffic Offences and Motor Vehicle Regulation",
            "description": (
                "Deals with licensing, registration, insurance, and penalties for traffic violations such as dangerous driving, driving under intoxication, and negligent driving causing injury."
            ),
            "punishment": "Fines, disqualification of license, imprisonment in serious cases"
        }
    },

    # =====================================================
    # CYBER / ELECTRONIC OFFENCES – ADDITIONAL ITEMS
    # =====================================================
    "Additional Cyber & Electronic Offences": {

        "IT Act 72A": {
            "title": "Disclosure of Personal Information",
            "description": (
                "Imposes penal consequences for disclosure of personal information by an intermediary or person without consent where such disclosure causes harm or loss to the individual."
            ),
            "punishment": "Penal consequences and damages subject to provisions"
        },

        "IT Act 67B (Child Pornography)": {
            "title": "Punishment for Publishing of Child Pornographic Material in Electronic Form",
            "description": (
                "Addresses creation, transmission or storage of child sexual abuse material in electronic form; focused on protecting children and penalizing offenders and intermediaries facilitating such material."
            ),
            "punishment": "Rigorous imprisonment and fine; severity commensurate with protection objectives"
        }
    },

    # =====================================================
    # EVIDENCE & PROCEDURAL SUPPORT (ADDITIONAL)
    # =====================================================
    "Evidence & Forensics (Selected Provisions)": {

        "DNA Evidence (Judicial Standards)": {
            "title": "Use of DNA and Forensic Evidence in Criminal Prosecutions",
            "description": (
                "While specific statutory frameworks govern scientific evidence, courts have developed standards for admissibility, chain of custody, expert testimony, and reliability for DNA, fingerprint, digital forensics and other scientific methods."
            ),
            "punishment": "Evidentiary; impacts weight and conviction probability"
        },

        "Electronic Evidence Best Practices": {
            "title": "Digital Evidence Collection and Chain of Custody",
            "description": (
                "Best practices advise preservation of logs, timestamps, use of certified devices, and documentation (hashing, checksums) to ensure admissibility under Section 65B and related rules."
            ),
            "punishment": "Evidentiary — improper preservation may render evidence inadmissible"
        }
    },

    # =====================================================
    # SELECTED ADDITIONAL PROVISIONS (USEFUL FOR LIBRARY)
    # =====================================================
    "Miscellaneous Useful Sections & Concepts": {

        "Extradition (Selected Provisions)": {
            "title": "Extradition and Mutual Legal Assistance",
            "description": (
                "Rules and treaties governing surrender of fugitives across international borders for prosecution or sentence execution; includes procedural safeguards and treaty-based requirements."
            ),
            "punishment": "International legal process — not a punishment but a procedural mechanism"
        },

        "Juvenile Justice (Selected Provisions)": {
            "title": "Juvenile Justice and Protection of Children",
            "description": (
                "Special procedures, rehabilitative approach and protective measures for offenses involving minors; distinct adjudicatory systems and custodial standards to prioritize reform over retribution."
            ),
            "punishment": "Rehabilitation and custody under juvenile law frameworks; custodial sentences differ from adult sanctions"
        },

        "Consumer Protection (Selected Provisions)": {
            "title": "Consumer Rights and Redressal",
            "description": (
                "Statutory framework for consumer protection provides civil remedies for defective goods, unfair trade practices, false advertising and deficiency in services."
            ),
            "punishment": "Monetary compensation, injunctions and corrective orders by consumer forums"
        }
    }
}

# End of LAW_SECTIONS
