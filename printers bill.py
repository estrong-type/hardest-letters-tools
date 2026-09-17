"""
THE PRINTER'S BILL
-------------------
A shop like Master Alvise's had to decide, before casting a single letter,
how many of each one to make. Cast too few e's, and the compositors run
dry halfway through a page. Cast too many z's, and the extras just sit
in a drawer, gathering dust.

But "how many pieces should we cast?" isn't really a question you can
answer with one number pulled out of the air. It depends on how the
whole shop actually runs:

  - How many complete sheets is the shop setting and printing each day?
    (A quarto sheet isn't one page -- it's four pages of type locked
    up together as a "forme," printed on one side, then a SECOND
    forme of four more pages printed on the other side. Fold it
    twice, and one sheet becomes eight pages of a book.)
  - How many characters does a typical page hold?
  - Once a page is printed, how many days pass before someone
    distributes its type back into the case, freeing it up to be
    used again?

That last question matters more than it looks like it should. If
distribution happens like clockwork the day after a page is set, the
shop only ever needs enough type for the pages currently "in flight."
But what if Isabetta -- the shop's fastest distributor -- gets sick for
two days? Every page that would have been broken down and returned to
the case is instead sitting locked up, unusable, and the shop needs
EXTRA type on hand to keep composing while it waits for her to get
better. That extra cushion is called a buffer, and every real business
that manufactures anything has to decide how big a buffer it can afford.

This program models that whole chain: it reads a sample of text to
learn the shop's letter-frequency habits, then asks how the shop
actually operates, and calculates a bill that would keep it running
even through a bad week -- not just an average one.

TRY IT YOURSELF:
1. Change SAMPLE_CHOICE to "short", "constitution", "lear", or "alice"
   to try a different built-in passage -- or write your own text
   between the triple quotes of SAMPLE_SHORT and set SAMPLE_CHOICE to
   "short" to use it.
2. Change the four production settings below to describe a shop of
   your own invention.
3. Run the program and look at the bill. Then try raising BUFFER_DAYS
   from 0 to 3 and see how much more type the shop suddenly needs --
   that's the real cost of protecting against Isabetta's sick days.
4. Try changing POINT_SIZE too. Bigger type means bigger, heavier
   pieces -- watch how many pounds of lead a shop needs just to
   print in a larger size.
"""

from collections import Counter
import string

# Four sample passages are built in below, so you don't have to type in
# a long text yourself just to see how the bill changes. Pick one by
# changing SAMPLE_CHOICE to "short", "constitution", "lear", or "alice".

SAMPLE_SHORT = """
Marietta had been sorting type since before dawn, and her fingers
already knew what her eyes were too tired to check.
"""

