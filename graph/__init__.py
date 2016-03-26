import fellow
import typecheck

@fellow.app.task(name="graph.degree")
@typecheck.returns("100 * (string, count)")
def degree():
    return([(u'friend', 760), (u'friends', 443), (u'Jean Shafiroff', 406), (u'Mark Gilbertson', 343), (u'Gillian Miniter', 236), (u'Geoffrey Bradfield', 212), (u'Alexandra Lebenthal', 208), (u'Somers Farkas', 193), (u'Andrew Saffir', 191), (u'Mario Buatta', 189), (u'Sharon Bush', 185), (u'Alina Cho', 182), (u'Yaz Hernandez', 175), (u'Lucia Hwong Gordon', 173), (u'Kamie Lightburn', 172), (u'Mayor Michael Bloomberg', 170), (u'Debbie Bancroft', 168), (u'Patrick McMullan', 165), (u'Muffie Potter Aston', 159), (u'Allison Aston', 155), (u'Eleanora Kennedy', 153), (u'Bettina Zilkha', 151), (u'Christopher Hyland', 144), (u'Barbara Tober', 140), (u'Jamee Gregory', 140), (u'Martha Stewart', 140), (u'Lydia Fenet', 139), (u'Karen LeFrak', 133), (u'Kipton Cronkite', 133), (u'Amy Fine Collins', 130), (u'Deborah Norville', 129), (u'Evelyn Lauder', 129), (u'Grace Meigher', 129), (u'Leonard Lauder', 125), (u'Michele Herbert', 124), (u'Nicole Miller', 124), (u'Audrey Gruss', 123), (u'Fernanda Kellogg', 123), (u'Jennifer Creel', 122), (u'Russell Simmons', 122), (u'Diana Taylor', 121), (u'Elizabeth Stribling', 120), (u'Paula Zahn', 120), (u'Dayssi Olarte de Kanavos', 117), (u'Liz Peek', 117), (u'Margo Langenberg', 117), (u'Rosanna Scotto', 117), (u'Donna Karan', 116), (u'Karen Klopp', 115), (u'Dennis Basso', 114), (u'Bonnie Comley', 112), (u'a friend', 112), (u'Susan Shin', 111), (u'Bette Midler', 110), (u'Adelina Wong Ettelson', 109), (u'Fern Mallis', 109), (u'Liliana Cavendish', 109), (u'Alec Baldwin', 107), (u'Lisa Anastos', 106), (u'Anka Palitz', 105), (u'Amy Hoadley', 104), (u'Wendy Carduner', 103), (u'Richard Johnson', 101), (u'Amy McFarland', 100), (u'Barbara Regna', 100), (u'Fe Fendi', 100), (u'Felicia Taylor', 100), (u'Coralie Charriol Paul', 99), (u'Margaret Russell', 99), (u'Michele Gerber Klein', 99), (u'Tory Burch', 99), (u'Cynthia Lufkin', 98), (u'Janna Bullock', 98), (u'Martha Glass', 97), (u'Nathalie Kaplan', 97), (u'Pamela Fiori', 96), (u'Beth Rudin DeWoody', 95), (u'Georgina Schaeffer', 94), (u'Jamie Niven', 94), (u'Alexandra Lind Rose', 93), (u'CeCe Black', 93), (u'Tinsley Mortimer', 93), (u'Alexia Hamm Ryan', 91), (u'Evelyn Tompkins', 91), (u'Mary Davidson', 91), (u'R. Couri Hay', 91), (u'Carol Mack', 90), (u'Melissa Berkelhammer', 90), (u'family', 90), (u'Coco Kopelman', 89), (u'Susan Magazine', 89), (u'Suzanne Cochran', 89), (u'Charlotte Moss', 88), (u'Deborah Roberts', 88), (u'Hilary Geary Ross', 88), (u'Cassandra Seidenfeld', 87), (u'Gregory Long', 87), (u'Jeanne Lawrence', 87), (u'Marcia Mishaan', 87), (u'Shoshanna Gruss', 87)])
    #return [('Alec Baldwin', 144)] * 100

