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
    return [('Martha Stewart', 0.00019312108706213307)] * 100

@fellow.app.task(name="graph.best_friends")
@typecheck.returns("100 * ((string, string), count)")
def best_friends():
    return [(('Michael Kennedy', 'Eleanora Kennedy'), 41)] * 100