# The U.S. Constitution, Preamble through Article VII (public domain).
SAMPLE_CONSTITUTION = """
We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.

Article I

Section 1: Congress

All legislative Powers herein granted shall be vested in a Congress of the United States, which shall consist of a Senate and House of Representatives.

Section 2: The House of Representatives

The House of Representatives shall be composed of Members chosen every second Year by the People of the several States, and the Electors in each State shall have the Qualifications requisite for Electors of the most numerous Branch of the State Legislature.

No Person shall be a Representative who shall not have attained to the Age of twenty five Years, and been seven Years a Citizen of the United States, and who shall not, when elected, be an Inhabitant of that State in which he shall be chosen.

Representatives and direct Taxes shall be apportioned among the several States which may be included within this Union, according to their respective Numbers, which shall be determined by adding to the whole Number of free Persons, including those bound to Service for a Term of Years, and excluding Indians not taxed, three fifths of all other Persons. The actual Enumeration shall be made within three Years after the first Meeting of the Congress of the United States, and within every subsequent Term of ten Years, in such Manner as they shall by Law direct. The Number of Representatives shall not exceed one for every thirty Thousand, but each State shall have at Least one Representative; and until such enumeration shall be made, the State of New Hampshire shall be entitled to chuse three, Massachusetts eight, Rhode-Island and Providence Plantations one, Connecticut five, New-York six, New Jersey four, Pennsylvania eight, Delaware one, Maryland six, Virginia ten, North Carolina five, South Carolina five, and Georgia three.

When vacancies happen in the Representation from any State, the Executive Authority thereof shall issue Writs of Election to fill such Vacancies.

The House of Representatives shall chuse their Speaker and other Officers; and shall have the sole Power of Impeachment.

Section 3: The Senate

The Senate of the United States shall be composed of two Senators from each State, chosen by the Legislature thereof, for six Years; and each Senator shall have one Vote.

Immediately after they shall be assembled in Consequence of the first Election, they shall be divided as equally as may be into three Classes. The Seats of the Senators of the first Class shall be vacated at the Expiration of the second Year, of the second Class at the Expiration of the fourth Year, and of the third Class at the Expiration of the sixth Year, so that one third may be chosen every second Year; and if Vacancies happen by Resignation, or otherwise, during the Recess of the Legislature of any State, the Executive thereof may make temporary Appointments until the next Meeting of the Legislature, which shall then fill such Vacancies.

No Person shall be a Senator who shall not have attained to the Age of thirty Years, and been nine Years a Citizen of the United States, and who shall not, when elected, be an Inhabitant of that State for which he shall be chosen.

The Vice President of the United States shall be President of the Senate, but shall have no Vote, unless they be equally divided.

The Senate shall chuse their other Officers, and also a President pro tempore, in the Absence of the Vice President, or when he shall exercise the Office of President of the United States.

The Senate shall have the sole Power to try all Impeachments. When sitting for that Purpose, they shall be on Oath or Affirmation. When the President of the United States is tried, the Chief Justice shall preside: And no Person shall be convicted without the Concurrence of two thirds of the Members present.

Judgment in Cases of Impeachment shall not extend further than to removal from Office, and disqualification to hold and enjoy any Office of honor, Trust or Profit under the United States: but the Party convicted shall nevertheless be liable and subject to Indictment, Trial, Judgment and Punishment, according to Law.

Section 4: Elections

The Times, Places and Manner of holding Elections for Senators and Representatives, shall be prescribed in each State by the Legislature thereof; but the Congress may at any time by Law make or alter such Regulations, except as to the Places of chusing Senators.

The Congress shall assemble at least once in every Year, and such Meeting shall be on the first Monday in December, unless they shall by Law appoint a different Day.

Section 5: Powers and Duties of Congress

Each House shall be the Judge of the Elections, Returns and Qualifications of its own Members, and a Majority of each shall constitute a Quorum to do Business; but a smaller Number may adjourn from day to day, and may be authorized to compel the Attendance of absent Members, in such Manner, and under such Penalties as each House may provide.

Each House may determine the Rules of its Proceedings, punish its Members for disorderly Behaviour, and, with the Concurrence of two thirds, expel a Member.

Each House shall keep a Journal of its Proceedings, and from time to time publish the same, excepting such Parts as may in their Judgment require Secrecy; and the Yeas and Nays of the Members of either House on any question shall, at the Desire of one fifth of those Present, be entered on the Journal.

Neither House, during the Session of Congress, shall, without the Consent of the other, adjourn for more than three days, nor to any other Place than that in which the two Houses shall be sitting.

Section 6: Rights and Disabilities of Members

The Senators and Representatives shall receive a Compensation for their Services, to be ascertained by Law, and paid out of the Treasury of the United States. They shall in all Cases, except Treason, Felony and Breach of the Peace, be privileged from Arrest during their Attendance at the Session of their respective Houses, and in going to and returning from the same; and for any Speech or Debate in either House, they shall not be questioned in any other Place.

No Senator or Representative shall, during the Time for which he was elected, be appointed to any civil Office under the Authority of the United States, which shall have been created, or the Emoluments whereof shall have been encreased during such time; and no Person holding any Office under the United States, shall be a Member of either House during his Continuance in Office.

Section 7: Legislative Process

All Bills for raising Revenue shall originate in the House of Representatives; but the Senate may propose or concur with Amendments as on other Bills.

Every Bill which shall have passed the House of Representatives and the Senate, shall, before it become a Law, be presented to the President of the United States; If he approve he shall sign it, but if not he shall return it, with his Objections to that House in which it shall have originated, who shall enter the Objections at large on their Journal, and proceed to reconsider it. If after such Reconsideration two thirds of that House shall agree to pass the Bill, it shall be sent, together with the Objections, to the other House, by which it shall likewise be reconsidered, and if approved by two thirds of that House, it shall become a Law. But in all such Cases the Votes of both Houses shall be determined by yeas and Nays, and the Names of the Persons voting for and against the Bill shall be entered on the Journal of each House respectively. If any Bill shall not be returned by the President within ten Days (Sundays excepted) after it shall have been presented to him, the Same shall be a Law, in like Manner as if he had signed it, unless the Congress by their Adjournment prevent its Return, in which Case it shall not be a Law.

Every Order, Resolution, or Vote to which the Concurrence of the Senate and House of Representatives may be necessary (except on a question of Adjournment) shall be presented to the President of the United States; and before the Same shall take Effect, shall be approved by him, or being disapproved by him, shall be repassed by two thirds of the Senate and House of Representatives, according to the Rules and Limitations prescribed in the Case of a Bill.

Section 8: Powers of Congress

The Congress shall have Power To lay and collect Taxes, Duties, Imposts and Excises, to pay the Debts and provide for the common Defence and general Welfare of the United States; but all Duties, Imposts and Excises shall be uniform throughout the United States;

To borrow Money on the credit of the United States;

To regulate Commerce with foreign Nations, and among the several States, and with the Indian Tribes;

To establish a uniform Rule of Naturalization, and uniform Laws on the subject of Bankruptcies throughout the United States;

To coin Money, regulate the Value thereof, and of foreign Coin, and fix the Standard of Weights and Measures;

To provide for the Punishment of counterfeiting the Securities and current Coin of the United States;

To establish Post Offices and post Roads;

To promote the Progress of Science and useful Arts, by securing for limited Times to Authors and Inventors the exclusive Right to their respective Writings and Discoveries;

To constitute Tribunals inferior to the supreme Court;

To define and punish Piracies and Felonies committed on the high Seas, and Offences against the Law of Nations;

To declare War, grant Letters of Marque and Reprisal, and make Rules concerning Captures on Land and Water;

To raise and support Armies, but no Appropriation of Money to that Use shall be for a longer Term than two Years;

To provide and maintain a Navy;

To make Rules for the Government and Regulation of the land and naval Forces;

To provide for calling forth the Militia to execute the Laws of the Union, suppress Insurrections and repel Invasions;

To provide for organizing, arming, and disciplining, the Militia, and for governing such Part of them as may be employed in the Service of the United States, reserving to the States respectively, the Appointment of the Officers, and the Authority of training the Militia according to the discipline prescribed by Congress;

To exercise exclusive Legislation in all Cases whatsoever, over such District (not exceeding ten Miles square) as may, by Cession of particular States, and the Acceptance of Congress, become the Seat of the Government of the United States, and to exercise like Authority over all Places purchased by the Consent of the Legislature of the State in which the Same shall be, for the Erection of Forts, Magazines, Arsenals, dock-Yards and other needful Buildings; And

To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers, and all other Powers vested by this Constitution in the Government of the United States, or in any Department or Officer thereof.

Section 9: Powers Denied Congress

The Migration or Importation of such Persons as any of the States now existing shall think proper to admit, shall not be prohibited by the Congress prior to the Year one thousand eight hundred and eight, but a Tax or duty may be imposed on such Importation, not exceeding ten dollars for each Person.

The Privilege of the Writ of Habeas Corpus shall not be suspended, unless when in Cases of Rebellion or Invasion the public Safety may require it.

No Bill of Attainder or ex post facto Law shall be passed.

No Capitation, or other direct, Tax shall be laid, unless in Proportion to the Census or enumeration herein before directed to be taken.

No Tax or Duty shall be laid on Articles exported from any State.

No Preference shall be given by any Regulation of Commerce or Revenue to the Ports of one State over those of another: nor shall Vessels bound to, or from, one State, be obliged to enter, clear, or pay Duties in another.

No Money shall be drawn from the Treasury, but in Consequence of Appropriations made by Law; and a regular Statement and Account of the Receipts and Expenditures of all public Money shall be published from time to time.

No Title of Nobility shall be granted by the United States: And no Person holding any Office of Profit or Trust under them, shall, without the Consent of the Congress, accept of any present, Emolument, Office, or Title, of any kind whatever, from any King, Prince, or foreign State.

Section 10: Powers Denied to the States

No State shall enter into any Treaty, Alliance, or Confederation; grant Letters of Marque and Reprisal; coin Money; emit Bills of Credit; make any Thing but gold and silver Coin a Tender in Payment of Debts; pass any Bill of Attainder, ex post facto Law, or Law impairing the Obligation of Contracts, or grant any Title of Nobility.

No State shall, without the Consent of the Congress, lay any Imposts or Duties on Imports or Exports, except what may be absolutely necessary for executing it's inspection Laws: and the net Produce of all Duties and Imposts, laid by any State on Imports or Exports, shall be for the Use of the Treasury of the United States; and all such Laws shall be subject to the Revision and Controul of the Congress.

No State shall, without the Consent of Congress, lay any Duty of Tonnage, keep Troops, or Ships of War in time of Peace, enter into any Agreement or Compact with another State, or with a foreign Power, or engage in War, unless actually invaded, or in such imminent Danger as will not admit of delay.

Article II

Section 1

The executive Power shall be vested in a President of the United States of America.

He shall hold his Office during the Term of four Years, and, together with the Vice President, chosen for the same Term, be elected, as follows:

Each State shall appoint, in such Manner as the Legislature thereof may direct, a Number of Electors, equal to the whole Number of Senators and Representatives to which the State may be entitled in the Congress: but no Senator or Representative, or Person holding an Office of Trust or Profit under the United States, shall be appointed an Elector.

The Electors shall meet in their respective States, and vote by Ballot for two Persons, of whom one at least shall not be an Inhabitant of the same State with themselves. And they shall make a List of all the Persons voted for, and of the Number of Votes for each; which List they shall sign and certify, and transmit sealed to the Seat of the Government of the United States, directed to the President of the Senate. The President of the Senate shall, in the Presence of the Senate and House of Representatives, open all the Certificates, and the Votes shall then be counted. The Person having the greatest Number of Votes shall be the President, if such Number be a Majority of the whole Number of Electors appointed; and if there be more than one who have such Majority, and have an equal Number of Votes, then the House of Representatives shall immediately chuse by Ballot one of them for President; and if no Person have a Majority, then from the five highest on the List the said House shall in like Manner chuse the President. But in chusing the President, the Votes shall be taken by States, the Representation from each State having one Vote; A quorum for this Purpose shall consist of a Member or Members from two thirds of the States, and a Majority of all the States shall be necessary to a Choice. In every Case, after the Choice of the President, the Person having the greatest Number of Votes of the Electors shall be the Vice President. But if there should remain two or more who have equal Votes, the Senate shall chuse from them by Ballot the Vice President.

The Congress may determine the Time of chusing the Electors, and the Day on which they shall give their Votes; which Day shall be the same throughout the United States.

No Person except a natural born Citizen, or a Citizen of the United States, at the time of the Adoption of this Constitution, shall be eligible to the Office of President; neither shall any Person be eligible to that Office who shall not have attained to the Age of thirty five Years, and been fourteen Years a Resident within the United States.

In Case of the Removal of the President from Office, or of his Death, Resignation, or Inability to discharge the Powers and Duties of the said Office, the Same shall devolve on the Vice President, and the Congress may by Law provide for the Case of Removal, Death, Resignation or Inability, both of the President and Vice President, declaring what Officer shall then act as President, and such Officer shall act accordingly, until the Disability be removed, or a President shall be elected.

The President shall, at stated Times, receive for his Services, a Compensation, which shall neither be encreased nor diminished during the Period for which he shall have been elected, and he shall not receive within that Period any other Emolument from the United States, or any of them.

Before he enter on the Execution of his Office, he shall take the following Oath or Affirmation: "I do solemnly swear (or affirm) that I will faithfully execute the Office of President of the United States, and will to the best of my Ability, preserve, protect and defend the Constitution of the United States."

Section 2

The President shall be Commander in Chief of the Army and Navy of the United States, and of the Militia of the several States, when called into the actual Service of the United States; he may require the Opinion, in writing, of the principal Officer in each of the executive Departments, upon any Subject relating to the Duties of their respective Offices, and he shall have Power to grant Reprieves and Pardons for Offences against the United States, except in Cases of Impeachment.

He shall have Power, by and with the Advice and Consent of the Senate, to make Treaties, provided two thirds of the Senators present concur; and he shall nominate, and by and with the Advice and Consent of the Senate, shall appoint Ambassadors, other public Ministers and Consuls, Judges of the supreme Court, and all other Officers of the United States, whose Appointments are not herein otherwise provided for, and which shall be established by Law: but the Congress may by Law vest the Appointment of such inferior Officers, as they think proper, in the President alone, in the Courts of Law, or in the Heads of Departments.

The President shall have Power to fill up all Vacancies that may happen during the Recess of the Senate, by granting Commissions which shall expire at the End of their next Session.

Section 3

He shall from time to time give to the Congress Information of the State of the Union, and recommend to their Consideration such Measures as he shall judge necessary and expedient; he may, on extraordinary Occasions, convene both Houses, or either of them, and in Case of Disagreement between them, with Respect to the Time of Adjournment, he may adjourn them to such Time as he shall think proper; he shall receive Ambassadors and other public Ministers; he shall take Care that the Laws be faithfully executed, and shall Commission all the Officers of the United States.

Section 4

The President, Vice President and all civil Officers of the United States, shall be removed from Office on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors.

Article III

Section 1

The judicial Power of the United States, shall be vested in one supreme Court, and in such inferior Courts as the Congress may from time to time ordain and establish. The Judges, both of the supreme and inferior Courts, shall hold their Offices during good Behaviour, and shall, at stated Times, receive for their Services, a Compensation, which shall not be diminished during their Continuance in Office.

Section 2

The judicial Power shall extend to all Cases, in Law and Equity, arising under this Constitution, the Laws of the United States, and Treaties made, or which shall be made, under their Authority; to all Cases affecting Ambassadors, other public Ministers and Consuls; to all Cases of admiralty and maritime Jurisdiction; to Controversies to which the United States shall be a Party; to Controversies between two or more States; between a State and Citizens of another State; between Citizens of different States; between Citizens of the same State claiming Lands under Grants of different States, and between a State, or the Citizens thereof, and foreign States, Citizens or Subjects.

In all Cases affecting Ambassadors, other public Ministers and Consuls, and those in which a State shall be Party, the supreme Court shall have original Jurisdiction. In all the other Cases before mentioned, the supreme Court shall have appellate Jurisdiction, both as to Law and Fact, with such Exceptions, and under such Regulations as the Congress shall make.

The Trial of all Crimes, except in Cases of Impeachment; shall be by Jury; and such Trial shall be held in the State where the said Crimes shall have been committed; but when not committed within any State, the Trial shall be at such Place or Places as the Congress may by Law have directed.

Section 3

Treason against the United States, shall consist only in levying War against them, or in adhering to their Enemies, giving them Aid and Comfort. No Person shall be convicted of Treason unless on the Testimony of two Witnesses to the same overt Act, or on Confession in open Court.

The Congress shall have Power to declare the Punishment of Treason, but no Attainder of Treason shall work Corruption of Blood, or Forfeiture except during the Life of the Person attainted.

Article IV

Section 1

Full Faith and Credit shall be given in each State to the public Acts, Records, and judicial Proceedings of every other State. And the Congress may by general Laws prescribe the Manner in which such Acts, Records and Proceedings shall be proved, and the Effect thereof.

Section 2

The Citizens of each State shall be entitled to all Privileges and Immunities of Citizens in the several States.

A Person charged in any State with Treason, Felony, or other Crime, who shall flee from Justice, and be found in another State, shall on Demand of the executive Authority of the State from which he fled, be delivered up, to be removed to the State having Jurisdiction of the Crime.

No Person held to Service or Labour in one State, under the Laws thereof, escaping into another, shall, in Consequence of any Law or Regulation therein, be discharged from such Service or Labour, but shall be delivered up on Claim of the Party to whom such Service or Labour may be due.

Section 3

New States may be admitted by the Congress into this Union; but no new State shall be formed or erected within the Jurisdiction of any other State; nor any State be formed by the Junction of two or more States, or Parts of States, without the Consent of the Legislatures of the States concerned as well as of the Congress.

The Congress shall have Power to dispose of and make all needful Rules and Regulations respecting the Territory or other Property belonging to the United States; and nothing in this Constitution shall be so construed as to Prejudice any Claims of the United States, or of any particular State.

Section 4

The United States shall guarantee to every State in this Union a Republican Form of Government, and shall protect each of them against Invasion; and on Application of the Legislature, or of the Executive (when the Legislature cannot be convened) against domestic Violence.

Article V

The Congress, whenever two thirds of both Houses shall deem it necessary, shall propose Amendments to this Constitution, or, on the Application of the Legislatures of two thirds of the several States, shall call a Convention for proposing Amendments, which, in either Case, shall be valid to all Intents and Purposes, as Part of this Constitution, when ratified by the Legislatures of three fourths of the several States, or by Conventions in three fourths thereof, as the one or the other Mode of Ratification may be proposed by the Congress; Provided that no Amendment which may be made prior to the Year One thousand eight hundred and eight shall in any Manner affect the first and fourth Clauses in the Ninth Section of the first Article; and that no State, without its Consent, shall be deprived of its equal Suffrage in the Senate.

Article VI

All Debts contracted and Engagements entered into, before the Adoption of this Constitution, shall be as valid against the United States under this Constitution, as under the Confederation.

This Constitution, and the Laws of the United States which shall be made in Pursuance thereof; and all Treaties made, or which shall be made, under the Authority of the United States, shall be the supreme Law of the Land; and the Judges in every State shall be bound thereby, any Thing in the Constitution or Laws of any State to the Contrary notwithstanding.

The Senators and Representatives before mentioned, and the Members of the several State Legislatures, and all executive and judicial Officers, both of the United States and of the several States, shall be bound by Oath or Affirmation, to support this Constitution; but no religious Test shall ever be required as a Qualification to any Office or public Trust under the United States.

Article VII

The Ratification of the Conventions of nine States, shall be sufficient for the Establishment of this Constitution between the States so ratifying the Same.

"""