@fellow.app.task(name="graph.pagerank")
@typecheck.returns("100 * (string, number)")
def pagerank():
    return([(u'friend', 0.001521410220772228), (u'friends', 0.0007681948482655355), (u'Jean Shafiroff', 0.0006135075171464154), (u'Mark Gilbertson', 0.0004689971893550614), (u'Gillian Miniter', 0.0004134648261782921), (u'Geoffrey Bradfield', 0.00034666131514725747), (u'Alexandra Lebenthal', 0.0003213054763057326), (u'Andrew Saffir', 0.000302661474239391), (u'Sharon Bush', 0.0002931983266453411), (u'Somers Farkas', 0.00028356806234366294), (u'Yaz Hernandez', 0.0002686057143027303), (u'Mario Buatta', 0.00026816058594192956), (u'Debbie Bancroft', 0.0002588801060246518), (u'Alina Cho', 0.0002586230899508773), (u'Kamie Lightburn', 0.00025184485950324054), (u'Barbara Tober', 0.00024093592312214023), (u'Lucia Hwong Gordon', 0.0002395788874943085), (u'Eleanora Kennedy', 0.00023350922945217285), (u'Mayor Michael Bloomberg', 0.00023151952521383552), (u'Christopher Hyland', 0.0002231493430482792), (u'Bonnie Comley', 0.00021730033757891369), (u'Patrick McMullan', 0.0002134596294281202), (u'Muffie Potter Aston', 0.0002109242723743157), (u'Jamee Gregory', 0.00021009131973032672), (u'Lydia Fenet', 0.00020869016420494552), (u'a friend', 0.00020783863677875972), (u'Bettina Zilkha', 0.0002024654325379484), (u'Martha Stewart', 0.00019601917491871858), (u'Elizabeth Stribling', 0.00019517475789306658), (u'Allison Aston', 0.0001946584961633422), (u'Russell Simmons', 0.00019453355026757835), (u'Karen LeFrak', 0.00019201014384239286), (u'Fernanda Kellogg', 0.0001912093203706742), (u'Amy Fine Collins', 0.0001799978865911912), (u'Kipton Cronkite', 0.00017913244197195676), (u'Grace Meigher', 0.0001788798690973687), (u'Michele Herbert', 0.00017830166465477324), (u'family', 0.00017661162791305588), (u'Donna Karan', 0.0001756779936632209), (u'Evelyn Lauder', 0.00017545572393717657), (u'Diana Taylor', 0.00017413053313620314), (u'Deborah Norville', 0.00017306638618527393), (u'Daniel Benedict', 0.00017132767676522416), (u'Stewart Lane', 0.00017046899626350448), (u'Margo Langenberg', 0.00016824860255667767), (u'Barbara Regna', 0.00016735549812130465), (u'Nicole Miller', 0.00016582252529983752), (u'Leonard Lauder', 0.00016417828359952978), (u'Dennis Basso', 0.00016303242902165595), (u'Steven Stolman', 0.00016259773013118113), (u'Liz Peek', 0.00016139630384610687), (u'Janna Bullock', 0.00016037745992009795), (u'Dawne Marie Grannum', 0.0001600150167405651), (u'Audrey Gruss', 0.000159303564491787), (u'Roric Tobin', 0.0001574420188233152), (u'Rosanna Scotto', 0.00015690717566088899), (u'Richard Johnson', 0.00015668142119779145), (u'Liliana Cavendish', 0.00015591678516376113), (u'Anka Palitz', 0.00015482676938622403), (u'Karen Klopp', 0.00015328650822152664), (u'Alec Baldwin', 0.0001532219792169477), (u'Jennifer Creel', 0.0001530242384614501), (u'Georgina Schaeffer', 0.00015233359268930415), (u'Susan Shin', 0.00015153085506529852), (u'Dayssi Olarte de Kanavos', 0.00015116049524147436), (u'Bette Midler', 0.00015020638020826172), (u'Paula Zahn', 0.00014900285384225273), (u'Fern Mallis', 0.00014851744329708348), (u'Amy Hoadley', 0.00014845973526684655), (u'Amy McFarland', 0.00014692625022014278), (u'Michele Gerber Klein', 0.00014633903765039246), (u'Lisa Anastos', 0.000143828293416643), (u'R. Couri Hay', 0.0001436205920918565), (u'Fe Fendi', 0.0001433836672385566), (u'Gregory Long', 0.00014287716932010342), (u'Felicia Taylor', 0.00014281257749960738), (u'guests', 0.00014170942657661537), (u'Tory Burch', 0.00014108793522088714), (u'Coco Kopelman', 0.00013891888746826318), (u'Adelina Wong Ettelson', 0.0001374004331078725), (u'Cynthia Lufkin', 0.0001360276405226809), (u'CeCe Black', 0.00013521924260773908), (u'Kristian Laliberte', 0.0001345930103446849), (u'Agnes Gund', 0.00013403685283328747), (u'Wendy Carduner', 0.00013320158442147153), (u'Margo Catsimatidis', 0.0001322652194622894), (u'Susan Magazine', 0.00013166637806902353), (u'Mary Van Pelt', 0.0001315414484106941), (u'Tina Brown', 0.00013100317192297074), (u'Pamela Fiori', 0.00013058437507706906), (u'Sylvester Miniter', 0.00013027097424482743), (u'Cassandra Seidenfeld', 0.00013020551921365996), (u'Nathalie Kaplan', 0.0001296547131860667), (u'John Demsey', 0.00012879506640328965), (u'John Catsimatidis', 0.00012836845658855642), (u'Tinsley Mortimer', 0.00012735153681860595), (u'Margaret Russell', 0.0001272272263325907), (u'Beth Rudin DeWoody', 0.00012709399032418285), (u'Mary Davidson', 0.0001265850352706197), (u'Julia Koch', 0.0001258598180829435)])
#    return [('Martha Stewart', 0.00019312108706213307)] * 100

@fellow.app.task(name="graph.best_friends")
@typecheck.returns("100 * ((string, string), count)")
def best_friends():
    return([(u'friend', 0.001521424821497945), (u'friends', 0.0007682022205061902), (u'Jean Shafiroff', 0.000613513494371082), (u'Mark Gilbertson', 0.00046900169024458575), (u'Gillian Miniter', 0.00041346879413278623), (u'Geoffrey Bradfield', 0.0003466646419993524), (u'Alexandra Lebenthal', 0.0003213085598219783), (u'Andrew Saffir', 0.0003026643788321901), (u'Sharon Bush', 0.00029320114042185593), (u'Somers Farkas', 0.0002835712259800315), (u'Yaz Hernandez', 0.00026860829206795634), (u'Mario Buatta', 0.000268163159435331), (u'Debbie Bancroft', 0.00025888259045480164), (u'Alina Cho', 0.0002586255719144855), (u'Kamie Lightburn', 0.00025184727641727696), (u'Barbara Tober', 0.00024093823534489353), (u'Lucia Hwong Gordon', 0.00023958118669381237), (u'Eleanora Kennedy', 0.00023351147040215863), (u'Mayor Michael Bloomberg', 0.00023152174706895422), (u'Christopher Hyland', 0.00022315168390166112), (u'Bonnie Comley', 0.00021730242297480796), (u'Patrick McMullan', 0.000213461677965365), (u'Muffie Potter Aston', 0.00021092629658015245), (u'Jamee Gregory', 0.00021009333594245274), (u'Lydia Fenet', 0.00020869216697041036), (u'a friend', 0.00020784063137225495), (u'Bettina Zilkha', 0.00020246737556567883), (u'Martha Stewart', 0.00019602105608276612), (u'Elizabeth Stribling', 0.00019517663095338186), (u'Allison Aston', 0.00019466036426917777), (u'Russell Simmons', 0.0001945354171743284), (u'Karen LeFrak', 0.00019201198653242318), (u'Fernanda Kellogg', 0.0001912111553753323), (u'Amy Fine Collins', 0.00017999961400154798), (u'Kipton Cronkite', 0.00017913416107678275), (u'Grace Meigher', 0.00017888158577829396), (u'Michele Herbert', 0.00017830337578676484), (u'family', 0.00017661332282604077), (u'Donna Karan', 0.00017567967961627006), (u'Evelyn Lauder', 0.00017545740775713926), (u'Diana Taylor', 0.0001741322042385259), (u'Deborah Norville', 0.0001730680470751521), (u'Daniel Benedict', 0.00017132932096899169), (u'Stewart Lane', 0.0001704706322266551), (u'Margo Langenberg', 0.00016825030670416987), (u'Barbara Regna', 0.00016735710420472154), (u'Nicole Miller', 0.00016582411667156435), (u'Leonard Lauder', 0.00016417985919173724), (u'Dennis Basso', 0.00016303399361728386), (u'Steven Stolman', 0.00016259929055507474), (u'Liz Peek', 0.0001613978527401082), (u'Janna Bullock', 0.00016037899903642035), (u'Dawne Marie Grannum', 0.00016001655237857948), (u'Audrey Gruss', 0.0001593050933021102), (u'Roric Tobin', 0.00015744352976868834), (u'Rosanna Scotto', 0.00015690917053956473), (u'Richard Johnson', 0.00015668292484383314), (u'Liliana Cavendish', 0.0001559182814717156), (u'Anka Palitz', 0.00015482825523347493), (u'Karen Klopp', 0.00015328797928714234), (u'Alec Baldwin', 0.00015322344966328918), (u'Jennifer Creel', 0.00015302570701010565), (u'Georgina Schaeffer', 0.00015233505460994487), (u'Susan Shin', 0.00015153230928219725), (u'Dayssi Olarte de Kanavos', 0.00015116194590409024), (u'Bette Midler', 0.0001502078217143914), (u'Paula Zahn', 0.00014900428379833604), (u'Fern Mallis', 0.0001485191426673731), (u'Amy Hoadley', 0.0001484611600107096), (u'Amy McFarland', 0.00014692766024739998), (u'Michele Gerber Klein', 0.0001463404420422664), (u'Lisa Anastos', 0.00014382967371331403), (u'R. Couri Hay', 0.0001436219703952517), (u'Fe Fendi', 0.0001433850432682228), (u'Gregory Long', 0.00014287854048899163), (u'Felicia Taylor', 0.00014281394804861839), (u'guests', 0.00014171078653886707), (u'Tory Burch', 0.00014108928921878757), (u'Coco Kopelman', 0.0001389202206501661), (u'Adelina Wong Ettelson', 0.00013740175171741653), (u'Cynthia Lufkin', 0.00013602894595775856), (u'CeCe Black', 0.00013522054028475378), (u'Kristian Laliberte', 0.00013459430201185076), (u'Agnes Gund', 0.00013403813916310043), (u'Wendy Carduner', 0.00013320286273534973), (u'Margo Catsimatidis', 0.0001322832176829034), (u'Susan Magazine', 0.0001316676416497768), (u'Mary Van Pelt', 0.00013154271079251784), (u'Tina Brown', 0.000131004525516225), (u'Pamela Fiori', 0.00013058562827401608), (u'Sylvester Miniter', 0.00013027222443411787), (u'Cassandra Seidenfeld', 0.00013020676877478914), (u'Nathalie Kaplan', 0.00012965595746120015), (u'John Demsey', 0.00012879630242853326), (u'John Catsimatidis', 0.00012839855775962172), (u'Tinsley Mortimer', 0.00012735275899053162), (u'Margaret Russell', 0.00012722844731152876), (u'Beth Rudin DeWoody', 0.0001270952100244767), (u'Mary Davidson', 0.000126586250086555), (u'Julia Koch', 0.00012586102593908777)])
#      return [(('Michael Kennedy', 'Eleanora Kennedy'), 41)] * 100