# King Lear, Act 1 Scene 1, in the ORIGINAL First Folio spelling (1623) --
# note "vs" for "us," "haue" for "have," and so on. Public domain.
SAMPLE_LEAR = """
Enter Kent, Gloucester, and Edmond.

Kent. I thought the King had more affected the
Duke of Albany, then Cornwall

Glou. It did alwayes seeme so to vs: But
now in the diuision of the Kingdome, it appeares
not which of the Dukes hee valewes
most, for qualities are so weigh'd, that curiosity in neither,
can make choise of eithers moity

Kent. Is not this your Son, my Lord?
Glou. His breeding Sir, hath bin at my charge. I haue
so often blush'd to acknowledge him, that now I am
braz'd too't

Kent. I cannot conceiue you

Glou. Sir, this yong Fellowes mother could; wherevpon
she grew round womb'd, and had indeede (Sir) a
Sonne for her Cradle, ere she had a husband for her bed.
Do you smell a fault?
Kent. I cannot wish the fault vndone, the issue of it,
being so proper

Glou. But I haue a Sonne, Sir, by order of Law, some
yeere elder then this; who, yet is no deerer in my account,
though this Knaue came somthing sawcily to the
world before he was sent for: yet was his Mother fayre,
there was good sport at his making, and the horson must
be acknowledged. Doe you know this Noble Gentleman,
Edmond?
Edm. No, my Lord

Glou. My Lord of Kent:
Remember him heereafter, as my Honourable Friend

Edm. My seruices to your Lordship

Kent. I must loue you, and sue to know you better

Edm. Sir, I shall study deseruing

Glou. He hath bin out nine yeares, and away he shall
againe. The King is comming.

Sennet. Enter King Lear, Cornwall, Albany, Gonerill, Regan,
Cordelia, and attendants.

Lear. Attend the Lords of France & Burgundy, Gloster

Glou. I shall, my Lord.
Enter.

Lear. Meane time we shal expresse our darker purpose.
Giue me the Map there. Know, that we haue diuided
In three our Kingdome: and 'tis our fast intent,
To shake all Cares and Businesse from our Age,
Conferring them on yonger strengths, while we
Vnburthen'd crawle toward death. Our son of Cornwal,
And you our no lesse louing Sonne of Albany,
We haue this houre a constant will to publish
Our daughters seuerall Dowers, that future strife
May be preuented now. The Princes, France & Burgundy,
Great Riuals in our yongest daughters loue,
Long in our Court, haue made their amorous soiourne,
And heere are to be answer'd. Tell me my daughters
(Since now we will diuest vs both of Rule,
Interest of Territory, Cares of State)
Which of you shall we say doth loue vs most,
That we, our largest bountie may extend
Where Nature doth with merit challenge. Gonerill,
Our eldest borne, speake first

Gon. Sir, I loue you more then word can weild y matter,
Deerer then eye-sight, space, and libertie,
Beyond what can be valewed, rich or rare,
No lesse then life, with grace, health, beauty, honor:
As much as Childe ere lou'd, or Father found.
A loue that makes breath poore, and speech vnable,
Beyond all manner of so much I loue you

Cor. What shall Cordelia speake? Loue, and be silent

Lear. Of all these bounds euen from this Line, to this,
With shadowie Forrests, and with Champains rich'd
With plenteous Riuers, and wide-skirted Meades
We make thee Lady. To thine and Albanies issues
Be this perpetuall. What sayes our second Daughter?
Our deerest Regan, wife of Cornwall?
Reg. I am made of that selfe-mettle as my Sister,
And prize me at her worth. In my true heart,
I finde she names my very deede of loue:
Onely she comes too short, that I professe
My selfe an enemy to all other ioyes,
Which the most precious square of sense professes,
And finde I am alone felicitate
In your deere Highnesse loue

Cor. Then poore Cordelia,
And yet not so, since I am sure my loue's
More ponderous then my tongue

Lear. To thee, and thine hereditarie euer,
Remaine this ample third of our faire Kingdome,
No lesse in space, validitie, and pleasure
Then that conferr'd on Gonerill. Now our Ioy,
Although our last and least; to whose yong loue,
The Vines of France, and Milke of Burgundie,
Striue to be interest. What can you say, to draw
A third, more opilent then your Sisters? speake

Cor. Nothing my Lord

Lear. Nothing?
Cor. Nothing

Lear. Nothing will come of nothing, speake againe

Cor. Vnhappie that I am, I cannot heaue
My heart into my mouth: I loue your Maiesty
According to my bond, no more nor lesse

Lear. How, how Cordelia? Mend your speech a little,
Least you may marre your Fortunes

Cor. Good my Lord,
You haue begot me, bred me, lou'd me.
I returne those duties backe as are right fit,
Obey you, Loue you, and most Honour you.
Why haue my Sisters Husbands, if they say
They loue you all? Happily when I shall wed,
That Lord, whose hand must take my plight, shall carry
Halfe my loue with him, halfe my Care, and Dutie,
Sure I shall neuer marry like my Sisters

Lear. But goes thy heart with this?
Cor. I my good Lord

Lear. So young, and so vntender?
Cor. So young my Lord, and true

Lear. Let it be so, thy truth then be thy dowre:
For by the sacred radience of the Sunne,
The misteries of Heccat and the night:
By all the operation of the Orbes,
From whom we do exist, and cease to be,
Heere I disclaime all my Paternall care,
Propinquity and property of blood,
And as a stranger to my heart and me,
Hold thee from this for euer. The barbarous Scythian,
Or he that makes his generation messes
To gorge his appetite, shall to my bosome
Be as well neighbour'd, pittied, and releeu'd,
As thou my sometime Daughter

Kent. Good my Liege

Lear. Peace Kent,
Come not betweene the Dragon and his wrath,
I lou'd her most, and thought to set my rest
On her kind nursery. Hence and avoid my sight:
So be my graue my peace, as here I giue
Her Fathers heart from her; call France, who stirres?
Call Burgundy, Cornwall, and Albanie,
With my two Daughters Dowres, digest the third,
Let pride, which she cals plainnesse, marry her:
I doe inuest you ioyntly with my power,
Preheminence, and all the large effects
That troope with Maiesty. Our selfe by Monthly course,
With reseruation of an hundred Knights,
By you to be sustain'd, shall our abode
Make with you by due turne, onely we shall retaine
The name, and all th' addition to a King: the Sway,
Reuennew, Execution of the rest,
Beloued Sonnes be yours, which to confirme,
This Coronet part betweene you

Kent. Royall Lear,
Whom I haue euer honor'd as my King,
Lou'd as my Father, as my Master follow'd,
As my great Patron thought on in my praiers

Le. The bow is bent & drawne, make from the shaft

Kent. Let it fall rather, though the forke inuade
The region of my heart, be Kent vnmannerly,
When Lear is mad, what wouldest thou do old man?
Think'st thou that dutie shall haue dread to speake,
When power to flattery bowes?
To plainnesse honour's bound,
When Maiesty falls to folly, reserue thy state,
And in thy best consideration checke
This hideous rashnesse, answere my life, my iudgement:
Thy yongest Daughter do's not loue thee least,
Nor are those empty hearted, whose low sounds
Reuerbe no hollownesse

Lear. Kent, on thy life no more

Kent. My life I neuer held but as pawne
To wage against thine enemies, nere feare to loose it,
Thy safety being motiue

Lear. Out of my sight

Kent. See better Lear, and let me still remaine
The true blanke of thine eie

Lear. Now by Apollo,
Kent. Now by Apollo, King
Thou swear'st thy Gods in vaine

Lear. O Vassall! Miscreant

Alb. Cor. Deare Sir forbeare

Kent. Kill thy Physition, and thy fee bestow
Vpon the foule disease, reuoke thy guift,
Or whil'st I can vent clamour from my throate,
Ile tell thee thou dost euill

Lea. Heare me recreant, on thine allegeance heare me;
That thou hast sought to make vs breake our vowes,
Which we durst neuer yet; and with strain'd pride,
To come betwixt our sentences, and our power,
Which, nor our nature, nor our place can beare;
Our potencie made good, take thy reward.
Fiue dayes we do allot thee for prouision,
To shield thee from disasters of the world,
And on the sixt to turne thy hated backe
Vpon our kingdome: if on the tenth day following,
Thy banisht trunke be found in our Dominions,
The moment is thy death, away. By Iupiter,
This shall not be reuok'd,
Kent. Fare thee well King, sith thus thou wilt appeare,
Freedome liues hence, and banishment is here;
The Gods to their deere shelter take thee Maid,
That iustly think'st, and hast most rightly said:
And your large speeches, may your deeds approue,
That good effects may spring from words of loue:
Thus Kent, O Princes, bids you all adew,
Hee'l shape his old course, in a Country new.
Enter.

Flourish. Enter Gloster with France, and Burgundy, Attendants.

Cor. Heere's France and Burgundy, my Noble Lord

Lear. My Lord of Burgundie,
We first addresse toward you, who with this King
Hath riuald for our Daughter; what in the least
Will you require in present Dower with her,
Or cease your quest of Loue?
Bur. Most Royall Maiesty,
I craue no more then hath your Highnesse offer'd,
Nor will you tender lesse?
Lear. Right Noble Burgundy,
When she was deare to vs, we did hold her so,
But now her price is fallen: Sir, there she stands,
If ought within that little seeming substance,
Or all of it with our displeasure piec'd,
And nothing more may fitly like your Grace,
Shee's there, and she is yours

Bur. I know no answer

Lear. Will you with those infirmities she owes,
Vnfriended, new adopted to our hate,
Dow'rd with our curse, and stranger'd with our oath,
Take her or, leaue her

Bur. Pardon me Royall Sir,
Election makes not vp in such conditions

Le. Then leaue her sir, for by the powre that made me,
I tell you all her wealth. For you great King,
I would not from your loue make such a stray,
To match you where I hate, therefore beseech you
T' auert your liking a more worthier way,
Then on a wretch whom Nature is asham'd
Almost t' acknowledge hers

Fra. This is most strange,
That she whom euen but now, was your obiect,
The argument of your praise, balme of your age,
The best, the deerest, should in this trice of time
Commit a thing so monstrous, to dismantle
So many folds of fauour: sure her offence
Must be of such vnnaturall degree,
That monsters it: Or your fore-voucht affection
Fall into taint, which to beleeue of her
Must be a faith that reason without miracle
Should neuer plant in me

Cor. I yet beseech your Maiesty.
If for I want that glib and oylie Art,
To speake and purpose not, since what I will intend,
Ile do't before I speake, that you make knowne
It is no vicious blot, murther, or foulenesse,
No vnchaste action or dishonoured step
That hath depriu'd me of your Grace and fauour,
But euen for want of that, for which I am richer,
A still soliciting eye, and such a tongue,
That I am glad I haue not, though not to haue it,
Hath lost me in your liking

Lear. Better thou had'st
Not beene borne, then not t'haue pleas'd me better

Fra. Is it but this? A tardinesse in nature,
Which often leaues the history vnspoke
That it intends to do: my Lord of Burgundy,
What say you to the Lady? Loue's not loue
When it is mingled with regards, that stands
Aloofe from th' intire point, will you haue her?
She is herselfe a Dowrie

Bur. Royall King,
Giue but that portion which your selfe propos'd,
And here I take Cordelia by the hand,
Dutchesse of Burgundie

Lear. Nothing, I haue sworne, I am firme

Bur. I am sorry then you haue so lost a Father,
That you must loose a husband

Cor. Peace be with Burgundie,
Since that respect and Fortunes are his loue,
I shall not be his wife

Fra. Fairest Cordelia, that art most rich being poore,
Most choise forsaken, and most lou'd despis'd,
Thee and thy vertues here I seize vpon,
Be it lawfull I take vp what's cast away.
Gods, Gods! 'Tis strange, that from their cold'st neglect
My Loue should kindle to enflam'd respect.
Thy dowrelesse Daughter King, throwne to my chance,
Is Queene of vs, of ours, and our faire France:
Not all the Dukes of watrish Burgundy,
Can buy this vnpriz'd precious Maid of me.
Bid them farewell Cordelia, though vnkinde,
Thou loosest here a better where to finde

Lear. Thou hast her France, let her be thine, for we
Haue no such Daughter, nor shall euer see
That face of hers againe, therfore be gone,
Without our Grace, our Loue, our Benizon:
Come Noble Burgundie.

Flourish. Exeunt.

Fra. Bid farwell to your Sisters

Cor. The Iewels of our Father, with wash'd eies
Cordelia leaues you, I know you what you are,
And like a Sister am most loth to call
Your faults as they are named. Loue well our Father:
To your professed bosomes I commit him,
But yet alas, stood I within his Grace,
I would prefer him to a better place,
So farewell to you both

Regn. Prescribe not vs our dutie

Gon. Let your study
Be to content your Lord, who hath receiu'd you
At Fortunes almes, you haue obedience scanted,
And well are worth the want that you haue wanted

Cor. Time shall vnfold what plighted cunning hides,
Who couers faults, at last with shame derides:
Well may you prosper

Fra. Come my faire Cordelia.

Exit France and Cor.

Gon. Sister, it is not little I haue to say,
Of what most neerely appertaines to vs both,
I thinke our Father will hence to night

Reg. That's most certaine, and with you: next moneth with vs

Gon. You see how full of changes his age is, the obseruation
we haue made of it hath beene little; he alwaies
lou'd our Sister most, and with what poore iudgement he
hath now cast her off, appeares too grossely

Reg. 'Tis the infirmity of his age, yet he hath euer but
slenderly knowne himselfe

Gon. The best and soundest of his time hath bin but
rash, then must we looke from his age, to receiue not alone
the imperfections of long ingraffed condition, but
therewithall the vnruly way-wardnesse, that infirme and
cholericke yeares bring with them

Reg. Such vnconstant starts are we like to haue from
him, as this of Kents banishment

Gon. There is further complement of leaue-taking betweene
France and him, pray you let vs sit together, if our
Father carry authority with such disposition as he beares,
this last surrender of his will but offend vs

Reg. We shall further thinke of it

Gon. We must do something, and i'th' heate.

"""


# Alice's Adventures in Wonderland, Chapter 1: Down the Rabbit-Hole (public domain).
SAMPLE_ALICE = """
Down the Rabbit-Hole

Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversations?"

So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.

There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, "Oh dear! Oh dear! I shall be late!" (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge.

In another moment down went Alice after it, never once considering how in the world she was to get out again.

The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down a very deep well.

Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed; it was labelled "ORANGE MARMALADE", but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody underneath, so managed to put it into one of the cupboards as she fell past it.

"Well!" thought Alice to herself, "after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!" (Which was very likely true.)

Down, down, down. Would the fall never come to an end? "I wonder how many miles I've fallen by this time?" she said aloud. "I must be getting somewhere near the centre of the earth. Let me see: that would be four thousand miles down, I think—" (for, you see, Alice had learnt several things of this sort in her lessons in the schoolroom, and though this was not a very good opportunity for showing off her knowledge, as there was no one to listen to her, still it was good practice to say it over) "—yes, that's about the right distance—but then I wonder what Latitude or Longitude I've got to?" (Alice had no idea what Latitude was, or Longitude either, but thought they were nice grand words to say.)

Presently she began again. "I wonder if I shall fall right through the earth! How funny it'll seem to come out among the people that walk with their heads downward! The Antipathies, I think—" (she was rather glad there was no one listening, this time, as it didn't sound at all the right word) "—but I shall have to ask them what the name of the country is, you know. Please, Ma'am, is this New Zealand or Australia?" (and she tried to curtsey as she spoke—fancy curtseying as you're falling through the air! Do you think you could manage it?) "And what an ignorant little girl she'll think me for asking! No, it'll never do to ask: perhaps I shall see it written up somewhere."

Down, down, down. There was nothing else to do, so Alice soon began talking again. "Dinah'll miss me very much to-night, I should think!" (Dinah was the cat.) "I hope they'll remember her saucer of milk at tea-time. Dinah my dear! I wish you were down here with me! There are no mice in the air, I'm afraid, but you might catch a bat, and that's very like a mouse, you know. But do cats eat bats, I wonder?" And here Alice began to get rather sleepy, and went on saying to herself, in a dreamy sort of way, "Do cats eat bats? Do cats eat bats?" and sometimes, "Do bats eat cats?" for, you see, as she couldn't answer either question, it didn't much matter which way she put it. She felt that she was dozing off, and had just begun to dream that she was walking hand in hand with Dinah, and saying to her very earnestly, "Now, Dinah, tell me the truth: did you ever eat a bat?" when suddenly, thump! thump! down she came upon a heap of sticks and dry leaves, and the fall was over.

Alice was not a bit hurt, and she jumped up on to her feet in a moment: she looked up, but it was all dark overhead; before her was another long passage, and the White Rabbit was still in sight, hurrying down it. There was not a moment to be lost: away went Alice like the wind, and was just in time to hear it say, as it turned a corner, "Oh my ears and whiskers, how late it's getting!" She was close behind it when she turned the corner, but the Rabbit was no longer to be seen: she found herself in a long, low hall, which was lit up by a row of lamps hanging from the roof.

There were doors all round the hall, but they were all locked; and when Alice had been all the way down one side and up the other, trying every door, she walked sadly down the middle, wondering how she was ever to get out again.

Suddenly she came upon a little three-legged table, all made of solid glass; there was nothing on it except a tiny golden key, and Alice's first thought was that it might belong to one of the doors of the hall; but, alas! either the locks were too large, or the key was too small, but at any rate it would not open any of them. However, on the second time round, she came upon a low curtain she had not noticed before, and behind it was a little door about fifteen inches high: she tried the little golden key in the lock, and to her great delight it fitted!

Alice opened the door and found that it led into a small passage, not much larger than a rat-hole: she knelt down and looked along the passage into the loveliest garden you ever saw. How she longed to get out of that dark hall, and wander about among those beds of bright flowers and those cool fountains, but she could not even get her head through the doorway; "and even if my head would go through," thought poor Alice, "it would be of very little use without my shoulders. Oh, how I wish I could shut up like a telescope! I think I could, if I only knew how to begin." For, you see, so many out-of-the-way things had happened lately, that Alice had begun to think that very few things indeed were really impossible.

There seemed to be no use in waiting by the little door, so she went back to the table, half hoping she might find another key on it, or at any rate a book of rules for shutting people up like telescopes: this time she found a little bottle on it, ("which certainly was not here before," said Alice,) and round the neck of the bottle was a paper label, with the words "DRINK ME," beautifully printed on it in large letters.

It was all very well to say "Drink me," but the wise little Alice was not going to do that in a hurry. "No, I'll look first," she said, "and see whether it's marked 'poison' or not"; for she had read several nice little histories about children who had got burnt, and eaten up by wild beasts and other unpleasant things, all because they would not remember the simple rules their friends had taught them: such as, that a red-hot poker will burn you if you hold it too long; and that if you cut your finger very deeply with a knife, it usually bleeds; and she had never forgotten that, if you drink much from a bottle marked "poison," it is almost certain to disagree with you, sooner or later.

However, this bottle was not marked "poison," so Alice ventured to taste it, and finding it very nice, (it had, in fact, a sort of mixed flavour of cherry-tart, custard, pine-apple, roast turkey, toffee, and hot buttered toast,) she very soon finished it off.

"What a curious feeling!" said Alice; "I must be shutting up like a telescope."

And so it was indeed: she was now only ten inches high, and her face brightened up at the thought that she was now the right size for going through the little door into that lovely garden. First, however, she waited for a few minutes to see if she was going to shrink any further: she felt a little nervous about this; "for it might end, you know," said Alice to herself, "in my going out altogether, like a candle. I wonder what I should be like then?" And she tried to fancy what the flame of a candle is like after the candle is blown out, for she could not remember ever having seen such a thing.

After a while, finding that nothing more happened, she decided on going into the garden at once; but, alas for poor Alice! when she got to the door, she found she had forgotten the little golden key, and when she went back to the table for it, she found she could not possibly reach it: she could see it quite plainly through the glass, and she tried her best to climb up one of the legs of the table, but it was too slippery; and when she had tired herself out with trying, the poor little thing sat down and cried.

"Come, there's no use in crying like that!" said Alice to herself, rather sharply; "I advise you to leave off this minute!" She generally gave herself very good advice, (though she very seldom followed it), and sometimes she scolded herself so severely as to bring tears into her eyes; and once she remembered trying to box her own ears for having cheated herself in a game of croquet she was playing against herself, for this curious child was very fond of pretending to be two people. "But it's no use now," thought poor Alice, "to pretend to be two people! Why, there's hardly enough of me left to make one respectable person!"

Soon her eye fell on a little glass box that was lying under the table: she opened it, and found in it a very small cake, on which the words "EAT ME" were beautifully marked in currants. "Well, I'll eat it," said Alice, "and if it makes me grow larger, I can reach the key; and if it makes me grow smaller, I can creep under the door; so either way I'll get into the garden, and I don't care which happens!"

She ate a little bit, and said anxiously to herself, "Which way? Which way?", holding her hand on the top of her head to feel which way it was growing, and she was quite surprised to find that she remained the same size: to be sure, this generally happens when one eats cake, but Alice had got so much into the way of expecting nothing but out-of-the-way things to happen, that it seemed quite dull and stupid for life to go on in the common way.

So she set to work, and very soon finished off the cake.

"""

SAMPLES = {
    "short": SAMPLE_SHORT,
    "constitution": SAMPLE_CONSTITUTION,
    "lear": SAMPLE_LEAR,
    "alice": SAMPLE_ALICE,
}

SAMPLE_CHOICE = "short"  # <-- change this to try a different sample
SAMPLE_TEXT = SAMPLES[SAMPLE_CHOICE]

# --- How a quarto sheet actually works ---
# A quarto sheet isn't printed one page at a time. Four pages of type
# are locked up together as a single unit -- called a forme -- and
# the whole forme is printed in one pass. Print one side, turn the
# sheet over, print the other side (a second forme, four more pages),
# then fold the sheet twice: four leaves, eight pages, from one sheet
# of paper. That's what "quarto" means.
PAGES_PER_FORME = 4          # pages of type locked up together per side
FORMES_PER_SHEET = 2         # one forme per side of the sheet
PAGES_PER_SHEET = PAGES_PER_FORME * FORMES_PER_SHEET  # = 8

# --- How the shop actually runs ---
SHEETS_PER_DAY = 1           # complete sheets (both sides) the shop sets and prints in a day
CHARACTERS_PER_PAGE = 1700   # a rough estimate for a Venetian quarto page, c. 1490
DISTRIBUTION_LAG_DAYS = 1    # normal days between printing a page and distributing its type
BUFFER_DAYS = 0              # EXTRA days of cushion in case something goes wrong
MINIMUM_CAST_PER_LETTER = 2  # every font needs at least a few of EVERY letter --
                              # even a Q or a Z that this sample never happens to use

# --- How much a piece of type actually weighs ---
# Real, physically grounded numbers, not guesses:
#   - Type-high (the foot-to-face body height every piece shares,
#     the whole subject of Chapter Four) is a genuine historical
#     standard: 0.918 inches.
#   - Point size is the body's depth -- how "big" the type is. 12
#     points (one "Pica") is a common size for ordinary book text.
#   - A letter's WIDTH varies -- an i is narrow, an m is wide -- so
#     there's no single true width. 0.7 times the point size is a
#     reasonable average across a normal mix of letters.
#   - Type metal itself (lead, tin, and antimony, per Chapter Two)
#     has a real measured density of about 9.4 grams per cubic
#     centimeter -- close to pure lead, but a bit lighter.
POINT_SIZE = 12                    # body size in points; try 8, 10, 14, 18...
TYPE_HIGH_INCHES = 0.918           # foot-to-face height, industry standard
AVERAGE_SET_WIDTH_FACTOR = 0.7     # average letter width, as a fraction of point size
TYPE_METAL_DENSITY_G_PER_CM3 = 9.4 # lead-tin-antimony alloy


def count_letters(text):
    """Count how many times each letter appears in the text -- keeping
    uppercase and lowercase SEPARATE. A printed capital E and a printed
    lowercase e are two different pieces of type, cast separately and
    stored in two different cases, exactly as Chapter Six describes.
    Punctuation, numbers, and spaces are ignored."""
    counts = Counter({letter: 0 for letter in string.ascii_uppercase})
    counts.update({letter: 0 for letter in string.ascii_lowercase})
    counts.update(ch for ch in text if ch in string.ascii_letters)
    return counts


def working_inventory_size():
    """How many total pieces of type does the shop need on hand at
    once, given how it actually operates? This is NOT the total
    characters printed over the shop's whole history -- type gets
    reused constantly. It's the amount needed to cover every page
    that's 'in flight' between being set and being distributed back
    into the case, plus a safety buffer for when distribution falls
    behind schedule."""
    pages_per_day = SHEETS_PER_DAY * PAGES_PER_SHEET
    days_of_type_tied_up = DISTRIBUTION_LAG_DAYS + BUFFER_DAYS
    pages_in_flight = pages_per_day * days_of_type_tied_up
    return pages_in_flight * CHARACTERS_PER_PAGE


def weight_per_piece_grams():
    """How much does one average piece of type weigh, in grams?
    Multiplies the body's three dimensions together for a volume,
    then multiplies by the density of real type metal."""
    point_size_inches = POINT_SIZE / 72.27  # the traditional point, not quite 1/72"
    avg_width_inches = AVERAGE_SET_WIDTH_FACTOR * point_size_inches
    volume_cubic_inches = TYPE_HIGH_INCHES * point_size_inches * avg_width_inches
    volume_cubic_cm = volume_cubic_inches * 16.387
    return volume_cubic_cm * TYPE_METAL_DENSITY_G_PER_CM3


def weight_of_bill_grams(total_pieces):
    """Total weight, in grams, of every piece of type in the bill."""
    return weight_per_piece_grams() * total_pieces


def print_bill(counts, font_size):
    """Print a printer's bill as TWO separate cases -- upper case
    (capitals) and lower case (ordinary letters) -- exactly the way
    a real shop's type actually lived. The total working inventory
    is split across all 52 possibilities (26 capitals + 26 lowercase)
    according to how often each one really appears in the sample,
    with a minimum floor applied to every single one, whether this
    sample used it or not."""
    total_letters = sum(counts.values())
    if total_letters == 0:
        print("No letters found in that text -- try a longer passage.")
        return

    def print_case(title, letters):
        print(title)
        print("-" * 45)
        print(f"{'Letter':<8}{'Count':<8}{'Percent':<10}{'Cast (of ' + str(font_size) + ')':<15}")
        print("-" * 45)

        items = sorted(((l, counts[l]) for l in letters), key=lambda x: -x[1])
        absent = []
        case_total = 0
        for letter, count in items:
            percent = count / total_letters * 100
            recommended = round(count / total_letters * font_size)
            if recommended < MINIMUM_CAST_PER_LETTER:
                recommended = MINIMUM_CAST_PER_LETTER
            if count == 0:
                absent.append(letter)
            case_total += recommended
            print(f"{letter:<8}{count:<8}{percent:>6.1f}%   {recommended:<15}")

        print("-" * 45)
        print(f"Case total: {case_total} pieces")
        if absent:
            print(f"Absent from this sample (cast at the minimum anyway): {', '.join(absent)}")
        print()

    print_case("UPPER CASE (capitals)", string.ascii_uppercase)
    print_case("LOWER CASE (ordinary letters)", string.ascii_lowercase)


if __name__ == "__main__":
    inventory_target = working_inventory_size()
    total_weight_g = weight_of_bill_grams(inventory_target)
    total_weight_kg = total_weight_g / 1000
    total_weight_lb = total_weight_g / 453.592

    print("SHOP SETTINGS")
    print("-" * 45)
    print(f"Quarto imposition: {PAGES_PER_FORME} pages/forme x {FORMES_PER_SHEET} formes/sheet = {PAGES_PER_SHEET} pages/sheet")
    print(f"Sheets set and printed per day:        {SHEETS_PER_DAY}")
    print(f"  --> pages of type composed per day:  {SHEETS_PER_DAY * PAGES_PER_SHEET}")
    print(f"Characters per page (estimate):       {CHARACTERS_PER_PAGE}")
    print(f"Normal distribution lag (days):       {DISTRIBUTION_LAG_DAYS}")
    print(f"Extra buffer for bad days (days):     {BUFFER_DAYS}")
    print(f"Point size (body size, in points):    {POINT_SIZE}")
    print(f"--> Working inventory needed:         {inventory_target} pieces of type")
    print(f"--> That's roughly {total_weight_lb:.1f} lb ({total_weight_kg:.1f} kg) of lead-tin-antimony type metal")
    print()

    letter_counts = count_letters(SAMPLE_TEXT)
    print_bill(letter_counts, font_size=inventory_target)

